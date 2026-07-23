import sys
from pathlib import Path

ptbr = "--ptbr" in sys.argv

REPO = "Special-Operation-Decagrammaton/Build-Assets"
LAUNCHER_REPO = "Special-Operation-Decagrammaton/Kei-Launcher"
VERSION = "1.3.0"
CONFIG_DIR = Path(Path.home()).joinpath('Kei-Launcher')
CONFIG_PATH = CONFIG_DIR.joinpath('Config.json')
MANIFEST_PATH = CONFIG_DIR.joinpath('Manifest.json')
