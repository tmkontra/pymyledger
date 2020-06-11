import sys
import os
from pathlib import Path
import json 

if sys.platform.startswith('java'):
    import platform
    os_name = platform.java_ver()[3][0]
    if os_name.startswith('Windows'): # "Windows XP", "Windows 7", etc.
        system = 'win32'
    elif os_name.startswith('Mac'): # "Mac OS X", etc.
        system = 'darwin'
    else: # "Linux", "SunOS", "FreeBSD", etc.
        # Setting this to "linux2" is not ideal, but only Windows or Mac
        # are actually checked for and the rest of the module expects
        # *sys.platform* style strings.
        system = 'linux2'
else:
    system = sys.platform

def user_cache_dir(appname=None, appauthor=None, version=None, opinion=True):
    r"Return full path to the user-specific cache dir for this application."

    if system == "win32":
        if appauthor is None:
            appauthor = appname
        path = os.path.normpath(_get_win_folder("CSIDL_LOCAL_APPDATA"))
        if appname:
            if appauthor is not False:
                path = os.path.join(path, appauthor, appname)
            else:
                path = os.path.join(path, appname)
            if opinion:
                path = os.path.join(path, "Cache")
    elif system == 'darwin':
        path = os.path.expanduser('~/Library/Caches')
        if appname:
            path = os.path.join(path, appname)
    else:
        path = os.getenv('XDG_CACHE_HOME', os.path.expanduser('~/.cache'))
        if appname:
            path = os.path.join(path, appname)
    if appname and version:
        path = os.path.join(path, version)
    return path

class Cache:
    def __init__(self, appname):
        self._dir = user_cache_dir(appname)
        Path(self._dir).mkdir(exist_ok=True)
        self._fp = os.path.join(self._dir, "app_data.json")
        print(f"using cache location: {self._fp}")
        self.data = self.load()

    def update(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def load(self):
        try:
            with open(self._fp, 'r') as f:
                return json.load(f)
        except Exception as e:
            print("could not load application cache", e)
            return {}

    def flush(self):
        with open(self._fp, 'w') as f:
            json.dump(self.data, f)
