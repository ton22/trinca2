def chamarThread(self):       
    self.thread = threading.Thread(target=self.sena).start()
    stop_flag = True

def enviar(self):    
    if self.radioButton_4.isChecked(): 
        self.desativarButton()      
    arqui = self.lineEdit.text().split("/")
    arqui = len(arqui)-1
    arqui2 =self.lineEdit.text().split("/")[arqui]
    if arqui2 != "PlanilhaNumeros.xlsm" :
        self.avisos(1) 
        return 
    if self.label.text() == "Mega Sena Escolhida" :
        if self.webEngineView.history().currentItem().url().toString() == urlMega:               
            self.chamarThread()
            return 
        else:
            self.avisos(2)                                
    elif self.label.text() == "Quina Escolhida":
        if self.webEngineView.history().currentItem().url().toString() == urlQuina:
            self.quina()
        else:
            self.avisos(2)        
    elif self.label.text() == "Lotofácil Escolhida":
        if self.webEngineView.history().currentItem().url().toString() == urlLotofacil:
            self.lotofacil()
        else:
            self.avisos(2)
    
    else:
        self.avisos(3)

def sena(self):
    self.listWidget.addItem("Lendo Arquivo...")        
    sleep(1) 
    FileName = self.lineEdit.text()
    if self.radioButton_3.isChecked():
        self.listWidget.addItem("Sheet Carregado.")
        FileCSV = (r"F:\ProjTrincaDaSorte\config\Trinca da Sorte_v_1\jogos")
        #"config\Trinca da Sorte_v_1\jogos.csv"
        sena = pd.read_csv(FileCSV, sep=";",encoding="utf-8",dtype=str)
        sena = 'n' + sena.astype(str) 
        print(sena)
    else:
        if self.radioButton_4.isChecked():
            self.listWidget.addItem("Sheet Carregado.")
            sena = pd.read_excel(r"%s" %FileName, sheet_name= 'MEGA SENA',usecols=['DZ1','DZ2','DZ3','DZ4','DZ5','DZ6'],dtype=str)                        
            print(sena)
            sena = 'n' + sena.astype(str) 
            
    final = len(sena)
    if final == 0:           
        self.listWidget.addItem("Nenhum Jogo Encontrado.")            
        self.listWidget.addItem("         <---------->           ") 
        self.avisos(args=7)
        return          
    else:
        self.listWidget.addItem(str(final) + " Jogos Carregados" ) 
        self.listWidget.addItem("____________________________________")         
        self.senaJogos(sena,final)


def senaJogos(self,sena,final):
        contagem = 0              
        while contagem < final:
            h = sena.replace({'n1':'n01','n2':'n02','n3':'n03','n4':'n04','n5':'n05','n6':'n06','n7':'n07','n8':'n08','n9':'n09'})            
            z = h.iloc[contagem]                
            k = h.loc[contagem]           
            w = (str(k).replace('n','').replace("Name:", '').replace('dtype: object', '').replace('DZ1','').replace('DZ2','').replace('DZ3', '').replace('DZ4', '').replace('DZ5', '').replace('DZ6', '').format(',').replace(', ','').replace('\n',''))[:-2]        
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
                %i  
                    )                      
                self.webEngineView.page().runJavaScript(s)                                                                
                if conta == 6:                    
                    try:                       
                        xx = 1
                        while xx == 1:        
                            self.webEngineView.page().runJavaScript("""document.getElementById('colocarnocarrinho').click();""")
                            sleep(1)
                            if self.webEngineView.loadFinished:
                                self.webEngineView.page().runJavaScript("""if (dialog.className == 'modal fade in') {
                                    document.querySelector("[ng-click='callbackConfirmar[0]()']").click();
                                    ('R');
                                    
                                    }                          
                                    """,0,lambda bounds: llrep.append(bounds))
                            sleep(1)                        
                            lista1 = (str(z).split(' '))                   
                            lista2 = lista1[25].replace(',', '')                        
                            lista3 = int(lista2)               
                            lista4 = lista3 + 1                            
                            lista5 = (str(h).replace('n', ''))                   
                            self.listWidget.addItem(str(lista4) + ' - ' + str(w)+ '  ' + (''.join(llrep)))                            
                            listaJogos.append(str(lista4) + ' - ' + str(w) + '  ' + (''.join(llrep)))
                            llrep.clear()
                            xx = 0                      
                        sleep(1)                       
                        if contagem == final: 
                            self.listWidget.addItem("____________________________________ ")        
                            self.listWidget.addItem("Apostas enviadas para o site.") 
                            sleep(1)                            
                            self.listWidget.addItem("Checando o carrinho no site.")
                            sleep(1)
                            self.readyBounds(args=2)                            
                            sleep(2)    
                            self.listWidget.addItem("                                            ")
                            self.listWidget.addItem("                  " + self.lineEdit_4.text() + "               ") 
                            self.readyBounds(args=3)                            
                            sleep(2)                                                     
                            self.listWidget.addItem("         " + self.lineEdit_3.text() + " Jogos Carregados no site.        ")
                            sleep(1)                           
                            if int(self.lineEdit_3.text()) != final:
                                self.listWidget.addItem("  Apostas não enviadas corretamente.  ") 
                                self.listWidget.addItem("      Verifique o numero de apostas.    ")                                 
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


             