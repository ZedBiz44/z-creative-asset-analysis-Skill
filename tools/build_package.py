"""Build a clean local runtime package; never deploy or call a service."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
NAME = "z-creative-asset-analysis"
ALLOWED = {"references", "assets", "agents"}

def build():
    names = [x.strip() for x in (ROOT / "package-resources.txt").read_text().splitlines() if x.strip()]
    if len(names) != len(set(names)) or not set(names) <= ALLOWED:
        raise ValueError("Runtime manifest has duplicate or unapproved directories")
    selected = [ROOT / "SKILL.md"]
    for name in names:
        directory = ROOT / name
        if not directory.is_dir() or directory.is_symlink():
            raise ValueError("Missing or symlinked runtime directory: " + name)
        for source in sorted(directory.rglob("*")):
            if source.is_symlink():
                raise ValueError("Symlinks are not runtime inputs")
            if source.is_file():
                selected.append(source)
    for source in selected:
        if source.is_symlink() or not source.is_file():
            raise ValueError("Invalid runtime source")
    dist = ROOT / "dist"
    if dist.is_symlink():
        raise ValueError("Refuse symlinked dist")
    destination = dist / NAME
    if destination.is_symlink():
        raise ValueError("Refuse symlinked destination")
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    hashes = {}
    for source in selected:
        relative = source.relative_to(ROOT)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        hashes[str(relative)] = hashlib.sha256(target.read_bytes()).hexdigest()
    manifest = dist / (NAME + "-sha256.json")
    manifest.write_text(json.dumps(hashes, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"package": str(destination), "files": len(hashes), "manifest": str(manifest)}))

if __name__ == "__main__":
    build()

