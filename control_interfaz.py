import sys
from interfaz import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ProyectoPOO import clienteclass,servicioclass,vehiculoclass,facturasclass,contratoclass
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QLineEdit
from ventana2 import Ui_ventana2



class myapp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.actualizar_tabla()
        self.crear_datos
        self.ui.bactualizar.clicked.connect(self.iniciar_dialogo) 
        

    def iniciar_dialogo(self): # abre la ventanapara tomar datos
        self.ventana=QtWidgets.QMainWindow()
        self.diaologo=Ui_ventana2()
        self.diaologo.setupUi(self.ventana)
        self.ventana.show()
        self.diaologo.bguardar.clicked.connect (self.crear_datos)
        self.crear_datos
       
    def crear_datos(self): # toma los datos de los qlineedit
        cliente = clienteclass()
        cliente.setIdcliente(self.diaologo.le_cliente.text())
        cliente.setNombre(self.diaologo.lenombre.text())
        cliente.setapellid(self.diaologo.leapellido.text())
        cliente.setDireccion(self.diaologo.ledireccion.text())
        cliente.setTelefono((self.diaologo.lecelular.text()))
        cliente.setCiudad(self.diaologo.leciudad.text())
        diccionario = cliente.creardiccionario(cliente.getidcliente(),cliente.getNombre(), cliente.getapellid(),cliente.getDireccion(), cliente.getTelefono(), cliente.getCiudad())
        cliente.guardarInfo(diccionario, "bClientes.txt" )
        self.actualizar_tabla()
        
    def actualizar_tabla(self):
        cliente=clienteclass()
        diccionario=cliente.diccionario
        cabecera=diccionario.keys()
        lista=clienteclass.leerBase("bClientes.txt","2","",False,0)

        if lista=="Base de datos vacía":
            lista=[]
        print(lista)
        self.ui.tabladatos.setColumnCount(len(cabecera)) #pone el numero de columnas de la tabal
        self.ui.tabladatos.setRowCount(len(lista)) #pone el numero de filas
        self.ui.tabladatos.setHorizontalHeaderLabels(["ID-Cliente", "Nombre", "Apellido","Dirección", "Telefono", "Ciudad"])#pone los nombres alas columnas
        self.ui.tabladatos.setSortingEnabled(True)#ordena por columnas cuando elusuario presiona una columna
           
        fila=0
        for registro in lista:
            columna=0
            for dato in registro:
                cellinfo=QTableWidgetItem(dato)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEditable)#hace que las celdas no sean editables
                self.ui.tabladatos.setItem(fila,columna,cellinfo)
                columna+=1
            fila+=1



        
        
        







app = QtWidgets.QApplication([])
application = myapp()
application.show()
sys.exit(app.exec_())
