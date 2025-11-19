# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerzhwHdP.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QKeySequenceEdit, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QWidget, QFileDialog, QFrame)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(278, 366)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(60, 340, 151, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 151, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 231, 16))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 100, 191, 22))
        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(250, 40, 21, 20))
        self.radioButton_2 = QRadioButton(Dialog)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(250, 100, 21, 20))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 260, 131, 22))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 260, 61, 16))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 260, 31, 24))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 100, 31, 24))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 290, 61, 16))
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(70, 290, 131, 22))
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 210, 251, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 40, 231, 22))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 140, 231, 16))
        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 160, 191, 22))
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(210, 160, 31, 24))
        self.radioButton_3 = QRadioButton(Dialog)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(250, 160, 21, 20))

        self.retranslateUi(Dialog)

        self.radioButton.toggle()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Keyboard shortcut:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Application:", None))
        self.radioButton.setText("")
        self.radioButton_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Icon path:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Python script", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.radioButton_3.setText("")
    # retranslateUi

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

        self.ui.pushButton.clicked.connect(self.onInputFileButton1Clicked)
        self.ui.pushButton_2.clicked.connect(self.onInputFileButton2Clicked)
        self.ui.pushButton_3.clicked.connect(self.onInputFileButton3Clicked)
    
    def onInputFileButton2Clicked(self):
        filename, filter = QFileDialog.getOpenFileName(parent = self, caption = "Open file", dir = ".")
        self.ui.lineEdit.setText(QCoreApplication.translate("MainWindow", filename, None))

    def onInputFileButton1Clicked(self):
        default_dir = "."
        if self.ui.lineEdit.text() != "":
            default_dir = self.ui.lineEdit.text()
        filename, filter = QFileDialog.getOpenFileName(parent = self, caption = "Open file", dir = default_dir)
        self.ui.lineEdit_2.setText(QCoreApplication.translate("MainWindow", filename, None))

    def onInputFileButton3Clicked(self):
        default_dir = "."
        if self.ui.lineEdit_5.text() != "":
            default_dir = self.ui.lineEdit_5.text()
        filename, filter = QFileDialog.getOpenFileName(parent = self, caption = "Open file", dir = default_dir)
        self.ui.lineEdit_5.setText(QCoreApplication.translate("MainWindow", filename, None))

    def getSequence(self):
        return self.ui.lineEdit_4.text()

    def getApplication(self):
        if self.getSelected() == 2:
            return self.ui.lineEdit.text()
        else:
            return self.ui.lineEdit_5.text()
    
    def getName(self):
        return self.ui.lineEdit_3.text()
    
    def getIcon(self):
        return self.ui.lineEdit_2.text()
    

    # Returns 1 if key sequence is selected and 2 if application is selected
    def getSelected(self):
        if self.ui.radioButton.isChecked():
            return 1
        elif self.ui.radioButton_2.isChecked():
            return 2
        else:
            return 3