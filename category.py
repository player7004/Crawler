# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categmZhbwe.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(461, 280)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 451, 261))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bt_delete = QPushButton(self.gridLayoutWidget)
        self.bt_delete.setObjectName(u"bt_delete")

        self.gridLayout.addWidget(self.bt_delete, 3, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.bt_add = QPushButton(self.gridLayoutWidget)
        self.bt_add.setObjectName(u"bt_add")

        self.gridLayout.addWidget(self.bt_add, 3, 2, 1, 1)

        self.line_categ_name = QLineEdit(self.gridLayoutWidget)
        self.line_categ_name.setObjectName(u"line_categ_name")

        self.gridLayout.addWidget(self.line_categ_name, 2, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(32, 74, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.table_categ = QTableView(self.gridLayoutWidget)
        self.table_categ.setObjectName(u"table_categ")

        self.gridLayout.addWidget(self.table_categ, 1, 0, 4, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439", None))
        self.bt_delete.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.bt_add.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

