#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:11:59 2019

@author: nephilim
"""

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QFileDialog,QDockWidget,QTextEdit,QGridLayout,QTabWidget,QDialog
from PyQt5.QtCore import Qt,QTimer
from MainWindow_GPR import Ui_MainWindow
from PyQt5 import QtWidgets

class MainForm(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.showMaximized()
     
if __name__ == '__main__':   
    try:
        app
    except:                
        app=QApplication(sys.argv)  
    main=MainForm()  
    main.showMaximized()
    main.show()  
    app.exec_()
