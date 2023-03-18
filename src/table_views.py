
from PySide6.QtCore import QAbstractTableModel, Qt
class RegulTableModel(QAbstractTableModel):

    def __init__(self, parent, data):
        super().__init__(parent)
        self.my_data = data
        self.header = ["Категория", "Регулярное выражение"]

    def rowCount(self, index):
        return len(self.my_data)

    def columnCount(self, index):
        return  len(self.header)

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
