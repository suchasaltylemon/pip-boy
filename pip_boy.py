from queue import Queue
from pkg_resources import working_set

import pip as _pip

_STOP = object()
_INSTALL = object()
_UNINSTALL = object()
_FREEZE = object()

class PipBoy:
    def __init__(self) -> None:
        self._queue = Queue()
        self._running = False

    def start(self):
        self._running = True

        while self._running:
            req, package, return_queue = self._queue.get()

            if req is _STOP:
                self._running = False

            elif req is _INSTALL:
                _pip.main(["install", package])

            elif req is _UNINSTALL:
                _pip.main(["uninstall", package, "--yes"])

            elif req is _FREEZE:
                packages = working_set
                formatted_packages = sorted([f"{i.project_name}=={i.version}"  for i in packages])
                return_queue.put(formatted_packages)


    def stop(self):
        self._queue.put((_STOP, None, None))

    def install_package(self, package_name: str):
        self._queue.put((_INSTALL, package_name, None))

    def uninstall_package(self, package_name: str):
        self._queue.put((_UNINSTALL, package_name, None))

    def get_packages(self):
        return_queue = Queue()
        self._queue.put((_FREEZE, None, return_queue))

        return return_queue.get()
