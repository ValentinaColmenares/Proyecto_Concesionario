# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\aldo\Documents\GitHub\Proyecto_Concesionario\interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(596, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Modulos = QtWidgets.QTabWidget(self.centralwidget)
        self.Modulos.setObjectName("Modulos")
        self.usuarios = QtWidgets.QWidget()
        self.usuarios.setObjectName("usuarios")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.usuarios)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.usuarios)
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabladatos = QtWidgets.QTableWidget(self.usuarios)
        self.tabladatos.setObjectName("tabladatos")
        self.tabladatos.setColumnCount(0)
        self.tabladatos.setRowCount(0)
        self.verticalLayout.addWidget(self.tabladatos)
        self.bactualizar = QtWidgets.QPushButton(self.usuarios)
        self.bactualizar.setEnabled(True)
        self.bactualizar.setObjectName("bactualizar")
        self.verticalLayout.addWidget(self.bactualizar)
        self.verticalLayout_9.addLayout(self.verticalLayout)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.Modulos.addTab(self.usuarios, "")
        self.vehiculos = QtWidgets.QWidget()
        self.vehiculos.setObjectName("vehiculos")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.vehiculos)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_9 = QtWidgets.QLabel(self.vehiculos)
        self.label_9.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_12.addWidget(self.label_9)
        self.td_vehiculos = QtWidgets.QTableWidget(self.vehiculos)
        self.td_vehiculos.setObjectName("td_vehiculos")
        self.td_vehiculos.setColumnCount(0)
        self.td_vehiculos.setRowCount(0)
        self.verticalLayout_12.addWidget(self.td_vehiculos)
        self.ba_vehiculos = QtWidgets.QPushButton(self.vehiculos)
        self.ba_vehiculos.setEnabled(True)
        self.ba_vehiculos.setObjectName("ba_vehiculos")
        self.verticalLayout_12.addWidget(self.ba_vehiculos)
        self.Modulos.addTab(self.vehiculos, "")
        self.servicios = QtWidgets.QWidget()
        self.servicios.setObjectName("servicios")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.servicios)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.servicios)
        self.label_10.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_13.addWidget(self.label_10)
        self.tb_servicios = QtWidgets.QTableWidget(self.servicios)
        self.tb_servicios.setObjectName("tb_servicios")
        self.tb_servicios.setColumnCount(0)
        self.tb_servicios.setRowCount(0)
        self.verticalLayout_13.addWidget(self.tb_servicios)
        self.ba_servicios = QtWidgets.QPushButton(self.servicios)
        self.ba_servicios.setEnabled(True)
        self.ba_servicios.setObjectName("ba_servicios")
        self.verticalLayout_13.addWidget(self.ba_servicios)
        self.Modulos.addTab(self.servicios, "")
        self.contratos = QtWidgets.QWidget()
        self.contratos.setObjectName("contratos")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.contratos)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_11 = QtWidgets.QLabel(self.contratos)
        self.label_11.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_14.addWidget(self.label_11)
        self.tb_contratos = QtWidgets.QTableWidget(self.contratos)
        self.tb_contratos.setObjectName("tb_contratos")
        self.tb_contratos.setColumnCount(0)
        self.tb_contratos.setRowCount(0)
        self.verticalLayout_14.addWidget(self.tb_contratos)
        self.ba_contratos = QtWidgets.QPushButton(self.contratos)
        self.ba_contratos.setEnabled(True)
        self.ba_contratos.setObjectName("ba_contratos")
        self.verticalLayout_14.addWidget(self.ba_contratos)
        self.Modulos.addTab(self.contratos, "")
        self.facturas = QtWidgets.QWidget()
        self.facturas.setObjectName("facturas")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.facturas)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_12 = QtWidgets.QLabel(self.facturas)
        self.label_12.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_15.addWidget(self.label_12)
        self.tb_facturas = QtWidgets.QTableWidget(self.facturas)
        self.tb_facturas.setObjectName("tb_facturas")
        self.tb_facturas.setColumnCount(0)
        self.tb_facturas.setRowCount(0)
        self.verticalLayout_15.addWidget(self.tb_facturas)
        self.ba_facturas = QtWidgets.QPushButton(self.facturas)
        self.ba_facturas.setEnabled(True)
        self.ba_facturas.setObjectName("ba_facturas")
        self.verticalLayout_15.addWidget(self.ba_facturas)
        self.Modulos.addTab(self.facturas, "")
        self.verticalLayout_11.addWidget(self.Modulos)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Modulos.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "consecionario"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Base de datos de clientes</p></body></html>"))
        self.bactualizar.setText(_translate("MainWindow", "Agregar cliente"))
        self.Modulos.setTabText(self.Modulos.indexOf(self.usuarios), _translate("MainWindow", "Usuario"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Base de datos de Vehículos</p></body></html>"))
        self.ba_vehiculos.setText(_translate("MainWindow", "Agregar  vehículo"))
        self.Modulos.setTabText(self.Modulos.indexOf(self.vehiculos), _translate("MainWindow", "Vehículos"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Base de datos de Servicios</p></body></html>"))
        self.ba_servicios.setText(_translate("MainWindow", "Agregar servicio"))
        self.Modulos.setTabText(self.Modulos.indexOf(self.servicios), _translate("MainWindow", "Servicios"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Base de datos de Contratos</p></body></html>"))
        self.ba_contratos.setText(_translate("MainWindow", "Agregar contrato"))
        self.Modulos.setTabText(self.Modulos.indexOf(self.contratos), _translate("MainWindow", "Contratos"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Base de datos de Facturas</p></body></html>"))
        self.ba_facturas.setText(_translate("MainWindow", "Ver facturas"))
        self.Modulos.setTabText(self.Modulos.indexOf(self.facturas), _translate("MainWindow", "Facturas"))