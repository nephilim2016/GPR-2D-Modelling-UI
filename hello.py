#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:08:18 2019

@author: nephilim
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class hello_mainWindow(object):

    def __init__(self):
        super(hello_mainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.WindowModal)
        mainWindow.resize(624, 511)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "hello word"))

class MainForm(QtWidgets.QMainWindow,hello_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
if __name__ == "__main__":
    import sys
    try:
        app
    except:                
        app=QApplication(sys.argv)  
    mainWindow = MainForm()
    mainWindow.show()
    sys.exit(app.exec_())