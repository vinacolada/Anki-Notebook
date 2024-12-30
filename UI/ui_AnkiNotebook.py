# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AnkiNotebookCcbGjd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(751, 560)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionExport_as_txt = QAction(MainWindow)
        self.actionExport_as_txt.setObjectName(u"actionExport_as_txt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainHorizontal = QHBoxLayout()
        self.mainHorizontal.setObjectName(u"mainHorizontal")
        self.qColVert = QVBoxLayout()
        self.qColVert.setObjectName(u"qColVert")
        self.qGroup = QGroupBox(self.centralwidget)
        self.qGroup.setObjectName(u"qGroup")
        self.verticalLayout_4 = QVBoxLayout(self.qGroup)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.quesTable = QTableWidget(self.qGroup)
        if (self.quesTable.columnCount() < 2):
            self.quesTable.setColumnCount(2)
        if (self.quesTable.rowCount() < 5):
            self.quesTable.setRowCount(5)
        self.quesTable.setObjectName(u"quesTable")
        self.quesTable.setAlternatingRowColors(False)
        self.quesTable.setRowCount(5)
        self.quesTable.setColumnCount(2)
        self.quesTable.horizontalHeader().setVisible(True)
        self.quesTable.horizontalHeader().setCascadingSectionResizes(True)
        self.quesTable.horizontalHeader().setMinimumSectionSize(50)
        self.quesTable.horizontalHeader().setDefaultSectionSize(68)
        self.quesTable.horizontalHeader().setHighlightSections(True)
        self.quesTable.horizontalHeader().setStretchLastSection(True)
        self.quesTable.verticalHeader().setVisible(False)
        self.quesTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.quesTable)


        self.qColVert.addWidget(self.qGroup)

        self.tagGroupBox = QGroupBox(self.centralwidget)
        self.tagGroupBox.setObjectName(u"tagGroupBox")
        self.verticalLayout = QVBoxLayout(self.tagGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tagLineEdit = QLineEdit(self.tagGroupBox)
        self.tagLineEdit.setObjectName(u"tagLineEdit")

        self.verticalLayout.addWidget(self.tagLineEdit)


        self.qColVert.addWidget(self.tagGroupBox)

        self.numGroup = QGroupBox(self.centralwidget)
        self.numGroup.setObjectName(u"numGroup")
        self.verticalLayout_5 = QVBoxLayout(self.numGroup)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.numLineEdit = QLineEdit(self.numGroup)
        self.numLineEdit.setObjectName(u"numLineEdit")

        self.verticalLayout_5.addWidget(self.numLineEdit)


        self.qColVert.addWidget(self.numGroup)


        self.mainHorizontal.addLayout(self.qColVert)

        self.tColVert = QVBoxLayout()
        self.tColVert.setObjectName(u"tColVert")
        self.titleGroup = QGroupBox(self.centralwidget)
        self.titleGroup.setObjectName(u"titleGroup")
        self.verticalLayout_7 = QVBoxLayout(self.titleGroup)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.titleTextEdit = QTextEdit(self.titleGroup)
        self.titleTextEdit.setObjectName(u"titleTextEdit")

        self.verticalLayout_7.addWidget(self.titleTextEdit)


        self.tColVert.addWidget(self.titleGroup)

        self.textGroup = QGroupBox(self.centralwidget)
        self.textGroup.setObjectName(u"textGroup")
        self.verticalLayout_6 = QVBoxLayout(self.textGroup)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textTextEdit = QTextEdit(self.textGroup)
        self.textTextEdit.setObjectName(u"textTextEdit")

        self.verticalLayout_6.addWidget(self.textTextEdit)


        self.tColVert.addWidget(self.textGroup)

        self.topicGroup = QGroupBox(self.centralwidget)
        self.topicGroup.setObjectName(u"topicGroup")
        self.verticalLayout_2 = QVBoxLayout(self.topicGroup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(self.topicGroup)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)


        self.tColVert.addWidget(self.topicGroup)

        self.tColVert.setStretch(0, 1)
        self.tColVert.setStretch(1, 5)

        self.mainHorizontal.addLayout(self.tColVert)

        self.nColVert = QVBoxLayout()
        self.nColVert.setObjectName(u"nColVert")
        self.pagesGroup = QGroupBox(self.centralwidget)
        self.pagesGroup.setObjectName(u"pagesGroup")
        self.horizontalLayout = QHBoxLayout(self.pagesGroup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pagesListWidget = QListWidget(self.pagesGroup)
        self.pagesListWidget.setObjectName(u"pagesListWidget")

        self.horizontalLayout.addWidget(self.pagesListWidget)


        self.nColVert.addWidget(self.pagesGroup)


        self.mainHorizontal.addLayout(self.nColVert)

        self.mainHorizontal.setStretch(0, 1)
        self.mainHorizontal.setStretch(1, 2)
        self.mainHorizontal.setStretch(2, 1)

        self.gridLayout.addLayout(self.mainHorizontal, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 751, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_as_txt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionExport_as_txt.setText(QCoreApplication.translate("MainWindow", u"Export as .txt", None))
        self.qGroup.setTitle(QCoreApplication.translate("MainWindow", u"Questions", None))
        self.tagGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Tag", None))
        self.numGroup.setTitle(QCoreApplication.translate("MainWindow", u"Number", None))
        self.titleGroup.setTitle(QCoreApplication.translate("MainWindow", u"Title", None))
        self.textGroup.setTitle(QCoreApplication.translate("MainWindow", u"Text", None))
        self.topicGroup.setTitle(QCoreApplication.translate("MainWindow", u"Topic", None))
        self.pagesGroup.setTitle(QCoreApplication.translate("MainWindow", u"Pages", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

