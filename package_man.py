import pip as _pip


class PackageMan:
    def __init__(self, install_path: str):
        self.install_path = install_path

    def install_package(self, package_name: str):
        _pip.main(["install", package_name, "--target", self.install_path])

