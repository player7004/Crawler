# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categgLHSxK.ui'
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
        Dialog.resize(258, 368)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 241, 341))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.line_categ_name = QLineEdit(self.gridLayoutWidget)
        self.line_categ_name.setObjectName(u"line_categ_name")

        self.gridLayout.addWidget(self.line_categ_name, 6, 1, 1, 1)

        self.table_categ = QTableView(self.gridLayoutWidget)
        self.table_categ.setObjectName(u"table_categ")

        self.gridLayout.addWidget(self.table_categ, 1, 0, 5, 2)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)

        self.bt_add = QPushButton(self.gridLayoutWidget)
        self.bt_add.setObjectName(u"bt_add")

        self.gridLayout.addWidget(self.bt_add, 7, 0, 1, 1)

        self.bt_del = QPushButton(self.gridLayoutWidget)
        self.bt_del.setObjectName(u"bt_del")

        self.gridLayout.addWidget(self.bt_del, 7, 1, 1, 1)

        self.bt_exit = QPushButton(self.gridLayoutWidget)
        self.bt_exit.setObjectName(u"bt_exit")

        self.gridLayout.addWidget(self.bt_exit, 9, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 9, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.bt_add.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.bt_del.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.bt_exit.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

