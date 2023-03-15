# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regulScbOjJ.ui'
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
        Dialog.resize(469, 209)
        self.gridLayoutWidget_2 = QWidget(Dialog)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 450, 191))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.text_regul = QTextEdit(self.gridLayoutWidget_2)
        self.text_regul.setObjectName(u"text_regul")

        self.gridLayout_2.addWidget(self.text_regul, 1, 1, 1, 3)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.bt_categ_edit = QPushButton(self.gridLayoutWidget_2)
        self.bt_categ_edit.setObjectName(u"bt_categ_edit")

        self.gridLayout_2.addWidget(self.bt_categ_edit, 0, 3, 1, 1)

        self.combo_category = QComboBox(self.gridLayoutWidget_2)
        self.combo_category.addItem("")
        self.combo_category.setObjectName(u"combo_category")

        self.gridLayout_2.addWidget(self.combo_category, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(151, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(97, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(self.gridLayoutWidget_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 2, 2, 1, 2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0439", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.bt_categ_edit.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439", None))
        self.combo_category.setItemText(0, QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
    # retranslateUi

