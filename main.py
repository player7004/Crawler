from src import Crawler
from PySide6.QtWidgets import QApplication


def main():
    app = QApplication()
    window = Crawler()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
