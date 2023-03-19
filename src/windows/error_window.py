from PySide6.QtWidgets import QErrorMessage
from PySide6.QtCore import QLocale


class ErrorMessageWindow(QErrorMessage):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Внимание!")
        self.setLocale(QLocale(QLocale.Language.Russian))
        self.setFixedSize(int(self.width()/2), int(self.height()/2))
