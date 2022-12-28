# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Trinca_V_2YQqCKv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


import images_rc
#import icon_rc

class Ui_Trinca(object):
    def setupUi(self, Trinca):
        if not Trinca.objectName():
            Trinca.setObjectName(u"Trinca")
        Trinca.resize(1169, 636)
        Trinca.setMinimumSize(QSize(1169, 636))
        Trinca.setMaximumSize(QSize(1169, 636))
        icon = QIcon()
        icon.addFile(u"icons/2x/ORLDWW0.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Trinca.setWindowIcon(icon)
        self.actionBaixar_Planilha = QAction(Trinca)
        self.actionBaixar_Planilha.setObjectName(u"actionBaixar_Planilha")
        self.actionPOP_Planilha_Google = QAction(Trinca)
        self.actionPOP_Planilha_Google.setObjectName(u"actionPOP_Planilha_Google")
        self.actionConfigurar = QAction(Trinca)
        self.actionConfigurar.setObjectName(u"actionConfigurar")
        self.actionSobre = QAction(Trinca)
        self.actionSobre.setObjectName(u"actionSobre")
        self.actionVers_o = QAction(Trinca)
        self.actionVers_o.setObjectName(u"actionVers_o")
        self.centralwidget = QWidget(Trinca)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setMaximumSize(QSize(1168, 636))
        font = QFont()
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"QFrame{\n"
"\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"	background-image: url(:/back/background.png);\n"
"\n"
"\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(4, 12, 251, 147))
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(54, 12, 148, 19))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 32, 251, 97))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(170, 8, 75, 23))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"color: rgb(193, 16, 146);\n"
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
        icon1 = QIcon()
        icon1.addFile(u"icons/2x/icons8-selecionado-50.png", QSize(), QIcon.Selected, QIcon.Off)
        icon1.addFile(u"icons/2x/icons8-selecionado-48.png", QSize(), QIcon.Selected, QIcon.On)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(2, 8, 75, 23))
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(193, 16, 146);\n"
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
        self.pushButton.setIcon(icon1)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoExclusive(True)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(86, 8, 75, 23))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"color: rgb(193, 16, 146);\n"
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
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoExclusive(True)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QRect(58, 44, 132, 19))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(172, 68, 75, 23))
        font3 = QFont()
        font3.setPointSize(7)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	color: rgb(193, 16, 146);\n"
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
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)
        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(86, 68, 75, 23))
        self.pushButton_7.setFont(font3)
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	color: rgb(193, 16, 146);\n"
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
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(True)
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(2, 68, 75, 23))
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(193, 16, 146);\n"
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
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)
        self.pushButton_16 = QPushButton(self.frame_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(2, 38, 27, 23))
        self.pushButton_16.setStyleSheet(u"background:transparent;")
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setAutoExclusive(True)
        self.pushButton_16.raise_()
        self.pushButton_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_5.raise_()
        icon2 = QIcon()
        icon2.addFile(u"icons/2x/icons8-retirada-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon2, "")
        self.frame_2.raise_()
        self.label.raise_()
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(18, 28, 219, 19))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(6, 48, 237, 65))
        self.frame_3.setStyleSheet(u"background-color: transparent;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.radioButton_2 = QRadioButton(self.frame_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(136, 12, 42, 17))
        self.radioButton_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setAutoExclusive(True)
        self.radioButton = QRadioButton(self.frame_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(72, 12, 39, 17))
        self.radioButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(True)
        icon3 = QIcon()
        icon3.addFile(u"icons/2x/icons8-marcador-duplo-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon3, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(32, 28, 177, 19))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.radioButton_4 = QRadioButton(self.tab_3)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(142, 60, 61, 17))
        self.radioButton_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;")
        self.radioButton_4.setChecked(True)
        self.radioButton_3 = QRadioButton(self.tab_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(78, 60, 61, 17))
        self.radioButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;")
        icon4 = QIcon()
        icon4.addFile(u"icons/2x/icons8-google-drive-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon4, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_4.setStyleSheet(u"")
        self.pushButton_11 = QPushButton(self.tab_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(4, 52, 75, 23))
        self.pushButton_11.setFont(font3)
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"	color: rgb(193, 16, 146);\n"
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
        icon5 = QIcon()
        icon5.addFile(u"icons/2x/icons8-baixar-atualiza\u00e7\u00f5es-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon5)
        self.pushButton_12 = QPushButton(self.tab_4)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(84, 52, 75, 23))
        self.pushButton_12.setFont(font3)
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	color: rgb(193, 16, 146);\n"
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
        self.pushButton_12.setIcon(icon5)
        self.pushButton_13 = QPushButton(self.tab_4)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(164, 52, 75, 23))
        self.pushButton_13.setFont(font3)
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"	color: rgb(193, 16, 146);\n"
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
        icon6 = QIcon()
        icon6.addFile(u"icons/2x/icons8-configura\u00e7\u00f5es-3-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon6)
        self.label_6 = QLabel(self.tab_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QRect(14, 20, 222, 19))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.pushButton_14 = QPushButton(self.tab_4)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(84, 88, 75, 23))
        self.pushButton_14.setFont(font3)
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"	color: rgb(193, 16, 146);\n"
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
        icon7 = QIcon()
        icon7.addFile(u"icons/2x/icons8-sobre-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon7)
        self.tabWidget.addTab(self.tab_4, icon6, "")
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(430, 36, 113, 20))
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(432, 62, 171, 20))
        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(432, 88, 113, 20))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(64, 178, 132, 19))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QRect(8, 205, 221, 21))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        self.lineEdit.setFont(font4)
        self.lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.lineEdit.setReadOnly(True)
        self.toolButton = QToolButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setEnabled(True)
        self.toolButton.setGeometry(QRect(228, 204, 25, 23))
        self.toolButton.setStyleSheet(u"")
        self.toolButton.setIcon(icon5)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(92, 244, 71, 31))
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setFocusPolicy(Qt.WheelFocus)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"border-top-right-radius:15px;\n"
"border-top-left-radius:15px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width:3px;\n"
"border-style:double;\n"
"text-align: center;\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#04fc43;    \n"
"border-top-right-radius:15px;\n"
"border-top-left-radius:15px;\n"
"border-color: #04fc43;\n"
"border-style:double;\n"
"border-width:2px;\n"
"text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"\n"
"border-color:#04fc43;\n"
"\n"
"border-style:double;\n"
"border-width:2px;\n"
"text-align: center;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icons/2x/icons8-reproduzir-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon8)
        self.pushButton_4.setChecked(False)
        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(8, 566, 249, 21))
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(True)
        font5.setWeight(75)
        self.pushButton_9.setFont(font5)
        self.pushButton_9.setStyleSheet(u"QPushButton {			\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width:3px;\n"
"border-style:double;\n"
"text-align: center;\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#04fc43;    \n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-color: #04fc43;\n"
"border-style:double;\n"
"border-width:2px;\n"
"text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"border-color:#04fc43;\n"
"\n"
"border-style:double;\n"
"border-width:2px;\n"
"text-align: center;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"icons/2x/icons8-impress\u00e3o-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon9)
        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(130, 600, 129, 31))
        self.pushButton_8.setFont(font2)
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width:3px;\n"
"border-style:double;\n"
"text-align: center;\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#04fc43;    \n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"border-color: #04fc43;\n"
"border-style:double;\n"
"border-width:2px;\n"
"text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"border-color:#04fc43;\n"
"\n"
"border-style:double;\n"
"border-width:2px;\n"
"text-align: center;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"icons/2x/icons8-lixeira-de-reciclagem-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon10)
        self.webEngineView = QWebEngineView(self.frame)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setEnabled(True)
        self.webEngineView.setGeometry(QRect(258, 26, 907, 605))
        self.webEngineView.setStyleSheet(u"QWebEngineView{\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"\n"
"}")
        self.webEngineView.setUrl(QUrl(u"https://www.loteriasonline.caixa.gov.br/silce-web/#/termos-de-uso"))
        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(1144, 6, 14, 14))
        self.pushButton_10.setMaximumSize(QSize(14, 14))
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setWeight(50)
        self.pushButton_10.setFont(font6)
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 0, 0);\n"
"	\n"
"	\n"
"	background-color: transparent;\n"
"	background-color: rgb(255, 0, 0);\n"
"border-radius:6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-radius:6px;\n"
"	\n"
"	background-color: rgb(198, 0, 0);\n"
"\n"
"}\n"
"")
        self.pushButton_15 = QPushButton(self.frame)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(1124, 6, 13, 13))
        self.pushButton_15.setMaximumSize(QSize(14, 14))
        self.pushButton_15.setFont(font6)
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: transparent;   \n"
"	background-color: rgb(0, 255, 0);\n"
"    border-radius:6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"border-radius:6px;\n"
"	background-color: rgb(0, 200, 0);\n"
"\n"
"}\n"
"")
        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(8, 276, 249, 289))
        self.listWidget.setStyleSheet(u"color: rgb(193, 16, 146);\n"
"background:transparente;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:double;\n"
"border-width:6px;\n"
"border-color: rgb(85, 255, 127);")
        self.listWidget.setAutoScroll(True)
        self.listWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.listWidget.setDefaultDropAction(Qt.TargetMoveAction)
        self.listWidget.setWordWrap(True)
        self.listWidget.setItemAlignment(Qt.AlignCenter)
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(430, 110, 201, 20))
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(566, 0, 93, 23))
        font7 = QFont()
        font7.setPointSize(14)
        self.label_7.setFont(font7)
        self.label_7.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(664, 10, 47, 13))
        font8 = QFont()
        font8.setPointSize(6)
        self.label_8.setFont(font8)
        self.label_8.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.raise_()
        self.tabWidget.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.toolButton.raise_()
        self.pushButton_4.raise_()
        self.pushButton_9.raise_()
        self.pushButton_8.raise_()
        self.webEngineView.raise_()
        self.pushButton_10.raise_()
        self.pushButton_15.raise_()
        self.listWidget.raise_()
        self.label_7.raise_()
        self.label_8.raise_()

        self.verticalLayout.addWidget(self.frame)

        Trinca.setCentralWidget(self.centralwidget)

        self.retranslateUi(Trinca)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Trinca)
    # setupUi

    def retranslateUi(self, Trinca):
        Trinca.setWindowTitle(QCoreApplication.translate("Trinca", u"Trinca_V_2", None))
        self.actionBaixar_Planilha.setText(QCoreApplication.translate("Trinca", u"Baixar Planilha", None))
        self.actionPOP_Planilha_Google.setText(QCoreApplication.translate("Trinca", u"POP Planilha Google", None))
        self.actionConfigurar.setText(QCoreApplication.translate("Trinca", u"Configurar", None))
        self.actionSobre.setText(QCoreApplication.translate("Trinca", u"Sobre", None))
        self.actionVers_o.setText(QCoreApplication.translate("Trinca", u"Vers\u00e3o", None))
        self.label.setText(QCoreApplication.translate("Trinca", u"Escolha a sua Loteria", None))
        self.pushButton_3.setText(QCoreApplication.translate("Trinca", u"LotoFacil", None))
        self.pushButton.setText(QCoreApplication.translate("Trinca", u"Mega", None))
        self.pushButton_2.setText(QCoreApplication.translate("Trinca", u"Quina", None))
        self.label_5.setText(QCoreApplication.translate("Trinca", u"Concuros Especiais", None))
        self.pushButton_6.setText(QCoreApplication.translate("Trinca", u"Indep", None))
        self.pushButton_7.setText(QCoreApplication.translate("Trinca", u"S\u00e3o Jo\u00e3o", None))
        self.pushButton_5.setText(QCoreApplication.translate("Trinca", u"Virada", None))
        self.pushButton_16.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "")
        self.label_2.setText(QCoreApplication.translate("Trinca", u"Permite Fazer Jogos Repetidos", None))
        self.radioButton_2.setText(QCoreApplication.translate("Trinca", u"N\u00e3o", None))
        self.radioButton.setText(QCoreApplication.translate("Trinca", u"Sim", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "")
        self.label_3.setText(QCoreApplication.translate("Trinca", u"Utilizar a Planilha Google", None))
        self.radioButton_4.setText(QCoreApplication.translate("Trinca", u"N\u00e3o", None))
        self.radioButton_3.setText(QCoreApplication.translate("Trinca", u"Sim", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), "")
        self.pushButton_11.setText(QCoreApplication.translate("Trinca", u"Planilha", None))
        self.pushButton_12.setText(QCoreApplication.translate("Trinca", u"POP plan", None))
        self.pushButton_13.setText(QCoreApplication.translate("Trinca", u"Config ", None))
        self.label_6.setText(QCoreApplication.translate("Trinca", u"Planilha Modelo e Configura\u00e7\u00e3o", None))
        self.pushButton_14.setText(QCoreApplication.translate("Trinca", u"Sobre", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), "")
        self.label_4.setText(QCoreApplication.translate("Trinca", u"Importe o Arquivo", None))
        self.toolButton.setText(QCoreApplication.translate("Trinca", u"...", None))
        self.pushButton_4.setText(QCoreApplication.translate("Trinca", u"Enviar", None))
        self.pushButton_9.setText(QCoreApplication.translate("Trinca", u"Imprimir", None))
        self.pushButton_8.setText(QCoreApplication.translate("Trinca", u"Limpar Carrinho", None))
        self.pushButton_10.setText("")
        self.pushButton_15.setText("")
        self.label_7.setText(QCoreApplication.translate("Trinca", u"Trinca_V_2", None))
        self.label_8.setText(QCoreApplication.translate("Trinca", u"V_2", None))
    # retranslateUi

