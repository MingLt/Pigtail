# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pattern.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1039, 757)
        Dialog.setMinimumSize(QtCore.QSize(1039, 757))
        Dialog.setMaximumSize(QtCore.QSize(1039, 757))
        Dialog.setStyleSheet("")
        self.local = QtWidgets.QPushButton(Dialog)
        self.local.setGeometry(QtCore.QRect(90, 180, 231, 331))
        self.local.setStyleSheet("border-image:url(:/gamei/-2.png);\n"
"")
        self.local.setText("")
        self.local.setObjectName("local")
        self.machine = QtWidgets.QPushButton(Dialog)
        self.machine.setGeometry(QtCore.QRect(390, 180, 231, 331))
        self.machine.setStyleSheet("border-image:url(:/gamei/-3.png);\n"
"")
        self.machine.setText("")
        self.machine.setObjectName("machine")
        self.online = QtWidgets.QPushButton(Dialog)
        self.online.setGeometry(QtCore.QRect(700, 180, 231, 331))
        self.online.setStyleSheet("border-image:url(:/gamei/-4.png);\n"
"")
        self.online.setText("")
        self.online.setObjectName("online")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 757))
        self.label.setMinimumSize(QtCore.QSize(1024, 757))
        self.label.setMaximumSize(QtCore.QSize(1024, 757))
        self.label.setStyleSheet("QLabel\n"
"{\n"
"border-image: url(:/images/background.png);\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.local.raise_()
        self.machine.raise_()
        self.online.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
import apprcc_rc
import gamercc_rc
