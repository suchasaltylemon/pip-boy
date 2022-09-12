from threading import Thread
from tkinter import TOP, Checkbutton, IntVar, Tk as _Tk, Label as _Label, Frame as _Frame, Entry, Button, RIGHT, LEFT, BOTTOM, Text, END
from typing import Optional

from pip_boy import PipBoy

SCREEN_NAME = "Pip-Boy"


class UI:
    def __init__(self, pip_boy: PipBoy):
        self._reading = False
        self._thread = Thread(target=self._loop)

        self._pip_boy = pip_boy
        self._txt_logger: Optional[Text] = None
        self._uninstall = None

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

        if self._uninstall.get():
            self._pip_boy.uninstall_package(user_input)
            self._txt_logger.insert("1.0", f"Uninstalling {user_input}...")

        else:
            self._pip_boy.install_package(user_input)
            self._txt_logger.insert("1.0", f"Installing {user_input}. When '{user_input}' is installed, " + \
                "you can import it as normal.")

    def _display_installer(self):
        root_frame = _Frame(master=self._tk)
        container = _Frame(master=root_frame)

        lbl_description = _Label(master=container, text="Package Name:")
        ent_package = Entry(master=container)
        btn_confirm = Button(master=container, text="Confirm", command=lambda: self._handle_input(ent_package))
        btn_list_packages = Button(master=self._tk, text="List Packages", command=lambda: self._list_packages())
        self._uninstall = IntVar(master=container, value=False)

        btn_uninstall = Checkbutton(master=container, text="Uninstall?", variable=self._uninstall)
        self._txt_logger = Text(master=root_frame)

        lbl_description.pack(side=LEFT)
        ent_package.pack(side=LEFT)
        btn_confirm.pack(side=RIGHT)
        btn_uninstall.pack(side=RIGHT)
        self._txt_logger.pack(side=BOTTOM)
        btn_list_packages.pack(side=BOTTOM)

        root_frame.pack()
        container.pack()

    def _list_packages(self):
        packages = self._pip_boy.get_packages()
        self._txt_logger.insert("1.0", "\n".join(packages))

    def _handle_close(self):
        self._tk.destroy()
        self._pip_boy.stop()

    def _display(self):
        self._tk = _Tk(SCREEN_NAME)
        self._tk.title(SCREEN_NAME)
        self._tk.iconbitmap("./icon.ico")

        self._display_heading()
        self._display_installer()

    def _loop(self):
        self._display()

        self._tk.protocol("WM_DELETE_WINDOW", lambda: self._handle_close())

        self._tk.mainloop()
