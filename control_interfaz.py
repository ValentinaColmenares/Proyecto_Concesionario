import sys
from Ui_interfaz import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from ProyectoPOO import clienteclass,servicioclass,vehiculoclass,facturasclass,contratoclass
from PIL import Image, ImageOps
from PyQt5.QtCore import Qt, pyqtSignal, QByteArray, QIODevice, QBuffer
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QLineEdit, QFileDialog, QHeaderView, QLabel
from Ui_ventana2 import Ui_ventana2
from Ui_Agregarvehiculo import Ui_dialogo_vehiculo
from Ui_dialogoservicio import Ui_dialogo_servicio
from Ui_dialogo_contrato import Ui_dialogo_contrato 
from reportlab.pdfgen import canvas
import os

directorio= os.getcwd()# para obtener la ruta de la carpeta que contiene el programa



class myapp(QtWidgets.QMainWindow,Ui_MainWindow,Ui_ventana2):
    def __init__(self):
        super(myapp, self).__init__()
        self.path1=""
        self.path2=""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.abrir_bdatos("2","","")
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.ui.b_buscarCliente.clicked.connect(lambda: self.abrir_bdatos("1",self.ui.le_busacarCliente.text(),self.ui.b_buscarCliente))
        self.ui.b_buscarVehiculo.clicked.connect(lambda: self.abrir_bdatos("1",self.ui.le_buscarVehiculo.text(),self.ui.b_buscarVehiculo))
        self.ui.b_buscarServicio.clicked.connect(lambda: self.abrir_bdatos("1",self.ui.le_buscarServicio.text(),self.ui.b_buscarServicio))
        self.ui.b_buscarContrato.clicked.connect(lambda: self.abrir_bdatos("1",self.ui.le_buscarContrato.text(),self.ui.b_buscarContrato))
        self.ui.b_buscarFactura.clicked.connect(lambda: self.abrir_bdatos("1",self.ui.le_BuscarFactura.text(),self.ui.b_buscarFactura))

        self.ui.bactualizarCliente.clicked.connect(lambda: self.abrir_bdatos("2",self.ui.le_busacarCliente.text(),""))
        self.ui.bactualizarVehiculo.clicked.connect(lambda: self.abrir_bdatos("2",self.ui.le_buscarVehiculo.text(),""))
        self.ui.bactualizarcontrato.clicked.connect(lambda: self.abrir_bdatos("2",self.ui.le_buscarVehiculo.text(),""))
        self.ui.bactualizarFacturas.clicked.connect(lambda: self.abrir_bdatos("2",self.ui.le_buscarVehiculo.text(),""))
        self.ui.bactualizarServicio.clicked.connect(lambda: self.abrir_bdatos("2",self.ui.le_buscarVehiculo.text(),""))




        self.ui.bactualizar.clicked.connect(lambda: self.iniciar_dialogo(Ui_ventana2(),clienteclass(),"cliente", False)) # importante usar lambda
        self.ui.ba_servicios.clicked.connect(lambda: self.iniciar_dialogo(Ui_dialogo_servicio(),servicioclass(),"servicios", False))
        self.ui.ba_contratos.clicked.connect(lambda: self.iniciar_dialogo(Ui_dialogo_contrato(),contratoclass(),"contrato", True))
        self.ui.ba_vehiculos.clicked.connect(lambda: self.iniciar_dialogo(Ui_dialogo_vehiculo(),vehiculoclass(),"vehiculo", False))
        self.ui.ba_facturas.clicked.connect(lambda: os.system("start "+directorio+"\Facturas "))
          

    def iniciar_dialogo(self,ventana,clase,origen,imagen): # abre la ventana para tomar datos
            self.ventana=QtWidgets.QMainWindow()
            ventana.setupUi(self.ventana)
            self.ventana.show()
            if imagen == True:
                ventana.badjuntar.clicked.connect(lambda: self.getImage(ventana, 1))
                ventana.badjuntar_2.clicked.connect(lambda: self.getImage(ventana, 2))
            ventana.bguardar.clicked.connect (lambda: self.crear_datos(clase,origen,ventana))#importante usar lambda
    
    def insertImageTable(self, path ,label):

        self.pixmap = QPixmap(path).scaled(266, 278, Qt.KeepAspectRatio,
                                                  Qt.SmoothTransformation)
        
        label.setPixmap((self.pixmap))



    def getImage(self, ventana, label):
        self.fname = QFileDialog.getOpenFileName(parent=None, caption='Open file',directory='c:\'',filter="Image files (*.jpg *.png)")
        #para ajustar la imágen
        self.pixmap = QPixmap(self.fname[0]).scaled(166, 178, Qt.KeepAspectRatio,
                                                  Qt.SmoothTransformation)
                                                  
        self.imagePath = self.fname[0]
        print(self.imagePath)

        if self.imagePath == "":
            _translate = QtCore.QCoreApplication.translate
            if label == 1:
                ventana.lbantes.setText(_translate("dialogo_contrato", "FOTO ANTES"))
            else:
                ventana.lbdespues.setText(_translate("dialogo_contrato", "FOTO DESPUÉS"))
        else:
            if label == 1:
                ventana.lbantes.setPixmap(QPixmap(self.pixmap))
                self.path1=self.imagePath
            else:
                ventana.lbdespues.setPixmap(QPixmap(self.pixmap))
                self.path2=self.imagePath



    def guardarimagen(self,path,num,foto):
            global directorio
            ruta=directorio+"\imagenes"
            img=Image.open(path)
            if foto=="foto1":

                path=(ruta+"\ "+"foto_antes"+str(num)+".jpg")
                img.save(ruta+"\ "+"foto_antes"+str(num)+".jpg") # se guarda la imagèn en la carpeta imagenes del còdigo
            else:
                path=(ruta+"\ "+"foto_despues"+str(num)+".jpg")
                img.save(ruta+"\ "+"foto_despues"+str(num)+".jpg")


            with open("bImagenes.txt", "a") as baseDatos:
                baseDatos.write(path+"\n")# se guarda la imágen en la base de datos con el número de fáctura
                baseDatos.close
    


    def crear_datos(self,clase,origen,ventana): # toma los datos de los qlineedit

        qlines=[child for child in ventana.centralwidget.findChildren(QtWidgets.QLineEdit)]
        qlines=[texto.text() for texto in qlines]
        self.ventana.close() # cierra la venta de diálogo
        

        if origen=="cliente":
            diccionario = clase.creardiccionario(qlines[5],qlines[1],qlines[4],qlines[0],qlines[2],qlines[3])
            clase.guardarInfo(diccionario, "bClientes.txt" )
            self.abrir_bdatos("2","","")

        if origen=="vehiculo":
            diccionario = clase.creardiccionario(qlines[8],qlines[11],qlines[1],qlines[2],qlines[3],qlines[7],qlines[4],qlines[5],qlines[6],qlines[10],qlines[9],qlines[0])
            clase.guardarInfo(diccionario, "bVehiculos.txt" )
            self.abrir_bdatos("2","","")

        if origen== "servicios":
            diccionario = clase.creardiccionario(qlines[0],qlines[1],qlines[2],qlines[3])
            clase.guardarInfo(diccionario, "bServicios.txt" )
            self.abrir_bdatos("2","","")

        if origen== "contrato":
            diccionario = clase.creardiccionario(qlines[3],qlines[2],qlines[0],qlines[1],3)
            servicio=servicioclass()
            contrato=servicio.solServicio(qlines[0],qlines[1],qlines[2],qlines[3])
            if contrato != False:
                cliente = clienteclass()
                cliente.guardarInfo(contrato[0], "bContratos.txt")
                pdf=(contrato[1].split(sep='\n'))
                self.guardarimagen(self.path1,contrato[2],"foto1")
                self.guardarimagen(self.path2,contrato[2],"foto2")
                self.generar_pdf(pdf,contrato[2])
            self.abrir_bdatos("2","","")

    def generar_pdf(self,pdf,numero):
        c = canvas.Canvas(directorio+"\Facturas"+"\Factura"+str(numero)+".pdf")
        x=100
        y=750
        print(pdf)
        for i in pdf:
    
            n=i.split("\t\t")
            for m in n:
                if len(n)==1 and m!='':
                    c.line(x,y,500,y)
                c.drawString(x,y,m)
                y-=20

        file = open("bImagenes.txt", "r")
        j=100
        for ruta in file.readlines(): 
            if str(numero) in ruta: #busca por el número de factura
                if j==100:
                    c.drawString(j,70,"FOTO ANTES")
                else:
                    c.drawString(j,70,"FOTO DESPUÉS",)
                c.drawImage(ruta.replace("\n", ""), j, 100,104, 124)
                j+=200
  
        file.close
        c.save()
        os.system("start "+directorio+"\Facturas"+"\Factura"+str(numero)+".pdf &")

        
    def abrir_bdatos(self, op, noid, boton):
        cliente=clienteclass()
        vehiculo=vehiculoclass()
        servicio=servicioclass()
        contrato=contratoclass()
        factura=facturasclass()

        if op=="2":
            cabecera_c, listac= cliente.datos, clienteclass.leerBase("bClientes.txt",op,noid,False,0)
            cabecera_v, listav= vehiculo.datos, clienteclass.leerBase("bVehiculos.txt",op,noid,False,0)
            cabecera_s, listas= servicio.datos, clienteclass.leerBase("bServicios.txt",op,noid,False,0)
            cabecera_co, listaco= contrato.datos, clienteclass.leerBase("bContratos.txt",op,noid,False,0)
            listaf=clienteclass.leerBase("bFacturas.txt","2","",False,0)

            self.actualizar_tabla(listac,cabecera_c, self.ui.tabladatos)
            self.actualizar_tabla(listaco,cabecera_co, self.ui.tb_contratos)
            self.actualizar_tabla(listas,cabecera_s, self.ui.tb_servicios)
            self.actualizar_tabla(listav,cabecera_v, self.ui.td_vehiculos)
            self.actualizar_tabla(listaf,["factura","foto antes","foto después"], self.ui.tb_facturas)
        else:
            if boton==self.ui.b_buscarCliente:
                cabecera_c, listac= cliente.datos, [(clienteclass.leerBase("bClientes.txt","1",noid,False,0)).split(" ")]
                print(listac)
                self.actualizar_tabla(listac,cabecera_c, self.ui.tabladatos)
            if boton==self.ui.b_buscarVehiculo:
                cabecera_v, listav= vehiculo.datos, [(clienteclass.leerBase("bVehiculos.txt","1",noid,False,0)).split(" ")]
                print(listav)
                self.actualizar_tabla(listav,cabecera_v, self.ui.td_vehiculos)
            if boton== self.ui.b_buscarServicio:
                cabecera_s, listas= servicio.datos, [(clienteclass.leerBase("bServicios.txt","1",noid,False,0)).split(" ")]
                print(listas)
                self.actualizar_tabla(listas,cabecera_s, self.ui.tb_servicios)
            if boton== self.ui.b_buscarContrato:
                cabecera_co, listaco= contrato.datos, [(clienteclass.leerBase("bContratos.txt","1",noid,False,0)).split(" ")]
                self.actualizar_tabla(listaco,cabecera_co, self.ui.tb_contratos)
                
            if boton== self.ui.b_buscarFactura:
                listaf=[[factura.buscarfactura(int(noid))]]
                print(noid)
                print(listaf)
                self.actualizar_tabla(listaf,["facturas","foto antes","foto después"], self.ui.tb_facturas)
            




        


    def actualizar_tabla(self, info, cabecera,tabladatos):

        if info=="Base de datos vacía": # para imprimir una lista vacía en casao de que haya nada en la base de datos
            info=[]
        try:
            if (info[0][0])=="No":
                info=[]
            if (info[0][0])=="No info":
                info=[]
        except:
            pass


        
        tabladatos.setColumnCount(len(cabecera)) #pone el numero de columnas de la tabal
        tabladatos.setRowCount(len(info)) #pone el numero de filas
        tabladatos.setHorizontalHeaderLabels(cabecera)#pone los nombres alas columnas
                # Hacer que la última sección visible del encabezado ocupa todo el espacio disponible
        tabladatos.horizontalHeader().setStretchLastSection ( True )
        tabladatos.setSortingEnabled(True)#ordena por columnas cuando elusuario presiona una columna
        tabladatos.setAlternatingRowColors ( True )
        if len(cabecera)==3:
            tabladatos.horizontalHeader().setStretchLastSection ( False )
            tabladatos.verticalHeader().setDefaultSectionSize(300)
            header_view = tabladatos.horizontalHeader()
            header_view.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)# ajusta el espacio de la celda para que se alcance a ver toda la información
            header_view.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header_view.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)



        if tabladatos== self.ui.tb_facturas:
            file = open("bImagenes.txt", "r")
            listimage=file.readlines()



        fila=0  
        for registro in info:
            columna=0
            for dato in registro:
                if len(registro)==2:
                    cellinfo=QTableWidgetItem(registro[1])
                else:
                    cellinfo=QTableWidgetItem(dato)
                
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEditable)#hace que las celdas no sean editables

                
                if tabladatos== self.ui.tb_facturas:
                    if columna==0:
                        tabladatos.setItem(fila,columna,cellinfo)

                    qlabel= QtWidgets.QLabel()#SE CREA EL QLABEL
                    qlabel2= QtWidgets.QLabel()

                    
                    self.insertImageTable(directorio+"\imagenes"+"\ foto_antes"+str(fila),qlabel)# se llama la funcíon que inserta la imágen en el qlabel
                
                    self.insertImageTable(directorio+"\imagenes"+"\ foto_despues"+str(fila)+".jpg",qlabel2)

                    tabladatos.setCellWidget(fila,1,qlabel)
                    tabladatos.setCellWidget(fila,2,qlabel2)# se inserta el qlabel en la tabla
                    
                else:
                    tabladatos.setItem(fila,columna,cellinfo)
                columna+=1
            fila+=1



        
        
        







app = QtWidgets.QApplication([])
application = myapp()
application.show()
sys.exit(app.exec_())