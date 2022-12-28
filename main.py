# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from ui_Trinca_V_2 import Ui_Trinca
from sheet.GoogleSheets import Ui_GoogleSheets
from splash.ui_splashScreen import Ui_MainWindow
from PySide2.QtCore import *
from PySide2.QtGui import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from time import sleep
import sys
import threading 
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
import configparser
from functools import partial
import json
listaPDF= []
listaJogos = []
llrep = [] 
cartotal = []
stop_flag = False

class Ui_Trinca(QMainWindow,Ui_Trinca):
    def __init__(self):
        super(Ui_Trinca, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)         
        self.toolButton.clicked.connect(self.caminhoArquivo)
        self.pushButton_9.clicked.connect(self.chamarImpressao)
        self.pushButton_8.clicked.connect(self.limparCarrinho)
        self.pushButton_9.setEnabled(False) 
        self.pushButton.clicked.connect(partial(self.menu,args=("btnsena")))
        self.pushButton_2.clicked.connect(partial(self.menu,args=("btnquina")))    
        self.pushButton_3.clicked.connect(partial(self.menu,args=("btnlotofacil")))
        self.pushButton_5.clicked.connect(partial(self.menu,args=("btnvirada"))) 
        self.pushButton_7.clicked.connect(partial(self.menu,args=("btnsaojoao")))  
        self.pushButton_6.clicked.connect(partial(self.menu,args=("btnindependencia")))     
        self.pushButton_4.clicked.connect(partial(self.enviar))
        self.pushButton_10.clicked.connect(self.close_main)
        self.pushButton_15.clicked.connect(self.minimizar_main)      
        self.pushButton_11.clicked.connect(self.abrirDoc)
        self.pushButton_13.clicked.connect(self.sheets)
        self.verificarConexao()
        
    def abrirDoc(self):
        options = QFileDialog.Options()

        caminho_atual = os.path.abspath(os.path.curdir)
        caminho_pasta_doc = os.path.join(caminho_atual, "doc")
        arquivo_planilha = os.path.join(caminho_pasta_doc, "PlanilhaNumeros.xlsm")

        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo", arquivo_planilha, options=options)
    #def abrirDoc(self):        
        #options = QFileDialog.Options()  
        
        #directory = (r'.\doc\PlanilhaNumeros.xlsm')        
        #fileXLSX = QFileDialog.getSaveFileName(self,"Salvar",os.path.expanduser("~")+directory,options=QFileDialog.DontUseNativeDialog)[1]
                 
      
    
    
    def caminhoArquivo(self):       
        options = QFileDialog.Options()
        FileName = QFileDialog.getOpenFileName(self,"Arquivo XLS","\.","PlanilhaNumeros.xlsm",options=options)[0]         
       
        if FileName == '':  
            return       
        else:
            self.lineEdit.setText(str(FileName))  

    
    
    def sheets(self):
        if self.radioButton_3.isChecked():
            self.GoogleSheets = GoogleSheets()
            self.GoogleSheets.show()
        else:
            self.avisos(args=13)
    
    def close_main(self):
         sys.exit()    
            
            
            

    def minimizar_main(self):
        self.showMinimized()
   

    def verificarConexao(self):
        with open("\\ProjTrincaDaSorte\\url\\endereco.json", "r") as f:
            ur = json.load(f)
        self.webEngineView.load(ur['urlTermos'])
        self.webEngineView.loadFinished.connect(self.maiorde18)
        
    
    
    
    #def verificarConexao(self):
        #with open("\\ProjTrincaDaSorte\\url\\endereco.json", "r") as f:
           # ur = json.load(f)               
        #self.webEngineView.load(ur['urlTermos'])        
       # sleep(2)              
        #try:       
            #if self.webEngineView.loadFinished:  
                    
                #self.webEngineView.loadFinished.connect(self.maiorde18)
                             
                #return            
            #else:
                #self.avisos(5)
                #return
        #except:
            #print("erro de conexão")
            #exit()
    
    # def maiorde18(self):
    #     self.webEngineView.loadFinished.connect(self.clicar_botao_sim)

    def maiorde18(self, ok):
        if not ok:
            self.avisos("Erro de conexão")
            return
        try:
            self.webEngineView.page().runJavaScript("""document.getElementById("botaosim").click();""")
            self.webEngineView.loadFinished.connect(self.obter_bounds)
        except:
            self.avisos("Erro ao clicar no botão")

    def obter_bounds(self, ok):
        if not ok:
            self.avisos("Erro de conexão")
            return
        self.readyBounds(args=1)    
        self.webEngineView.page().runJavaScript("""document.querySelector("#bs-example-navbar-collapse-1").innerText""", 0, self.getBounds3)






    # def maiorde18(self):
    #     sleep(1)
    #     if self.webEngineView.loadFinished:
    #         try:                            
    #            self.webEngineView.page().runJavaScript("""document.getElementById("botaosim").click();""")               
    #            #self.webEngineView.page().runJavaScript("const dialog = document.querySelector('.modal.fade.in');")                
    #            self.webEngineView.loadFinished.connect(self.readyBounds(args=1)) 
    #            self.webEngineView.page().runJavaScript("""document.querySelector("#bs-example-navbar-collapse-1").innerText""",0,self.getBounds3)
    #            return              
    #         except:
    #             self.avisos(6)        
    #     else:
    #         self.avisos(6)   

   

    def readyBounds(self,args):
        if args == 1:
            #enderecamento da url
            self.webEngineView.page().runJavaScript("window.location.href",0,self.getBounds)
           
        if args == 2:
            #concurso           
            self.webEngineView.page().runJavaScript("""document.querySelector("body > div:nth-child(4) > div > header-volante > div > h3 > span").textContent;""",0,self.getBounds)
            
        if args == 3:
            #quantidade de jogos
            self.webEngineView.page().runJavaScript("""document.querySelector("#carrinho").text;""",0,self.getBounds)      
            
        if args == 4:
            #estimativa de premio
            self.webEngineView.page().runJavaScript("""document.querySelector("body > div:nth-child(4) > div > header-volante > div > ul > li.ng-binding.ng-scope").textContent;""",0,self.getBounds)
            
        if args == 5:
            #valor das apostas
            self.webEngineView.page().runJavaScript("""document.querySelector("#valortotalapostas").textContent;""",0,self.getBounds) 

        if args == 6:
            #apostas faltando numero
            self.webEngineView.page().runJavaScript("""document.querySelector("#alert").textContent;""",0,self.getBounds2)     
        if args == 7:
            #apostas duplicadas
            if self.webEngineView.loadFinished: 
                
                self.webEngineView.page().runJavaScript("""if (document.querySelector('#confirm-cancel.modal.fade.in')) {
                                                                    ("Encontrado");
                                                                    } else {
                                                                    ("Nada encontrado");
                                                                    };""",0,self.getBounds2)  

    
    
    def getBounds(self,bounds):        
        self.bounds = bounds       
        bb = bounds.split("/")        
        if bb[0] == "https:":   
            self.lineEdit_2.setText(str(bounds))           
            if self.lineEdit_2.text() == '':
              
               self.avisos(5)
            else:
               return
        else:
            bb = bounds.split(" ")            
            if bb[0]== "Concurso":
                self.lineEdit_4.setText(str(bounds))
                listaPDF.append(str(bounds))              
            else:                 
                self.lineEdit_3.setText(bounds)                   
                listaPDF.append(bounds)                
                if (bb) == "":
                    self.avisos(5) 

    
    def getBounds3(self,bounds):
        self.bounds = bounds        
        if "Mega-Sena" in bounds:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)
        if "Quina" in bounds:
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)
        if "Lotofácil" in bounds:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)
        if "Mega da Virada" in bounds:
            self.pushButton_5.setEnabled(True)
        else:
            self.pushButton_5.setEnabled(False)
        if "Quina-especial" in bounds:
            self.pushButton_7.setEnabled(True)
        else:
            self.pushButton_7.setEnabled(False)
        if "Lotofácil da Independência" in bounds:
            self.pushButton_6.setEnabled(True)
        else:
            self.pushButton_6.setEnabled(False)

   
    
    
    def getBounds2(self,bounds,args):
     
       str(llrep.append(bounds))

    def menu(self,args):  
        self.pushButton_9.setEnabled(False)
        cartotal.clear()
        listaPDF.clear()
        listaJogos.clear()
        self.webEngineView.page().runJavaScript("""document.querySelector("#carrinho").textContent;""",0,lambda bounds: cartotal.append(bounds))
        

        with open("\\ProjTrincaDaSorte\\url\\endereco.json", "r") as f:
            ur = json.load(f)                   
        if args == "btnsena":
            self.label.setText("Mega Sena Escolhida")
            self.webEngineView.setUrl(QUrl(ur["urlMega"]))                         
            self.listWidget.clear() 
            listaPDF.clear()
            listaPDF.append("Mega Sena")           
            self.readyBounds(args=1) 
            if self.webEngineView.url().toString() != ur["urlMega"]:
               self.avisos(2)  
        if args == "btnquina":
            self.label.setText("Quina Escolhida")
            self.webEngineView.setUrl(QUrl(ur["urlQuina"]))
            self.listWidget.clear()
            listaPDF.clear()
            listaPDF.append("Quina")  
            self.readyBounds(args=1) 
            if self.webEngineView.url().toString() != ur["urlQuina"]:
               self.avisos(2)          
        if args == "btnlotofacil":
            self.label.setText("Lotofácil Escolhida")
            self.webEngineView.setUrl(QUrl(ur["urlLotofacil"]))
            self.listWidget.clear()            
            listaPDF.clear()
            listaPDF.append("Loto Facil")  
            self.readyBounds(args=1) 
            if self.webEngineView.url().toString() != ur["urlLotofacil"]:      
                self.avisos(2)       
        if args == "btnvirada":
            self.label.setText("Mega da Virada Escolhida")
            self.webEngineView.setUrl(QUrl(ur["urlVirada"]))
            self.listWidget.clear()
            listaPDF.clear()
            listaPDF.append("Mega da Virada")  
            self.readyBounds(args=1) 
            if self.webEngineView.url().toString() != ur["urlVirada"]:      
                self.avisos(2)
        if args == "btnsaojoao":
            self.label.setText("São João Escolhida")
            self.webEngineView.setUrl(QUrl(ur["urlSaoJoao"]))
            self.listWidget.clear()
            listaPDF.clear()
            listaPDF.append("Quina São João")  
            self.readyBounds(args=1) 
            if self.webEngineView.url().toString() != ur["urlSaoJoao"]:      
                self.avisos(2)
        if args == "btnindependencia":
            self.label.setText("Independência Escolhida")
            self.webEngineView.setUrl(QUrl(ur["urlIndep"]))
            self.listWidget.clear()
            listaPDF.clear()
            listaPDF.append("LotoFacil Independência")  
            self.readyBounds(args=1) 
            if self.webEngineView.url().toString() != ur["urlIndep"]:      
                self.avisos(2)
    

    
    def avisos(self,args):
        
        # # Cria uma lista com as mensagens de aviso
        # mensagens = [
        #     "Por favor, selecione o arquivo xlsm para a leitura.",
        #     "Loteria não Disponivél. Talvez o Site esteja atualizando. Tente novamente mais tarde.",
        #     "Por favor, selecione a loteria.",
        #     "Por favor, selecione o arquivo xlsm correto para a leitura.",
        #     "Pagina fora do ar, volte depois.",
        #     "Este arquivo já foi lido anteriormente.",
        #     "O arquivo selecionado não é válido.",
        #     "O arquivo selecionado já foi lido.",
        #     "O arquivo selecionado não é um arquivo .xlsm.",
        #     "O arquivo selecionado não contém os dados da loteria.",
        #     "Por favor, selecione o arquivo xlsx para a leitura.",
        #     "O arquivo selecionado não é um arquivo .xlsx.",
        #     "O arquivo selecionado não contém os resultados da loteria.",
        #     "Por favor, selecione o arquivo xlsx correto para a leitura."
        # ]
        
        # # Exibe a mensagem de acordo com o índice passado como argumento
        # msg = QMessageBox(self)
        # icon = QIcon()
        # icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
        # msg.setWindowIcon(icon) 
        # msg.setIcon(QMessageBox.Information)          
        # msg.setText(mensagens[args])
        # msg.setWindowTitle("Aviso")
        # msg.setStyleSheet("QLabel {background: transparent;}")
        # msg.setStandardButtons(QMessageBox.Ok)
        # msg.exec_()
        # self.ativarButton()





        if args == 1:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon)            
            msg.setIcon(QMessageBox.Information)          
            msg.setText("Por favor, selecione o arquivo xlsm para a leitura.")
            msg.setWindowTitle("Aviso")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            # self.ativarButton()
        elif args == 2:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon) 
            msg.setIcon(QMessageBox.Information)          
            msg.setText("      Loteria não Disponivél. \nTalvez o Site esteja atualizando. \nTente novamente mais tarde.")
            msg.setWindowTitle("Aviso")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.ativarButton()
        elif args == 3:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon) 
            msg.setIcon(QMessageBox.Information)          
            msg.setText("Por favor, selecione a loteria.")
            msg.setWindowTitle("Aviso")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            #self.ativarButton()
        elif args == 4:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon) 
            msg.setIcon(QMessageBox.Information)          
            msg.setText("Por favor, selecione o arquivo xlsm correto para a leitura.")
            msg.setWindowTitle("Aviso")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.ativarButton()
        elif args == 5:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon) 
            msg.setIcon(QMessageBox.Information)          
            msg.setText("Pagina fora do ar, volte depois.")
            msg.setWindowTitle("Aviso")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.ativarButton()
        elif args == 6:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon) 
            msg.setIcon(QMessageBox.Information)          
            msg.setText("Pagina não encontrada.")
            msg.setWindowTitle("Aviso")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.ativarButton()
        elif args == 7:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon) 
            msg.setIcon(QMessageBox.Information)          
            msg.setText("Nenhum Jogo Encontrado.")
            msg.setWindowTitle("Aviso")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.ativarButton()    
        elif args == 8:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon) 
            msg.setIcon(QMessageBox.Information)        
            msg.setText("Corrija o jogo existem dezenas repetidas no mesmo jogo")
            msg.setWindowTitle("Aviso")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.ativarButton() 
        elif args == 9:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon) 
            msg.setIcon(QMessageBox.Information)          
            msg.setText("Erro ao gerar o PDF, verifique os jogos")
            msg.setWindowTitle("Aviso")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.ativarButton() 
        elif args == 10:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon) 
            msg.setIcon(QMessageBox.Information)          
            msg.setText("Jogo repetido")
            msg.setWindowTitle("Aviso")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.ativarButton()   
        elif args == 11:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon) 
            msg.setIcon(QMessageBox.Information)          
            msg.setText("Arquivo Salvo no Desktop")
            msg.setWindowTitle("Aviso")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.ativarButton()
        elif args == 12:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon) 
            msg.setIcon(QMessageBox.Information)          
            msg.setText("Arquivo não foi salvo!")
            msg.setWindowTitle("Erro")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.ativarButton()  
        elif args == 13:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon) 
            msg.setIcon(QMessageBox.Information)          
            msg.setText("Habilite o Parâmetro para usar a Planilha Google")
            msg.setWindowTitle("Erro")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.ativarButton()
        elif args == 14:
            msg = QMessageBox(self)
            icon = QIcon()
            icon.addFile(u"icons\\2x\icons8-ponto-de-exclamação-48.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon) 
            msg.setIcon(QMessageBox.Information)          
            msg.setText("Diminua a quantidade de jogos.")
            msg.setWindowTitle("Erro")
            msg.setStyleSheet("QLabel {background: transparent;}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.ativarButton()

    def ativarButton(self):
      
        # Cria a lista de botões
        button_list = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5, 
                       self.pushButton_6, self.pushButton_7, self.pushButton_8, self.toolButton, self.pushButton_9, 
                       self.webEngineView]

        # Percorre a lista de botões e ativa cada um deles
        for button in button_list:
            button.setEnabled(True)

        


        
        # self.pushButton.setEnabled(True) 
        # self.pushButton_2.setEnabled(True)
        # self.pushButton_3.setEnabled(True)
        # self.pushButton_4.setEnabled(True)
        # self.pushButton_5.setEnabled(True)
        # self.pushButton_6.setEnabled(True)
        # self.pushButton_7.setEnabled(True)
        # self.pushButton_8.setEnabled(True)
        # self.toolButton.setEnabled(True)
        # self.pushButton_9.setEnabled(True)
        # self.webEngineView.setEnabled(True) 

    def desativarButton(self):
        #  # Cria a lista de botões
        # button_lista = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5, 
        #                self.pushButton_6, self.pushButton_7, self.pushButton_8, self.toolButton, self.pushButton_9, 
        #                self.webEngineView]

        # # Percorre a lista de botões e ativa cada um deles
        # for button in button_lista:
        #     button.setEnabled(False)


        self.webEngineView.setEnabled(False) 
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.toolButton.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        

    


    

# ...

    # def chamarThread(self):        
    #     if not self.MainThread():
    #         self.evento_termino_thread = threading.Event()
    #         self.kall = True
    #         th = threading.Thread(target=self.kall)
    #         th.start()

    # # def kall(self):
    # #     try:
    # #         # código da thread
    # #     finally:
    # #         self.thread_ativa = False
    # #         self.evento_termino_thread.set()

    # def interromperThread(self):
    #     if self.kall():
    #         self.evento_termino_thread.set()

    
  
    




    def chamarThread(self):
        try:
            th = threading.Thread(target=self.kall)
            th.setDaemon(True)
            th.start()
            
        except Exception as e:
            th.join()
            print(f'Ocorreu um erro ao iniciar a thread: {e}')

    
    
    
    # def chamarThread(self):       
            
    #     th = threading.Thread(target=self.kall)
    #     th.start()
    #     # th.join()


             
         


    def enviar(self):
        with open("\\ProjTrincaDaSorte\\url\\endereco.json", "r") as f:
            ur = json.load(f)                  
                   
        if self.radioButton_4.isChecked():             
            # self.desativarButton()      
            arqui = self.lineEdit.text().split("/")
            arqui = len(arqui)-1
            arqui2 =self.lineEdit.text().split("/")[arqui]
            if arqui2 != "PlanilhaNumeros.xlsm" :
                self.avisos(1) 
                return         
        if self.label.text() == "Mega Sena Escolhida" :
            if self.webEngineView.history().currentItem().url().toString() == ur['urlMega']:               
                self.chamarThread()
                return 
            else:
                self.avisos(2)                                
        elif self.label.text() == "Quina Escolhida":
            if self.webEngineView.history().currentItem().url().toString() == ur['urlQuina']:
                self.chamarThread()
               
            else:
                self.avisos(2)        
        elif self.label.text() == "Lotofácil Escolhida":
            if self.webEngineView.history().currentItem().url().toString() == ur['urlLotofacil']:
                self.chamarThread()
            else:
                self.avisos(2)
        elif self.label.text() == "Mega da Virada Escolhida":
            if self.webEngineView.history().currentItem().url().toString() == ur['urlVirada']:
                self.chamarThread()
            else:
                self.avisos(2)
        elif self.label.text() == "São João Escolhida":
            if self.webEngineView.history().currentItem().url().toString() == ur['urlSaoJoao']:
                self.chamarThread()
            else:
                self.avisos(2)
        elif self.label.text() == "Indepencência Escolhida":
            if self.webEngineView.history().currentItem().url().toString() == ur['urlIndependencia']:
                self.chamarThread()
                
            else:
                self.avisos(2)
        
        else:
            self.avisos(3)


    def kall(self):
        
            self.listWidget.addItem("Lendo Arquivo...")        
            sleep(1) 
            FileName = self.lineEdit.text()
            self.desativarButton()
            if self.radioButton_3.isChecked():
                if self.pushButton.isChecked():                       
                    self.listWidget.addItem("Sheet Mega Sena Carregado.")
                    FileCSV = (r".\\config\\Trinca da Sorte_v_1\\MEGA SENA")            
                    dados = pd.read_csv(FileCSV, sep=";",encoding="utf-8",dtype=str)
                    dados = 'n' + dados.astype(str) 
                if self.pushButton_2.isChecked():
                    self.listWidget.addItem("Sheet Quina Carregado.")
                    FileCSV = (r".\\config\\Trinca da Sorte_v_1\\QUINA")            
                    dados   = pd.read_csv(FileCSV, sep=";",encoding="utf-8",dtype=str)
                    dados = 'n' + dados.astype(str)  
                if self.pushButton_3.isChecked():
                    self.listWidget.addItem("Sheet LotoFacil Carregado.")
                    FileCSV = (r".\\config\\Trinca da Sorte_v_1\\LOTO FACIL")            
                    dados = pd.read_csv(FileCSV, sep=";",encoding="utf-8",dtype=str)
                    dados = 'n' + dados.astype(str)  
                if self.pushButton_5.isChecked():
                    self.listWidget.addItem("Sheet Mega da Virada Carregado.")
                    FileCSV = (r".\\config\\Trinca da Sorte_v_1\\VIRADA")            
                    dados = pd.read_csv(FileCSV, sep=";",encoding="utf-8",dtype=str)
                    dados = 'n' + dados.astype(str) 
                if self.pushButton_7.isChecked(): 
                    self.listWidget.addItem("Sheet Quina de São João Carregado.")
                    FileCSV = (r".\\config\\Trinca da Sorte_v_1\\SAOJOAO")            
                    dados = pd.read_csv(FileCSV, sep=";",encoding="utf-8",dtype=str)
                    dados = 'n' + dados.astype(str)  
                if self.pushButton_6.isChecked():  
                    self.listWidget.addItem("Sheet LotoFacil da Independência Carregado.")
                    FileCSV = (r".\\config\\Trinca da Sorte_v_1\\INDEPENDENCIA")            
                    dados = pd.read_csv(FileCSV, sep=";",encoding="utf-8",dtype=str)
                    dados = 'n' + dados.astype(str)  
            else:
                if self.radioButton_4.isChecked():
                    if self.pushButton.isChecked():
                        dados = pd.read_excel(r"%s" %FileName, sheet_name= 'MEGA SENA',usecols=['DZ1','DZ2','DZ3','DZ4','DZ5','DZ6'],dtype=str)                            
                        dados = 'n' + dados.astype(str)
                    if self.pushButton_2.isChecked():
                        dados = pd.read_excel(r"%s" %FileName, sheet_name= 'QUINA',usecols=['DZ1','DZ2','DZ3','DZ4','DZ5'],dtype=str)                            
                        dados = 'n' + dados.astype(str) 
                    if self.pushButton_3.isChecked():
                        dados = pd.read_excel(r"%s" %FileName, sheet_name= 'LOTO FACIL',usecols=['DZ1','DZ2','DZ3','DZ4','DZ5','DZ6','DZ7','DZ8','DZ9','DZ10','DZ11','DZ12','DZ13','DZ14','DZ15'],dtype=str)                            
                        dados = 'n' + dados.astype(str)                  
                    if self.pushButton_5.isChecked():
                        dados = pd.read_excel(r"%s" %FileName, sheet_name= 'VIRADA',usecols=['DZ1','DZ2','DZ3','DZ4','DZ5','DZ6'],dtype=str)                            
                        dados = 'n' + dados.astype(str) 
                    if self.pushButton_7.isChecked():
                        dados = pd.read_excel(r"%s" %FileName, sheet_name= 'SAO JOAO',usecols=['DZ1','DZ2','DZ3','DZ4','DZ5'],dtype=str)                            
                        dados = 'n' + dados.astype(str)   
                    if self.pushButton_6.isChecked():
                        dados = pd.read_excel(r"%s" %FileName, sheet_name= 'INDEPENDENCIA',usecols=['DZ1','DZ2','DZ3','DZ4','DZ5','DZ6','DZ7','DZ8','DZ9','DZ10','DZ11','DZ12','DZ13','DZ14','DZ15'],dtype=str)                            
                        dados = 'n' + dados.astype(str)     
                            
            final = len(dados.index) 
            colunas = len(dados.columns)        
            if final == 0:           
                self.listWidget.addItem("Nenhum Jogo Encontrado.")            
                self.listWidget.addItem("         <---------->           ") 
                self.ativarButton()
                self.avisos(args=7)
                return          
            else:
                if final >= 999:
                    self.listWidget.addItem("Número de Jogos Excedido.")
                    self.listWidget.addItem("         <---------->           ") 
                    self.ativarButton()
                    self.avisos(args=14)
                    return
                else:
                    self.listWidget.addItem(str(final) + " Jogos Carregados" ) 
                    self.listWidget.addItem("____________________________________")         
                    self.senaJogos(dados,final,colunas)
        


    def senaJogos(self,dados,final,colunas):
        # try:
            contagem = 0 
            linha = 0           
            while contagem < final:
                h = dados.replace({'n1':'n01','n2':'n02','n3':'n03','n4':'n04','n5':'n05','n6':'n06','n7':'n07','n8':'n08','n9':'n09','n10':'n10','n11':'n11','n12':'n12','n13':'n13','n14':'n14','n15':'n15'})                   
                z = h.iloc[contagem]
                a = z.values.tolist()             
                w = (str(a).replace('n','').replace('[','').replace(']','').replace('\'','').replace('''''','').replace(',','').replace(' ', '   '))     
                k = h.loc[contagem]             
                contagem += 1
                conta = 0             
                for i in z:                         
                    duplicado = z.duplicated()
                    d = duplicado.sum()                
                    if d != 0: 
                        self.listWidget.addItem("Numeros Duplicados no Jogo:")
                        self.listWidget.addItem(str(w)) 
                        self.listWidget.addItem("                  <---------->                   ")
                        self.listWidget.addItem("Limpe o Carrinho, Corrija o Jogo e \n            tente Novamente")
                        self.pushButton_8.setEnabled(True)                 
                        return                    
                    conta += 1           
                    s = (
                    """
                    (function () {                 
                    document.getElementById ("%s"). click();
                    })()"""
                    %i ) 
                    ##todo
                                        
                    self.webEngineView.page().runJavaScript(s)                                                                
                    if conta == colunas:                    
                        try: 
                            linha = linha + 1                                          
                            xx = 1
                            while xx == 1:        
                                self.webEngineView.page().runJavaScript("""document.getElementById('colocarnocarrinho').click();""")                            
                                sleep(1)
                                if self.webEngineView.loadFinished:
                                    if self.radioButton.isChecked():
                                        self.webEngineView.page().runJavaScript("""if (document.querySelector('#confirm-cancel.modal.fade.in'))
                                        {document.querySelector('#confirm-cancel #confirmarModalConfirmacao').click();('R');};""",0,lambda bounds: llrep.append(bounds) )
                                    if self.radioButton_2.isChecked():
                                        self.webEngineView.page().runJavaScript("""if (document.querySelector('#confirm-cancel.modal.fade.in')) {
                                                                document.querySelector('#confirm-cancel .btn-warning').click();
                                                                document.querySelector("#limparvolante").click();
                                                                ('X');                                    
                                                                        }                          
                                            """,0,lambda bounds: llrep.append(bounds) )

                                sleep(1)                                
                                                                
                                self.listWidget.addItem(str(linha) + ' -  ' + str(w)+ '  ' + (''.join(llrep))) 
                                self.listWidget.addItem("------------------------------------ ")                               
                                listaJogos.append(str(linha) + ' -  ' + str(w) + '  ' + (''.join(llrep)))                                                  
                                llrep.clear()
                                xx = 0                                           
                            sleep(1)                        
                            if contagem == final: 
                                self.listWidget.addItem("____________________________________ ")                              
                                self.listWidget.addItem("Apostas enviadas para o site.") 
                                sleep(1)                            
                                self.listWidget.addItem("Checando o carrinho no site.")
                                sleep(1)
                                cart = cartotal
                                if (int(cart[0])) != 0:
                                    self.listWidget.addItem("O carrinho não está vazio.")
                                    self.listWidget.addItem("         <---------->           ") 
                                    
                                
                                # self.ListWidget.scrollToItem(self)
                                self.readyBounds(args=2)                            
                                sleep(2)    
                                self.listWidget.addItem("                                            ")
                                self.listWidget.addItem("                  " + self.lineEdit_4.text() + "               ") 
                                self.readyBounds(args=3)                            
                                sleep(2)                                                     
                                self.listWidget.addItem("         " + self.lineEdit_3.text() + " Jogos Carregados no site.        ")
                                sleep(1)   
                                # self.ListWidget.scrollToItem(self)                       
                                if int(self.lineEdit_3.text()) != (final + (int(cart[0]))):
                                    self.listWidget.addItem("       Apostas não Enviadas Totalmente.     ") 
                                    self.listWidget.addItem("      Verifique a Quantidade de Apostas.    ")                                 
                                else: 
                                    self.listWidget.addItem("                      BOA SORTE!!                     ")
                                    self.listWidget.addItem("                         <---------->                    ")
                                self.readyBounds(args=4)
                                sleep(2)
                                self.readyBounds(args=5)  
                                self.label.setText("Escolha a sua Loteria")                                 
                                self.ativarButton()                          
                                                    
                        except:
                            self.avisos(args=10) 
                            exit()  
            
            self.webEngineView.page().runJavaScript("""document.querySelector("#bs-example-navbar-collapse-1").innerText""",0,self.getBounds3)     
            
        # finally:
        #     self.thread_ativa = False
        #     self.evento_termino_thread.set()
        

    def limparCarrinho(self): 
        with open("\\ProjTrincaDaSorte\\url\\endereco.json", "r") as f:
            ur = json.load(f)
        if self.webEngineView.history().currentItem().url().toString() == ur['urlCarrinho']:
            if self.webEngineView.loadFinished:
                self.webEngineView.page().runJavaScript("""
                                        document.querySelector("body > div:nth-child(4) > div > div.bts-suas-apostas.ng-scope > div.float-left > button.btn.btn-primary.data-limpar-carrinho").click();
                                        document.querySelector("[ng-click='limpaCarrinhoController.limparCarrinho()']").click();                                     
                                            """)             
                self.label.setText("Escolha a sua Loteria")
                self.listWidget.clear()            
                self.webEngineView.reload() 
                listaPDF.clear()
                listaJogos.clear()  
                self.listWidget.addItem("Carrinho limpo.")
                self.ativarButton()
                self.pushButton_9.setEnabled(False)
                
        else:
           self.webEngineView.page().load(QUrl(ur['urlCarrinho']))
           if self.webEngineView.loadFinished:
                self.webEngineView.page().runJavaScript("""
                                        document.querySelector("body > div:nth-child(4) > div > div.bts-suas-apostas.ng-scope > div.float-left > button.btn.btn-primary.data-limpar-carrinho").click();
                                        document.querySelector("[ng-click='limpaCarrinhoController.limparCarrinho()']").click();                                     
                                            """)             
                self.label.setText("Escolha a sua Loteria")
                self.listWidget.clear()            
                self.webEngineView.reload() 
                listaPDF.clear()
                listaJogos.clear()  
                self.listWidget.addItem("Carrinho limpo.")
                self.ativarButton()
                self.pushButton_9.setEnabled(False)
        self.pushButton_16.setChecked(True)
    

    def chamarImpressao(self):
        if self.pushButton.isChecked() or self.pushButton_5.isChecked():
            self.printMega()
        if self.pushButton_3.isChecked() or self.pushButton_6.isChecked():
            self.printFacil()
        if self.pushButton_2.isChecked() or self.pushButton_7.isChecked():
            self.printQuina()
    
    def chamarImpressao2(self):
        if self.webEngineView.loadFinished:
            self.webEngineView.page().runJavaScript("""
                                        document.querySelector("body > div:nth-child(4) > div > div.bts-suas-apostas.ng-scope > div.float-left > button.btn.btn-primary.data-imprimir-apostas").click();
                                        document.querySelector("[ng-click='imprimirApostasController.imprimirApostas()']").click();                                     
                                            """)             
            self.label.setText("Escolha a sua Loteria")
            self.listWidget.clear()            
            self.webEngineView.reload() 
            listaPDF.clear()
            listaJogos.clear()  
            self.listWidget.addItem("Apostas Impressas.")
            self.ativarButton()
            self.pushButton_9.setEnabled(False)
        else:
           self.webEngineView.page().load(QUrl(['urlCarrinho']))
           if self.webEngineView.loadFinished:
                self.webEngineView.page().runJavaScript("""
                                        document.querySelector("body > div:nth-child(4) > div > div.bts-suas-apostas.ng-scope > div.float-left > button.btn.btn-primary.data-imprimir-apostas").click();
                                        document.querySelector("[ng-click='imprimirApostasController.imprimirApostas()']").click();                                     
                                            """)             
                self.label.setText("Escolha a sua Loteria")
                self.listWidget.clear()            
                self.webEngineView.reload() 
                listaPDF.clear()
                listaJogos.clear()  
                self.listWidget.addItem("Apostas Impressas.")
                self.ativarButton()
                self.pushButton_9.setEnabled(False)
        self.pushButton_16.setChecked(True)
    
    
    
    def printFacil(self):
        nomeLoteria = None
        if self.pushButton_3.isChecked():
            nomeLoteria = "LotoFacil" 
        if self.pushButton_6.isChecked():
            nomeLoteria = "Independencia"           
        filePath, _ = QFileDialog.getSaveFileName(self, 'Save ', 'Trinca_v_2_' + nomeLoteria,'*.pdf')                     
        if len(listaPDF) <= 1 or filePath == "":
            self.avisos(9)
            return 
        pdf=canvas.Canvas (filePath)    
        i = 0 
        pg = (len(listaJogos))
        pgf = (str(pg/46 + 1).split(".")[0])
        pgnum = int(pgf)
        num_pg = 0
        for j in range(pgnum):
            y = 0
            u = 0         
            pdf.drawImage(r"\ProjTrincaDaSorte\icons\2x\Gradient-background22.jpg", 0, 750)
            pdf.drawImage(r"\ProjTrincaDaSorte\icons\2x\Gradient-background22rodape.jpg", 0, -20)            
            pdf.line(10, 10, 10, 750)
            pdf.line(585, 10, 585, 750)
            pdf.setFont("Times-Roman", 20)       
            pdf.drawString (230,800, "Apostas Realizadas") 
            pdf.setFont("Times-Roman", 20)
            pdf.drawString(165, 780, listaPDF[3])
            pdf.setFont("Times-Bold", 10)
            pdf.drawString(190, 765, listaPDF[0] + " " + listaPDF[1])
            pdf.drawString(320, 765,"Valor das Apostas:" + " " + listaPDF[4])          
            pdf.setFont("Times-Bold", 10)            
            pageNumber = str(pdf.getPageNumber())
            pdf.setFont("Times-Roman", 10)
            pdf.drawString(550, 800,pageNumber + " de " + (str(pgnum)))        
            for nome in listaJogos[i:i+162]:
                pdf.setFont("Times-Roman", 12)
                if j == num_pg:            
                        if (i in range(0 , 9)):                      
                            i += 1
                            y = y + 18
                            pdf.drawString(23, 725 - y, nome[0:55])
                            y = y + 13
                            pdf.drawString(23, 725 - y, nome[55:100])                               
                                            
                        elif (i in range(9,23)) or (i in range(46 , 69)) or (i in range(92 , 115)) \
                            or (i in range(138 , 161)) or (i in range(184,207)) or (i in range(230,253)) \
                                 or ( i in range(276,299)) or (i in range(322,345)) or (i in range(358,381)) \
                                     or (i in range(404,427)) or (i in range(450,473)) or (i in range(496,519)) \
                                        or (i in range(542,565)) or (i in range(588,611)) or (i in range(636,659)) \
                                            or (i in range(682,705)) or (i in range(728,751)) or (i in range(774,797)) \
                                                or (i in range(820,843)) or (i in range(866,889)) or (i in range(912,935)) \
                                                    or (i in range(958,981)):
                            i += 1
                            y = y + 18
                            pdf.drawString(17, 725 - y, nome[0:55]) 
                            y = y + 13
                            pdf.drawString(17, 725 - y, nome[55:100])

                        elif (i in range(23,46)) or (i in range(69 , 92)) or (i in range(115 , 138)) \
                            or (i in range(161 , 184)) or (i in range(207 , 230)) or (i in range(253 , 276)) \
                                or (i in range(299 , 322)) or (i in range(345,358)) or (i in range(381,404) \
                                    or (i in range(427,450)) or (i in range(473,496)) or (i in range(519,542)) \
                                        or (i in range(565,588)) or (i in range(611,636)) or (i in range(659,682)) \
                                            or (i in range(705,728)) or (i in range(751,774)) or (i in range(797,820)) \
                                                or (i in range(843,866)) or (i in range(889,912)) or (i in range(935,958)) \
                                                    or (i in range(981,999))): 
                            i += 1
                            u = u + 18
                            pdf.drawString(300, 725 - u, nome[0:55])
                            u = u + 13
                            pdf.drawString(300, 725 - u, nome[55:100])
                            if i == 46 or i == 92 or i == 138 or i == 184 or i == 230 \
                                or i == 276 or i == 322 or i == 358 or i == 404 or i == 450 \
                                    or i == 496 or i == 542 or i == 588 or i == 636 or i == 682 \
                                        or i == 728 or i == 774 or i == 820 or i == 866 or i == 912 or i == 958 or i == 999:
                               break
            num_pg =+ 1                                                         
            pdf.showPage()  
        pdf.save()        
        os.startfile(filePath) 



    def printMega(self):
        nomeLoteria = None
        if self.pushButton.isChecked():
            nomeLoteria = "Mega Sena" 
        if self.pushButton_5.isChecked():
            nomeLoteria = "Virada"        
        filePath, _ = QFileDialog.getSaveFileName(self, 'Save ', 'Trinca_v_2_' + nomeLoteria,'*.pdf') 
        if filePath == "": 
            return               
        pdf=canvas.Canvas (filePath)    
        if len(listaPDF) <= 1:
            self.avisos(9)
            return  
        i = 0 
        pg = (len(listaJogos))
        pgf = (str(pg/162 + 1).split(".")[0])
        pgnum = int(pgf)
        for j in range(pgnum):
            y = 0
            u = 0
            t = 0
            pdf.drawImage(r"\ProjTrincaDaSorte\icons\2x\Gradient-background22.jpg", 0, 750)
            pdf.drawImage(r"\ProjTrincaDaSorte\icons\2x\Gradient-background22rodape.jpg", 0, -20)            
            pdf.line(10, 10, 10, 750)
            pdf.line(585, 10, 585, 750)
            pdf.setFont("Times-Roman", 20)       
            pdf.drawString (230,800, "Apostas Realizadas") 
            pdf.setFont("Times-Roman", 20)
            pdf.drawString(165, 780, listaPDF[3])
            pdf.setFont("Times-Bold", 10)
            pdf.drawString(190, 765, listaPDF[0] + " " + listaPDF[1])
            pdf.drawString(320, 765,"Valor das Apostas:" + " " + listaPDF[4])          
            pdf.setFont("Times-Bold", 10)            
            pageNumber = str(pdf.getPageNumber())
            pdf.setFont("Times-Roman", 10)
            pdf.drawString(550, 800,pageNumber + " de " + (str(pgnum)))        
            for nome in listaJogos[i:i+162]:
                pdf.setFont("Times-Roman", 12)
                if j == 0:            
                        if (i in range(0 , 9)):                      
                                i += 1
                                y = y + 13
                                pdf.drawString(23, 720 - y, nome)                              
                        elif (i in range(9,54)): 
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)  
                        elif (i in range(54,99)): 
                                i += 1
                                u = u + 13
                                pdf.drawString(210, 720 - u, nome)   
                        elif (i in range(99,108)):
                                i += 1
                                u = u + 13
                                pdf.drawString(204, 720 - u, nome)        
                        elif (i in range (108,162)): 
                                i += 1
                                t = t + 13           
                                pdf.drawString(400, 720 - t, nome)                                                
                
                if (j == 1):
                        if (i in range(162,217)):                                                          
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)                
                        elif (i in range(217,271)):
                                i += 1
                                y = y + 13
                                pdf.drawString(204, 720 - y, nome)  
                        elif (i in range(271,325)):
                                i += 1
                                u = u + 13
                                pdf.drawString(400, 720 - u, nome)            
                if (j == 2):
                        if (i in range(325,380)):
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)                
                        elif (i in range(380,434)):
                                i += 1
                                y = y + 13
                                pdf.drawString(204, 720 - y, nome)  
                        elif (i in range(434,488)):
                                i += 1
                                u = u + 13
                                pdf.drawString(400, 720 - u, nome)
                if (j == 3):
                        if (i in range(488,543)):
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)                
                        elif (i in range(543,597)):
                                i += 1
                                y = y + 13
                                pdf.drawString(204, 720 - y, nome)  
                        elif (i in range(597,651)):
                                i += 1
                                u = u + 13
                                pdf.drawString(400, 720 - u, nome)  
                if (j == 4):
                        if (i in range(651,706)):
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)                
                        elif (i in range(706,760)):
                                i += 1
                                y = y + 13
                                pdf.drawString(204, 720 - y, nome)  
                        elif (i in range(760,814)):
                                i += 1
                                u = u + 13
                                pdf.drawString(400, 720 - u, nome)
                if (j == 5):
                        if (i in range(814,869)):
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)                
                        elif (i in range(869,923)):
                                i += 1
                                y = y + 13
                                pdf.drawString(204, 720 - y, nome)  
                        elif (i in range(923,977)):
                                i += 1
                                u = u + 13
                                pdf.drawString(400, 720 - u, nome) 
                if (j == 6):
                        if (i in range(977,999)):
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)                
                  
                       
            pdf.showPage()  
        pdf.save() 
        os.startfile(filePath)         

    def printQuina(self):
        nomeLoteria = None
        if self.pushButton_2.isChecked():
            nomeLoteria = "Quina" 
        if self.pushButton_7.isChecked():
            nomeLoteria = "São João"          
        filePath, _ = QFileDialog.getSaveFileName(self, 'Save ', 'Trinca_v_2_' + nomeLoteria,'*.pdf') 
        if filePath == "": 
            return               
        pdf=canvas.Canvas (filePath)    
        if len(listaPDF) <= 1:
            self.avisos(9)
            return  
        i = 0 
        pg = (len(listaJogos))
        pgf = (str(pg/162 + 1).split(".")[0])
        pgnum = int(pgf)
        for j in range(pgnum):
            y = 0
            u = 0
            t = 0
            pdf.drawImage(r"\ProjTrincaDaSorte\icons\2x\Gradient-background22.jpg", 0, 750)
            pdf.drawImage(r"\ProjTrincaDaSorte\icons\2x\Gradient-background22rodape.jpg", 0, -20)            
            pdf.line(10, 10, 10, 750)
            pdf.line(585, 10, 585, 750)
            pdf.setFont("Times-Roman", 20)       
            pdf.drawString (230,800, "Apostas Realizadas") 
            pdf.setFont("Times-Roman", 20)
            pdf.drawString(165, 780, listaPDF[3])
            pdf.setFont("Times-Bold", 10)
            pdf.drawString(190, 765, listaPDF[0] + " " + listaPDF[1])
            pdf.drawString(320, 765,"Valor das Apostas:" + " " + listaPDF[4])          
            pdf.setFont("Times-Bold", 10)            
            pageNumber = str(pdf.getPageNumber())
            pdf.setFont("Times-Roman", 10)
            pdf.drawString(550, 800,pageNumber + " de " + (str(pgnum)))        
            for nome in listaJogos[i:i+162]:
                pdf.setFont("Times-Roman", 12)
                if j == 0:            
                        if (i in range(0 , 9)):                      
                                i += 1
                                y = y + 13
                                pdf.drawString(23, 720 - y, nome)                              
                        elif (i in range(9,54)): 
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)  
                        elif (i in range(54,99)): 
                                i += 1
                                u = u + 13
                                pdf.drawString(210, 720 - u, nome)   
                        elif (i in range(99,108)):
                                i += 1
                                u = u + 13
                                pdf.drawString(204, 720 - u, nome)        
                        elif (i in range (108,162)): 
                                i += 1
                                t = t + 13           
                                pdf.drawString(400, 720 - t, nome)                                                
                
                if (j == 1):
                        if (i in range(162,217)):                                                          
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)                
                        elif (i in range(217,271)):
                                i += 1
                                y = y + 13
                                pdf.drawString(204, 720 - y, nome)  
                        elif (i in range(271,325)):
                                i += 1
                                u = u + 13
                                pdf.drawString(400, 720 - u, nome)            
                if (j == 2):
                        if (i in range(325,380)):
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)                
                        elif (i in range(380,434)):
                                i += 1
                                y = y + 13
                                pdf.drawString(204, 720 - y, nome)  
                        elif (i in range(434,488)):
                                i += 1
                                u = u + 13
                                pdf.drawString(400, 720 - u, nome)
                if (j == 3):
                        if (i in range(488,543)):
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)                
                        elif (i in range(543,597)):
                                i += 1
                                y = y + 13
                                pdf.drawString(204, 720 - y, nome)  
                        elif (i in range(597,651)):
                                i += 1
                                u = u + 13
                                pdf.drawString(400, 720 - u, nome)  
                if (j == 4):
                        if (i in range(651,706)):
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)                
                        elif (i in range(706,760)):
                                i += 1
                                y = y + 13
                                pdf.drawString(204, 720 - y, nome)  
                        elif (i in range(760,814)):
                                i += 1
                                u = u + 13
                                pdf.drawString(400, 720 - u, nome)
                if (j == 5):
                        if (i in range(814,869)):
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)                
                        elif (i in range(869,923)):
                                i += 1
                                y = y + 13
                                pdf.drawString(204, 720 - y, nome)  
                        elif (i in range(923,977)):
                                i += 1
                                u = u + 13
                                pdf.drawString(400, 720 - u, nome) 
                if (j == 6):
                        if (i in range(977,999)):
                                i += 1
                                y = y + 13
                                pdf.drawString(17, 720 - y, nome)     
            pdf.showPage()  
        pdf.save() 
        os.startfile(filePath)         


    def mousePressEvent(self, event):    
        if event.buttons() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
            # self.dragPos = event.globalPos()
            # event.accept()           
   
    def mouseMoveEvent(self, event):    
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
            # self.move(self.pos() + event.globalPos() - self.dragPos)
            # self.dragPos = event.globalPos()
            # event.accept()   


class GoogleSheets(QMainWindow, Ui_GoogleSheets):
    def __init__(self):
        super(GoogleSheets, self).__init__()        
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
    def mousePressEvent(self, event):    
        if event.buttons() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
                   
   
    def mouseMoveEvent(self, event):    
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
          

class MainWindow(QMainWindow, Ui_MainWindow):  
    def __init__(self):
        super(MainWindow, self).__init__()          
        self.setupUi(self)
        self.pushButton.clicked.connect(self.chamar)
        self.pushButton_2.clicked.connect(self.sair)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        
    def mousePressEvent(self, event):    
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()
            
   
    def mouseMoveEvent(self, event):
    
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def chamar(self):
        if self.lineEdit.text() == "ton" and self.lineEdit_2.text() == "123":           
            self.Trinca = Ui_Trinca()
            self.Trinca.show()
            MainWindow.hide(self)
        else:
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Warning)
            self.msgbox.setText("Senha incorreta.")
            self.msgbox.setWindowTitle("Aviso")
            self.msgbox.exec_()

    def sair(self):
        self.close()     
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


   
# if __name__ == "__main__":
#     app = QApplication()
#     #app.processEvents()
#     window = MainWindow()
#     window.show()    
#     app.exec_()