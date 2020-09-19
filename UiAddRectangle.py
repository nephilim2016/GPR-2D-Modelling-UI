#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:08:01 2019

@author: nephilim
"""
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_AddRectangle(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Ui_AddRectangle,self).__init__(parent)
        self.setObjectName("Dialog")
        self.setWindowTitle('Add Rectangle Model')
        self.setFixedSize(750, 360)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setGeometry(QtCore.QRect(10, 10, 730, 340))
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 670, 280))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        # Left Label
        self.label_Left = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Left.setObjectName("label_Left")
        self.label_Left.setText('Left')
        self.gridLayout_2.addWidget(self.label_Left, 0, 0, 1, 1)
        # Bottom Label
        self.label_Bottom = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Bottom.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Bottom.setObjectName("label_Bottom")
        self.label_Bottom.setText('Bottom')
        self.gridLayout_2.addWidget(self.label_Bottom, 1, 0, 1, 1)
        # Width Label
        self.label_Width = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Width.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Width.setObjectName("label_Width")
        self.label_Width.setText('Width')
        self.gridLayout_2.addWidget(self.label_Width, 2, 0, 1, 1)
        # High Label
        self.label_High = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_High.setAlignment(QtCore.Qt.AlignCenter)
        self.label_High.setObjectName("label_High")
        self.label_High.setText('High')
        self.gridLayout_2.addWidget(self.label_High, 3, 0, 1, 1)
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
        # Left lineEdit
        self.lineEdit_Left = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Left.setObjectName("lineEdit_Left")
        self.lineEdit_Left.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Left.setPlaceholderText('0.001')
        pDoubleValidator=QtGui.QDoubleValidator(self)
        pDoubleValidator.setRange(0,100.0)
        pDoubleValidator.setDecimals(10)
        self.lineEdit_Left.setValidator(pDoubleValidator)
        self.gridLayout_2.addWidget(self.lineEdit_Left, 0, 1, 1, 1)
        # Bottom lineEdit
        self.lineEdit_Bottom = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Bottom.setObjectName("lineEdit_Bottom")
        self.lineEdit_Bottom.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Bottom.setPlaceholderText('0.001')
        pDoubleValidator=QtGui.QDoubleValidator(self)
        pDoubleValidator.setRange(0,100.0)
        pDoubleValidator.setDecimals(10)
        self.lineEdit_Bottom.setValidator(pDoubleValidator)
        self.gridLayout_2.addWidget(self.lineEdit_Bottom, 1, 1, 1, 1)
        # Width lineEdit
        self.lineEdit_Width = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Width.setObjectName("lineEdit_Width")
        self.lineEdit_Width.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Width.setPlaceholderText('0.01')
        pDoubleValidator=QtGui.QDoubleValidator(self)
        pDoubleValidator.setRange(0,100.0)
        pDoubleValidator.setDecimals(10)
        self.lineEdit_Width.setValidator(pDoubleValidator)
        self.gridLayout_2.addWidget(self.lineEdit_Width, 2, 1, 1, 1)
        # High lineEdit
        self.lineEdit_High = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_High.setObjectName("lineEdit_High")
        self.lineEdit_High.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_High.setPlaceholderText('0.01')
        pDoubleValidator=QtGui.QDoubleValidator(self)
        pDoubleValidator.setRange(0,100.0)
        pDoubleValidator.setDecimals(10)
        self.lineEdit_High.setValidator(pDoubleValidator)
        self.gridLayout_2.addWidget(self.lineEdit_High, 3, 1, 1, 1)
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
        # Magnetic Permeability doubleSpinBox
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
        self.gridLayout_2.setColumnStretch(1, 20)
        self.gridLayout_2.setColumnStretch(2, 10)
        self.gridLayout_2.setColumnStretch(3, 20)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        # Buttion Ok
        self.pushButtonOk = QtWidgets.QPushButton(self.frame)
        self.pushButtonOk.setGeometry(QtCore.QRect(200, 280, 90, 30))
        self.pushButtonOk.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonOk.setObjectName("pushButtonOk")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UI_Ico/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonOk.setIcon(icon)
        self.pushButtonOk.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonOk.setText('Ok')
        # Buttion Cancel
        self.pushButtonCancel = QtWidgets.QPushButton(self.frame)
        self.pushButtonCancel.setGeometry(QtCore.QRect(460, 280, 90, 30))
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
    ex = Ui_AddRectangle()
    ex.show()
    sys.exit(app.exec_())