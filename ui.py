import sys
from threading import Thread
from tkinter import Tk as _Tk, Label as _Label, Frame as _Frame, Entry, Button, RIGHT, LEFT, BOTTOM, Text, END
from typing import Optional

from package_man import PackageMan

SCREEN_NAME = "PackageMan"


def get_package_install_code(package_path: str):
    return \
        f"""
        ```
        from sys import path
        sys.path.append({package_path})
        ```
        
        """


class UI:
    def __init__(self, package_man: PackageMan):
        self._reading = False
        self._thread = Thread(target=self._loop)

        self._package_man = package_man
        self._txt_logger: Optional[Text] = None

    def start(self):
        self._thread.start()

    def _display_heading(self):
        lbl_heading = _Label(master=self._tk)
        lbl_heading["text"] = SCREEN_NAME
        lbl_heading["fg"] = "black"

        lbl_heading.pack()

    def _handle_input(self, ent: Entry):
        user_input = ent.get()

        self._txt_logger.delete("0.0", END)
        self._package_man.install_package(user_input)
        self._txt_logger.insert("1.0", f"Finished installing {user_input}. Please add the following to the top of the "
                                       f"main python module: " + get_package_install_code(
            self._package_man.install_path) + \
                                f"and import '{user_input}' as normal.")

    def _display_installer(self):
        container = _Frame(master=self._tk)

        lbl_description = _Label(master=container, text="Package Name:")
        ent_package = Entry(master=container)
        btn_confirm = Button(master=container, text="Confirm", command=lambda: self._handle_input(ent_package))
        self._txt_logger = Text(master=self._tk)

        lbl_description.pack(side=LEFT)
        ent_package.pack(side=LEFT)
        btn_confirm.pack(side=RIGHT)
        self._txt_logger.pack(side=BOTTOM)

        container.pack()

    def _display(self):
        self._tk = _Tk(SCREEN_NAME)
        self._display_heading()
        self._display_installer()

    def _loop(self):
        self._display()

        self._tk.mainloop()
