import sys
from Ui_interfaz import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ProyectoPOO import clienteclass,servicioclass,vehiculoclass,facturasclass,contratoclass
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QLineEdit
from ventana2 import Ui_ventana2
from Ui_Agregarvehiculo import Ui_dialogo_vehculo
from Ui_dialogoservicio import Ui_dialogo_servicio
from Ui_dialogo_contrato import Ui_dialogo_contrato 



class myapp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.abrir_bdatos()
        self.ui.bactualizar.clicked.connect(self.iniciar_dialogo) 
        

        

    def iniciar_dialogo(self): # abre la ventanapara tomar datos
        self.ventana=QtWidgets.QMainWindow()
        self.diaologo=Ui_ventana2()
        self.diaologo.setupUi(self.ventana)
        self.ventana.show()
        self.diaologo.bguardar.clicked.connect (self.crear_datos)
        self.crear_datos()
       
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
        self.abrir_bdatos()
        
    def abrir_bdatos(self):
        cliente=clienteclass()
        vehiculo=vehiculoclass()
        servicio=servicioclass()
        contrato=contratoclass()
        cabecera_c, listac= cliente.datos, clienteclass.leerBase("bClientes.txt","2","",False,0)
        cabecera_v, listav= vehiculo.datos, clienteclass.leerBase("bVehiculos.txt","2","",False,0)
        cabecera_s, listas= servicio.datos, clienteclass.leerBase("bServicios.txt","2","",False,0)
        cabecera_co, listaco= contrato.datos, clienteclass.leerBase("bContratos.txt","2","",False,0)
        self.actualizar_tabla(listac,cabecera_c, self.ui.tabladatos)
        self.actualizar_tabla(listaco,cabecera_co, self.ui.tb_contratos)
        self.actualizar_tabla(listas,cabecera_s, self.ui.tb_servicios)
        self.actualizar_tabla(listav,cabecera_v, self.ui.td_vehiculos)


    def actualizar_tabla(self, info, cabecera,tabladatos):

        if info=="Base de datos vacía": # para imprimir una lista vacía en casao de que haya nada en la base de datos
            info=[]

        print(info)
        tabladatos.setColumnCount(len(cabecera)) #pone el numero de columnas de la tabal
        tabladatos.setRowCount(len(info)) #pone el numero de filas
        tabladatos.setHorizontalHeaderLabels(cabecera)#pone los nombres alas columnas
        tabladatos.setSortingEnabled(True)#ordena por columnas cuando elusuario presiona una columna
           
        fila=0
        for registro in info:
            columna=0
            for dato in registro:
                cellinfo=QTableWidgetItem(dato)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEditable)#hace que las celdas no sean editables
                tabladatos.setItem(fila,columna,cellinfo)
                columna+=1
            fila+=1



        
        
        







app = QtWidgets.QApplication([])
application = myapp()
application.show()
sys.exit(app.exec_())
