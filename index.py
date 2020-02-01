# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from admin import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox

class Ui_loginform(object):
    def login(self):
            
        a=self.lineEdit.text()
        b=self.lineEdit_2.text()
        if (a=='admin' and b=='admin123'):
                
            self.Main = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.Main)
            self.Main.show()
            
        else:
               
            QMessageBox.critical(None, "error!!!!!",
            "incorrect user name or password",
            QMessageBox.Cancel)
       
    def setupUi(self, loginform):
        loginform.setObjectName("loginform")
        loginform.resize(447, 300)
        self.pushButton = QtWidgets.QPushButton(loginform)
        self.pushButton.setGeometry(QtCore.QRect(180, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(loginform)
        self.lineEdit.setGeometry(QtCore.QRect(140, 90, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(loginform)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 140, 191, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label = QtWidgets.QLabel(loginform)
        self.label.setGeometry(QtCore.QRect(60, 100, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(loginform)
        self.label_2.setGeometry(QtCore.QRect(60, 150, 47, 13))
        self.label_2.setObjectName("label_2")
        self.pushButton.clicked.connect(self.login)

        self.retranslateUi(loginform)
        QtCore.QMetaObject.connectSlotsByName(loginform)

    def retranslateUi(self, loginform):
        _translate = QtCore.QCoreApplication.translate
        loginform.setWindowTitle(_translate("loginform", "login"))
        self.pushButton.setText(_translate("loginform", "LOGIN"))
        self.label.setText(_translate("loginform", "ID"))
        self.label_2.setText(_translate("loginform", "password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginform = QtWidgets.QWidget()
    ui = Ui_loginform()
    ui.setupUi(loginform)
    loginform.show()
    sys.exit(app.exec_())

