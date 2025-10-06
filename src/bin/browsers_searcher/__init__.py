import sys
from typing import TypedDict
from . import linux_browser_search, osx_browser_search, windows_browser_search
class Browser(TypedDict):
    browser_type: str
    path: str
    display_name: str
    version: str
def browsers():
    if sys.platform == "linux":
        yield from linux_browser_search.browsers()
    elif sys.platform == "win32" or sys.platform=="windows" or sys.platform=="Windows":
        yield from windows_browser_search.browsers()
    elif sys.platform == "darwin":
        yield from osx_browser_search.browsers()
    else:
        return False
def get():
    browsers_list=[]
    for b in browsers():
        browsers_list.append(b)
    return browsers_list










