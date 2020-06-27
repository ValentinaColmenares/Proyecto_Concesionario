# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogo_clientes.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adduser(object):
    def setupUi(self, adduser):
        adduser.setObjectName("adduser")
        adduser.resize(590, 329)
        self.horizontalLayout = QtWidgets.QHBoxLayout(adduser)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(adduser)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbIdcliente = QtWidgets.QLabel(self.widget)
        self.lbIdcliente.setObjectName("lbIdcliente")
        self.gridLayout.addWidget(self.lbIdcliente, 0, 0, 1, 1)
        self.lbNombre = QtWidgets.QLabel(self.widget)
        self.lbNombre.setObjectName("lbNombre")
        self.gridLayout.addWidget(self.lbNombre, 1, 0, 1, 1)
        self.le_cliente_4 = QtWidgets.QLineEdit(self.widget)
        self.le_cliente_4.setObjectName("le_cliente_4")
        self.gridLayout.addWidget(self.le_cliente_4, 2, 1, 1, 1)
        self.le_cliente = QtWidgets.QLineEdit(self.widget)
        self.le_cliente.setObjectName("le_cliente")
        self.gridLayout.addWidget(self.le_cliente, 0, 1, 1, 1)
        self.lbapellido = QtWidgets.QLabel(self.widget)
        self.lbapellido.setObjectName("lbapellido")
        self.gridLayout.addWidget(self.lbapellido, 2, 0, 1, 1)
        self.le_cliente_5 = QtWidgets.QLineEdit(self.widget)
        self.le_cliente_5.setObjectName("le_cliente_5")
        self.gridLayout.addWidget(self.le_cliente_5, 1, 1, 1, 1)
        self.Lbcelular = QtWidgets.QLabel(self.widget)
        self.Lbcelular.setObjectName("Lbcelular")
        self.gridLayout.addWidget(self.Lbcelular, 4, 0, 1, 1)
        self.lbdireccion = QtWidgets.QLabel(self.widget)
        self.lbdireccion.setObjectName("lbdireccion")
        self.gridLayout.addWidget(self.lbdireccion, 3, 0, 1, 1)
        self.lbciudad = QtWidgets.QLabel(self.widget)
        self.lbciudad.setObjectName("lbciudad")
        self.gridLayout.addWidget(self.lbciudad, 6, 0, 1, 1)
        self.le_cliente_6 = QtWidgets.QLineEdit(self.widget)
        self.le_cliente_6.setObjectName("le_cliente_6")
        self.gridLayout.addWidget(self.le_cliente_6, 6, 1, 1, 1)
        self.le_cliente_3 = QtWidgets.QLineEdit(self.widget)
        self.le_cliente_3.setObjectName("le_cliente_3")
        self.gridLayout.addWidget(self.le_cliente_3, 3, 1, 1, 1)
        self.le_cliente_2 = QtWidgets.QLineEdit(self.widget)
        self.le_cliente_2.setObjectName("le_cliente_2")
        self.gridLayout.addWidget(self.le_cliente_2, 4, 1, 1, 1)
        self.bguardar = QtWidgets.QPushButton(self.widget)
        self.bguardar.setObjectName("bguardar")
        self.gridLayout.addWidget(self.bguardar, 7, 1, 1, 1)
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(adduser)
        QtCore.QMetaObject.connectSlotsByName(adduser)

    def retranslateUi(self, adduser):
        _translate = QtCore.QCoreApplication.translate
        adduser.setWindowTitle(_translate("adduser", "Dialog"))
        self.lbIdcliente.setText(_translate("adduser", "Id-Cliente"))
        self.lbNombre.setText(_translate("adduser", "Nombre"))
        self.lbapellido.setText(_translate("adduser", "apellido"))
        self.Lbcelular.setText(_translate("adduser", "celular"))
        self.lbdireccion.setText(_translate("adduser", "dirección"))
        self.lbciudad.setText(_translate("adduser", "ciudad"))
        self.bguardar.setText(_translate("adduser", "Guardar"))
