from PySide6.QtCore import QAbstractListModel, Qt


class RegularsEditListModel(QAbstractListModel):

    def __init__(self, parent, data):
        super().__init__(parent)
        self.__my_data = data
        self.header = ["Выражение"]

    def rowCount(self, index):
        return len(self.__my_data)

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.__my_data[index.row()]

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self.__my_data[index.row()] = value
        return super(RegularsEditListModel, self).setData(index, value, role)


class CategoriesEditListModel(QAbstractListModel):

    def __init__(self, parent, data):
        super().__init__(parent)
        self.__my_data = data
        self.header = ["Категория"]

    def rowCount(self, index):
        return len(self.__my_data)

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.__my_data[index.row()]

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self.__my_data[index.row()] = value
        return super(RegularsEditListModel, self).setData(index, value, role)
