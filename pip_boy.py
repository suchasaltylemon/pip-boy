import pip as _pip


class PipBoy:
    def install_package(self, package_name: str):
        _pip.main(["install", package_name])

