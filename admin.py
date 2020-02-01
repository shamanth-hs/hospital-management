# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import app
import sqlite3
import webbrowser
import os
from subprocess import Popen
import psutil

class Ui_MainWindow(object):
    def runserver(self):
        Popen('python app.py')
        
        
    def openbrowser(self):
        webbrowser.open("http://127.0.0.1:5000")
    def showtrigger(self):
        cn=sqlite3.connect("database.db")
        result=cn.execute("select * from doc_logs")
        
       
        self.tableWidget.setRowCount(1)
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number+1)
            for coln_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number+1,coln_number,QtWidgets.QTableWidgetItem(str(data)))
        self.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem("ID"))
        self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem("NAME"))
        self.tableWidget.setItem(0,2,QtWidgets.QTableWidgetItem("OLD PHONE"))
        self.tableWidget.setItem(0,3,QtWidgets.QTableWidgetItem("NEW PHONE"))
        self.tableWidget.setItem(0,4,QtWidgets.QTableWidgetItem("OLD ADDRESS"))
        self.tableWidget.setItem(0,5,QtWidgets.QTableWidgetItem("NEW ADDRESS"))
        self.tableWidget.setItem(0,6,QtWidgets.QTableWidgetItem("ACTION"))
        self.tableWidget.setItem(0,7,QtWidgets.QTableWidgetItem("CHANGED AT"))
        cn.close()
    def stopserver(self):
        #print('stop')
        os.system("kill.bat")
    #def logout(self):
        #print('quit')
        #sys.exit(app.exec_())
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1031, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btnserver = QtWidgets.QPushButton(self.tab)
        self.btnserver.setGeometry(QtCore.QRect(280, 120, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.btnserver.setFont(font)
        self.btnserver.setObjectName("btnserver")
        self.btnserver.clicked.connect(self.runserver)
        self.btnbrowse = QtWidgets.QPushButton(self.tab)
        self.btnbrowse.setGeometry(QtCore.QRect(280, 232, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.btnbrowse.setFont(font)
        self.btnbrowse.setObjectName("btnbrowse")
        self.btnbrowse.clicked.connect(self.openbrowser)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 1021, 451))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(129)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.verticalHeader().setDefaultSectionSize(31)
        self.btnrefresh = QtWidgets.QPushButton(self.tab_2)
        self.btnrefresh.setGeometry(QtCore.QRect(400, 480, 91, 31))
        self.btnrefresh.setObjectName("btnrefresh")
        self.btnrefresh.clicked.connect(self.showtrigger)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStop_server = QtWidgets.QAction(MainWindow)
        self.actionStop_server.setObjectName("actionStop_server")
        self.actionStop_server.triggered.connect(self.stopserver)
        #self.actionQuit = QtWidgets.QAction(MainWindow)
        #self.actionQuit.setObjectName("actionQuit")
        #self.actionQuit.triggered.connect(self.logout)
        self.menuMenu.addAction(self.actionStop_server)
        #self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnserver.setText(_translate("MainWindow", "START SERVER"))
        self.btnbrowse.setText(_translate("MainWindow", "OPEN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.btnrefresh.setText(_translate("MainWindow", "REFRESH"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuMenu.setTitle(_translate("MainWindow", "menu"))
        self.actionStop_server.setText(_translate("MainWindow", "stop server"))
        #self.actionQuit.setText(_translate("MainWindow", "quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

