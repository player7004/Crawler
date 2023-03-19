# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'titlejZRmtG.ui'
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
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 3, 781, 571))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.table_base = QTableView(self.gridLayoutWidget_2)
        self.table_base.setObjectName(u"table_base")

        self.gridLayout_2.addWidget(self.table_base, 3, 8, 4, 4)

        self.bt_regul_save = QPushButton(self.gridLayoutWidget_2)
        self.bt_regul_save.setObjectName(u"bt_regul_save")

        self.gridLayout_2.addWidget(self.bt_regul_save, 1, 1, 1, 1)

        self.bt_exit = QPushButton(self.gridLayoutWidget_2)
        self.bt_exit.setObjectName(u"bt_exit")
        sizePolicy.setHeightForWidth(self.bt_exit.sizePolicy().hasHeightForWidth())
        self.bt_exit.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.bt_exit, 9, 11, 1, 1)

        self.bt_regul = QPushButton(self.gridLayoutWidget_2)
        self.bt_regul.setObjectName(u"bt_regul")

        self.gridLayout_2.addWidget(self.bt_regul, 1, 4, 1, 1)

        self.sites_label = QLabel(self.gridLayoutWidget_2)
        self.sites_label.setObjectName(u"sites_label")

        self.gridLayout_2.addWidget(self.sites_label, 8, 0, 1, 1)

        self.bt_start = QPushButton(self.gridLayoutWidget_2)
        self.bt_start.setObjectName(u"bt_start")
        sizePolicy.setHeightForWidth(self.bt_start.sizePolicy().hasHeightForWidth())
        self.bt_start.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.bt_start, 8, 11, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 8, 3, 1, 2)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 9, 1, 1)

        self.tableView = QTableView(self.gridLayoutWidget_2)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_2.addWidget(self.tableView, 3, 0, 4, 5)

        self.horizontalSpacer_3 = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 4, 5, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.sites_button = QRadioButton(self.gridLayoutWidget_2)
        self.sites_button.setObjectName(u"sites_button")

        self.gridLayout_2.addWidget(self.sites_button, 9, 0, 1, 5)

        self.bt_base_save = QPushButton(self.gridLayoutWidget_2)
        self.bt_base_save.setObjectName(u"bt_base_save")
        sizePolicy.setHeightForWidth(self.bt_base_save.sizePolicy().hasHeightForWidth())
        self.bt_base_save.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.bt_base_save, 1, 10, 1, 1)

        self.bt_regul_load = QPushButton(self.gridLayoutWidget_2)
        self.bt_regul_load.setObjectName(u"bt_regul_load")

        self.gridLayout_2.addWidget(self.bt_regul_load, 1, 2, 1, 2)

        self.bt_base_open = QPushButton(self.gridLayoutWidget_2)
        self.bt_base_open.setObjectName(u"bt_base_open")

        self.gridLayout_2.addWidget(self.bt_base_open, 1, 11, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_regul_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a...", None))
        self.bt_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.bt_regul.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.sites_label.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0441\u0430\u0439\u0442\u043e\u0432", None))
        self.bt_start.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0443\u043b. \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.sites_button.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u043d\u0435 \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u0430", None))
        self.bt_base_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a...", None))
        self.bt_regul_load.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.bt_base_open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0431\u0430\u0437\u0443", None))
    # retranslateUi

