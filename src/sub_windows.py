from PySide6.QtWidgets import QDialog
from ui import CategoryUI
from ui import RegularUI


class CategoryEditWindow(QDialog, CategoryUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.__init_buttons()

    def __init_buttons(self):
        self.bt_exit.clicked.connect(self.__exit)

    def __exit(self):
        self.close()


class RegulaEditWindow(QDialog, RegularUI):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.__init_buttons()

    def __open_category_editor(self):
        dialog = CategoryEditWindow()
        dialog.exec()

    def __init_buttons(self):
        self.bt_categ_edit.clicked.connect(self.__open_category_editor)
        self.bt_cancel.clicked.connect(self.__exit)

    def __exit(self):
        self.close()