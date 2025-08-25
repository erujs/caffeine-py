# caffeine/build.py
import subprocess
from pathlib import Path
import shutil
import sys

def main():
    cwd = Path.cwd()  # directory where the command is run
    artifacts_dir = cwd / "caffeine-py-artifacts"

    # Clean old artifacts folder
    if artifacts_dir.exists():
        shutil.rmtree(artifacts_dir)
        print(f"🧹 Removed old artifacts folder: {artifacts_dir}")

    artifacts_dir.mkdir()
    print(f"📂 Created artifacts folder: {artifacts_dir}")

    # Path to the main script inside the package
    script_path = Path(__file__).parent / "main.py"

    # Run PyInstaller with --onefile
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--distpath", str(artifacts_dir),
        "--workpath", str(artifacts_dir / "build"),
        "--specpath", str(artifacts_dir / "spec"),
        "--name=caffeine-py",
        str(script_path)
    ], check=True)

    print(f"✅ Build complete! Check the caffeine-py-artifacts folder at {artifacts_dir}")

if __name__ == "__main__":
    sys.exit(main())
