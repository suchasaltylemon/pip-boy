from package_man import PackageMan
from ui import UI


def main():
    package_man = PackageMan()
    ui = UI(package_man)

    ui.start()


if __name__ == "__main__":
    main()
