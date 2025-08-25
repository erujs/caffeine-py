# caffeine-py

System Awake Script ~ A Python-based CLI tool that prevents your system from going into sleep mode.
This project was scaffolded using [cc-py](https://github.com/erujs/cc-py), a Cookiecutter template for building Python CLI applications.

## Dependencies

Ensure you have the following dependencies installed (if you haven’t already):

- **Python 3.8+** - required to develop and run the project
- **pipx** – recommended for installing and running the generated CLI apps in isolated environments
- **PyInstaller** (optional) - to package the project into a standalone executable

## Installation

You can install using `pipx` (recommended) or clone the repo directly:

### Option 1: Install with pipx
```bash
pipx install git+https://github.com/erujs/caffeine-py.git
```

### Option 2: Clone the repo
```bash
git clone https://github.com/erujs/caffeine-py.git
cd caffeine-py
pip install -e .
```

## Usage

```bash
caffeine-py # Run the main CLI to start the program
```

```bash
caffeine-build  
# Package the project into a standalone executable (via PyInstaller).
# This will create a folder called `caffeine-py-artifacts` in the directory
# where the command is executed. Inside it, you’ll find:
#
# - `build/` → Temporary build files generated during packaging.  
# - `spec/caffeine.spec` → A configuration file describing how PyInstaller built the project
#   (entry point, options, resources, etc.). You normally don’t need to edit this manually.  
# - The final binary executable → A self-contained file you can run without Python installed.  
#
# The binary will automatically match the operating system and terminal where
# you run `caffeine-build`. For example:
#   - Running on Linux → produces a Linux executable  
#   - Running on macOS → produces a macOS executable  
#   - Running on Windows → produces a Windows `.exe` file  
```

## 🧾 License
MIT — do whatever you want with it.

✨ Happy coding!
If you find this project useful, a ⭐ on the repo is always appreciated!