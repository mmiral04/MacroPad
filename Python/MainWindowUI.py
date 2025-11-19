# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerFWfLiR.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from Dialog import Dialog
from SettingsDialog import SettingsDialog

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)


class Ui_MainWindow(object):
    def __init__(self, mapping):
        self.mapping = mapping
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MacroPad")
        MainWindow.resize(370, 425)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 20, 91, 71))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(140, 20, 91, 71))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(240, 20, 91, 71))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(140, 100, 91, 71))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(40, 100, 91, 71))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(240, 100, 91, 71))
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(140, 180, 91, 71))
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(40, 180, 91, 71))
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(240, 180, 91, 71))
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(70, 260, 91, 24))
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(170, 260, 91, 24))
        self.Log = QFrame(self.centralwidget)
        self.Log.setObjectName(u"Log")
        self.Log.setGeometry(QRect(10, 290, 351, 101))
        self.Log.setFrameShape(QFrame.Shape.StyledPanel)
        self.Log.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.Log)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 49, 16))
        self.textEdit = QTextEdit(self.Log)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 20, 331, 71))
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(270, 260, 31, 24))
        icon = QIcon(QIcon.fromTheme(u"document-properties"))
        self.pushButton_12.setIcon(icon)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 370, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(lambda: self.openDialog("Boton 1", self.pushButton))
        self.pushButton_2.clicked.connect(lambda: self.openDialog("Boton 2", self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.openDialog("Boton 3", self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.openDialog("Boton 4", self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.openDialog("Boton 5", self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.openDialog("Boton 6", self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.openDialog("Boton 7", self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.openDialog("Boton 8", self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.openDialog("Boton 9", self.pushButton_9))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.load_mapping()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MacroPad", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Button 1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Button 2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Button 3", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Button 5", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Button 4", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Button 6", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Button 8", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Button 7", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Button 9", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Log", None))
    # retranslateUi

    def openDialog(self, buttonNumber, buttonReference):
        dlg = Dialog()
        dlg.exec()
        if dlg.result():
            self.mapping[buttonNumber] = {}
            name  = dlg.getName()
            icon = dlg.getIcon()

            if name != "":
                buttonReference.setText(QCoreApplication.translate("MainWindow", name, None))
                self.mapping[buttonNumber]["name"] = name
            if icon != "":
                buttonReference.setIcon(QIcon(icon))
                buttonReference.setIconSize(QSize(60, 60))
                buttonReference.setText(QCoreApplication.translate("MainWindow", "", None))
                self.mapping[buttonNumber]["icon"] = icon


            if dlg.getSelected() == 1: # key sequence
                seq = dlg.getSequence()
                self.mapping[buttonNumber]["type"] = 1
                self.mapping[buttonNumber]["shortcut"] = seq

                if name == "" and icon == "":
                    if len(seq) <= 14:
                        buttonReference.setText(QCoreApplication.translate("MainWindow", seq, None))
                    else:
                        buttonReference.setText(QCoreApplication.translate("MainWindow", u"...", None))
                buttonReference.setToolTip(seq)

            else: # Application / python script
                path = dlg.getApplication()
                app_name = path.split("/")[-1].split(".")[0]
                self.mapping[buttonNumber]["type"] = dlg.getSelected()
                self.mapping[buttonNumber]["app"] = path
                if icon == "":
                    buttonReference.setText(QCoreApplication.translate("MainWindow", app_name, None))
                buttonReference.setToolTip(app_name)

    def openSettings(self, config_file):
        dlg = SettingsDialog(config_file)
        dlg.exec()
        if dlg.result():
            return dlg.getFile()
        return 0

    def getLogger(self):
        return lambda str: self.textEdit.append(str)
    
    def setDisconnect(self, func):
        self.pushButton_11.clicked.connect(func)

    def setConnect(self, func):
        self.pushButton_10.clicked.connect(func)

    def string_to_reference(self, s):
        if s == "Boton 1":
            return self.pushButton
        elif s == "Boton 2":
            return self.pushButton_2
        elif s == "Boton 3":
            return self.pushButton_3
        elif s == "Boton 4":
            return self.pushButton_4
        elif s == "Boton 5":
            return self.pushButton_5
        elif s == "Boton 6":
            return self.pushButton_6
        elif s == "Boton 7":
            return self.pushButton_7
        elif s == "Boton 8":
            return self.pushButton_8
        elif s == "Boton 9":
            return self.pushButton_9
        else:
            raise ValueError

    def load_mapping(self):
        for b in self.mapping:
            reference = self.string_to_reference(b)
            name = ""
            icon = ""
            if "name" in self.mapping[b]:
                name = self.mapping[b]["name"]
                reference.setText(QCoreApplication.translate("MainWindow", name, None))
            if "icon" in self.mapping[b]:
                icon = self.mapping[b]["icon"]
                reference.setIcon(QIcon(icon))
                reference.setIconSize(QSize(60, 60))
                reference.setText(QCoreApplication.translate("MainWindow", "", None))

            if self.mapping[b]["type"] == 1: # key sequence
                seq = self.mapping[b]["shortcut"]
                if name == "" and icon == "":
                    if len(seq) <= 14:
                        reference.setText(QCoreApplication.translate("MainWindow", seq, None))
                    else:
                        reference.setText(QCoreApplication.translate("MainWindow", u"...", None))
                reference.setToolTip(seq)

            else: # application
                path = self.mapping[b]["app"]
                app_name = path.split("/")[-1].split(".")[0]
                if icon == "":
                    reference.setText(QCoreApplication.translate("MainWindow", app_name, None))
                reference.setToolTip(app_name)
