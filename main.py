from src import Crawler
from PySide6.QtWidgets import QApplication
import urllib3

def main():
    urllib3.disable_warnings()
    app = QApplication()
    window = Crawler()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
