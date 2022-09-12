from pip_boy import PipBoy
from ui import UI


def main():
    pip_boy = PipBoy()
    ui = UI(pip_boy)

    ui.start()


if __name__ == "__main__":
    main()
