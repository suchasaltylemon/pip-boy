import pip as _pip


class PackageMan:
    def install_package(self, package_name: str):
        _pip.main(["install", package_name])

