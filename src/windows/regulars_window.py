from ui import RegularUI
from views import RegularsEditListModel
from windows import CategoryEditWindow
from PySide6.QtWidgets import QDialog


class RegularEditWindow(QDialog, RegularUI):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.__regulars_data = {}
        self.__categories_edit_window = CategoryEditWindow()

        self.__init_buttons()
        self.__update_combo_categories()
        self.__init_table()

    def __init_buttons(self):
        self.bt_categ_edit.clicked.connect(self.__open_category_editor)
        self.bt_cancel.clicked.connect(self.__exit)
        self.combo_category.currentIndexChanged.connect(self.__init_table)

    def __init_table(self):
        index = self.combo_category.currentText()
        if index == '' or index == "Выберите категорию":
            return
        model = RegularsEditListModel(self.regular_list, self.__regulars_data[index])
        self.regular_list.setModel(model)

    def update_regulars_data(self, data):
        self.__regulars_data = data
        self.__update_combo_categories()
        self.__init_table()

    def __update_combo_categories(self):
        self.combo_category.clear()
        if not len(self.__regulars_data.keys()):
            self.combo_category.addItem("Выберите категорию")
        else:
            self.combo_category.addItems(self.__regulars_data.keys())

    def __open_category_editor(self):
        self.__categories_edit_window.update_regulars_categories_data(self.__regulars_data)
        self.__categories_edit_window.exec()
        self.__regulars_data = self.__categories_edit_window.get_regulars_categories_data()
        self.__update_combo_categories()

    def get_regulars_data(self):
        return self.__regulars_data

    def __exit(self):
        self.close()