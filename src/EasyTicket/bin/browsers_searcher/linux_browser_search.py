import os
import re
import sys
import glob
import shlex
import shutil
import subprocess
import configparser
from typing import Iterator
from typing import TypedDict
class Browser(TypedDict):
    browser_type: str
    path: str
    display_name: str
    version: str
IGNORE_LIST = ("kfmclient",)
LINUX_DESKTOP_BROWSER_NAMES = {
    "Brave": "brave",
    "Brave Web Browser": "brave",
    "Brave Web Browser (beta)": "brave-beta",
    "Brave Web Browser (nightly)": "brave-nightly",
    "Floorp": "floorp",
    "Google Chrome": "chrome",
    "Google Chrome dev": "chrome-dev",
    "Google Chrome (unstable)": "chrome-dev",
    "Chromium": "chromium",
    "Chromium Web Browser": "chromium",
    "Falkon": "falkon",
    "Firefox": "firefox",
    "Firefox Web Browser": "firefox",
    "Konqueror": "konqueror",
    "LibreWorf": "librewolf",
    "Microsoft Edge": "msedge",
    "Microsoft Edge (dev)": "msedge-dev",
    "Opera": "opera",
    "Opera beta": "opera-beta",
    "Opera developer": "opera-developer",
    "Ungoogled Chromium": "ungoogled-chromium",
    "Vivaldi": "vivaldi",
    "Waterfox": "waterfox",
    "Yandex Browser": "yandex",
    "Zen Browser": "zen",
}
XDG_DATA_LOCATIONS = (
    "~/.local/share/applications",
    "/usr/share/applications",
    "/var/lib/snapd/desktop/applications",
    "~/.local/share/flatpak/exports/share/applications",
    "/var/lib/flatpak/exports/share/applications",
)
VERSION_PATTERN = re.compile(r"\b(\S+\.\S+)\b")
def browsers() -> Iterator[Browser]:
    if sys.platform == "linux":
        for application_dir in XDG_DATA_LOCATIONS:
            for desktop_file in glob.glob(os.path.join(os.path.expanduser(application_dir), "*.desktop")):
                config = configparser.ConfigParser(interpolation=None)
                config.read(desktop_file, encoding="utf-8")
                if (
                    "WebBrowser" not in config.get("Desktop Entry", "Categories", fallback="").split(";")
                    and config.get("Desktop Entry", "GenericName", fallback="") != "Web Browser"
                ):
                    continue
                display_name = config.get("Desktop Entry", "Name")
                if flatpak_name := config.get("Desktop Entry", "X-Flatpak", fallback=""):
                    executable_path = os.path.join(
                        os.path.dirname(os.path.dirname(os.path.dirname(desktop_file))),
                        "bin",
                        flatpak_name,
                    )
                else:
                    executable_path = config.get(
                        "Desktop Entry", "TryExec", fallback=config.get("Desktop Entry", "Exec")
                    )
                    found = False
                    for path in shlex.split(executable_path):
                        if path == "env":
                            continue
                        if os.path.exists(path):
                            executable_path = path
                            found = True
                            break
                        if result := shutil.which(path):
                            executable_path = result
                            found = True
                            break
                    if not found or executable_path.endswith(IGNORE_LIST):
                        continue
                if browser_type := LINUX_DESKTOP_BROWSER_NAMES.get(display_name):
                    version = subprocess.getoutput(f"{executable_path} --version 2>/dev/null").strip()
                    if match := VERSION_PATTERN.search(version):
                        version = match[0]
                    yield Browser(
                        browser_type=browser_type, path=executable_path, display_name=display_name, version=version
                    )











