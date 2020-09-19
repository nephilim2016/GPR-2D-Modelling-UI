#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:22:41 2019

@author: nephilim
"""

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_AddPolygon(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Ui_AddPolygon,self).__init__(parent)
        self.setObjectName("Dialog")
        self.setWindowTitle('Add Polygon Model')
        self.setFixedSize(600, 230)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 530, 140))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        # X-Axis Data Label
        self.label_XAxisData = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_XAxisData.setAlignment(QtCore.Qt.AlignCenter)
        self.label_XAxisData.setObjectName("label_XAxisData")
        self.label_XAxisData.setText('X-axis data')
        self.gridLayout_2.addWidget(self.label_XAxisData, 0, 0, 1, 1)
        # Z-Axis Data Label
        self.label_ZAxisData = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_ZAxisData.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ZAxisData.setObjectName("label_ZAxisData")
        self.label_ZAxisData.setText('Z-axis data')
        self.gridLayout_2.addWidget(self.label_ZAxisData, 1, 0, 1, 1)
        # Conductivity Label
        self.label_Conductivity = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Conductivity.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Conductivity.setObjectName("label_Conductivity")
        self.label_Conductivity.setText('Conductivity')
        self.gridLayout_2.addWidget(self.label_Conductivity, 0, 2, 1, 1)
        # Dielectric Constant Label
        self.label_DielectricConstant = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_DielectricConstant.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DielectricConstant.setObjectName("label_DielectricConstant")
        self.label_DielectricConstant.setText('Dielectric Constant')
        self.gridLayout_2.addWidget(self.label_DielectricConstant, 1, 2, 1, 1)
        # Magnetic Permeability Label
        self.label_MagneticPermeability = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_MagneticPermeability.setAlignment(QtCore.Qt.AlignCenter)
        self.label_MagneticPermeability.setObjectName("label_MagneticPermeability")
        self.label_MagneticPermeability.setText('Magnetic Permeability')
        self.gridLayout_2.addWidget(self.label_MagneticPermeability, 2, 2, 1, 1)
        # X-Axis Data lineEdit
        self.lineEdit_XAxisData = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_XAxisData.setObjectName("lineEdit_XAxisData")
        self.lineEdit_XAxisData.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_XAxisData.setPlaceholderText('0,0.01,0.02,0.03,0.04,0.05')
        self.gridLayout_2.addWidget(self.lineEdit_XAxisData, 0, 1, 1, 1)
        # Z-Axis Data lineEdit
        self.lineEdit_ZAxisData = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ZAxisData.setObjectName("lineEdit_ZAxisData")
        self.lineEdit_ZAxisData.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ZAxisData.setPlaceholderText('0,0.01,0.02,0.03,0.04,0.05')
        self.gridLayout_2.addWidget(self.lineEdit_ZAxisData, 1, 1, 1, 1)
        # Conductivity lineEdit
        self.lineEdit_Conductivity = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Conductivity.sizePolicy().hasHeightForWidth())
        self.lineEdit_Conductivity.setSizePolicy(sizePolicy)
        self.lineEdit_Conductivity.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit_Conductivity.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Conductivity.setObjectName("lineEdit_Conductivity")
        self.lineEdit_Conductivity.setPlaceholderText('1e-5')
        pDoubleRegex = QtCore.QRegExp("[+-]?[\\d]+([\\.][\\d]*)?([Ee][+-]?[0-9]{0,6})?")
        pDoubleValidator = QtGui.QRegExpValidator(pDoubleRegex, self.lineEdit_Conductivity)
        self.lineEdit_Conductivity.setValidator(pDoubleValidator)
        self.gridLayout_2.addWidget(self.lineEdit_Conductivity, 0, 3, 1, 1)
        # Dielectric Constant doubleSpinBox        
        self.doubleSpinBox_DielectricConstant = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_DielectricConstant.setMinimum(0.0)
        self.doubleSpinBox_DielectricConstant.setMaximum(81.0)
        self.doubleSpinBox_DielectricConstant.setSingleStep(0.5)
        self.doubleSpinBox_DielectricConstant.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_DielectricConstant.setProperty("value", 7.0)
        self.doubleSpinBox_DielectricConstant.setObjectName("doubleSpinBox_DielectricConstant") 
        self.gridLayout_2.addWidget(self.doubleSpinBox_DielectricConstant, 1, 3, 1, 1)
        # Magnetic Permeability lineEdit
        self.lineEdit_MagneticPermeability = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_MagneticPermeability.sizePolicy().hasHeightForWidth())
        self.lineEdit_MagneticPermeability.setSizePolicy(sizePolicy)
        self.lineEdit_MagneticPermeability.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit_MagneticPermeability.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_MagneticPermeability.setObjectName("lineEdit_MagneticPermeability")
        self.lineEdit_MagneticPermeability.setPlaceholderText('1')
        pDoubleRegex = QtCore.QRegExp("[+-]?[\\d]+([\\.][\\d]*)?([Ee][+-]?[0-9]{0,6})?")
        pDoubleValidator = QtGui.QRegExpValidator(pDoubleRegex, self.lineEdit_MagneticPermeability)
        self.lineEdit_MagneticPermeability.setValidator(pDoubleValidator)
        self.gridLayout_2.addWidget(self.lineEdit_MagneticPermeability, 2, 3, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 10)
        self.gridLayout_2.setColumnStretch(1, 10)
        self.gridLayout_2.setColumnStretch(2, 10)
        self.gridLayout_2.setColumnStretch(3, 10)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        
        # Buttion Ok
        self.pushButtonOk = QtWidgets.QPushButton(self.frame)
        self.pushButtonOk.setGeometry(QtCore.QRect(100, 160, 90, 30))
        self.pushButtonOk.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonOk.setObjectName("pushButtonOk")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UI_Ico/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonOk.setIcon(icon)
        self.pushButtonOk.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonOk.setText('Ok')
        # Buttion Cancel
        self.pushButtonCancel = QtWidgets.QPushButton(self.frame)
        self.pushButtonCancel.setGeometry(QtCore.QRect(400, 160, 90, 30))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UI_Ico/cancel.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCancel.setIcon(icon)
        self.pushButtonCancel.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonCancel.setText('Cancel')
        
        self.pushButtonOk.clicked.connect(self.accept)
        self.pushButtonCancel.clicked.connect(self.reject)
        
if __name__=='__main__':
    import sys
    try:
        app
    except:                
        app=QtWidgets.QApplication(sys.argv)
    ex = Ui_AddPolygon()
    ex.show()
    sys.exit(app.exec_())