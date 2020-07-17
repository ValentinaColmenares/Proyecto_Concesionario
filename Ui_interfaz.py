# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Claudia\Documents\GitHub\Proyecto_Concesionario\interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Modulos = QtWidgets.QTabWidget(self.centralwidget)
        self.Modulos.setObjectName("Modulos")
        self.usuarios = QtWidgets.QWidget()
        self.usuarios.setObjectName("usuarios")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.usuarios)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bactualizar = QtWidgets.QPushButton(self.usuarios)
        self.bactualizar.setEnabled(True)
        self.bactualizar.setObjectName("bactualizar")
        self.gridLayout_2.addWidget(self.bactualizar, 4, 0, 1, 2)
        self.tabladatos = QtWidgets.QTableWidget(self.usuarios)
        self.tabladatos.setObjectName("tabladatos")
        self.tabladatos.setColumnCount(0)
        self.tabladatos.setRowCount(0)
        self.gridLayout_2.addWidget(self.tabladatos, 3, 0, 1, 2)
        self.le_busacarCliente = QtWidgets.QLineEdit(self.usuarios)
        self.le_busacarCliente.setObjectName("le_busacarCliente")
        self.gridLayout_2.addWidget(self.le_busacarCliente, 1, 1, 1, 1)
        self.b_buscarCliente = QtWidgets.QPushButton(self.usuarios)
        self.b_buscarCliente.setObjectName("b_buscarCliente")
        self.gridLayout_2.addWidget(self.b_buscarCliente, 1, 0, 1, 1)
        self.bactualizarCliente = QtWidgets.QPushButton(self.usuarios)
        self.bactualizarCliente.setObjectName("bactualizarCliente")
        self.gridLayout_2.addWidget(self.bactualizarCliente, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.usuarios)
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.Modulos.addTab(self.usuarios, "")
        self.vehiculos = QtWidgets.QWidget()
        self.vehiculos.setObjectName("vehiculos")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.vehiculos)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ba_vehiculos = QtWidgets.QPushButton(self.vehiculos)
        self.ba_vehiculos.setEnabled(True)
        self.ba_vehiculos.setObjectName("ba_vehiculos")
        self.gridLayout_3.addWidget(self.ba_vehiculos, 4, 0, 1, 2)
        self.le_buscarVehiculo = QtWidgets.QLineEdit(self.vehiculos)
        self.le_buscarVehiculo.setObjectName("le_buscarVehiculo")
        self.gridLayout_3.addWidget(self.le_buscarVehiculo, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.vehiculos)
        self.label_9.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 2)
        self.bactualizarVehiculo = QtWidgets.QPushButton(self.vehiculos)
        self.bactualizarVehiculo.setObjectName("bactualizarVehiculo")
        self.gridLayout_3.addWidget(self.bactualizarVehiculo, 2, 0, 1, 2)
        self.b_buscarVehiculo = QtWidgets.QPushButton(self.vehiculos)
        self.b_buscarVehiculo.setObjectName("b_buscarVehiculo")
        self.gridLayout_3.addWidget(self.b_buscarVehiculo, 1, 0, 1, 1)
        self.td_vehiculos = QtWidgets.QTableWidget(self.vehiculos)
        self.td_vehiculos.setObjectName("td_vehiculos")
        self.td_vehiculos.setColumnCount(0)
        self.td_vehiculos.setRowCount(0)
        self.gridLayout_3.addWidget(self.td_vehiculos, 3, 0, 1, 2)
        self.Modulos.addTab(self.vehiculos, "")
        self.servicios = QtWidgets.QWidget()
        self.servicios.setObjectName("servicios")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.servicios)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tb_servicios = QtWidgets.QTableWidget(self.servicios)
        self.tb_servicios.setObjectName("tb_servicios")
        self.tb_servicios.setColumnCount(0)
        self.tb_servicios.setRowCount(0)
        self.gridLayout_4.addWidget(self.tb_servicios, 3, 0, 1, 2)
        self.b_buscarServicio = QtWidgets.QPushButton(self.servicios)
        self.b_buscarServicio.setObjectName("b_buscarServicio")
        self.gridLayout_4.addWidget(self.b_buscarServicio, 1, 0, 1, 1)
        self.ba_servicios = QtWidgets.QPushButton(self.servicios)
        self.ba_servicios.setEnabled(True)
        self.ba_servicios.setObjectName("ba_servicios")
        self.gridLayout_4.addWidget(self.ba_servicios, 4, 0, 1, 2)
        self.le_buscarServicio = QtWidgets.QLineEdit(self.servicios)
        self.le_buscarServicio.setObjectName("le_buscarServicio")
        self.gridLayout_4.addWidget(self.le_buscarServicio, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.servicios)
        self.label_10.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 2)
        self.bactualizarServicio = QtWidgets.QPushButton(self.servicios)
        self.bactualizarServicio.setObjectName("bactualizarServicio")
        self.gridLayout_4.addWidget(self.bactualizarServicio, 2, 0, 1, 2)
        self.Modulos.addTab(self.servicios, "")
        self.contratos = QtWidgets.QWidget()
        self.contratos.setObjectName("contratos")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.contratos)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tb_contratos = QtWidgets.QTableWidget(self.contratos)
        self.tb_contratos.setObjectName("tb_contratos")
        self.tb_contratos.setColumnCount(0)
        self.tb_contratos.setRowCount(0)
        self.gridLayout_5.addWidget(self.tb_contratos, 3, 0, 1, 2)
        self.b_buscarContrato = QtWidgets.QPushButton(self.contratos)
        self.b_buscarContrato.setObjectName("b_buscarContrato")
        self.gridLayout_5.addWidget(self.b_buscarContrato, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.contratos)
        self.label_11.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 2)
        self.ba_contratos = QtWidgets.QPushButton(self.contratos)
        self.ba_contratos.setEnabled(True)
        self.ba_contratos.setObjectName("ba_contratos")
        self.gridLayout_5.addWidget(self.ba_contratos, 4, 0, 1, 2)
        self.le_buscarContrato = QtWidgets.QLineEdit(self.contratos)
        self.le_buscarContrato.setObjectName("le_buscarContrato")
        self.gridLayout_5.addWidget(self.le_buscarContrato, 1, 1, 1, 1)
        self.bactualizarcontrato = QtWidgets.QPushButton(self.contratos)
        self.bactualizarcontrato.setObjectName("bactualizarcontrato")
        self.gridLayout_5.addWidget(self.bactualizarcontrato, 2, 0, 1, 2)
        self.Modulos.addTab(self.contratos, "")
        self.facturas = QtWidgets.QWidget()
        self.facturas.setObjectName("facturas")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.facturas)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.b_buscarFactura = QtWidgets.QPushButton(self.facturas)
        self.b_buscarFactura.setObjectName("b_buscarFactura")
        self.gridLayout_6.addWidget(self.b_buscarFactura, 1, 0, 1, 1)
        self.le_BuscarFactura = QtWidgets.QLineEdit(self.facturas)
        self.le_BuscarFactura.setObjectName("le_BuscarFactura")
        self.gridLayout_6.addWidget(self.le_BuscarFactura, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.facturas)
        self.label_12.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 0, 0, 1, 2)
        self.ba_facturas = QtWidgets.QPushButton(self.facturas)
        self.ba_facturas.setEnabled(True)
        self.ba_facturas.setObjectName("ba_facturas")
        self.gridLayout_6.addWidget(self.ba_facturas, 4, 0, 1, 2)
        self.bactualizarFacturas = QtWidgets.QPushButton(self.facturas)
        self.bactualizarFacturas.setObjectName("bactualizarFacturas")
        self.gridLayout_6.addWidget(self.bactualizarFacturas, 2, 0, 1, 2)
        self.tb_facturas = QtWidgets.QTableWidget(self.facturas)
        self.tb_facturas.setObjectName("tb_facturas")
        self.tb_facturas.setColumnCount(0)
        self.tb_facturas.setRowCount(0)
        self.gridLayout_6.addWidget(self.tb_facturas, 3, 0, 1, 2)
        self.Modulos.addTab(self.facturas, "")
        self.gridLayout.addWidget(self.Modulos, 0, 0, 1, 1)
        self.bSalir = QtWidgets.QPushButton(self.centralwidget)
        self.bSalir.setObjectName("bSalir")
        self.gridLayout.addWidget(self.bSalir, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Modulos.setCurrentIndex(0)
        self.bSalir.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Modulos, self.b_buscarCliente)
        MainWindow.setTabOrder(self.b_buscarCliente, self.le_busacarCliente)
        MainWindow.setTabOrder(self.le_busacarCliente, self.bactualizarCliente)
        MainWindow.setTabOrder(self.bactualizarCliente, self.tabladatos)
        MainWindow.setTabOrder(self.tabladatos, self.bactualizar)
        MainWindow.setTabOrder(self.bactualizar, self.bSalir)
        MainWindow.setTabOrder(self.bSalir, self.le_buscarVehiculo)
        MainWindow.setTabOrder(self.le_buscarVehiculo, self.ba_vehiculos)
        MainWindow.setTabOrder(self.ba_vehiculos, self.td_vehiculos)
        MainWindow.setTabOrder(self.td_vehiculos, self.bactualizarVehiculo)
        MainWindow.setTabOrder(self.bactualizarVehiculo, self.b_buscarServicio)
        MainWindow.setTabOrder(self.b_buscarServicio, self.le_buscarServicio)
        MainWindow.setTabOrder(self.le_buscarServicio, self.tb_servicios)
        MainWindow.setTabOrder(self.tb_servicios, self.ba_servicios)
        MainWindow.setTabOrder(self.ba_servicios, self.bactualizarServicio)
        MainWindow.setTabOrder(self.bactualizarServicio, self.tb_contratos)
        MainWindow.setTabOrder(self.tb_contratos, self.b_buscarContrato)
        MainWindow.setTabOrder(self.b_buscarContrato, self.ba_contratos)
        MainWindow.setTabOrder(self.ba_contratos, self.le_buscarContrato)
        MainWindow.setTabOrder(self.le_buscarContrato, self.bactualizarcontrato)
        MainWindow.setTabOrder(self.bactualizarcontrato, self.le_BuscarFactura)
        MainWindow.setTabOrder(self.le_BuscarFactura, self.b_buscarFactura)
        MainWindow.setTabOrder(self.b_buscarFactura, self.tb_facturas)
        MainWindow.setTabOrder(self.tb_facturas, self.ba_facturas)
        MainWindow.setTabOrder(self.ba_facturas, self.bactualizarFacturas)
        MainWindow.setTabOrder(self.bactualizarFacturas, self.b_buscarVehiculo)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Concesionario"))
        self.bactualizar.setText(_translate("MainWindow", "Agregar cliente"))
        self.b_buscarCliente.setText(_translate("MainWindow", "Buscar cliente"))
        self.bactualizarCliente.setText(_translate("MainWindow", "Mostrar base de datos completa"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Base de datos de clientes</p></body></html>"))
        self.Modulos.setTabText(self.Modulos.indexOf(self.usuarios), _translate("MainWindow", "Usuario"))
        self.ba_vehiculos.setText(_translate("MainWindow", "Agregar vehículo"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Base de datos de Vehículos</p></body></html>"))
        self.bactualizarVehiculo.setText(_translate("MainWindow", "Actualizar"))
        self.b_buscarVehiculo.setText(_translate("MainWindow", "Buscar vehículo"))
        self.Modulos.setTabText(self.Modulos.indexOf(self.vehiculos), _translate("MainWindow", "Vehículos"))
        self.b_buscarServicio.setText(_translate("MainWindow", "Buscar servicio"))
        self.ba_servicios.setText(_translate("MainWindow", "Agregar servicio"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Base de datos de Servicios</p></body></html>"))
        self.bactualizarServicio.setText(_translate("MainWindow", "Actualizar"))
        self.Modulos.setTabText(self.Modulos.indexOf(self.servicios), _translate("MainWindow", "Servicios"))
        self.b_buscarContrato.setText(_translate("MainWindow", "Buscar Contrato"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Base de datos de Contratos</p></body></html>"))
        self.ba_contratos.setText(_translate("MainWindow", "Agregar contrato"))
        self.bactualizarcontrato.setText(_translate("MainWindow", "Actualizar"))
        self.Modulos.setTabText(self.Modulos.indexOf(self.contratos), _translate("MainWindow", "Contratos"))
        self.b_buscarFactura.setText(_translate("MainWindow", "Buscar factura"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Base de datos de Facturas</p></body></html>"))
        self.ba_facturas.setText(_translate("MainWindow", "Ver facturas"))
        self.bactualizarFacturas.setText(_translate("MainWindow", "Actualizar"))
        self.Modulos.setTabText(self.Modulos.indexOf(self.facturas), _translate("MainWindow", "Facturas"))
        self.bSalir.setText(_translate("MainWindow", "Salir"))
