import os.path
from json import load

from package_man import PackageMan
from ui import UI


def get_install_path():
    if not os.path.isfile("./config.json"):
        raise FileNotFoundError("Could not find config file")

    with open("./config.json", 'r') as fs:
        data = load(fs)

        if not type(data) == dict:
            raise TypeError("Config is not a dictionary")

        install_path = data.get("installPath", None)
        if install_path is None:
            raise KeyError("No 'installPath' key in config")

        elif not os.path.exists(install_path):
            raise NotADirectoryError(f"No directory '{install_path}' could be found")

        else:
            return install_path


def main():
    install_path = get_install_path()

    package_man = PackageMan(install_path)
    ui = UI(package_man)

    ui.start()


if __name__ == "__main__":
    main()
