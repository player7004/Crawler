from PySide6.QtWidgets import QDialog

from ui import CategoryUI
from views import CategoriesEditListModel


class CategoryEditWindow(QDialog, CategoryUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.__regulars_data = {}
        self.__categories_data = []

        self.__init_buttons()

    def __init_buttons(self):
        self.bt_exit.clicked.connect(self.__exit)

    def update_regulars_categories_data(self, data):
        self.__regulars_data = data
        self.__categories_data = [i for i in data.keys()]
        model = CategoriesEditListModel(self.table_categ, self.__categories_data)
        self.table_categ.setModel(model)
        self.table_categ.setColumnWidth(0, self.table_categ.width() - 25)

    def get_regulars_categories_data(self):
        return

    def __exit(self):
        self.close()


