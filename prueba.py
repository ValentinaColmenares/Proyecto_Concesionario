# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_prueba(object):
    def setupUi(self, prueba):
        prueba.setObjectName("prueba")
        prueba.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(prueba)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(prueba)
        self.buttonBox.rejected.connect(prueba.reject)
        QtCore.QMetaObject.connectSlotsByName(prueba)

    def retranslateUi(self, prueba):
        _translate = QtCore.QCoreApplication.translate
        prueba.setWindowTitle(_translate("prueba", "Dialog"))
