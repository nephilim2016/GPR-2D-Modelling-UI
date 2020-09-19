#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 21:56:16 2019

@author: nephilim
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time

class TestWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        btn1 = QtWidgets.QPushButton("Start", self)
        btn2 = QtWidgets.QPushButton("Stop", self)
        self.sec_label = QtWidgets.QLabel(self)

        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(btn1,0,0)
        layout.addWidget(btn2,0,1)
        layout.addWidget(self.sec_label,1,0,1,2)

        
        self.thread = MyThread() # 创建一个线程 
        # thread.sec_changed_signal.connect(self.update) # 线程发过来的信号挂接到槽：update
        btn1.clicked.connect(self.Get_)
        btn2.clicked.connect(lambda :self.thread.terminate()) # 线程中止

    def Get_(self):
        self.thread.sec=10
        self.thread.start()
        
    def update(self, sec):  
        self.sec_label.setText(str(sec))
        
        
  
class MyThread(QtCore.QThread):  
    
    # sec_changed_signal = pyqtSignal(int) # 信号类型：int
  
    def __init__(self, sec=1000, parent=None):  
        super().__init__(parent)
        self.sec = sec # 默认1000秒
  
    def run(self):  
        for i in range(self.sec):
            # self.sec_changed_signal.emit(i)  #发射信号
            time.sleep(0.1)
            print(i)
              
  
import sys
try:
    app
except:                
    app=QtWidgets.QApplication(sys.argv)
form = TestWindow()
form.show()
app.exec_()