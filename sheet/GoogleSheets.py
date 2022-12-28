# coding: utf-8 

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
import configparser
import os
from functools import partial
app_name = "Trinca da Sorte_v_2"
config_folder = os.path.join(os.path.expanduser(""), 'config', app_name)
os.makedirs(config_folder, exist_ok=True)
settings_file = "settings.conf"
full_config_file_path = os.path.join(config_folder, settings_file)     
config = configparser.ConfigParser()
config['DEFAULT'] = {"IDplan" : "0", "Nome" : ""}
config['User'] = {"IDplan" : "", "Nome" : "","app_name" : "Trinca_V_2"}
config.read(full_config_file_path)
plan = config['User'].get('IDplan')
nome = config['User'].get('Nome')
app = config['User'].get('app_name')
if not os.path.exists(full_config_file_path) or os.stat(full_config_file_path).st_size == 0:
    with open(full_config_file_path, 'w') as configfile:
        config.write(configfile) 
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
import images_rc

class Ui_GoogleSheets(object):
    def setupUi(self, GoogleSheets):
        if not GoogleSheets.objectName():
            GoogleSheets.setObjectName(u"GoogleSheets")
        GoogleSheets.setWindowModality(Qt.ApplicationModal)
        GoogleSheets.resize(390, 250)
        GoogleSheets.setMaximumSize(QSize(390, 250))
        icon = QIcon()
        icon.addFile(u":/back/background.png", QSize(), QIcon.Normal, QIcon.Off)
        GoogleSheets.setWindowIcon(icon)
        self.lineEdit = QLineEdit(GoogleSheets)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 45, 263, 21))
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"color: rgb(201, 16, 146);")
        self.label = QLabel(GoogleSheets)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(8, 54, 60, 13))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(GoogleSheets)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 70, 263, 21))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"color: rgb(201, 16, 146);\n"
"")
        self.lineEdit_2.setReadOnly(True)
        self.label_2 = QLabel(GoogleSheets)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(42, 78, 26, 13))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(GoogleSheets)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(28, 106, 40, 13))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.comboBox = QComboBox(GoogleSheets)
        icon1 = QIcon()
        icon1.addFile(u"../ProjTrincaDaSorte/icons/2x/icon8.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon1, "")
        self.comboBox.addItem(icon1, "")
        self.comboBox.addItem(icon1, "")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(70, 96, 149, 23))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.comboBox.setFont(font2)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(214, 16, 146);\n"
"\n"
"\n"
"}\n"
"")
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.pushButton = QPushButton(GoogleSheets)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(98, 132, 201, 23))
        self.pushButton.setFont(font1)
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
        self.toolButton_2 = QToolButton(GoogleSheets)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(332, 70, 25, 21))
        icon2 = QIcon()
        icon2.addFile(u"../ProjGoogleSheets/icons/2x/icons8-baixar-atualiza\u00e7\u00f5es-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.frame = QFrame(GoogleSheets)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 390, 250))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-image: url(:/back/background.png);\n"
"    border-top-right-radius:10px;\n"
"	border-top-left-radius:10px;\n"
"   \n"
"\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(368, 6, 14, 14))
        self.pushButton_2.setMaximumSize(QSize(14, 14))
        font3 = QFont()
        font3.setPointSize(9)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"QPushButton{	\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"	\n"
"    border-radius:6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-radius:6px;\n"
"	\n"
"	background-color: rgb(190, 0, 0);\n"
"\n"
"}\n"
"")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(134, 12, 114, 23))
        font4 = QFont()
        font4.setPointSize(14)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background:transparente;\n"
"background-color: rgb(201, 16, 146);")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(252, 20, 18, 13))
        font5 = QFont()
        font5.setPointSize(6)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background:transparent;")
        self.toolButton = QToolButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(360, 70, 25, 21))
        icon3 = QIcon()
        icon3.addFile(u"../ProjGoogleSheets/icons/2x/icons8-vassoura-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon3)
        self.textBrowser = QTextBrowser(GoogleSheets)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(24, 162, 341, 80))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(9)
        self.textBrowser.setFont(font6)
        self.textBrowser.setStyleSheet(u"color: rgb(170, 16, 146);")
        self.frame.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.comboBox.raise_()
        self.pushButton.raise_()
        self.toolButton_2.raise_()
        self.textBrowser.raise_()

        self.retranslateUi(GoogleSheets)

        QMetaObject.connectSlotsByName(GoogleSheets)
    # setupUi

        self.toolButton_2.clicked.connect(self.idJson)
        self.toolButton.clicked.connect(self.excluirJson)
        self.pushButton.clicked.connect(partial(self.plangoogle,args=(1)))
        #self.toolButton.clicked.connect(self.visualizar)       
        self.plangoogle(args=0) 
        self.pushButton_2.clicked.connect(self.close_buttom)


    def close_buttom(self):
        self.close()
    
    def plangoogle(self,args):
        loto_trinca_nome = (self.comboBox.currentText())  
        # if os.path.exists('\\config\\Trinca da Sorte_v_1\\token.json'):
        #     self.lineEdit_2.setText(str('token.json'))       
        if loto_trinca_nome == "MEGA SENA":
            loto_trinca_nome = "MEGA SENA!A1:F999" 
            SAMPLE_RANGE_NAME = loto_trinca_nome
        if loto_trinca_nome == "LOTO FACIL":
            loto_trinca_nome = "LOTO FACIL!A1:O999"
            SAMPLE_RANGE_NAME = loto_trinca_nome 
        if loto_trinca_nome == "QUINA":
            loto_trinca_nome = "QUINA!A1:E999"
            SAMPLE_RANGE_NAME = loto_trinca_nome
           
        nome_loteria = self.comboBox.currentText()
        
        edit = configparser.ConfigParser()
        edit.read(full_config_file_path)
        edit2 = edit.get("User", "IDplan")
        edit3 = edit.get("User", "nome")
        if self.lineEdit.text() == '':
            if edit2 == '':
                self.textBrowser.setText("Planilha não selecionada")
                if args == 1:
                   self.verificarJson(edit2,SAMPLE_RANGE_NAME)
                return                
            elif edit2 != '':                
                self.lineEdit.setText(edit2)
                e = edit3.split("\\")                
                self.lineEdit_2.setText(e[1])             
                #chamar aki o processo seguinte
                self.textBrowser.setText("Planilha selecionada" + '\n' + "Id da Planilha: " + edit2  + '\n' + "Nome da Planilha: " + nome_loteria + '\n' + "                                    -->CLIQUE EM CONECTAR<--                     ")
                return
            elif args == 3:
                self.verificarJson(edit2,SAMPLE_RANGE_NAME)
        else:                   
            if self.lineEdit.text() == edit2:
                self.textBrowser.setText("Planilha selecionada")
                #chamar aki o processo seguinte
                self.textBrowser.setText("Id da Planilha: " + edit2  + '\n' + "Nome da Planilha: " + nome_loteria)
                self.verificarJson(edit2,SAMPLE_RANGE_NAME)            
                return
            else:  
                edit = configparser.ConfigParser()
                edit.read(full_config_file_path)
                #Get the postgresql section
                postgresql = edit["User"]
                #Update the password
                postgresql["IDplan"] = self.lineEdit.text()
                #Write changes back to file
                postgresql["Nome"] = self.lineEdit_2.text()
                with open(full_config_file_path, 'w') as configfile:
                    edit.write(configfile) 
                    self.textBrowser.setText("Planilha salva" '\n' "CLIQUE EM CONECTAR")
                     
        if args == 1:
            self.verificarJson(edit2,SAMPLE_RANGE_NAME)        


    def verificarJson(self,edit2,SAMPLE_RANGE_NAME):
        creds = None
        caminhojson = self.lineEdit_2.text()
         
        #config_folder = os.path.dirname(os.path.abspath(__file__))                      
        if os.path.exists(r'.\\config\\Trinca da Sorte_v_1\\token.json'):
            creds = Credentials.from_authorized_user_file(r'.\\config\\Trinca da Sorte_v_1\\token.json', SCOPES)            
        # Se não houver credenciais (válidas) disponíveis, deixe o usuário fazer login.
        else:
            if self.lineEdit_2.text() == '':
                self.textBrowser.setText("Arquivo Json não selecionado")
                return
        try:
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:                                
                    flow = InstalledAppFlow.from_client_secrets_file(
                        caminhojson, SCOPES)
                    creds = flow.run_local_server(port=0)
                    
                # Salve as credenciais para a próxima corrida
                if os.path.exists(r'.\\config\\Trinca da Sorte_v_1\\token.json'):
                    with open(r'.\\config\\Trinca da Sorte_v_1\\token.json', 'w') as token:
                        token.write(creds.to_json())
                else:
                    with open(r'.\\config\\Trinca da Sorte_v_1\\token.json', 'w') as token:
                        token.write(creds.to_json())
                        self.textBrowser.setText("Arquivo Json salvo")
            # Crie um cliente Sheets e obtenha uma referência para o serviço.     
            else:
                
                self.leitura(creds,edit2,SAMPLE_RANGE_NAME) 
        except Exception as e:
            self.textBrowser.setText("Erro ao conectar a Planilha" + '\n' + str(e))
            self.textBrowser.setText("Exclua o arquivo token.json e configure o acesso ao Google Sheets novamente importando a chave(json) de acesso.")
            print(e)
            return   
            
        
    def excluirJson(self):
        if os.path.exists(r'.\\config\\Trinca da Sorte_v_1\\token.json'):
            os.remove(r'.\\config\\Trinca da Sorte_v_1\\token.json')
            self.textBrowser.setText("Arquivo Json excluido")
            self.lineEdit_2.setText('')
        else:
            self.textBrowser.setText("Arquivo Json não existe")
            self.lineEdit_2.setText('')



    def leitura(self,creds,edit2,SAMPLE_RANGE_NAME):    
        nome_loteria = self.comboBox.currentText()
        caminhoIDplan = self.lineEdit.text()
        if self.lineEdit.text() == '':
            if edit2 == '':
                self.textBrowser.setText("Planilha não selecionada")
                return                
            elif edit2 != '':
                self.lineEdit.setText(edit2)               
                self.textBrowser.setText("Planilha selecionada")                
                self.textBrowser.setText("Id da Planilha: " + edit2  + '\n' + "Nome da Planilha: " + nome_loteria)
                try:
                    service = build('sheets', 'v4', credentials=creds)
                    # Call the Sheets API
                    sheet = service.spreadsheets()                    
                    result = sheet.values().get(spreadsheetId=edit2,
                                                range=SAMPLE_RANGE_NAME).execute()
                    values = result.get('values', [])
                    dados_plan = pd.DataFrame(values)  
                    numeros_jogos = (len(dados_plan)) - 1                                      
                    if numeros_jogos  == '':
                        self.textBrowser.setText("Planilha vazia") 
                        return                       
                    else:
                                             
                        self.textBrowser.setText(str(numeros_jogos) + " " + "Jogos encontrados" + '\n' + "Nome da Planilha: " + nome_loteria + '\n' "Salvo na Memória" + '\n'  "CLIQUE EM ENVIAR")
                        jgsalvostring = ".\\config\\Trinca da Sorte_v_1\\" + nome_loteria
                        jgsalvos = dados_plan.to_csv(jgsalvostring,index=False,sep=';',header=False)                                            
                        return             
                    
                    if not values:
                       
                        return
                except HttpError as err:
                    self.textBrowser.setText("Planilha não encontrada")
                   
                    return

        else:            
            if caminhoIDplan != edit2:                             
                edit = configparser.ConfigParser()
                edit.read(full_config_file_path)
                #Get the postgresql section
                postgresql = edit["User"]
                #Update the password
                postgresql["IDplan"] = self.lineEdit.text()
                #Write changes back to file
                postgresql["Nome"] = self.lineEdit_2.text()  

                #voltar aki         

                with open(full_config_file_path, 'w') as configfile:
                    edit.write(configfile) 
                    config.read(full_config_file_path)
                    self.textBrowser.setText("Planilha salva" '\n' "CLIQUE EM CONECTAR") 
                    self.plangoogle
                    return 
                
            else:
                try:
                    service = build('sheets', 'v4', credentials=creds)
                    # Call the Sheets API
                    sheet = service.spreadsheets()
                    result = sheet.values().get(spreadsheetId=edit2,
                                                range=SAMPLE_RANGE_NAME).execute()
                    values = result.get('values', [])
                    dados_plan = pd.DataFrame(values)
                    numeros_jogos = (len(dados_plan)) - 1                                        
                    if numeros_jogos  == 0:
                        self.textBrowser.setText("Planilha vazia")
                        return                        
                    else:
                                            
                        self.textBrowser.setText(str(numeros_jogos) + " " + "Jogos encontrados" + '\n' + "Nome da Planilha: " + nome_loteria + '\n' "Salvo na Memória" + '\n'  "CLIQUE EM ENVIAR")
                        jgsalvostring = ".\\config\\Trinca da Sorte_v_1\\" + nome_loteria
                        jgsalvos = dados_plan.to_csv(jgsalvostring, index=False,sep=';',header=False)                       
                        return
                    if not values:
                       
                        return
                   
                except HttpError as err:
                    self.textBrowser.setText("Planilha não encontrada")
                   

    def idJson(self):       
        options = QFileDialog.Options()
        # options = QFileDialog.DontUseNativeDialog                  
        FileName = QFileDialog.getOpenFileName(None,"Arquivo JSON","","*.json",options=options)[0]       
        if FileName == '':
            return       
        else:
            self.lineEdit_2.setText(str(FileName).replace("/","\\"))






    def retranslateUi(self, GoogleSheets):
        GoogleSheets.setWindowTitle(QCoreApplication.translate("GoogleSheets", u"GoogleSheets", None))
        self.label.setText(QCoreApplication.translate("GoogleSheets", u"ID Planilha", None))
        self.label_2.setText(QCoreApplication.translate("GoogleSheets", u"Json", None))
        self.label_3.setText(QCoreApplication.translate("GoogleSheets", u"Loteria", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("GoogleSheets", u"MEGA SENA", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("GoogleSheets", u"QUINA", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("GoogleSheets", u"LOTO FACIL", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("GoogleSheets", u"MEGA SENA", None))
        self.pushButton.setText(QCoreApplication.translate("GoogleSheets", u"Conectar", None))
#if QT_CONFIG(tooltip)
        self.toolButton_2.setToolTip(QCoreApplication.translate("GoogleSheets", u"Buscar Aquivo Json", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_2.setText(QCoreApplication.translate("GoogleSheets", u"...", None))
        self.pushButton_2.setText("")
        self.label_4.setText(QCoreApplication.translate("GoogleSheets", u"GoogleSheets", None))
        self.label_5.setText(QCoreApplication.translate("GoogleSheets", u"V_2", None))
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("GoogleSheets", u"Excluir Arquivo Json", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton.setText(QCoreApplication.translate("GoogleSheets", u"...", None))
    # retranslateUi

