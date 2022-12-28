# -*- coding: utf-8 -*-


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(410, 200)
        MainWindow.setMaximumSize(QSize(410, 200))
        icon = QIcon()
        icon.addFile(u"icons/2x/ORLDWW0.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-image: url(:/back/background.png);\n"
"   border-radius:10px;\n"
"\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 20, 181, 33))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background:transparent;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 70, 36, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(46, 100, 41, 16))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(88, 66, 245, 20))
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(88, 94, 245, 20))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(174, 178, 53, 13))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 124, 75, 23))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:#04fc43;    \n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:10px;\n"
"border-color:#04fc43;\n"
"\n"
"border-style:solid;\n"
"border-width:2px;\n"
"text-align: center;\n"
"}\n"
"")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(202, 124, 75, 23))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:#04fc43;    \n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:10px;\n"
"border-color:#04fc43;\n"
"\n"
"border-style:solid;\n"
"border-width:2px;\n"
"text-align: center;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Trinca da Sorte", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Trinca_V_1", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
      
    # retranslateUi

