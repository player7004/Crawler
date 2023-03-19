# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regulpNpdts.ui'
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
        Dialog.resize(551, 209)
        self.gridLayoutWidget_2 = QWidget(Dialog)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 526, 191))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_categ_edit = QPushButton(self.gridLayoutWidget_2)
        self.bt_categ_edit.setObjectName(u"bt_categ_edit")

        self.gridLayout_2.addWidget(self.bt_categ_edit, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(97, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.bt_add = QPushButton(self.gridLayoutWidget_2)
        self.bt_add.setObjectName(u"bt_add")

        self.gridLayout_2.addWidget(self.bt_add, 2, 1, 1, 1)

        self.combo_category = QComboBox(self.gridLayoutWidget_2)
        self.combo_category.addItem("")
        self.combo_category.setObjectName(u"combo_category")

        self.gridLayout_2.addWidget(self.combo_category, 0, 1, 1, 1)

        self.bt_del = QPushButton(self.gridLayoutWidget_2)
        self.bt_del.setObjectName(u"bt_del")

        self.gridLayout_2.addWidget(self.bt_del, 2, 2, 1, 1)

        self.regular_list = QListView(self.gridLayoutWidget_2)
        self.regular_list.setObjectName(u"regular_list")

        self.gridLayout_2.addWidget(self.regular_list, 1, 1, 1, 3)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.bt_cancel = QPushButton(self.gridLayoutWidget_2)
        self.bt_cancel.setObjectName(u"bt_cancel")

        self.gridLayout_2.addWidget(self.bt_cancel, 2, 3, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0439", None))
        self.bt_categ_edit.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439", None))
        self.bt_add.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.combo_category.setItemText(0, QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))

        self.bt_del.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.bt_cancel.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
    # retranslateUi

