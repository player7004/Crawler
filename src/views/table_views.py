from PySide6.QtCore import QAbstractTableModel, Qt


class RegularTableModel(QAbstractTableModel):

    def __init__(self, parent, data):
        super().__init__(parent)
        self.my_data = self.__prepare_data(data)
        self.header = ["Категория", "Регулярное выражение"]

    @staticmethod
    def __prepare_data(data):
        normalised_data = []
        for i in data:
            for j in data[i]:
                normalised_data.append([i, j])
        return normalised_data

    def update_data(self, data):
        self.my_data = self.__prepare_data(data)

    def rowCount(self, index):
        return len(self.my_data)

    def columnCount(self, index):
        return len(self.header)

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.my_data[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None


class BaseTableModel(QAbstractTableModel):

    def __init__(self, parent, data):
        super().__init__(parent)
        self.my_data = data
        self.header = ["Сайт", "Код", "Категория"]

    def rowCount(self, index):
        return len(self.my_data)

    def columnCount(self, index):
        return len(self.header)

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.my_data[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
