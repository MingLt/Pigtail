from PyQt5 import QtCore, QtGui, QtWidgets
import apprcc_rc


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 757)
        Dialog.setMinimumSize(QtCore.QSize(1024, 757))
        Dialog.setMaximumSize(QtCore.QSize(1024, 757))
        Dialog.setStyleSheet("QDialog{border-image:url(:/images/firstback.png)}\n"
                             "QLabel{border-image:url()}")
        self.u = QtWidgets.QLabel(Dialog)
        self.u.setGeometry(QtCore.QRect(340, 260, 61, 71))
        self.u.setText("")
        self.u.setPixmap(QtGui.QPixmap(":/images/username.png"))
        self.u.setObjectName("u")
        self.usernameEdit = QtWidgets.QLineEdit(Dialog)
        self.usernameEdit.setGeometry(QtCore.QRect(430, 270, 281, 51))
        self.usernameEdit.setStyleSheet("QLineEdit\n"
                                        "{\n"
                                        "background-color:rgba(255,255,255,180);\n"
                                        "border:none;\n"
                                        "font: 12pt \"3ds\";\n"
                                        "color:#55007f;\n"
                                        "}")
        self.usernameEdit.setText("")
        self.usernameEdit.setFrame(True)
        self.usernameEdit.setObjectName("usernameEdit")
        self.p = QtWidgets.QLabel(Dialog)
        self.p.setGeometry(QtCore.QRect(340, 360, 61, 71))
        self.p.setText("")
        self.p.setPixmap(QtGui.QPixmap(":/images/psw.png"))
        self.p.setObjectName("p")
        self.pswEdit = QtWidgets.QLineEdit(Dialog)
        self.pswEdit.setGeometry(QtCore.QRect(430, 370, 281, 51))
        self.pswEdit.setStyleSheet("QLineEdit\n"
                                   "{\n"
                                   "background-color:rgba(255,255,255,180);\n"
                                   "border:none;\n"
                                   "font: 12pt \"3ds\";\n"
                                   "color:#55007f;\n"
                                   "}")
        self.pswEdit.setText("")
        self.pswEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pswEdit.setObjectName("pswEdit")
        self.pushbutton = QtWidgets.QPushButton(Dialog)
        self.pushbutton.setGeometry(QtCore.QRect(380, 500, 281, 51))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushbutton.setFont(font)
        self.pushbutton.setStyleSheet("QPushButton\n"
                                      "{\n"
                                      "background-color:rgb(56, 182, 137,200);\n"
                                      "color:#FFFFFF;\n"
                                      "font: 12pt \"3ds\";\n"
                                      "}")
        self.pushbutton.setObjectName("pushbutton")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.usernameEdit.setPlaceholderText(_translate("Dialog", "请输入账号......"))
        self.pushbutton.setText(_translate("Dialog", "登      录"))


def main():
    a = Ui_Dialog()

    a.setupUi(Dialog)


if __name__ == '__main__':
    main()
