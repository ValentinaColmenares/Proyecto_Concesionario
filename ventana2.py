# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana2(object):
    def setupUi(self, ventana2):
        ventana2.setObjectName("ventana2")
        ventana2.resize(444, 350)
        self.centralwidget = QtWidgets.QWidget(ventana2)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbNombre = QtWidgets.QLabel(self.layoutWidget)
        self.lbNombre.setObjectName("lbNombre")
        self.gridLayout.addWidget(self.lbNombre, 1, 0, 1, 1)
        self.lbapellido = QtWidgets.QLabel(self.layoutWidget)
        self.lbapellido.setObjectName("lbapellido")
        self.gridLayout.addWidget(self.lbapellido, 2, 0, 1, 1)
        self.lbdireccion = QtWidgets.QLabel(self.layoutWidget)
        self.lbdireccion.setObjectName("lbdireccion")
        self.gridLayout.addWidget(self.lbdireccion, 3, 0, 1, 1)
        self.lbIdcliente = QtWidgets.QLabel(self.layoutWidget)
        self.lbIdcliente.setObjectName("lbIdcliente")
        self.gridLayout.addWidget(self.lbIdcliente, 0, 0, 1, 1)
        self.ledireccion = QtWidgets.QLineEdit(self.layoutWidget)
        self.ledireccion.setObjectName("ledireccion")
        self.gridLayout.addWidget(self.ledireccion, 3, 1, 1, 1)
        self.Lbcelular = QtWidgets.QLabel(self.layoutWidget)
        self.Lbcelular.setObjectName("Lbcelular")
        self.gridLayout.addWidget(self.Lbcelular, 4, 0, 1, 1)
        self.lbciudad = QtWidgets.QLabel(self.layoutWidget)
        self.lbciudad.setObjectName("lbciudad")
        self.gridLayout.addWidget(self.lbciudad, 6, 0, 1, 1)
        self.lenombre = QtWidgets.QLineEdit(self.layoutWidget)
        self.lenombre.setObjectName("lenombre")
        self.gridLayout.addWidget(self.lenombre, 1, 1, 1, 1)
        self.lecelular = QtWidgets.QLineEdit(self.layoutWidget)
        self.lecelular.setObjectName("lecelular")
        self.gridLayout.addWidget(self.lecelular, 4, 1, 1, 1)
        self.leciudad = QtWidgets.QLineEdit(self.layoutWidget)
        self.leciudad.setObjectName("leciudad")
        self.gridLayout.addWidget(self.leciudad, 6, 1, 1, 1)
        self.leapellido = QtWidgets.QLineEdit(self.layoutWidget)
        self.leapellido.setObjectName("leapellido")
        self.gridLayout.addWidget(self.leapellido, 2, 1, 1, 1)
        self.bguardar = QtWidgets.QPushButton(self.layoutWidget)
        self.bguardar.setEnabled(True)
        self.bguardar.setAutoDefault(False)
        self.bguardar.setDefault(False)
        self.bguardar.setFlat(False)
        self.bguardar.setObjectName("bguardar")
        self.gridLayout.addWidget(self.bguardar, 7, 1, 1, 1)
        self.le_cliente = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_cliente.setObjectName("le_cliente")
        self.gridLayout.addWidget(self.le_cliente, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.splitter)
        ventana2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ventana2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 444, 21))
        self.menubar.setObjectName("menubar")
        ventana2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ventana2)
        self.statusbar.setObjectName("statusbar")
        ventana2.setStatusBar(self.statusbar)

        self.retranslateUi(ventana2)
        QtCore.QMetaObject.connectSlotsByName(ventana2)

    def retranslateUi(self, ventana2):
        _translate = QtCore.QCoreApplication.translate
        ventana2.setWindowTitle(_translate("ventana2", "MainWindow"))
        self.lbNombre.setText(_translate("ventana2", "Nombre"))
        self.lbapellido.setText(_translate("ventana2", "apellido"))
        self.lbdireccion.setText(_translate("ventana2", "dirección"))
        self.lbIdcliente.setText(_translate("ventana2", "Id-Cliente"))
        self.Lbcelular.setText(_translate("ventana2", "celular"))
        self.lbciudad.setText(_translate("ventana2", "ciudad"))
        self.bguardar.setText(_translate("ventana2", "Guardar"))