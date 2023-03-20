from src.ui import RegularUI
from src.views import RegularsEditListModel
from src.windows import ErrorMessageWindow
from PySide6.QtWidgets import QDialog


class RegularEditWindow(QDialog, RegularUI):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.__error_window_message = ErrorMessageWindow()

        self.__regulars_data = {}

        self.__init_buttons()
        self.__update_combo_categories()
        self.__init_table()

    def __init_buttons(self):
        self.bt_cancel.clicked.connect(self.__exit)
        self.combo_category.currentIndexChanged.connect(self.__init_table)
        self.bt_add.clicked.connect(self.__add_regular)
        self.bt_del.clicked.connect(self.__del_regular)

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

    def __add_regular(self):
        data = self.__regulars_data[self.combo_category.currentText()] + [self.lineEdit.text()]
        self.__regulars_data.pop(self.combo_category.currentText())
        old = self.__regulars_data
        self.__regulars_data = {self.combo_category.currentText(): data}
        self.__regulars_data.update(old)
        self.__init_table()

    def __del_regular(self):
        self.__regulars_data[self.combo_category.currentText()].pop(self.regular_list.currentIndex().row())
        self.__init_table()

    def get_regulars_data(self):
        return self.__regulars_data

    def __exit(self):
        self.close()
