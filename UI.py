# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'titleDmeIDg.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(617, 546)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 13, 604, 482))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.bt_exit = QPushButton(self.gridLayoutWidget_2)
        self.bt_exit.setObjectName(u"bt_exit")
        sizePolicy.setHeightForWidth(self.bt_exit.sizePolicy().hasHeightForWidth())
        self.bt_exit.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.bt_exit, 7, 9, 1, 1)

        self.bt_base_open = QPushButton(self.gridLayoutWidget_2)
        self.bt_base_open.setObjectName(u"bt_base_open")

        self.gridLayout_2.addWidget(self.bt_base_open, 1, 9, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)

        self.bt_base_save = QPushButton(self.gridLayoutWidget_2)
        self.bt_base_save.setObjectName(u"bt_base_save")
        sizePolicy.setHeightForWidth(self.bt_base_save.sizePolicy().hasHeightForWidth())
        self.bt_base_save.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.bt_base_save, 1, 8, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 7, 1, 1)

        self.bt_start = QPushButton(self.gridLayoutWidget_2)
        self.bt_start.setObjectName(u"bt_start")
        sizePolicy.setHeightForWidth(self.bt_start.sizePolicy().hasHeightForWidth())
        self.bt_start.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.bt_start, 7, 8, 1, 1)

        self.horizontalSpacer = QSpacerItem(103, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 7, 7, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 7, 1, 1, 1)

        self.table_base = QTableView(self.gridLayoutWidget_2)
        self.table_base.setObjectName(u"table_base")

        self.gridLayout_2.addWidget(self.table_base, 3, 7, 4, 3)

        self.horizontalSpacer_3 = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 4, 3, 1, 1)

        self.table_sites = QTableView(self.gridLayoutWidget_2)
        self.table_sites.setObjectName(u"table_sites")

        self.gridLayout_2.addWidget(self.table_sites, 6, 0, 1, 3)

        self.tableView = QTableView(self.gridLayoutWidget_2)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_2.addWidget(self.tableView, 3, 0, 1, 3)

        self.bt_regul = QPushButton(self.gridLayoutWidget_2)
        self.bt_regul.setObjectName(u"bt_regul")

        self.gridLayout_2.addWidget(self.bt_regul, 1, 1, 1, 2)

        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 4, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 617, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0443\u043b. \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.bt_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.bt_base_open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0431\u0430\u0437\u0443", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0441\u0430\u0439\u0442\u043e\u0432", None))
        self.bt_base_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
        self.bt_start.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.bt_regul.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

