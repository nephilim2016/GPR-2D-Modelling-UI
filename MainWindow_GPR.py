# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_GPR.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os
from matplotlib.figure import Figure
import DZTFileRead
import re
import wigb
from matplotlib import pyplot,cm
import numpy as np
import MainWindow_Modelling

class Ui_MainWindow(object):     
    def setupUi(self, MainWindow):
        # MenuBar and ToolBar
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UI_Ico/GPR.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.FileList=[]
        self.UserAspect=1
        self.UserCmap='cm.viridis'
        self.UiGetProfileData=[]
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        #MENU--->File
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        #MENU--->View
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuView.setEnabled(False)
        
        #MENU--->Data Process
        self.menuData_Process = QtWidgets.QMenu(self.menubar)
        self.menuData_Process.setObjectName("menuData_Process")
        self.menuData_Process.setEnabled(False)
        
        #MENU--->Modelling
        self.menuModelling = QtWidgets.QMenu(self.menubar)
        self.menuModelling.setObjectName("menuModelling")
        
        #MENU--->Inversion_2D
        self.menuInversion_2D = QtWidgets.QMenu(self.menubar)
        self.menuInversion_2D.setObjectName("menuInversion_2D")
        self.menuInversion_2D.setEnabled(False)
        
        #MENU--->Help
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        
        # STATUSBAR
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # self.DisplayPosition = QtWidgets.QLabel("x=    ,  z=    ")  
        # self.DisplayPosition.setAlignment(QtCore.Qt.AlignCenter)
        # self.DisplayPosition.setEnabled(False)
        # self.statusBar().addWidget(self.DisplayPosition, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.statusbar.showMessage('Ready...')
        
        
        # TOOLBAR
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
        # MENU--->File--->New
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        
        # MENU--->File--->Open
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        
        # MENU--->File--->Recent File
        self.menuRecent_File = QtWidgets.QMenu(self.menuFile)
        self.menuRecent_File.setObjectName("actionRecent_File")
        self.menuRecent_File.setEnabled(False)
        
        # MENU--->File--->Close
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.setEnabled(False)     
        
        # MENU--->File--->Close All
        self.actionCloseAll = QtWidgets.QAction(MainWindow)
        self.actionCloseAll.setObjectName("actionCloseAll")
        self.actionCloseAll.setEnabled(False)    
        
        # MENU--->File--->Save
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setEnabled(False)
        
        # MENU--->File--->Save as...
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave_as.setEnabled(False)
        
        # MENU--->File--->Print Preview
        self.actionPrint_Preview = QtWidgets.QAction(MainWindow)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")
        self.actionPrint_Preview.setEnabled(False)
        
        # MENU--->File--->Print 
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrint.setEnabled(False)
        
        # MENU--->File--->Print Setting
        self.actionPrint_Setting = QtWidgets.QAction(MainWindow)
        self.actionPrint_Setting.setObjectName("actionPrint_Setting")
        
        # MENU--->File--->Exit CSU GPR
        self.actionExit_CSU_GPR = QtWidgets.QAction(MainWindow)
        self.actionExit_CSU_GPR.setObjectName("actionExit_CSU_GPR")
        
        # MENU--->View--->Display Mode(menu)
        self.menuDisplay_Mode = QtWidgets.QMenu(self.menuView)
        self.menuDisplay_Mode.setObjectName("menuDisplay_Mode")
        
        # MENU--->View--->Display Mode(menu)--->Wiggle
        self.actionWiggle = QtWidgets.QAction(MainWindow)
        self.actionWiggle.setObjectName("actionWiggle")
        self.actionWiggle.triggered.connect(self.ActionSwitchingStateWigb)
        
        # MENU--->View--->Display Mode(menu)--->Pseudo Color
        self.actionPseudo_Color = QtWidgets.QAction(MainWindow)
        self.actionPseudo_Color.setObjectName("actionPseudo_Color")
        self.actionPseudo_Color.triggered.connect(self.ActionSwitchingStatePColor)
        
        # MENU--->View--->Scan Line
        self.actionScan_Line = QtWidgets.QAction(MainWindow)
        self.actionScan_Line.setObjectName("actionScan_Line")
        self.actionScan_Line.triggered.connect(self.ActionScanLine)
        
        # MENU--->View--->Color Map(menu)
        self.menuColor_Map = QtWidgets.QMenu(self.menuView)
        self.menuColor_Map.setObjectName("menuColor_Map")
        
        # MENU--->View--->Color Map(menu)--->Accent
        self.actionAccent = QtWidgets.QAction(MainWindow)
        self.actionAccent.setObjectName("actionAccent")
        self.actionAccent.triggered.connect(lambda: self.ChangeCmap(self.actionAccent.text()))
        # MENU--->View--->Color Map(menu)--->Blues
        self.actionBlues = QtWidgets.QAction(MainWindow)
        self.actionBlues.setObjectName("actionBlues")
        self.actionBlues.triggered.connect(lambda: self.ChangeCmap(self.actionBlues.text()))
        # MENU--->View--->Color Map(menu)--->BrBG
        self.actionBrBG = QtWidgets.QAction(MainWindow)
        self.actionBrBG.setObjectName("actionBrBG")
        self.actionBrBG.triggered.connect(lambda: self.ChangeCmap(self.actionBrBG.text()))
        # MENU--->View--->Color Map(menu)--->BuGn
        self.actionBuGn = QtWidgets.QAction(MainWindow)
        self.actionBuGn.setObjectName("actionBuGn")
        self.actionBuGn.triggered.connect(lambda: self.ChangeCmap(self.actionBuGn.text()))
        # MENU--->View--->Color Map(menu)--->BuPu
        self.actionBuPu = QtWidgets.QAction(MainWindow)
        self.actionBuPu.setObjectName("actionBuPu")
        self.actionBuPu.triggered.connect(lambda: self.ChangeCmap(self.actionBuPu.text()))
        # MENU--->View--->Color Map(menu)--->CMRmap
        self.actionCMRmap = QtWidgets.QAction(MainWindow)
        self.actionCMRmap.setObjectName("actionCMRmap")
        self.actionCMRmap.triggered.connect(lambda: self.ChangeCmap(self.actionCMRmap.text()))
        # MENU--->View--->Color Map(menu)--->Dark2
        self.actionDark2 = QtWidgets.QAction(MainWindow)
        self.actionDark2.setObjectName("actionDark2")
        self.actionDark2.triggered.connect(lambda: self.ChangeCmap(self.actionDark2.text()))
        # MENU--->View--->Color Map(menu)--->GnBu
        self.actionGnBu = QtWidgets.QAction(MainWindow)
        self.actionGnBu.setObjectName("actionGnBu")
        self.actionGnBu.triggered.connect(lambda: self.ChangeCmap(self.actionGnBu.text()))
        # MENU--->View--->Color Map(menu)--->Greens
        self.actionGreens = QtWidgets.QAction(MainWindow)
        self.actionGreens.setObjectName("actionGreens")
        self.actionGreens.triggered.connect(lambda: self.ChangeCmap(self.actionGreens.text()))
        # MENU--->View--->Color Map(menu)--->Greys
        self.actionGreys = QtWidgets.QAction(MainWindow)
        self.actionGreys.setObjectName("actionGreys")
        self.actionGreys.triggered.connect(lambda: self.ChangeCmap(self.actionGreys.text()))
        # MENU--->View--->Color Map(menu)--->OrRd
        self.actionOrRd = QtWidgets.QAction(MainWindow)
        self.actionOrRd.setObjectName("actionOrRd")
        self.actionOrRd.triggered.connect(lambda: self.ChangeCmap(self.actionOrRd.text()))
        # MENU--->View--->Color Map(menu)--->Oranges
        self.actionOranges = QtWidgets.QAction(MainWindow)
        self.actionOranges.setObjectName("actionOranges")
        self.actionOranges.triggered.connect(lambda: self.ChangeCmap(self.actionOranges.text()))
        # MENU--->View--->Color Map(menu)--->PRGn
        self.actionPRGn = QtWidgets.QAction(MainWindow)
        self.actionPRGn.setObjectName("actionPRGn")
        self.actionPRGn.triggered.connect(lambda: self.ChangeCmap(self.actionPRGn.text()))
        # MENU--->View--->Color Map(menu)--->Paired
        self.actionPaired = QtWidgets.QAction(MainWindow)
        self.actionPaired.setObjectName("actionPaired")
        self.actionPaired.triggered.connect(lambda: self.ChangeCmap(self.actionPaired.text()))
        # MENU--->View--->Color Map(menu)--->Pastel1
        self.actionPastel1 = QtWidgets.QAction(MainWindow)
        self.actionPastel1.setObjectName("actionPastel1")
        self.actionPastel1.triggered.connect(lambda: self.ChangeCmap(self.actionPastel1.text()))
        # MENU--->View--->Color Map(menu)--->Pastel2
        self.actionPastel2 = QtWidgets.QAction(MainWindow)
        self.actionPastel2.setObjectName("actionPastel2")
        self.actionPastel2.triggered.connect(lambda: self.ChangeCmap(self.actionPastel2.text()))
        # MENU--->View--->Color Map(menu)--->PiYG
        self.actionPiYG = QtWidgets.QAction(MainWindow)
        self.actionPiYG.setObjectName("actionPiYG")
        self.actionPiYG.triggered.connect(lambda: self.ChangeCmap(self.actionPiYG.text()))
        # MENU--->View--->Color Map(menu)--->PuBu
        self.actionPuBu = QtWidgets.QAction(MainWindow)
        self.actionPuBu.setObjectName("actionPuBu")
        self.actionPuBu.triggered.connect(lambda: self.ChangeCmap(self.actionPuBu.text()))
        # MENU--->View--->Color Map(menu)--->PuBuGn
        self.actionPuBuGn = QtWidgets.QAction(MainWindow)
        self.actionPuBuGn.setObjectName("actionPuBuGn")
        self.actionPuBuGn.triggered.connect(lambda: self.ChangeCmap(self.actionPuBuGn.text()))
        # MENU--->View--->Color Map(menu)--->PuOr
        self.actionPuOr = QtWidgets.QAction(MainWindow)
        self.actionPuOr.setObjectName("actionPuOr")
        self.actionPuOr.triggered.connect(lambda: self.ChangeCmap(self.actionPuOr.text()))
        # MENU--->View--->Color Map(menu)--->PuRd
        self.actionPuRd = QtWidgets.QAction(MainWindow)
        self.actionPuRd.setObjectName("actionPuRd")
        self.actionPuRd.triggered.connect(lambda: self.ChangeCmap(self.actionPuRd.text()))
        # MENU--->View--->Color Map(menu)--->Purples
        self.actionPurples = QtWidgets.QAction(MainWindow)
        self.actionPurples.setObjectName("actionPurples")
        self.actionPurples.triggered.connect(lambda: self.ChangeCmap(self.actionPurples.text()))
        # MENU--->View--->Color Map(menu)--->RdBu
        self.actionRdBu = QtWidgets.QAction(MainWindow)
        self.actionRdBu.setObjectName("actionRdBu")
        self.actionRdBu.triggered.connect(lambda: self.ChangeCmap(self.actionRdBu.text()))
        # MENU--->View--->Color Map(menu)--->RdGy
        self.actionRdGy = QtWidgets.QAction(MainWindow)
        self.actionRdGy.setObjectName("actionRdGy")
        self.actionRdGy.triggered.connect(lambda: self.ChangeCmap(self.actionRdGy.text()))
        # MENU--->View--->Color Map(menu)--->RdPu
        self.actionRdPu = QtWidgets.QAction(MainWindow)
        self.actionRdPu.setObjectName("actionRdPu")
        self.actionRdPu.triggered.connect(lambda: self.ChangeCmap(self.actionRdPu.text()))
        # MENU--->View--->Color Map(menu)--->RdYlBu
        self.actionRdYlBu = QtWidgets.QAction(MainWindow)
        self.actionRdYlBu.setObjectName("actionRdYlBu")
        self.actionRdYlBu.triggered.connect(lambda: self.ChangeCmap(self.actionRdYlBu.text()))
        # MENU--->View--->Color Map(menu)--->RdYlGn
        self.actionRdYlGn = QtWidgets.QAction(MainWindow)
        self.actionRdYlGn.setObjectName("actionRdYlGn")
        self.actionRdYlGn.triggered.connect(lambda: self.ChangeCmap(self.actionRdYlGn.text()))
        # MENU--->View--->Color Map(menu)--->Reds
        self.actionReds = QtWidgets.QAction(MainWindow)
        self.actionReds.setObjectName("actionReds")
        self.actionReds.triggered.connect(lambda: self.ChangeCmap(self.actionReds.text()))
        # MENU--->View--->Color Map(menu)--->Set1
        self.actionSet1 = QtWidgets.QAction(MainWindow)
        self.actionSet1.setObjectName("actionSet1")
        self.actionSet1.triggered.connect(lambda: self.ChangeCmap(self.actionSet1.text()))
        # MENU--->View--->Color Map(menu)--->Set2
        self.actionSet2 = QtWidgets.QAction(MainWindow)
        self.actionSet2.setObjectName("actionSet2")
        self.actionSet2.triggered.connect(lambda: self.ChangeCmap(self.actionSet2.text()))
        # MENU--->View--->Color Map(menu)--->Set3
        self.actionSet3 = QtWidgets.QAction(MainWindow)
        self.actionSet3.setObjectName("actionSet3")
        self.actionSet3.triggered.connect(lambda: self.ChangeCmap(self.actionSet3.text()))
        # MENU--->View--->Color Map(menu)--->Spectral
        self.actionSpectral = QtWidgets.QAction(MainWindow)
        self.actionSpectral.setObjectName("actionSpectral")
        self.actionSpectral.triggered.connect(lambda: self.ChangeCmap(self.actionSpectral.text()))
        # MENU--->View--->Color Map(menu)--->Vega10
        self.actionVega10 = QtWidgets.QAction(MainWindow)
        self.actionVega10.setObjectName("actionVega10")
        self.actionVega10.triggered.connect(lambda: self.ChangeCmap(self.actionVega10.text()))
        # MENU--->View--->Color Map(menu)--->Vega20
        self.actionVega20 = QtWidgets.QAction(MainWindow)
        self.actionVega20.setObjectName("actionVega20")
        self.actionVega20.triggered.connect(lambda: self.ChangeCmap(self.actionVega20.text()))
        # MENU--->View--->Color Map(menu)--->Vega20b
        self.actionVega20b = QtWidgets.QAction(MainWindow)
        self.actionVega20b.setObjectName("actionVega20b")
        self.actionVega20b.triggered.connect(lambda: self.ChangeCmap(self.actionVega20b.text()))
        # MENU--->View--->Color Map(menu)--->Vega20c
        self.actionVega20c = QtWidgets.QAction(MainWindow)
        self.actionVega20c.setObjectName("actionVega20c")
        self.actionVega20c.triggered.connect(lambda: self.ChangeCmap(self.actionVega20c.text()))
        # MENU--->View--->Color Map(menu)--->Wistia
        self.actionWistia = QtWidgets.QAction(MainWindow)
        self.actionWistia.setObjectName("actionWistia")
        self.actionWistia.triggered.connect(lambda: self.ChangeCmap(self.actionWistia.text()))
        # MENU--->View--->Color Map(menu)--->YlGn
        self.actionYlGn = QtWidgets.QAction(MainWindow)
        self.actionYlGn.setObjectName("actionYlGn")
        self.actionYlGn.triggered.connect(lambda: self.ChangeCmap(self.actionYlGn.text()))
        # MENU--->View--->Color Map(menu)--->YlGnBu
        self.actionYlGnBu = QtWidgets.QAction(MainWindow)
        self.actionYlGnBu.setObjectName("actionYlGnBu")
        self.actionYlGnBu.triggered.connect(lambda: self.ChangeCmap(self.actionYlGnBu.text()))
        # MENU--->View--->Color Map(menu)--->YlOrBr
        self.actionYlOrBr = QtWidgets.QAction(MainWindow)
        self.actionYlOrBr.setObjectName("actionYlOrBr")
        self.actionYlOrBr.triggered.connect(lambda: self.ChangeCmap(self.actionYlOrBr.text()))
        # MENU--->View--->Color Map(menu)--->YlOrRd
        self.actionYlOrRd = QtWidgets.QAction(MainWindow)
        self.actionYlOrRd.setObjectName("actionYlOrRd")
        self.actionYlOrRd.triggered.connect(lambda: self.ChangeCmap(self.actionYlOrRd.text()))
        # MENU--->View--->Color Map(menu)--->afmhot
        self.actionafmhot = QtWidgets.QAction(MainWindow)
        self.actionafmhot.setObjectName("actionafmhot")
        self.actionafmhot.triggered.connect(lambda: self.ChangeCmap(self.actionafmhot.text()))
        # MENU--->View--->Color Map(menu)--->autumn
        self.actionautumn = QtWidgets.QAction(MainWindow)
        self.actionautumn.setObjectName("actionautumn")
        self.actionautumn.triggered.connect(lambda: self.ChangeCmap(self.actionautumn.text()))
        # MENU--->View--->Color Map(menu)--->binary
        self.actionbinary = QtWidgets.QAction(MainWindow)
        self.actionbinary.setObjectName("actionbinary")
        self.actionbinary.triggered.connect(lambda: self.ChangeCmap(self.actionbinary.text()))
        # MENU--->View--->Color Map(menu)--->bone
        self.actionbone = QtWidgets.QAction(MainWindow)
        self.actionbone.setObjectName("actionbone")
        self.actionbone.triggered.connect(lambda: self.ChangeCmap(self.actionbone.text()))
        # MENU--->View--->Color Map(menu)--->brg
        self.actionbrg = QtWidgets.QAction(MainWindow)
        self.actionbrg.setObjectName("actionbrg")
        self.actionbrg.triggered.connect(lambda: self.ChangeCmap(self.actionbrg.text()))
        # MENU--->View--->Color Map(menu)--->bwr
        self.actionbwr = QtWidgets.QAction(MainWindow)
        self.actionbwr.setObjectName("actionbwr")
        self.actionbwr.triggered.connect(lambda: self.ChangeCmap(self.actionbwr.text()))
        # MENU--->View--->Color Map(menu)--->cool
        self.actioncool = QtWidgets.QAction(MainWindow)
        self.actioncool.setObjectName("actioncool")
        self.actioncool.triggered.connect(lambda: self.ChangeCmap(self.actioncool.text()))
        # MENU--->View--->Color Map(menu)--->coolwarm
        self.actioncoolwarm = QtWidgets.QAction(MainWindow)
        self.actioncoolwarm.setObjectName("actioncoolwarm")
        self.actioncoolwarm.triggered.connect(lambda: self.ChangeCmap(self.actioncoolwarm.text()))
        # MENU--->View--->Color Map(menu)--->copper
        self.actioncopper = QtWidgets.QAction(MainWindow)
        self.actioncopper.setObjectName("actioncopper")
        self.actioncopper.triggered.connect(lambda: self.ChangeCmap(self.actioncopper.text()))
        # MENU--->View--->Color Map(menu)--->cubehelix
        self.actioncubehelix = QtWidgets.QAction(MainWindow)
        self.actioncubehelix.setObjectName("actioncubehelix")
        self.actioncubehelix.triggered.connect(lambda: self.ChangeCmap(self.actioncubehelix.text()))
        # MENU--->View--->Color Map(menu)--->flag
        self.actionflag = QtWidgets.QAction(MainWindow)
        self.actionflag.setObjectName("actionflag")
        self.actionflag.triggered.connect(lambda: self.ChangeCmap(self.actionflag.text()))
        # MENU--->View--->Color Map(menu)--->gist_earth
        self.actiongist_earth = QtWidgets.QAction(MainWindow)
        self.actiongist_earth.setObjectName("actiongist_earth")
        self.actiongist_earth.triggered.connect(lambda: self.ChangeCmap(self.actiongist_earth.text()))
        # MENU--->View--->Color Map(menu)--->gist_gray
        self.actiongist_gray = QtWidgets.QAction(MainWindow)
        self.actiongist_gray.setObjectName("actiongist_gray")
        self.actiongist_gray.triggered.connect(lambda: self.ChangeCmap(self.actiongist_gray.text()))
        # MENU--->View--->Color Map(menu)--->gist_heat
        self.actiongist_heat = QtWidgets.QAction(MainWindow)
        self.actiongist_heat.setObjectName("actiongist_heat")
        self.actiongist_heat.triggered.connect(lambda: self.ChangeCmap(self.actiongist_heat.text()))
        # MENU--->View--->Color Map(menu)--->gist_ncar
        self.actiongist_ncar = QtWidgets.QAction(MainWindow)
        self.actiongist_ncar.setObjectName("actiongist_ncar")
        self.actiongist_ncar.triggered.connect(lambda: self.ChangeCmap(self.actiongist_ncar.text()))
        # MENU--->View--->Color Map(menu)--->gist_rainbow
        self.actiongist_rainbow = QtWidgets.QAction(MainWindow)
        self.actiongist_rainbow.setObjectName("actiongist_rainbow")
        self.actiongist_rainbow.triggered.connect(lambda: self.ChangeCmap(self.actiongist_rainbow.text()))
        # MENU--->View--->Color Map(menu)--->gist_stern
        self.actiongist_stern = QtWidgets.QAction(MainWindow)
        self.actiongist_stern.setObjectName("actiongist_stern")
        self.actiongist_stern.triggered.connect(lambda: self.ChangeCmap(self.actiongist_stern.text()))
        # MENU--->View--->Color Map(menu)--->gist_yarg
        self.actiongist_yarg = QtWidgets.QAction(MainWindow)
        self.actiongist_yarg.setObjectName("actiongist_yarg")
        self.actiongist_yarg.triggered.connect(lambda: self.ChangeCmap(self.actiongist_yarg.text()))
        # MENU--->View--->Color Map(menu)--->gnuplot
        self.actiongnuplot = QtWidgets.QAction(MainWindow)
        self.actiongnuplot.setObjectName("actiongnuplot")
        self.actiongnuplot.triggered.connect(lambda: self.ChangeCmap(self.actiongnuplot.text()))
        # MENU--->View--->Color Map(menu)--->gnuplot2
        self.actiongnuplot2 = QtWidgets.QAction(MainWindow)
        self.actiongnuplot2.setObjectName("actiongnuplot2")
        self.actiongnuplot2.triggered.connect(lambda: self.ChangeCmap(self.actiongnuplot2.text()))
        # MENU--->View--->Color Map(menu)--->gray
        self.actiongray = QtWidgets.QAction(MainWindow)
        self.actiongray.setObjectName("actiongray")
        self.actiongray.triggered.connect(lambda: self.ChangeCmap(self.actiongray.text()))
        # MENU--->View--->Color Map(menu)--->hot
        self.actionhot = QtWidgets.QAction(MainWindow)
        self.actionhot.setObjectName("actionhot")
        self.actionhot.triggered.connect(lambda: self.ChangeCmap(self.actionhot.text()))
        # MENU--->View--->Color Map(menu)--->hsv
        self.actionhsv = QtWidgets.QAction(MainWindow)
        self.actionhsv.setObjectName("actionhsv")
        self.actionhsv.triggered.connect(lambda: self.ChangeCmap(self.actionhsv.text()))
        # MENU--->View--->Color Map(menu)--->inferno
        self.actioninferno = QtWidgets.QAction(MainWindow)
        self.actioninferno.setObjectName("actioninferno")
        self.actioninferno.triggered.connect(lambda: self.ChangeCmap(self.actioninferno.text()))
        # MENU--->View--->Color Map(menu)--->jet
        self.actionjet = QtWidgets.QAction(MainWindow)
        self.actionjet.setObjectName("actionjet")
        self.actionjet.triggered.connect(lambda: self.ChangeCmap(self.actionjet.text()))
        # MENU--->View--->Color Map(menu)--->magma
        self.actionmagma = QtWidgets.QAction(MainWindow)
        self.actionmagma.setObjectName("actionmagma")
        self.actionmagma.triggered.connect(lambda: self.ChangeCmap(self.actionmagma.text()))
        # MENU--->View--->Color Map(menu)--->nipy_spectral
        self.actionnipy_spectral = QtWidgets.QAction(MainWindow)
        self.actionnipy_spectral.setObjectName("actionnipy_spectral")
        self.actionnipy_spectral.triggered.connect(lambda: self.ChangeCmap(self.actionnipy_spectral.text()))
        # MENU--->View--->Color Map(menu)--->ocean
        self.actionocean = QtWidgets.QAction(MainWindow)
        self.actionocean.setObjectName("actionocean")
        self.actionocean.triggered.connect(lambda: self.ChangeCmap(self.actionocean.text()))
        # MENU--->View--->Color Map(menu)--->pink
        self.actionpink = QtWidgets.QAction(MainWindow)
        self.actionpink.setObjectName("actionpink")
        self.actionpink.triggered.connect(lambda: self.ChangeCmap(self.actionpink.text()))
        # MENU--->View--->Color Map(menu)--->plasma
        self.actionplasma = QtWidgets.QAction(MainWindow)
        self.actionplasma.setObjectName("actionplasma")
        self.actionplasma.triggered.connect(lambda: self.ChangeCmap(self.actionplasma.text()))
        # MENU--->View--->Color Map(menu)--->prism
        self.actionprism = QtWidgets.QAction(MainWindow)
        self.actionprism.setObjectName("actionprism")
        self.actionprism.triggered.connect(lambda: self.ChangeCmap(self.actionprism.text()))
        # MENU--->View--->Color Map(menu)--->rainbow
        self.actionrainbow = QtWidgets.QAction(MainWindow)
        self.actionrainbow.setObjectName("actionrainbow")
        self.actionrainbow.triggered.connect(lambda: self.ChangeCmap(self.actionrainbow.text()))
        # MENU--->View--->Color Map(menu)--->seismic
        self.actionseismic = QtWidgets.QAction(MainWindow)
        self.actionseismic.setObjectName("actionseismic")
        self.actionseismic.triggered.connect(lambda: self.ChangeCmap(self.actionseismic.text()))
        # MENU--->View--->Color Map(menu)--->spectral
        self.actionspectral = QtWidgets.QAction(MainWindow)
        self.actionspectral.setObjectName("actionspectral")
        self.actionspectral.triggered.connect(lambda: self.ChangeCmap(self.actionspectral.text()))
        # MENU--->View--->Color Map(menu)--->spring
        self.actionspring = QtWidgets.QAction(MainWindow)
        self.actionspring.setObjectName("actionspring")
        self.actionspring.triggered.connect(lambda: self.ChangeCmap(self.actionspring.text()))
        # MENU--->View--->Color Map(menu)--->summer
        self.actionsummer = QtWidgets.QAction(MainWindow)
        self.actionsummer.setObjectName("actionsummer")
        self.actionsummer.triggered.connect(lambda: self.ChangeCmap(self.actionsummer.text()))
        # MENU--->View--->Color Map(menu)--->tab10
        self.actiontab10 = QtWidgets.QAction(MainWindow)
        self.actiontab10.setObjectName("actiontab10")
        self.actiontab10.triggered.connect(lambda: self.ChangeCmap(self.actiontab10.text()))
        # MENU--->View--->Color Map(menu)--->tab20
        self.actiontab20 = QtWidgets.QAction(MainWindow)
        self.actiontab20.setObjectName("actiontab20")
        self.actiontab20.triggered.connect(lambda: self.ChangeCmap(self.actiontab20.text()))
        # MENU--->View--->Color Map(menu)--->tab20b
        self.actiontab20b = QtWidgets.QAction(MainWindow)
        self.actiontab20b.setObjectName("actiontab20b")
        self.actiontab20b.triggered.connect(lambda: self.ChangeCmap(self.actiontab20b.text()))
        # MENU--->View--->Color Map(menu)--->tab20c
        self.actiontab20c = QtWidgets.QAction(MainWindow)
        self.actiontab20c.setObjectName("actiontab20c")
        self.actiontab20c.triggered.connect(lambda: self.ChangeCmap(self.actiontab20c.text()))
        # MENU--->View--->Color Map(menu)--->terrain
        self.actionterrain = QtWidgets.QAction(MainWindow)
        self.actionterrain.setObjectName("actionterrain")
        self.actionterrain.triggered.connect(lambda: self.ChangeCmap(self.actionterrain.text()))
        # MENU--->View--->Color Map(menu)--->viridis
        self.actionviridis = QtWidgets.QAction(MainWindow)
        self.actionviridis.setObjectName("actionviridis")
        self.actionviridis.triggered.connect(lambda: self.ChangeCmap(self.actionviridis.text()))
        # MENU--->View--->Color Map(menu)--->winter
        self.actionwinter = QtWidgets.QAction(MainWindow)
        self.actionwinter.setObjectName("actionwinter")
        self.actionwinter.triggered.connect(lambda: self.ChangeCmap(self.actionwinter.text()))

        # MENU--->View--->Display Gain(menu)
        self.menuDisplay_Gain = QtWidgets.QMenu(self.menuView)
        self.menuDisplay_Gain.setObjectName("menuDisplay_Gain")
        # MENU--->View--->Display Gain(menu)--->0.1
        self.actionZoomOutDisplayGain10 = QtWidgets.QAction(MainWindow)
        self.actionZoomOutDisplayGain10.setObjectName("actionZoomOutDisplayGain10")
        self.actionZoomOutDisplayGain10.triggered.connect(lambda: self.ChangeGain(self.actionZoomOutDisplayGain10.text()))
        # MENU--->View--->Display Gain(menu)--->0.2
        self.actionZoomOutDisplayGain5 = QtWidgets.QAction(MainWindow)
        self.actionZoomOutDisplayGain5.setObjectName("actionZoomOutDisplayGain5")
        self.actionZoomOutDisplayGain5.triggered.connect(lambda: self.ChangeGain(self.actionZoomOutDisplayGain5.text()))
        # MENU--->View--->Display Gain(menu)--->0.5
        self.actionZoomOutDisplayGain2 = QtWidgets.QAction(MainWindow)
        self.actionZoomOutDisplayGain2.setObjectName("actionZoomOutDisplayGain2")
        self.actionZoomOutDisplayGain2.triggered.connect(lambda: self.ChangeGain(self.actionZoomOutDisplayGain2.text()))
        # MENU--->View--->Display Gain(menu)--->1
        self.actionNormalDisplayGain = QtWidgets.QAction(MainWindow)
        self.actionNormalDisplayGain.setObjectName("actionNormalDisplayGain")
        self.actionNormalDisplayGain.triggered.connect(lambda: self.ChangeGain(self.actionNormalDisplayGain.text()))
        # MENU--->View--->Display Gain(menu)--->2
        self.actionZoomDisplayGain2 = QtWidgets.QAction(MainWindow)
        self.actionZoomDisplayGain2.setObjectName("actionZoomDisplayGain2")
        self.actionZoomDisplayGain2.triggered.connect(lambda: self.ChangeGain(self.actionZoomDisplayGain2.text()))
        # MENU--->View--->Display Gain(menu)--->5
        self.actionZoomDisplayGain5 = QtWidgets.QAction(MainWindow)
        self.actionZoomDisplayGain5.setObjectName("actionZoomDisplayGain5")
        self.actionZoomDisplayGain5.triggered.connect(lambda: self.ChangeGain(self.actionZoomDisplayGain5.text()))
        # MENU--->View--->Display Gain(menu)--->10
        self.actionZoomDisplayGain10 = QtWidgets.QAction(MainWindow)
        self.actionZoomDisplayGain10.setObjectName("actionZoomDisplayGain10")
        self.actionZoomDisplayGain10.triggered.connect(lambda: self.ChangeGain(self.actionZoomDisplayGain10.text()))
        # MENU--->View--->Display Gain(menu)--->20
        self.actionZoomDisplayGain20 = QtWidgets.QAction(MainWindow)
        self.actionZoomDisplayGain20.setObjectName("actionZoomDisplayGain20")
        self.actionZoomDisplayGain20.triggered.connect(lambda: self.ChangeGain(self.actionZoomDisplayGain20.text()))
        
        # MENU--->View--->Scale Out(menu)
        self.menuScale_Out = QtWidgets.QMenu(self.menuView)
        self.menuScale_Out.setObjectName("menuScale_Out")
        # MENU--->View--->Scale Out(menu)--->0.1
        self.actionZoomOutScaleOut10 = QtWidgets.QAction(MainWindow)
        self.actionZoomOutScaleOut10.setObjectName("actionZoomOutScaleOut10")
        self.actionZoomOutScaleOut10.triggered.connect(lambda: self.ChangeAspect(self.actionZoomDisplayGain10.text()))
        # MENU--->View--->Scale Out(menu)--->0.2
        self.actionZoomOutScaleOut5 = QtWidgets.QAction(MainWindow)
        self.actionZoomOutScaleOut5.setObjectName("actionZoomOutScaleOut5")
        self.actionZoomOutScaleOut5.triggered.connect(lambda: self.ChangeAspect(self.actionZoomDisplayGain5.text()))
        # MENU--->View--->Scale Out(menu)--->0.5
        self.actionZoomOutScaleOut2 = QtWidgets.QAction(MainWindow)
        self.actionZoomOutScaleOut2.setObjectName("actionZoomOutScaleOut2")
        self.actionZoomOutScaleOut2.triggered.connect(lambda: self.ChangeAspect(self.actionZoomDisplayGain2.text()))
        # MENU--->View--->Scale Out(menu)--->1
        self.actionNormalScaleOut = QtWidgets.QAction(MainWindow)
        self.actionNormalScaleOut.setObjectName("actionNormalScaleOut")
        self.actionNormalScaleOut.triggered.connect(lambda: self.ChangeAspect(self.actionNormalScaleOut.text()))
        # MENU--->View--->Scale Out(menu)--->2
        self.actionZoomScaleOut2 = QtWidgets.QAction(MainWindow)
        self.actionZoomScaleOut2.setObjectName("actionZoomScaleOut2")
        self.actionZoomScaleOut2.triggered.connect(lambda: self.ChangeAspect(self.actionZoomScaleOut2.text()))
        # MENU--->View--->Scale Out(menu)--->5
        self.actionZoomScaleOut5 = QtWidgets.QAction(MainWindow)
        self.actionZoomScaleOut5.setObjectName("actionZoomScaleOut5")
        self.actionZoomScaleOut5.triggered.connect(lambda: self.ChangeAspect(self.actionZoomScaleOut5.text()))
        # MENU--->View--->Scale Out(menu)--->10
        self.actionZoomScaleOut10 = QtWidgets.QAction(MainWindow)
        self.actionZoomScaleOut10.setObjectName("actionZoomScaleOut10")
        self.actionZoomScaleOut10.triggered.connect(lambda: self.ChangeAspect(self.actionZoomScaleOut10.text()))
        # MENU--->View--->Scale Out(menu)--->20
        self.actionZoomScaleOut20 = QtWidgets.QAction(MainWindow)
        self.actionZoomScaleOut20.setObjectName("actionZoomScaleOut20")
        self.actionZoomScaleOut20.triggered.connect(lambda: self.ChangeAspect(self.actionZoomScaleOut20.text()))
        # MENU--->View--->Scale Out(menu)--->30
        self.actionZoomScaleOut30 = QtWidgets.QAction(MainWindow)
        self.actionZoomScaleOut30.setObjectName("actionZoomScaleOut30")
        self.actionZoomScaleOut30.triggered.connect(lambda: self.ChangeAspect(self.actionZoomScaleOut30.text()))
        
        # MENU--->View--->Vertical Operation(menu)
        self.menuVertical_Operation = QtWidgets.QMenu(self.menuView)
        self.menuVertical_Operation.setObjectName("menuVertical_Operation")
        # MENU--->View--->Vertical Operation(menu)--->Sample
        self.actionVerticalOperationSample = QtWidgets.QAction(MainWindow)
        self.actionVerticalOperationSample.setObjectName("actionVerticalOperationSample")
        self.actionVerticalOperationSample.triggered.connect(lambda: self.ChangeVertical(self.actionVerticalOperationSample.text()))
        # MENU--->View--->Vertical Operation(menu)--->Time
        self.actionVerticalOperationTime = QtWidgets.QAction(MainWindow)
        self.actionVerticalOperationTime.setObjectName("actionVerticalOperationTime")
        self.actionVerticalOperationTime.triggered.connect(lambda: self.ChangeVertical(self.actionVerticalOperationTime.text()))
        # MENU--->View--->Vertical Operation(menu)--->Depth
        self.actionVerticalOperationDepth = QtWidgets.QAction(MainWindow)
        self.actionVerticalOperationDepth.setObjectName("actionVerticalOperationDepth")
        self.actionVerticalOperationDepth.triggered.connect(lambda: self.ChangeVertical(self.actionVerticalOperationDepth.text()))

        # MENU--->Help--->Help Files
        self.actionHelp_Files = QtWidgets.QAction(MainWindow)
        self.actionHelp_Files.setObjectName("actionHelp_Files")
        
        # MENU--->Help--->Contants
        self.actionContants = QtWidgets.QAction(MainWindow)
        self.actionContants.setObjectName("actionContants")
        
        
        
        # NewFile Slot
        self.actionNew.triggered.connect(lambda: self.NewFile(MainWindow))
        # OpenFile Slot
        self.actionOpen.triggered.connect(lambda: self.OpenFile(MainWindow))
        # CloseFile Slot
        self.actionClose.triggered.connect(lambda: self.CloseFile(MainWindow))
        # CloseAllFile Slot
        self.actionCloseAll.triggered.connect(lambda: self.CloseAllFile(MainWindow))
        # HelpFiles Slot
        self.actionHelp_Files.triggered.connect(self.OpenHelpFile)
        # Contants Slot
        self.actionContants.triggered.connect(lambda: self.OpenContants(MainWindow))
        # Exit Slot
        self.actionExit_CSU_GPR.triggered.connect(self.ExitClose)
        
        # TOOL--->New
        self.ToolActionNewFile = QtWidgets.QAction(MainWindow)
        iconNew = QtGui.QIcon()
        iconNew.addPixmap(QtGui.QPixmap("./UI_Ico/new.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionNewFile.setIcon(iconNew)
        self.ToolActionNewFile.setObjectName("ToolActionNewFile")
        
        # TOOL--->Open
        self.ToolActionOpenFile = QtWidgets.QAction(MainWindow)
        iconOpen = QtGui.QIcon()
        iconOpen.addPixmap(QtGui.QPixmap("./UI_Ico/open.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionOpenFile.setIcon(iconOpen)
        self.ToolActionOpenFile.setObjectName("ToolActionOpenFile")
        
        # TOOL--->Save
        self.ToolActionSave = QtWidgets.QAction(MainWindow)
        iconSave = QtGui.QIcon()
        iconSave.addPixmap(QtGui.QPixmap("./UI_Ico/save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionSave.setIcon(iconSave)
        self.ToolActionSave.setObjectName("ToolActionSave")
        self.ToolActionSave.setEnabled(False)
        
        # TOOL--->Save as
        self.ToolActionSaveAs = QtWidgets.QAction(MainWindow)
        iconSaveas = QtGui.QIcon()
        iconSaveas.addPixmap(QtGui.QPixmap("./UI_Ico/save as.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionSaveAs.setIcon(iconSaveas)
        self.ToolActionSaveAs.setObjectName("ToolActionSaveAs")
        self.ToolActionSaveAs.setEnabled(False)
        
        # TOOL--->Print Preview
        self.ToolActionPrintPreview = QtWidgets.QAction(MainWindow)
        iconPrintPreview = QtGui.QIcon()
        iconPrintPreview.addPixmap(QtGui.QPixmap("./UI_Ico/print preview.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionPrintPreview.setIcon(iconPrintPreview)
        self.ToolActionPrintPreview.setObjectName("ToolActionPrintPreview")
        self.ToolActionPrintPreview.setEnabled(False)
        
        # TOOL--->Print
        self.ToolActionPrint = QtWidgets.QAction(MainWindow)
        iconPrint = QtGui.QIcon()
        iconPrint.addPixmap(QtGui.QPixmap("./UI_Ico/print.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionPrint.setIcon(iconPrint)
        self.ToolActionPrint.setObjectName("ToolActionPrint")
        self.ToolActionPrint.setEnabled(False)
        
        # TOOL--->Modelling
        self.ToolActionModelling = QtWidgets.QAction(MainWindow)
        iconForward = QtGui.QIcon()
        iconForward.addPixmap(QtGui.QPixmap("./UI_Ico/forward.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionModelling.setIcon(iconForward)
        self.ToolActionModelling.setObjectName("ToolActionModelling")
        
        
        # TOOL--->Help
        self.ToolActionHelp = QtWidgets.QAction(MainWindow)
        iconHelp = QtGui.QIcon()
        iconHelp.addPixmap(QtGui.QPixmap("./UI_Ico/help.icns"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionHelp.setIcon(iconHelp)
        self.ToolActionHelp.setObjectName("ToolActionHelp")
        
        # TOOL--->Contants
        self.ToolContants = QtWidgets.QAction(MainWindow)
        iconContants = QtGui.QIcon()
        iconContants.addPixmap(QtGui.QPixmap("./UI_Ico/contants.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolContants.setIcon(iconContants)
        self.ToolContants.setObjectName("ToolContants")
        
        # NewFile Slot
        self.ToolActionNewFile.triggered.connect(lambda: self.NewFile(MainWindow))
        # OpenFile Slot
        self.ToolActionOpenFile.triggered.connect(lambda: self.OpenFile(MainWindow))
        # Modelling Slot
        self.ToolActionModelling.triggered.connect(lambda: self.GetUiModelling(MainWindow))
        # HelpFiles Slot
        self.ToolActionHelp.triggered.connect(self.OpenHelpFile)
        # Contants Slot
        self.ToolContants.triggered.connect(lambda: self.OpenContants(MainWindow))
        
        # Add action to File
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuRecent_File.menuAction())
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionCloseAll)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint_Preview)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionPrint_Setting)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_CSU_GPR)
        
        # Add Display Mode to View
        self.menuView.addAction(self.menuDisplay_Mode.menuAction())
        # Add to Display Mode
        self.menuDisplay_Mode.addAction(self.actionWiggle)
        self.menuDisplay_Mode.addAction(self.actionPseudo_Color)
        self.menuView.addAction(self.actionScan_Line)
        # Add Color Map to View
        self.menuView.addAction(self.menuColor_Map.menuAction())
        # Add to Color Map
        self.menuColor_Map.addAction(self.actionAccent)
        self.menuColor_Map.addAction(self.actionBlues)
        self.menuColor_Map.addAction(self.actionBrBG)
        self.menuColor_Map.addAction(self.actionBuGn)
        self.menuColor_Map.addAction(self.actionBuPu)
        self.menuColor_Map.addAction(self.actionCMRmap)
        self.menuColor_Map.addAction(self.actionDark2)
        self.menuColor_Map.addAction(self.actionGnBu)
        self.menuColor_Map.addAction(self.actionGreens)
        self.menuColor_Map.addAction(self.actionGreys)
        self.menuColor_Map.addAction(self.actionOrRd)
        self.menuColor_Map.addAction(self.actionOranges)
        self.menuColor_Map.addAction(self.actionPRGn)
        self.menuColor_Map.addAction(self.actionPaired)
        self.menuColor_Map.addAction(self.actionPastel1)
        self.menuColor_Map.addAction(self.actionPastel2)
        self.menuColor_Map.addAction(self.actionPiYG)
        self.menuColor_Map.addAction(self.actionPuBu)
        self.menuColor_Map.addAction(self.actionPuBuGn)
        self.menuColor_Map.addAction(self.actionPuOr)
        self.menuColor_Map.addAction(self.actionPuRd)
        self.menuColor_Map.addAction(self.actionPurples)
        self.menuColor_Map.addAction(self.actionRdBu)
        self.menuColor_Map.addAction(self.actionRdGy)
        self.menuColor_Map.addAction(self.actionRdPu)
        self.menuColor_Map.addAction(self.actionRdYlBu)
        self.menuColor_Map.addAction(self.actionRdYlGn)
        self.menuColor_Map.addAction(self.actionReds)
        self.menuColor_Map.addAction(self.actionSet1)
        self.menuColor_Map.addAction(self.actionSet2)
        self.menuColor_Map.addAction(self.actionSet3)
        self.menuColor_Map.addAction(self.actionSpectral)
        self.menuColor_Map.addAction(self.actionVega10)
        self.menuColor_Map.addAction(self.actionVega20)
        self.menuColor_Map.addAction(self.actionVega20b)
        self.menuColor_Map.addAction(self.actionVega20c)
        self.menuColor_Map.addAction(self.actionWistia)
        self.menuColor_Map.addAction(self.actionYlGn)
        self.menuColor_Map.addAction(self.actionYlGnBu)
        self.menuColor_Map.addAction(self.actionYlOrBr)
        self.menuColor_Map.addAction(self.actionYlOrRd)
        self.menuColor_Map.addAction(self.actionafmhot)
        self.menuColor_Map.addAction(self.actionautumn)
        self.menuColor_Map.addAction(self.actionbinary)
        self.menuColor_Map.addAction(self.actionbone)
        self.menuColor_Map.addAction(self.actionbrg)
        self.menuColor_Map.addAction(self.actionbwr)
        self.menuColor_Map.addAction(self.actioncool)
        self.menuColor_Map.addAction(self.actioncoolwarm)
        self.menuColor_Map.addAction(self.actioncopper)
        self.menuColor_Map.addAction(self.actioncubehelix)
        self.menuColor_Map.addAction(self.actionflag)
        self.menuColor_Map.addAction(self.actiongist_earth)
        self.menuColor_Map.addAction(self.actiongist_gray)
        self.menuColor_Map.addAction(self.actiongist_heat)
        self.menuColor_Map.addAction(self.actiongist_ncar)
        self.menuColor_Map.addAction(self.actiongist_rainbow)
        self.menuColor_Map.addAction(self.actiongist_stern)
        self.menuColor_Map.addAction(self.actiongist_yarg)
        self.menuColor_Map.addAction(self.actiongnuplot)
        self.menuColor_Map.addAction(self.actiongnuplot2)
        self.menuColor_Map.addAction(self.actiongray)
        self.menuColor_Map.addAction(self.actionhot)
        self.menuColor_Map.addAction(self.actionhsv)
        self.menuColor_Map.addAction(self.actioninferno)
        self.menuColor_Map.addAction(self.actionjet)
        self.menuColor_Map.addAction(self.actionmagma)
        self.menuColor_Map.addAction(self.actionnipy_spectral)
        self.menuColor_Map.addAction(self.actionocean)
        self.menuColor_Map.addAction(self.actionpink)
        self.menuColor_Map.addAction(self.actionplasma)
        self.menuColor_Map.addAction(self.actionprism)
        self.menuColor_Map.addAction(self.actionrainbow)
        self.menuColor_Map.addAction(self.actionseismic)
        self.menuColor_Map.addAction(self.actionspectral)
        self.menuColor_Map.addAction(self.actionspring)
        self.menuColor_Map.addAction(self.actionsummer)
        self.menuColor_Map.addAction(self.actiontab10)
        self.menuColor_Map.addAction(self.actiontab20)
        self.menuColor_Map.addAction(self.actiontab20b)
        self.menuColor_Map.addAction(self.actiontab20c)
        self.menuColor_Map.addAction(self.actionterrain)
        self.menuColor_Map.addAction(self.actionviridis)
        self.menuColor_Map.addAction(self.actionwinter)
        # Add Display Gain to View
        self.menuView.addAction(self.menuDisplay_Gain.menuAction())
        # Add to Display Gain
        self.menuDisplay_Gain.addAction(self.actionZoomOutDisplayGain10)
        self.menuDisplay_Gain.addAction(self.actionZoomOutDisplayGain5)
        self.menuDisplay_Gain.addAction(self.actionZoomOutDisplayGain2)
        self.menuDisplay_Gain.addSeparator()
        self.menuDisplay_Gain.addAction(self.actionNormalDisplayGain)
        self.menuDisplay_Gain.addSeparator()
        self.menuDisplay_Gain.addAction(self.actionZoomDisplayGain2)
        self.menuDisplay_Gain.addAction(self.actionZoomDisplayGain5)
        self.menuDisplay_Gain.addAction(self.actionZoomDisplayGain10)
        self.menuDisplay_Gain.addAction(self.actionZoomDisplayGain20)
        # Add Scale Out to View
        self.menuView.addAction(self.menuScale_Out.menuAction())
        # Add to Scale Out
        self.menuScale_Out.addAction(self.actionZoomOutScaleOut10)
        self.menuScale_Out.addAction(self.actionZoomOutScaleOut5)
        self.menuScale_Out.addAction(self.actionZoomOutScaleOut2)
        self.menuScale_Out.addSeparator()
        self.menuScale_Out.addAction(self.actionNormalScaleOut)
        self.menuScale_Out.addSeparator()
        self.menuScale_Out.addAction(self.actionZoomScaleOut2)
        self.menuScale_Out.addAction(self.actionZoomScaleOut5)
        self.menuScale_Out.addAction(self.actionZoomScaleOut10)
        self.menuScale_Out.addAction(self.actionZoomScaleOut20)
        self.menuScale_Out.addAction(self.actionZoomScaleOut30)
        # Add Vertical Operation to View
        self.menuView.addAction(self.menuVertical_Operation.menuAction())
        # Add to Vertical Operation
        self.menuVertical_Operation.addAction(self.actionVerticalOperationSample)
        self.menuVertical_Operation.addAction(self.actionVerticalOperationTime)
        self.menuVertical_Operation.addAction(self.actionVerticalOperationDepth)
        
        
        self.menuHelp.addAction(self.actionHelp_Files)
        self.menuHelp.addAction(self.actionContants)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuData_Process.menuAction())
        self.menubar.addAction(self.menuModelling.menuAction())
        self.menubar.addAction(self.menuInversion_2D.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.ToolActionNewFile)
        self.toolBar.addAction(self.ToolActionOpenFile)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ToolActionSave)
        self.toolBar.addAction(self.ToolActionSaveAs)
        self.toolBar.addAction(self.ToolActionPrintPreview)
        self.toolBar.addAction(self.ToolActionPrint)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ToolActionModelling)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ToolActionHelp)
        self.toolBar.addAction(self.ToolContants)
        self.toolBar.addSeparator()
        
        ## Create dockWidgetsTools
        self.dockWidgetTools = QtWidgets.QDockWidget('Tools Windows',MainWindow)
        self.dockWidgetTools.setEnabled(True)
        self.dockWidgetTools.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetTools.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetTools.setObjectName("dockWidgetTools")
        self.dockWidgetTools.setEnabled(False)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        #vlayout with 2 frame
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        #create frame_View
        self.label_frame_View = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_frame_View.setObjectName("label_frame_View")
        self.verticalLayout.addWidget(self.label_frame_View)
        self.frame_View = QtWidgets.QFrame(self.dockWidgetContents)
        self.frame_View.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_View.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_View.setObjectName("frame_View")
        #grid layout within frame_View
        self.gridLayout = QtWidgets.QGridLayout(self.frame_View)
        self.gridLayout.setObjectName("gridLayout_View")
        
        self.toolButtonWigb = QtWidgets.QToolButton(self.frame_View)
        ToolBtniconWigb = QtGui.QIcon()
        ToolBtniconWigb.addPixmap(QtGui.QPixmap("./UI_Ico/wigb.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonWigb.setIcon(ToolBtniconWigb)
        self.toolButtonWigb.setIconSize(QtCore.QSize(40, 40))
        self.toolButtonWigb.setCheckable(True)
        # self.toolButtonWigb.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonWigb.setAutoRaise(True)
        self.toolButtonWigb.setObjectName("toolBtnButtonWigb")
        self.gridLayout.addWidget(self.toolButtonWigb, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.toolButtonPcolor = QtWidgets.QToolButton(self.frame_View)
        ToolBtniconPcolor = QtGui.QIcon()
        ToolBtniconPcolor.addPixmap(QtGui.QPixmap("./UI_Ico/pcolor.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonPcolor.setIcon(ToolBtniconPcolor)
        self.toolButtonPcolor.setIconSize(QtCore.QSize(40, 40))
        self.toolButtonPcolor.setCheckable(True)
        # self.toolButtonPcolor.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonPcolor.setAutoRaise(True)
        self.toolButtonPcolor.setObjectName("toolButtonPcolor")
        self.gridLayout.addWidget(self.toolButtonPcolor, 0, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        # Wiggle and PColor State Switching
        self.toolButtonWigb.clicked.connect(self.SwitchingStateWigb)
        self.toolButtonPcolor.clicked.connect(self.SwitchingStatePColor)
        
        self.toolButtonScanLine = QtWidgets.QToolButton(self.frame_View)
        ToolBtniconScanLine = QtGui.QIcon()
        ToolBtniconScanLine.addPixmap(QtGui.QPixmap("./UI_Ico/scanline.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonScanLine.setIcon(ToolBtniconScanLine)
        self.toolButtonScanLine.setIconSize(QtCore.QSize(40, 40))
        # self.toolButtonScanLine.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonScanLine.setAutoRaise(True)
        self.toolButtonScanLine.setCheckable(True)
        self.toolButtonScanLine.setObjectName("toolButtonScanLine")
        self.gridLayout.addWidget(self.toolButtonScanLine, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.toolButtonColorMap = QtWidgets.QToolButton(self.frame_View)
        ToolBtniconColorMap = QtGui.QIcon()
        ToolBtniconColorMap.addPixmap(QtGui.QPixmap("./UI_Ico/colormap.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonColorMap.setIcon(ToolBtniconColorMap)
        self.toolButtonColorMap.setIconSize(QtCore.QSize(40, 40))
        self.toolButtonColorMap.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        # Add Color Map
        self.ToolButtonMenu = QtWidgets.QMenu(self)
        # Accent
        self.AccentColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Accent.ico'),'Accent', self)
        self.ToolButtonMenu.addAction(self.AccentColorMap)
        self.AccentColorMap.triggered.connect(lambda: self.ChangeCmap(self.AccentColorMap.text()))
        # Blues
        self.BluesColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Blues.ico'),'Blues', self)
        self.ToolButtonMenu.addAction(self.BluesColorMap)
        self.BluesColorMap.triggered.connect(lambda: self.ChangeCmap(self.BluesColorMap.text()))
        # BrBG
        self.BrBGColorMap = QtWidgets.QAction(QtGui.QIcon('icon/BrBG.ico'),'BrBG', self)
        self.ToolButtonMenu.addAction(self.BrBGColorMap)
        self.BrBGColorMap.triggered.connect(lambda: self.ChangeCmap(self.BrBGColorMap.text()))
        # BuGn
        self.BuGnColorMap = QtWidgets.QAction(QtGui.QIcon('icon/BuGn.ico'),'BuGn', self)
        self.ToolButtonMenu.addAction(self.BuGnColorMap)
        self.BrBGColorMap.triggered.connect(lambda: self.ChangeCmap(self.BuGnColorMap.text()))
        # BuPu
        self.BuPuColorMap = QtWidgets.QAction(QtGui.QIcon('icon/BuPu.ico'),'BuPu', self)
        self.ToolButtonMenu.addAction(self.BuPuColorMap)
        self.BuPuColorMap.triggered.connect(lambda: self.ChangeCmap(self.BuPuColorMap.text()))
        # BuPu
        self.CMRmapColorMap = QtWidgets.QAction(QtGui.QIcon('icon/CMRmap.ico'),'CMRmap', self)
        self.ToolButtonMenu.addAction(self.CMRmapColorMap)
        self.CMRmapColorMap.triggered.connect(lambda: self.ChangeCmap(self.CMRmapColorMap.text()))
        # Dark2
        self.Dark2ColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Dark2.ico'),'Dark2', self)
        self.ToolButtonMenu.addAction(self.Dark2ColorMap)
        self.Dark2ColorMap.triggered.connect(lambda: self.ChangeCmap(self.Dark2ColorMap.text()))
        # GnBu
        self.GnBuColorMap = QtWidgets.QAction(QtGui.QIcon('icon/GnBu.ico'),'GnBu', self)
        self.ToolButtonMenu.addAction(self.GnBuColorMap)
        self.GnBuColorMap.triggered.connect(lambda: self.ChangeCmap(self.GnBuColorMap.text()))
        # Greens       
        self.GreensColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Greens.ico'),'Greens', self)
        self.ToolButtonMenu.addAction(self.GreensColorMap)
        self.GreensColorMap.triggered.connect(lambda: self.ChangeCmap(self.GreensColorMap.text()))
        # Greys
        self.GreysColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Greys.ico'),'Greys', self)
        self.ToolButtonMenu.addAction(self.GreysColorMap)
        self.GreysColorMap.triggered.connect(lambda: self.ChangeCmap(self.GreysColorMap.text()))
        # OrRd
        self.OrRdColorMap = QtWidgets.QAction(QtGui.QIcon('icon/OrRd.ico'),'OrRd', self)
        self.ToolButtonMenu.addAction(self.OrRdColorMap)
        self.OrRdColorMap.triggered.connect(lambda: self.ChangeCmap(self.OrRdColorMap.text()))
        # Oranges
        self.OrangesColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Oranges.ico'),'Oranges', self)
        self.ToolButtonMenu.addAction(self.OrangesColorMap)
        self.OrangesColorMap.triggered.connect(lambda: self.ChangeCmap(self.OrangesColorMap.text()))
        # PRGn
        self.PRGnColorMap = QtWidgets.QAction(QtGui.QIcon('icon/PRGn.ico'),'PRGn', self)
        self.ToolButtonMenu.addAction(self.PRGnColorMap)
        self.PRGnColorMap.triggered.connect(lambda: self.ChangeCmap(self.PRGnColorMap.text()))
        # Paired
        self.PairedColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Paired.ico'),'Paired', self)
        self.ToolButtonMenu.addAction(self.PairedColorMap)
        self.PairedColorMap.triggered.connect(lambda: self.ChangeCmap(self.PairedColorMap.text()))
        # Pastel1
        self.Pastel1ColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Pastel1.ico'),'Pastel1', self)
        self.ToolButtonMenu.addAction(self.Pastel1ColorMap)
        self.Pastel1ColorMap.triggered.connect(lambda: self.ChangeCmap(self.Pastel1ColorMap.text()))
        # Pastel2
        self.Pastel2ColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Pastel2.ico'),'Pastel2', self)
        self.ToolButtonMenu.addAction(self.Pastel2ColorMap)
        self.Pastel2ColorMap.triggered.connect(lambda: self.ChangeCmap(self.Pastel2ColorMap.text()))
        # PiYG
        self.PiYGMap = QtWidgets.QAction(QtGui.QIcon('icon/PiYG.ico'),'PiYG', self)
        self.ToolButtonMenu.addAction(self.PiYGMap)
        self.PiYGMap.triggered.connect(lambda: self.ChangeCmap(self.PiYGMap.text()))
        # PuBu
        self.PuBuColorMap = QtWidgets.QAction(QtGui.QIcon('icon/PuBu.ico'),'PuBu', self)
        self.ToolButtonMenu.addAction(self.PuBuColorMap)
        self.PuBuColorMap.triggered.connect(lambda: self.ChangeCmap(self.PuBuColorMap.text()))
        # PuBuGn
        self.PuBuGnColorMap = QtWidgets.QAction(QtGui.QIcon('icon/PuBuGn.ico'),'PuBuGn', self)
        self.ToolButtonMenu.addAction(self.PuBuGnColorMap)
        self.PuBuGnColorMap.triggered.connect(lambda: self.ChangeCmap(self.PuBuGnColorMap.text()))
        # PuOr
        self.PuOrColorMap = QtWidgets.QAction(QtGui.QIcon('icon/PuOr.ico'),'PuOr', self)
        self.ToolButtonMenu.addAction(self.PuOrColorMap)
        self.PuOrColorMap.triggered.connect(lambda: self.ChangeCmap(self.PuOrColorMap.text()))
        # PuRd
        self.PuRdColorMap = QtWidgets.QAction(QtGui.QIcon('icon/PuRd.ico'),'PuRd', self)
        self.ToolButtonMenu.addAction(self.PuRdColorMap)
        self.PuRdColorMap.triggered.connect(lambda: self.ChangeCmap(self.PuRdColorMap.text()))
        # Purples
        self.PurplesColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Purples.ico'),'Purples', self)
        self.ToolButtonMenu.addAction(self.PurplesColorMap)
        self.PurplesColorMap.triggered.connect(lambda: self.ChangeCmap(self.PurplesColorMap.text()))
        # RdBu
        self.RdBuColorMap = QtWidgets.QAction(QtGui.QIcon('icon/RdBu.ico'),'RdBu', self)
        self.ToolButtonMenu.addAction(self.RdBuColorMap)
        self.RdBuColorMap.triggered.connect(lambda: self.ChangeCmap(self.RdBuColorMap.text()))
        # RdGy
        self.RdGyColorMap = QtWidgets.QAction(QtGui.QIcon('icon/RdGy.ico'),'RdGy', self)
        self.ToolButtonMenu.addAction(self.RdGyColorMap)
        self.RdGyColorMap.triggered.connect(lambda: self.ChangeCmap(self.RdGyColorMap.text()))
        # RdPu
        self.RdPuColorMap = QtWidgets.QAction(QtGui.QIcon('icon/RdPu.ico'),'RdPu', self)
        self.ToolButtonMenu.addAction(self.RdPuColorMap)
        self.RdPuColorMap.triggered.connect(lambda: self.ChangeCmap(self.RdPuColorMap.text()))
        # RdYlBu
        self.RdYlBuColorMap = QtWidgets.QAction(QtGui.QIcon('icon/RdYlBu.ico'),'RdYlBu', self)
        self.ToolButtonMenu.addAction(self.RdYlBuColorMap)
        self.RdYlBuColorMap.triggered.connect(lambda: self.ChangeCmap(self.RdYlBuColorMap.text()))
        # RdYlGn
        self.RdYlGnColorMap = QtWidgets.QAction(QtGui.QIcon('icon/RdYlGn.ico'),'RdYlGn', self)
        self.ToolButtonMenu.addAction(self.RdYlGnColorMap)
        self.RdYlGnColorMap.triggered.connect(lambda: self.ChangeCmap(self.RdYlGnColorMap.text()))
        # Reds
        self.RedsColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Reds.ico'),'Reds', self)
        self.ToolButtonMenu.addAction(self.RedsColorMap)
        self.RedsColorMap.triggered.connect(lambda: self.ChangeCmap(self.RedsColorMap.text()))
        # Set1
        self.Set1ColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Set1.ico'),'Set1', self)
        self.ToolButtonMenu.addAction(self.Set1ColorMap)
        self.Set1ColorMap.triggered.connect(lambda: self.ChangeCmap(self.Set1ColorMap.text()))
        # Set2
        self.Set2ColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Set2.ico'),'Set2', self)
        self.ToolButtonMenu.addAction(self.Set2ColorMap)
        self.Set2ColorMap.triggered.connect(lambda: self.ChangeCmap(self.Set2ColorMap.text()))
        # Set3
        self.Set3ColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Set3.ico'),'Set3', self)
        self.ToolButtonMenu.addAction(self.Set3ColorMap)
        self.Set3ColorMap.triggered.connect(lambda: self.ChangeCmap(self.Set3ColorMap.text()))
        # Spectral
        self.SpectralColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Spectral.ico'),'Spectral', self)
        self.ToolButtonMenu.addAction(self.SpectralColorMap)
        self.SpectralColorMap.triggered.connect(lambda: self.ChangeCmap(self.SpectralColorMap.text()))
        # Vega10
        self.Vega10ColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Vega10.ico'),'Vega10', self)
        self.ToolButtonMenu.addAction(self.Vega10ColorMap)
        self.Vega10ColorMap.triggered.connect(lambda: self.ChangeCmap(self.Vega10ColorMap.text()))
        # Vega20
        self.Vega20ColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Vega20.ico'),'Vega20', self)
        self.ToolButtonMenu.addAction(self.Vega20ColorMap)
        self.Vega20ColorMap.triggered.connect(lambda: self.ChangeCmap(self.Vega20ColorMap.text()))
        # Vega20b
        self.Vega20bColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Vega20b.ico'),'Vega20b', self)
        self.ToolButtonMenu.addAction(self.Vega20bColorMap)
        self.Vega20bColorMap.triggered.connect(lambda: self.ChangeCmap(self.Vega20bColorMap.text()))
        # Vega20c
        self.Vega20cColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Vega20c.ico'),'Vega20c', self)
        self.ToolButtonMenu.addAction(self.Vega20cColorMap)
        self.Vega20cColorMap.triggered.connect(lambda: self.ChangeCmap(self.Vega20cColorMap.text()))
        # Wistia
        self.WistiaColorMap = QtWidgets.QAction(QtGui.QIcon('icon/Wistia.ico'),'Wistia', self)
        self.ToolButtonMenu.addAction(self.WistiaColorMap)
        self.WistiaColorMap.triggered.connect(lambda: self.ChangeCmap(self.WistiaColorMap.text()))
        # YlGn
        self.YlGnColorMap = QtWidgets.QAction(QtGui.QIcon('icon/YlGn.ico'),'YlGn', self)
        self.ToolButtonMenu.addAction(self.YlGnColorMap)
        self.YlGnColorMap.triggered.connect(lambda: self.ChangeCmap(self.YlGnColorMap.text()))
        # YlGnBu
        self.YlGnBuColorMap = QtWidgets.QAction(QtGui.QIcon('icon/YlGnBu.ico'),'YlGnBu', self)
        self.ToolButtonMenu.addAction(self.YlGnBuColorMap)
        self.YlGnBuColorMap.triggered.connect(lambda: self.ChangeCmap(self.YlGnBuColorMap.text()))
        # YlOrBr
        self.YlOrBrColorMap = QtWidgets.QAction(QtGui.QIcon('icon/YlOrBr.ico'),'YlOrBr', self)
        self.ToolButtonMenu.addAction(self.YlOrBrColorMap)
        self.YlOrBrColorMap.triggered.connect(lambda: self.ChangeCmap(self.YlOrBrColorMap.text()))
        # YlOrRd
        self.YlOrRdColorMap = QtWidgets.QAction(QtGui.QIcon('icon/YlOrRd.ico'),'YlOrRd', self)
        self.ToolButtonMenu.addAction(self.YlOrRdColorMap)
        self.YlOrRdColorMap.triggered.connect(lambda: self.ChangeCmap(self.YlOrRdColorMap.text()))
        # afmhot
        self.afmhotColorMap = QtWidgets.QAction(QtGui.QIcon('icon/afmhot.ico'),'afmhot', self)
        self.ToolButtonMenu.addAction(self.afmhotColorMap)
        self.afmhotColorMap.triggered.connect(lambda: self.ChangeCmap(self.afmhotColorMap.text()))
        # autumn
        self.autumnColorMap = QtWidgets.QAction(QtGui.QIcon('icon/autumn.ico'),'autumn', self)
        self.ToolButtonMenu.addAction(self.autumnColorMap)
        self.autumnColorMap.triggered.connect(lambda: self.ChangeCmap(self.autumnColorMap.text()))
        # binary
        self.binaryColorMap = QtWidgets.QAction(QtGui.QIcon('icon/binary.ico'),'binary', self)
        self.ToolButtonMenu.addAction(self.binaryColorMap)
        self.binaryColorMap.triggered.connect(lambda: self.ChangeCmap(self.binaryColorMap.text()))
        # bone
        self.boneColorMap = QtWidgets.QAction(QtGui.QIcon('icon/bone.ico'),'bone', self)
        self.ToolButtonMenu.addAction(self.boneColorMap)
        self.boneColorMap.triggered.connect(lambda: self.ChangeCmap(self.boneColorMap.text()))
        # brg
        self.brgColorMap = QtWidgets.QAction(QtGui.QIcon('icon/brg.ico'),'brg', self)
        self.ToolButtonMenu.addAction(self.brgColorMap)
        self.brgColorMap.triggered.connect(lambda: self.ChangeCmap(self.brgColorMap.text()))
        # bwr
        self.bwrColorMap = QtWidgets.QAction(QtGui.QIcon('icon/bwr.ico'),'bwr', self)
        self.ToolButtonMenu.addAction(self.bwrColorMap)
        self.bwrColorMap.triggered.connect(lambda: self.ChangeCmap(self.bwrColorMap.text()))
        # cool
        self.coolColorMap = QtWidgets.QAction(QtGui.QIcon('icon/cool.ico'),'cool', self)
        self.ToolButtonMenu.addAction(self.coolColorMap)
        self.coolColorMap.triggered.connect(lambda: self.ChangeCmap(self.coolColorMap.text()))
        # coolwarm
        self.coolwarmColorMap = QtWidgets.QAction(QtGui.QIcon('icon/coolwarm.ico'),'coolwarm', self)
        self.ToolButtonMenu.addAction(self.coolwarmColorMap)
        self.coolwarmColorMap.triggered.connect(lambda: self.ChangeCmap(self.coolwarmColorMap.text()))
        # copper
        self.copperColorMap = QtWidgets.QAction(QtGui.QIcon('icon/copper.ico'),'copper', self)
        self.ToolButtonMenu.addAction(self.copperColorMap)
        self.copperColorMap.triggered.connect(lambda: self.ChangeCmap(self.copperColorMap.text()))
        # cubehelix
        self.cubehelixColorMap = QtWidgets.QAction(QtGui.QIcon('icon/cubehelix.ico'),'cubehelix', self)
        self.ToolButtonMenu.addAction(self.cubehelixColorMap)
        self.cubehelixColorMap.triggered.connect(lambda: self.ChangeCmap(self.cubehelixColorMap.text()))
        # flag
        self.flagColorMap = QtWidgets.QAction(QtGui.QIcon('icon/flag.ico'),'flag', self)
        self.ToolButtonMenu.addAction(self.flagColorMap)
        self.flagColorMap.triggered.connect(lambda: self.ChangeCmap(self.flagColorMap.text()))
        # gist_earth
        self.gist_earthColorMap = QtWidgets.QAction(QtGui.QIcon('icon/gist_earth.ico'),'gist_earth', self)
        self.ToolButtonMenu.addAction(self.gist_earthColorMap)
        self.gist_earthColorMap.triggered.connect(lambda: self.ChangeCmap(self.gist_earthColorMap.text()))
        # gist_gray
        self.gist_grayColorMap = QtWidgets.QAction(QtGui.QIcon('icon/gist_gray.ico'),'gist_gray', self)   
        self.ToolButtonMenu.addAction(self.gist_grayColorMap)
        self.gist_grayColorMap.triggered.connect(lambda: self.ChangeCmap(self.gist_grayColorMap.text()))
        # gist_heat
        self.gist_heatColorMap = QtWidgets.QAction(QtGui.QIcon('icon/gist_heat.ico'),'gist_heat', self)
        self.ToolButtonMenu.addAction(self.gist_heatColorMap)
        self.gist_heatColorMap.triggered.connect(lambda: self.ChangeCmap(self.gist_heatColorMap.text()))
        # gist_ncar
        self.gist_ncarColorMap = QtWidgets.QAction(QtGui.QIcon('icon/gist_ncar.ico'),'gist_ncar', self)
        self.ToolButtonMenu.addAction(self.gist_ncarColorMap)
        self.gist_ncarColorMap.triggered.connect(lambda: self.ChangeCmap(self.gist_ncarColorMap.text()))
        # gist_rainbow
        self.gist_rainbowColorMap = QtWidgets.QAction(QtGui.QIcon('icon/gist_rainbow.ico'),'gist_rainbow', self)
        self.ToolButtonMenu.addAction(self.gist_rainbowColorMap)
        self.gist_rainbowColorMap.triggered.connect(lambda: self.ChangeCmap(self.gist_rainbowColorMap.text()))
        # gist_stern
        self.gist_sternColorMap = QtWidgets.QAction(QtGui.QIcon('icon/gist_stern.ico'),'gist_stern', self)
        self.ToolButtonMenu.addAction(self.gist_sternColorMap)
        self.gist_sternColorMap.triggered.connect(lambda: self.ChangeCmap(self.gist_sternColorMap.text()))
        # gist_yarg
        self.gist_yargColorMap = QtWidgets.QAction(QtGui.QIcon('icon/gist_yarg.ico'),'gist_yarg', self)
        self.ToolButtonMenu.addAction(self.gist_yargColorMap)
        self.gist_yargColorMap.triggered.connect(lambda: self.ChangeCmap(self.gist_yargColorMap.text()))
        # gnuplot
        self.gnuplotColorMap = QtWidgets.QAction(QtGui.QIcon('icon/gnuplot.ico'),'gnuplot', self)
        self.ToolButtonMenu.addAction(self.gnuplotColorMap)
        self.gnuplotColorMap.triggered.connect(lambda: self.ChangeCmap(self.gnuplotColorMap.text()))
        # gnuplot2
        self.gnuplot2ColorMap = QtWidgets.QAction(QtGui.QIcon('icon/gnuplot2.ico'),'gnuplot2', self)
        self.ToolButtonMenu.addAction(self.gnuplot2ColorMap)
        self.gnuplot2ColorMap.triggered.connect(lambda: self.ChangeCmap(self.gnuplot2ColorMap.text()))
        # gray
        self.grayColorMap = QtWidgets.QAction(QtGui.QIcon('icon/gray.ico'),'gray', self)
        self.ToolButtonMenu.addAction(self.grayColorMap)
        self.grayColorMap.triggered.connect(lambda: self.ChangeCmap(self.grayColorMap.text()))
        # hot
        self.hotColorMap = QtWidgets.QAction(QtGui.QIcon('icon/hot.ico'),'hot', self)
        self.ToolButtonMenu.addAction(self.hotColorMap)
        self.hotColorMap.triggered.connect(lambda: self.ChangeCmap(self.hotColorMap.text()))
        # hsv
        self.hsvColorMap = QtWidgets.QAction(QtGui.QIcon('icon/hsv.ico'),'hsv', self)
        self.ToolButtonMenu.addAction(self.hsvColorMap)
        self.hsvColorMap.triggered.connect(lambda: self.ChangeCmap(self.hsvColorMap.text()))
        # inferno
        self.infernoColorMap = QtWidgets.QAction(QtGui.QIcon('icon/inferno.ico'),'inferno', self)
        self.ToolButtonMenu.addAction(self.infernoColorMap)
        self.infernoColorMap.triggered.connect(lambda: self.ChangeCmap(self.infernoColorMap.text()))
        # jet
        self.jetColorMap = QtWidgets.QAction(QtGui.QIcon('icon/jet.ico'),'jet', self)
        self.ToolButtonMenu.addAction(self.jetColorMap)
        self.jetColorMap.triggered.connect(lambda: self.ChangeCmap(self.jetColorMap.text()))
        # magma
        self.magmaColorMap = QtWidgets.QAction(QtGui.QIcon('icon/magma.ico'),'magma', self)
        self.ToolButtonMenu.addAction(self.magmaColorMap)
        self.magmaColorMap.triggered.connect(lambda: self.ChangeCmap(self.magmaColorMap.text()))
        # nipy_spectral
        self.nipy_spectralColorMap = QtWidgets.QAction(QtGui.QIcon('icon/nipy_spectral.ico'),'nipy_spectral', self)
        self.ToolButtonMenu.addAction(self.nipy_spectralColorMap)
        self.nipy_spectralColorMap.triggered.connect(lambda: self.ChangeCmap(self.nipy_spectralColorMap.text()))
        # ocean
        self.oceanColorMap = QtWidgets.QAction(QtGui.QIcon('icon/ocean.ico'),'ocean', self)
        self.ToolButtonMenu.addAction(self.oceanColorMap)
        self.oceanColorMap.triggered.connect(lambda: self.ChangeCmap(self.oceanColorMap.text()))
        # pink
        self.pinkColorMap = QtWidgets.QAction(QtGui.QIcon('icon/pink.ico'),'pink', self)
        self.ToolButtonMenu.addAction(self.pinkColorMap)
        self.pinkColorMap.triggered.connect(lambda: self.ChangeCmap(self.pinkColorMap.text()))
        # plasma
        self.plasmaColorMap = QtWidgets.QAction(QtGui.QIcon('icon/plasma.ico'),'plasma', self)
        self.ToolButtonMenu.addAction(self.plasmaColorMap)
        self.plasmaColorMap.triggered.connect(lambda: self.ChangeCmap(self.plasmaColorMap.text()))
        # prism
        self.prismColorMap = QtWidgets.QAction(QtGui.QIcon('icon/prism.ico'),'prism', self)
        self.ToolButtonMenu.addAction(self.prismColorMap)
        self.prismColorMap.triggered.connect(lambda: self.ChangeCmap(self.prismColorMap.text()))
        # rainbow
        self.rainbowColorMap = QtWidgets.QAction(QtGui.QIcon('icon/rainbow.ico'),'rainbow', self)
        self.ToolButtonMenu.addAction(self.rainbowColorMap)
        self.rainbowColorMap.triggered.connect(lambda: self.ChangeCmap(self.rainbowColorMap.text()))
        # seismic
        self.seismicColorMap = QtWidgets.QAction(QtGui.QIcon('icon/seismic.ico'),'seismic', self)
        self.ToolButtonMenu.addAction(self.seismicColorMap)
        self.seismicColorMap.triggered.connect(lambda: self.ChangeCmap(self.seismicColorMap.text()))
        # spectral
        self.spectralColorMap = QtWidgets.QAction(QtGui.QIcon('icon/spectral.ico'),'spectral', self)
        self.ToolButtonMenu.addAction(self.spectralColorMap)
        self.spectralColorMap.triggered.connect(lambda: self.ChangeCmap(self.spectralColorMap.text()))
        # spring
        self.springColorMap = QtWidgets.QAction(QtGui.QIcon('icon/spring.ico'),'spring', self)
        self.ToolButtonMenu.addAction(self.springColorMap)
        self.springColorMap.triggered.connect(lambda: self.ChangeCmap(self.springColorMap.text()))
        # summer
        self.summerColorMap = QtWidgets.QAction(QtGui.QIcon('icon/summer.ico'),'summer', self)
        self.ToolButtonMenu.addAction(self.summerColorMap)
        self.summerColorMap.triggered.connect(lambda: self.ChangeCmap(self.summerColorMap.text()))
        # tab10
        self.tab10ColorMap = QtWidgets.QAction(QtGui.QIcon('icon/tab10.ico'),'tab10', self)
        self.ToolButtonMenu.addAction(self.tab10ColorMap)
        self.tab10ColorMap.triggered.connect(lambda: self.ChangeCmap(self.tab10ColorMap.text()))
        # tab20
        self.tab20ColorMap = QtWidgets.QAction(QtGui.QIcon('icon/tab20.ico'),'tab20', self)
        self.ToolButtonMenu.addAction(self.tab20ColorMap)
        self.tab20ColorMap.triggered.connect(lambda: self.ChangeCmap(self.tab20ColorMap.text()))
        # tab20b
        self.tab20bColorMap = QtWidgets.QAction(QtGui.QIcon('icon/tab20b.ico'),'tab20b', self)
        self.ToolButtonMenu.addAction(self.tab20bColorMap)
        self.tab20bColorMap.triggered.connect(lambda: self.ChangeCmap(self.tab20bColorMap.text()))
        # tab20c
        self.tab20cColorMap = QtWidgets.QAction(QtGui.QIcon('icon/tab20c.ico'),'tab20c', self)
        self.ToolButtonMenu.addAction(self.tab20cColorMap)
        self.tab20cColorMap.triggered.connect(lambda: self.ChangeCmap(self.tab20cColorMap.text()))
        # terrain
        self.terrainColorMap = QtWidgets.QAction(QtGui.QIcon('icon/terrain.ico'),'terrain', self)
        self.ToolButtonMenu.addAction(self.terrainColorMap)
        self.terrainColorMap.triggered.connect(lambda: self.ChangeCmap(self.terrainColorMap.text()))
        # viridis
        self.viridisColorMap = QtWidgets.QAction(QtGui.QIcon('icon/viridis.ico'),'viridis', self)
        self.ToolButtonMenu.addAction(self.viridisColorMap)
        self.viridisColorMap.triggered.connect(lambda: self.ChangeCmap(self.viridisColorMap.text()))
        # winter
        self.winterColorMap = QtWidgets.QAction(QtGui.QIcon('icon/winter.ico'),'winter', self)
        self.ToolButtonMenu.addAction(self.winterColorMap)
        self.winterColorMap.triggered.connect(lambda: self.ChangeCmap(self.winterColorMap.text()))
    
        self.toolButtonColorMap.setMenu(self.ToolButtonMenu)
        
        # self.toolButtonColorMap.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonColorMap.setAutoRaise(True)
        self.toolButtonColorMap.setObjectName("toolButtonColorMap")
        self.gridLayout.addWidget(self.toolButtonColorMap, 1, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.toolButtonDisplayGain = QtWidgets.QToolButton(self.frame_View)
        ToolBtniconDisplayGain = QtGui.QIcon()
        ToolBtniconDisplayGain.addPixmap(QtGui.QPixmap("./UI_Ico/displaygain.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonDisplayGain.setIcon(ToolBtniconDisplayGain)
        self.toolButtonDisplayGain.setIconSize(QtCore.QSize(40, 40))
        # self.toolButtonDisplayGain.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonDisplayGain.setAutoRaise(True)
        self.toolButtonDisplayGain.setObjectName("toolButtonDisplayGain")
        self.toolButtonDisplayGain.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.gridLayout.addWidget(self.toolButtonDisplayGain, 2, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        # Add DisplayGain Menu
        self.ToolButtonMenu = QtWidgets.QMenu(self)
        # 0.1
        self.ZoomOutDisplayGain10 = QtWidgets.QAction('0.1', self)
        self.ToolButtonMenu.addAction(self.ZoomOutDisplayGain10)
        # self.ZoomOutDisplayGain10.setCheckable(True)
        self.ZoomOutDisplayGain10.triggered.connect(lambda: self.ChangeGain(self.ZoomOutDisplayGain10.text()))
        # 0.2
        self.ZoomOutDisplayGain5 = QtWidgets.QAction('0.2', self)
        self.ToolButtonMenu.addAction(self.ZoomOutDisplayGain5)
        # self.ZoomOutDisplayGain5.setCheckable(True)
        self.ZoomOutDisplayGain5.triggered.connect(lambda: self.ChangeGain(self.ZoomOutDisplayGain5.text()))
        # 0.5
        self.ZoomOutDisplayGain2 = QtWidgets.QAction('0.5', self)
        self.ToolButtonMenu.addAction(self.ZoomOutDisplayGain2)
        # self.ZoomOutDisplayGain2.setCheckable(True)
        self.ZoomOutDisplayGain2.triggered.connect(lambda: self.ChangeGain(self.ZoomOutDisplayGain2.text()))
        self.ToolButtonMenu.addSeparator()
        # 1
        self.NormalDisplayGain = QtWidgets.QAction('1', self)
        self.ToolButtonMenu.addAction(self.NormalDisplayGain)
        # self.NormalDisplayGain.setCheckable(True)
        self.NormalDisplayGain.triggered.connect(lambda: self.ChangeGain(self.NormalDisplayGain.text()))
        self.ToolButtonMenu.addSeparator()
        # 2
        self.ZoomDisplayGain2 = QtWidgets.QAction('2', self)
        self.ToolButtonMenu.addAction(self.ZoomDisplayGain2)
        # self.ZoomDisplayGain2.setCheckable(True)
        self.ZoomDisplayGain2.triggered.connect(lambda: self.ChangeGain(self.ZoomDisplayGain2.text()))
        # 5
        self.ZoomDisplayGain5 = QtWidgets.QAction('5', self)
        self.ToolButtonMenu.addAction(self.ZoomDisplayGain5)
        # self.ZoomDisplayGain5.setCheckable(True)
        self.ZoomDisplayGain5.triggered.connect(lambda: self.ChangeGain(self.ZoomDisplayGain5.text()))
        # 10
        self.ZoomDisplayGain10 = QtWidgets.QAction('10', self)
        self.ToolButtonMenu.addAction(self.ZoomDisplayGain10)
        # self.ZoomDisplayGain10.setCheckable(True)
        self.ZoomDisplayGain10.triggered.connect(lambda: self.ChangeGain(self.ZoomDisplayGain10.text()))
        # 20
        self.ZoomDisplayGain20 = QtWidgets.QAction('20', self)
        self.ToolButtonMenu.addAction(self.ZoomDisplayGain20)
        # self.ZoomDisplayGain20.setCheckable(True)
        self.ZoomDisplayGain20.triggered.connect(lambda: self.ChangeGain(self.ZoomDisplayGain20.text()))
        self.toolButtonDisplayGain.setMenu(self.ToolButtonMenu)
        
        self.toolButtonScaleOut = QtWidgets.QToolButton(self.frame_View)
        ToolBtniconScaleOut = QtGui.QIcon()
        ToolBtniconScaleOut.addPixmap(QtGui.QPixmap("./UI_Ico/scaleout.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonScaleOut.setIcon(ToolBtniconScaleOut)
        self.toolButtonScaleOut.setIconSize(QtCore.QSize(40, 40))
        self.toolButtonScaleOut.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        # self.toolButtonScaleOut.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonScaleOut.setAutoRaise(True)
        self.toolButtonScaleOut.setObjectName("toolButtonScaleOut")
        self.gridLayout.addWidget(self.toolButtonScaleOut, 2, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)       
        # Add ScaleOut Menu
        self.ToolButtonMenu = QtWidgets.QMenu(self)
        # 0.1
        self.ZoomOutScaleOut10 = QtWidgets.QAction('0.1', self)
        self.ToolButtonMenu.addAction(self.ZoomOutScaleOut10)
        # self.ZoomOutScaleOut10.setCheckable(True)
        self.ZoomOutScaleOut10.triggered.connect(lambda: self.ChangeAspect(self.ZoomOutScaleOut10.text()))
        # 0.2
        self.ZoomOutScaleOut5 = QtWidgets.QAction('0.2', self)
        self.ToolButtonMenu.addAction(self.ZoomOutScaleOut5)
        # self.ZoomOutScaleOut5.setCheckable(True)
        self.ZoomOutScaleOut5.triggered.connect(lambda: self.ChangeAspect(self.ZoomOutScaleOut5.text()))
        # 0.5
        self.ZoomOutScaleOut2 = QtWidgets.QAction('0.5', self)
        self.ToolButtonMenu.addAction(self.ZoomOutScaleOut2)
        # self.ZoomOutScaleOut2.setCheckable(True)
        self.ZoomOutScaleOut2.triggered.connect(lambda: self.ChangeAspect(self.ZoomOutScaleOut2.text()))
        self.ToolButtonMenu.addSeparator()
        # 1
        self.NormalScale = QtWidgets.QAction('1', self)
        self.ToolButtonMenu.addAction(self.NormalScale)
        # self.NormalScale.setCheckable(True)
        self.NormalScale.triggered.connect(lambda: self.ChangeAspect(self.NormalScale.text()))
        self.ToolButtonMenu.addSeparator()
        # 2
        self.ZoomScale2 = QtWidgets.QAction('2', self)
        self.ToolButtonMenu.addAction(self.ZoomScale2)
        # self.ZoomScale2.setCheckable(True)
        self.ZoomScale2.triggered.connect(lambda: self.ChangeAspect(self.ZoomScale2.text()))
        # 5
        self.ZoomScale5 = QtWidgets.QAction('5', self)
        self.ToolButtonMenu.addAction(self.ZoomScale5)
        # self.ZoomScale5.setCheckable(True)
        self.ZoomScale5.triggered.connect(lambda: self.ChangeAspect(self.ZoomScale5.text()))
        # 10
        self.ZoomScale10 = QtWidgets.QAction('10', self)
        self.ToolButtonMenu.addAction(self.ZoomScale10)
        # self.ZoomScale10.setCheckable(True)
        self.ZoomScale10.triggered.connect(lambda: self.ChangeAspect(self.ZoomScale10.text()))
        # 20
        self.ZoomScale20 = QtWidgets.QAction('20', self)
        self.ToolButtonMenu.addAction(self.ZoomScale20)
        # self.ZoomScale20.setCheckable(True)
        self.ZoomScale20.triggered.connect(lambda: self.ChangeAspect(self.ZoomScale20.text()))
        # 30
        self.ZoomScale30 = QtWidgets.QAction('30', self)
        self.ToolButtonMenu.addAction(self.ZoomScale30)
        # self.ZoomScale30.setCheckable(True)
        self.ZoomScale30.triggered.connect(lambda: self.ChangeAspect(self.ZoomScale30.text()))
        self.toolButtonScaleOut.setMenu(self.ToolButtonMenu)
        
        self.widget_Placeholder0 = QtWidgets.QWidget(self.frame_View)
        self.widget_Placeholder0.setObjectName("widget_Placeholder0")
        self.gridLayout.addWidget(self.widget_Placeholder0, 3, 0, 1, 1)
        self.widget_Placeholder1 = QtWidgets.QWidget(self.frame_View)
        self.widget_Placeholder1.setObjectName("widget_Placeholder1")
        self.gridLayout.addWidget(self.widget_Placeholder1, 3, 1, 1, 1)
        
        self.verticalLayout.addWidget(self.frame_View)

        
        #create frame_Process
        self.label_frame_Process = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_frame_Process.setObjectName("label_frame_Process")
        self.verticalLayout.addWidget(self.label_frame_Process)
        
        self.frame_Process = QtWidgets.QFrame(self.dockWidgetContents)
        self.frame_Process.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Process.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Process.setObjectName("frame_Process")
        #grid layout within frame_View
        self.gridLayout = QtWidgets.QGridLayout(self.frame_Process)
        self.gridLayout.setObjectName("gridLayout_Process")
        
        self.toolButtonModifiedHeadFile = QtWidgets.QToolButton(self.frame_Process)
        ToolBtniconModifiedHeadFile = QtGui.QIcon()
        ToolBtniconModifiedHeadFile.addPixmap(QtGui.QPixmap("./UI_Ico/modifiedheadfile.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonModifiedHeadFile.setIcon(ToolBtniconModifiedHeadFile)
        self.toolButtonModifiedHeadFile.setIconSize(QtCore.QSize(40, 40))
        # self.toolButtonModifiedHeadFile.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonModifiedHeadFile.setAutoRaise(True)
        self.toolButtonModifiedHeadFile.setObjectName("toolBtnButtonModifiedHeadFile")
        self.gridLayout.addWidget(self.toolButtonModifiedHeadFile, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.toolButtonAreaGain = QtWidgets.QToolButton(self.frame_Process)
        ToolBtniconAreaGain = QtGui.QIcon()
        ToolBtniconAreaGain.addPixmap(QtGui.QPixmap("./UI_Ico/areagain.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonAreaGain.setIcon(ToolBtniconAreaGain)
        self.toolButtonAreaGain.setIconSize(QtCore.QSize(40, 40))
        # self.toolButtonAreaGain.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonAreaGain.setAutoRaise(True)
        self.toolButtonAreaGain.setObjectName("toolButtonAreaGain")
        self.gridLayout.addWidget(self.toolButtonAreaGain, 0, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.toolButtonDeleteTrack = QtWidgets.QToolButton(self.frame_Process)
        ToolBtniconDeleteTrack = QtGui.QIcon()
        ToolBtniconDeleteTrack.addPixmap(QtGui.QPixmap("./UI_Ico/deletetrack.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonDeleteTrack.setIcon(ToolBtniconDeleteTrack)
        self.toolButtonDeleteTrack.setIconSize(QtCore.QSize(40, 40))
        # self.toolButtonDeleteTrack.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonDeleteTrack.setAutoRaise(True)
        self.toolButtonDeleteTrack.setObjectName("toolButtonDeleteTrack")
        self.gridLayout.addWidget(self.toolButtonDeleteTrack, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.toolButtonExtractTrack = QtWidgets.QToolButton(self.frame_Process)
        ToolBtniconExtractTrack = QtGui.QIcon()
        ToolBtniconExtractTrack.addPixmap(QtGui.QPixmap("./UI_Ico/extracttrack.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonExtractTrack.setIcon(ToolBtniconExtractTrack)
        self.toolButtonExtractTrack.setIconSize(QtCore.QSize(40, 40))
        # self.toolButtonExtractTrack.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonExtractTrack.setAutoRaise(True)
        self.toolButtonExtractTrack.setObjectName("toolButtonExtractTrack")
        self.gridLayout.addWidget(self.toolButtonExtractTrack, 1, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.toolButtonZeroDrift = QtWidgets.QToolButton(self.frame_Process)
        ToolBtniconZeroDrift = QtGui.QIcon()
        ToolBtniconZeroDrift.addPixmap(QtGui.QPixmap("./UI_Ico/zerodrift.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonZeroDrift.setIcon(ToolBtniconZeroDrift)
        self.toolButtonZeroDrift.setIconSize(QtCore.QSize(40, 40))
        # self.toolButtonZeroDrift.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonZeroDrift.setAutoRaise(True)
        self.toolButtonZeroDrift.setObjectName("toolButtonZeroDrift")
        self.gridLayout.addWidget(self.toolButtonZeroDrift, 2, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.toolButtonFilter = QtWidgets.QToolButton(self.frame_Process)
        ToolBtniconFilter = QtGui.QIcon()
        ToolBtniconFilter.addPixmap(QtGui.QPixmap("./UI_Ico/filter.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonFilter.setIcon(ToolBtniconFilter)
        self.toolButtonFilter.setIconSize(QtCore.QSize(40, 40))
        # self.toolButtonFilter.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonFilter.setAutoRaise(True)
        self.toolButtonFilter.setObjectName("toolButtonFilter")
        self.gridLayout.addWidget(self.toolButtonFilter, 2, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)       
        
        self.toolButtonMigrate = QtWidgets.QToolButton(self.frame_Process)
        ToolBtniconMigrate = QtGui.QIcon()
        ToolBtniconMigrate.addPixmap(QtGui.QPixmap("./UI_Ico/migrate.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonMigrate.setIcon(ToolBtniconMigrate)
        self.toolButtonMigrate.setIconSize(QtCore.QSize(40, 40))
        # self.toolButtonMigrate.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonMigrate.setAutoRaise(True)
        self.toolButtonMigrate.setObjectName("toolButtonMigrate")
        self.gridLayout.addWidget(self.toolButtonMigrate, 3, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.toolButtonInversion = QtWidgets.QToolButton(self.frame_Process)
        ToolBtniconInversion = QtGui.QIcon()
        ToolBtniconInversion.addPixmap(QtGui.QPixmap("./UI_Ico/inversion.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonInversion.setIcon(ToolBtniconInversion)
        self.toolButtonInversion.setIconSize(QtCore.QSize(40, 40))
        self.toolButtonInversion.setAutoRaise(True)
        self.toolButtonInversion.setObjectName("toolButtonInversion")
        self.gridLayout.addWidget(self.toolButtonInversion, 3, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        # create vlayout
        self.verticalLayout.addWidget(self.frame_Process)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 20)
        self.dockWidgetTools.setWidget(self.dockWidgetContents)        
        
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea,self.dockWidgetTools)  
        
        
        ## Create dockWidgetsLogManagement
        self.dockWidgetLogManagement = QtWidgets.QDockWidget('Log Management',MainWindow)
        self.dockWidgetLogManagement.setEnabled(True)
        self.dockWidgetLogManagement.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetLogManagement.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.LeftDockWidgetArea)
        self.dockWidgetLogManagement.setObjectName("dockWidgetLogManagement")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_inner = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_inner.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_inner.setObjectName("gridLayout_inner")
        
        self.textBrowserLogManagement = QtWidgets.QTextBrowser(self.dockWidgetContents)
        self.textBrowserLogManagement.setObjectName("textBrowserLogManagement")
        timeLogManagementStart=QtCore.QDateTime.currentDateTime()
        timeDisplayLogManagementStart=timeLogManagementStart.toString('yyyy-MM-dd hh:mm:ss')
        self.textBrowserLogManagement.clear()
        self.textBrowserLogManagement.append('---------------------------------------------------')
        self.textBrowserLogManagement.append('%s:Software Start'%timeDisplayLogManagementStart)
        
        self.gridLayout_inner.addWidget(self.textBrowserLogManagement, 0, 0, 1, 1)
        
        self.gridLayout.addWidget(self.scrollAreaWidgetContents, 0, 0, 1, 1)
        self.dockWidgetLogManagement.setWidget(self.dockWidgetContents)  
        # MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetLogManagement)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea,self.dockWidgetLogManagement)  
        
        
        ## Create dockWidgetsDisplayFileInfo & dockWidgetsDisplayGraphInfo 
        # create dockWidgetsDisplayFileInfo
        self.dockWidgetDisplayFileInfo = QtWidgets.QDockWidget('Display File Info',MainWindow)
        self.dockWidgetDisplayFileInfo.setEnabled(True)
        self.dockWidgetDisplayFileInfo.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetDisplayFileInfo.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetDisplayFileInfo.setObjectName("dockWidgetDisplayFileInfo")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.treeView = QtWidgets.QTreeWidget(self.dockWidgetContents)
        self.treeView.setObjectName("treeView")
        # create treeView contents
        self.treeView.setColumnCount(2)
        self.treeView.setHeaderLabels(['Key','Value'])
        self.treeView.setIndentation(10)
        self.treeView.setColumnWidth(0,220)
        self.treeView.setColumnWidth(1,100)
        root_headfile=QtWidgets.QTreeWidgetItem(self.treeView)
        root_headfile.setText(0,'Head File Parameters')
        self.TreeViewOriginalFileName=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewOriginalFileName.setText(0,'Original File Name')
        self.TreeViewCreateFileTime=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewCreateFileTime.setText(0,'Create File Time')
        self.TreeViewEditFileTime=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewEditFileTime.setText(0,'Edit File Time')
        self.TreeViewNumberOfChannels=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewNumberOfChannels.setText(0,'Number of Channels')
        
        root_horizontalparameter=QtWidgets.QTreeWidgetItem(self.treeView)
        root_horizontalparameter.setText(0,'Horizontal Parameters')
        self.TreeViewScan_Seconds=QtWidgets.QTreeWidgetItem(root_horizontalparameter)
        self.TreeViewScan_Seconds.setText(0,'Scan/Seconds')
        self.TreeViewScan_Unit=QtWidgets.QTreeWidgetItem(root_horizontalparameter)
        self.TreeViewScan_Unit.setText(0,'Scan/Unit(m)')
        self.TreeViewUnit_Mark=QtWidgets.QTreeWidgetItem(root_horizontalparameter)
        self.TreeViewUnit_Mark.setText(0,'Unit/Mark(m)')
        
        root_verticalparameter=QtWidgets.QTreeWidgetItem(self.treeView)
        root_verticalparameter.setText(0,'Vertical Parameters')
        self.TreeViewSample_Scan=QtWidgets.QTreeWidgetItem(root_verticalparameter)
        self.TreeViewSample_Scan.setText(0,'Sample/Scan')
        self.TreeViewBit_Sample=QtWidgets.QTreeWidgetItem(root_verticalparameter)
        self.TreeViewBit_Sample.setText(0,'Bit/Sample')
        self.TreeViewDielectricConstant=QtWidgets.QTreeWidgetItem(root_verticalparameter)
        self.TreeViewDielectricConstant.setText(0,'Dielectric Constant')
        
        root_channelsinfomation=QtWidgets.QTreeWidgetItem(self.treeView)
        root_channelsinfomation.setText(0,'Channels Infomation')
        self.TreeViewChannel=QtWidgets.QTreeWidgetItem(root_channelsinfomation)
        self.TreeViewChannel.setText(0,'Channel')
        self.TreeViewAntennaStyle=QtWidgets.QTreeWidgetItem(root_channelsinfomation)
        self.TreeViewAntennaStyle.setText(0,'Antenna Style')
        self.TreeViewAntennaSerialNumber=QtWidgets.QTreeWidgetItem(root_channelsinfomation)
        self.TreeViewAntennaSerialNumber.setText(0,'Antenna Serial Number')
        self.TreeViewPostion=QtWidgets.QTreeWidgetItem(root_channelsinfomation)
        self.TreeViewPostion.setText(0,'Postion(ns)')
        self.TreeViewRange=QtWidgets.QTreeWidgetItem(root_channelsinfomation)
        self.TreeViewRange.setText(0,'Range(ns)')
        self.TreeViewTopSurface=QtWidgets.QTreeWidgetItem(root_channelsinfomation)
        self.TreeViewTopSurface.setText(0,'TopSurface(m)')
        self.TreeViewDepth=QtWidgets.QTreeWidgetItem(root_channelsinfomation)
        self.TreeViewDepth.setText(0,'Depth(m)')
        
        children_root_dataprocesshistory=QtWidgets.QTreeWidgetItem(root_channelsinfomation)
        children_root_dataprocesshistory.setText(0,'Data Process History')
        children_2level_root_IIRfilter=QtWidgets.QTreeWidgetItem(children_root_dataprocesshistory)
        children_2level_root_IIRfilter.setText(0,'IIR Filter')
        children_3level_root_vertical=QtWidgets.QTreeWidgetItem(children_2level_root_IIRfilter)
        children_3level_root_vertical.setText(0,'Vertical(MHz)')
        self.TreeViewLowpass=QtWidgets.QTreeWidgetItem(children_3level_root_vertical)
        self.TreeViewLowpass.setText(0,'High Pass')
        self.TreeViewHighpass=QtWidgets.QTreeWidgetItem(children_3level_root_vertical)
        self.TreeViewHighpass.setText(0,'High Pass')
        children_3level_root_horizontal=QtWidgets.QTreeWidgetItem(children_2level_root_IIRfilter)
        children_3level_root_horizontal.setText(0,'Horizontal(Number of Scan)')
        children_2level_root_positioncorrection=QtWidgets.QTreeWidgetItem(children_root_dataprocesshistory)
        children_2level_root_positioncorrection.setText(0,'Position Correction')
        self.TreeViewMigration=QtWidgets.QTreeWidgetItem(children_3level_root_vertical)
        self.TreeViewMigration.setText(0,'Migration(nS)')
        children_2level_root_editdatablock=QtWidgets.QTreeWidgetItem(children_root_dataprocesshistory)
        children_2level_root_editdatablock.setText(0,'Edit Data Block')
        self.treeView.addTopLevelItem(root_headfile)
        self.treeView.addTopLevelItem(root_channelsinfomation)
        self.treeView.expandAll()
        
        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)
        self.dockWidgetDisplayFileInfo.setWidget(self.dockWidgetContents)  
        # MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetLogManagement)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea,self.dockWidgetDisplayFileInfo)

        # create dockWidgetsDisplayGraphInfo 
        self.dockWidgetDisplayGraphInfo = QtWidgets.QDockWidget('Display Scan Line',MainWindow)
        # self.dockWidgetDisplayGraphInfo.setEnabled(True)
        self.dockWidgetDisplayGraphInfo.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetDisplayGraphInfo.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetDisplayGraphInfo.setObjectName("dockWidgetDisplayGraphInfo")
        self.dockWidgetDisplayGraphInfo.setEnabled(False)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        # self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setObjectName("scrollArea")
        # Log File
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_inner = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_inner.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_inner.setObjectName("gridLayout_inner")
       
        # self.graphicsViewScanLine = QtWidgets.QWidget(self.dockWidgetContents)
        self.graphicsViewScanLine = QtWidgets.QMdiArea(self.centralwidget)
        self.graphicsViewScanLine.tileSubWindows()
        self.graphicsViewScanLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsViewScanLine.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsViewScanLine.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsViewScanLine.setTabsClosable(True)
        self.graphicsViewScanLine.setDocumentMode(True)
        self.graphicsViewScanLine.setTabsMovable(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsViewScanLine.sizePolicy().hasHeightForWidth())
        self.graphicsViewScanLine.setSizePolicy(sizePolicy)
        
        subWindow=QtWidgets.QMdiSubWindow()
        InitFigureCanvas=ScanPlotCanvas(self,MainWindow,width=5,height=200,dpi=200)
        subWindow.setWidget(InitFigureCanvas)
        # self.graphicsViewScanLine.addSubWindow(ScanMdiChild())
        self.graphicsViewScanLine.addSubWindow(subWindow)
        subWindow.show()
        
        # print(self.graphicsViewScanLine)
        # print(self.graphicsViewScanLine.subWindowList())
        
        self.graphicsViewScanLine.setObjectName("graphicsViewScanLine")
        self.gridLayout_inner.addWidget(self.graphicsViewScanLine, 0, 0, 2, 2)
        
        self.gridLayout.addWidget(self.scrollAreaWidgetContents, 0, 0, 1, 1)
        self.dockWidgetDisplayGraphInfo.setWidget(self.dockWidgetContents)  
        # MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetLogManagement)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea,self.dockWidgetDisplayGraphInfo)
        # set tab
        self.tabifyDockWidget(self.dockWidgetDisplayFileInfo, self.dockWidgetDisplayGraphInfo) 
        self.dockWidgetDisplayFileInfo.raise_()
        self.setTabPosition(QtCore.Qt.TopDockWidgetArea, QtWidgets.QTabWidget.North)
        self.setTabPosition(QtCore.Qt.BottomDockWidgetArea, QtWidgets.QTabWidget.North)
        self.setTabPosition(QtCore.Qt.LeftDockWidgetArea, QtWidgets.QTabWidget.North)
        self.setTabPosition(QtCore.Qt.RightDockWidgetArea, QtWidgets.QTabWidget.North)
        # setCentralWidget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.TabbedView)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setDocumentMode(True)
        self.mdiArea.setTabsMovable(True)
        self.mdiArea.setTabPosition(QtWidgets.QTabWidget.North)
        self.mdichildlist=[]
        self.windowMapper=QtCore.QSignalMapper(self)
        self.windowMapper.mapped[QtWidgets.QWidget].connect(self.setActiveSubWindow)
        self.mdiArea.subWindowActivated.connect(self.updataHeaders)
        self.mdiArea.subWindowActivated.connect(lambda: self.updataToolButton(MainWindow))
        self.updataToolButton(MainWindow)
        self.updataRecentFile()
        self.updataHeaders()
        self.menuRecent_File.aboutToShow.connect(self.updataRecentFile)
        
        self.gridLayout.addWidget(self.mdiArea, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CSU_GPR"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuView.setTitle(_translate("MainWindow", " &View"))
        self.menuData_Process.setTitle(_translate("MainWindow", "&Data Process"))
        self.menuModelling.setTitle(_translate("MainWindow", "&Modelling"))
        self.menuInversion_2D.setTitle(_translate("MainWindow", "&Inversion 2D"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        # MENU--->File
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open ..."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.menuRecent_File.setTitle(_translate("MainWindow", "Recent File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionCloseAll.setText(_translate("MainWindow", "Close All"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as ..."))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionPrint_Preview.setText(_translate("MainWindow", "Print Preview"))
        self.actionPrint_Preview.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.actionPrint.setText(_translate("MainWindow", "Print..."))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionPrint_Setting.setText(_translate("MainWindow", "Print Setting"))
        self.actionExit_CSU_GPR.setText(_translate("MainWindow", "Exit CSU_GPR"))
        self.actionExit_CSU_GPR.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        # MENU--->View
        self.menuDisplay_Mode.setTitle(_translate("MainWindow", "Display Mode"))
        self.actionWiggle.setText(_translate("MainWindow", "Wiggle"))
        self.actionPseudo_Color.setText(_translate("MainWindow", "Pseudo Color"))
        self.actionScan_Line.setText(_translate("MainWindow", "Scan Line"))
        self.menuColor_Map.setTitle(_translate("MainWindow", "Color Map"))
        self.actionAccent.setText(_translate("MainWindow", "Accent"))
        self.actionBlues.setText(_translate("MainWindow", "Blues"))
        self.actionBrBG.setText(_translate("MainWindow", "BrBG"))
        self.actionBuGn.setText(_translate("MainWindow", "BuGn"))
        self.actionBuPu.setText(_translate("MainWindow", "BuPu"))
        self.actionCMRmap.setText(_translate("MainWindow", "CMRmap"))
        self.actionDark2.setText(_translate("MainWindow", "Dark2"))
        self.actionGnBu.setText(_translate("MainWindow", "GnBu"))
        self.actionGreens.setText(_translate("MainWindow", "Greens"))
        self.actionGreys.setText(_translate("MainWindow", "Greys"))
        self.actionOrRd.setText(_translate("MainWindow", "OrRd"))
        self.actionOranges.setText(_translate("MainWindow", "Oranges"))
        self.actionPRGn.setText(_translate("MainWindow", "PRGn"))
        self.actionPaired.setText(_translate("MainWindow", "Paired"))
        self.actionPastel1.setText(_translate("MainWindow", "Pastel1"))
        self.actionPastel2.setText(_translate("MainWindow", "Pastel2"))
        self.actionPiYG.setText(_translate("MainWindow", "PiYG"))
        self.actionPuBu.setText(_translate("MainWindow", "PuBu"))
        self.actionPuBuGn.setText(_translate("MainWindow", "PuBuGn"))
        self.actionPuOr.setText(_translate("MainWindow", "PuOr"))
        self.actionPuRd.setText(_translate("MainWindow", "PuRd"))
        self.actionPurples.setText(_translate("MainWindow", "Purples"))
        self.actionRdBu.setText(_translate("MainWindow", "RdBu"))
        self.actionRdGy.setText(_translate("MainWindow", "RdGy"))
        self.actionRdPu.setText(_translate("MainWindow", "RdPu"))
        self.actionRdYlBu.setText(_translate("MainWindow", "RdYlBu"))
        self.actionRdYlGn.setText(_translate("MainWindow", "RdYlGn"))
        self.actionReds.setText(_translate("MainWindow", "Reds"))
        self.actionSet1.setText(_translate("MainWindow", "Set1"))
        self.actionSet2.setText(_translate("MainWindow", "Set2"))
        self.actionSet3.setText(_translate("MainWindow", "Set3"))
        self.actionSpectral.setText(_translate("MainWindow", "Spectral"))
        self.actionVega10.setText(_translate("MainWindow", "Vega10"))
        self.actionVega20.setText(_translate("MainWindow", "Vega20"))
        self.actionVega20b.setText(_translate("MainWindow", "Vega20b"))
        self.actionVega20c.setText(_translate("MainWindow", "Vega20c"))
        self.actionWistia.setText(_translate("MainWindow", "Wistia"))
        self.actionYlGn.setText(_translate("MainWindow", "YlGn"))
        self.actionYlGnBu.setText(_translate("MainWindow", "YlGnBu"))
        self.actionYlOrBr.setText(_translate("MainWindow", "YlOrBr"))
        self.actionYlOrRd.setText(_translate("MainWindow", "YlOrRd"))
        self.actionafmhot.setText(_translate("MainWindow", "afmhot"))
        self.actionautumn.setText(_translate("MainWindow", "autumn"))
        self.actionbinary.setText(_translate("MainWindow", "binary"))
        self.actionbone.setText(_translate("MainWindow", "bone"))
        self.actionbrg.setText(_translate("MainWindow", "brg"))
        self.actionbwr.setText(_translate("MainWindow", "bwr"))
        self.actioncool.setText(_translate("MainWindow", "cool"))
        self.actioncoolwarm.setText(_translate("MainWindow", "coolwarm"))
        self.actioncopper.setText(_translate("MainWindow", "copper"))
        self.actioncubehelix.setText(_translate("MainWindow", "cubehelix"))
        self.actionflag.setText(_translate("MainWindow", "flag"))
        self.actiongist_earth.setText(_translate("MainWindow", "gist_earth"))
        self.actiongist_gray.setText(_translate("MainWindow", "gist_gray"))
        self.actiongist_heat.setText(_translate("MainWindow", "gist_heat"))
        self.actiongist_ncar.setText(_translate("MainWindow", "gist_ncar"))
        self.actiongist_rainbow.setText(_translate("MainWindow", "gist_rainbow"))
        self.actiongist_stern.setText(_translate("MainWindow", "gist_stern"))
        self.actiongist_yarg.setText(_translate("MainWindow", "gist_yarg"))
        self.actiongnuplot.setText(_translate("MainWindow", "gnuplot"))
        self.actiongnuplot2.setText(_translate("MainWindow", "gnuplot2"))
        self.actiongray.setText(_translate("MainWindow", "gray"))
        self.actionhot.setText(_translate("MainWindow", "hot"))
        self.actionhsv.setText(_translate("MainWindow", "hsv"))
        self.actioninferno.setText(_translate("MainWindow", "inferno"))
        self.actionjet.setText(_translate("MainWindow", "jet"))
        self.actionmagma.setText(_translate("MainWindow", "magma"))
        self.actionnipy_spectral.setText(_translate("MainWindow", "nipy_spectral"))
        self.actionocean.setText(_translate("MainWindow", "ocean"))
        self.actionpink.setText(_translate("MainWindow", "pink"))
        self.actionplasma.setText(_translate("MainWindow", "plasma"))
        self.actionprism.setText(_translate("MainWindow", "prism"))
        self.actionrainbow.setText(_translate("MainWindow", "rainbow"))
        self.actionseismic.setText(_translate("MainWindow", "seismic"))
        self.actionspectral.setText(_translate("MainWindow", "spectral"))
        self.actionspring.setText(_translate("MainWindow", "spring"))
        self.actionsummer.setText(_translate("MainWindow", "summer"))
        self.actiontab10.setText(_translate("MainWindow", "tab10"))
        self.actiontab20.setText(_translate("MainWindow", "tab20"))
        self.actiontab20b.setText(_translate("MainWindow", "tab20b"))
        self.actiontab20c.setText(_translate("MainWindow", "tab20c"))
        self.actionterrain.setText(_translate("MainWindow", "terrain"))
        self.actionviridis.setText(_translate("MainWindow", "viridis"))
        self.actionwinter.setText(_translate("MainWindow", "winter"))
        self.menuDisplay_Gain.setTitle(_translate("MainWindow", "Display Gain"))
        self.actionZoomOutDisplayGain10.setText(_translate("MainWindow", "0.1"))
        self.actionZoomOutDisplayGain5.setText(_translate("MainWindow", "0.2"))
        self.actionZoomOutDisplayGain2.setText(_translate("MainWindow", "0.5"))
        self.actionNormalDisplayGain.setText(_translate("MainWindow", "1"))
        self.actionZoomDisplayGain2.setText(_translate("MainWindow", "2"))
        self.actionZoomDisplayGain5.setText(_translate("MainWindow", "5"))
        self.actionZoomDisplayGain10.setText(_translate("MainWindow", "10"))
        self.actionZoomDisplayGain20.setText(_translate("MainWindow", "20"))
        self.menuScale_Out.setTitle(_translate("MainWindow", "Scale Out"))
        self.actionZoomOutScaleOut10.setText(_translate("MainWindow", "0.1"))
        self.actionZoomOutScaleOut5.setText(_translate("MainWindow", "0.2"))
        self.actionZoomOutScaleOut2.setText(_translate("MainWindow", "0.5"))
        self.actionNormalScaleOut.setText(_translate("MainWindow", "1"))
        self.actionZoomScaleOut2.setText(_translate("MainWindow", "2"))
        self.actionZoomScaleOut5.setText(_translate("MainWindow", "5"))
        self.actionZoomScaleOut10.setText(_translate("MainWindow", "10"))
        self.actionZoomScaleOut20.setText(_translate("MainWindow", "20"))
        self.actionZoomScaleOut30.setText(_translate("MainWindow", "30"))
        self.menuVertical_Operation.setTitle(_translate("MainWindow", "Vertical Operation"))
        self.actionVerticalOperationSample.setText(_translate("MainWindow", "Sample"))
        self.actionVerticalOperationTime.setText(_translate("MainWindow", "Time"))
        self.actionVerticalOperationDepth.setText(_translate("MainWindow", "Depth"))
        
        self.ToolActionOpenFile.setText(_translate("MainWindow", "OpenFile"))
        self.ToolActionOpenFile.setToolTip(_translate("MainWindow", "<html><head/><body><p>Open File</p></body></html>"))
        self.ToolActionNewFile.setText(_translate("MainWindow", "NewFile"))
        self.ToolActionNewFile.setToolTip(_translate("MainWindow", "<html><head/><body><p>New File</p></body></html>"))
        self.ToolActionSave.setText(_translate("MainWindow", "Save"))
        self.ToolActionSave.setToolTip(_translate("MainWindow", "<html><head/><body><p>Save</p></body></html>"))
        self.ToolActionSaveAs.setText(_translate("MainWindow", "Save as"))
        self.ToolActionSaveAs.setToolTip(_translate("MainWindow", "<html><head/><body><p>Save as </p></body></html>"))
        self.ToolActionPrintPreview.setText(_translate("MainWindow", "Print Preview"))
        self.ToolActionPrintPreview.setToolTip(_translate("MainWindow", "<html><head/><body><p>Print Preview</p></body></html>"))
        self.ToolActionPrint.setText(_translate("MainWindow", "Print"))
        self.ToolActionPrint.setToolTip(_translate("MainWindow", "<html><head/><body><p>Print</p></body></html>"))
        self.ToolActionHelp.setText(_translate("MainWindow", "Help"))
        self.ToolActionHelp.setToolTip(_translate("MainWindow", "<html><head/><body><p>Help</p></body></html>"))
        self.actionHelp_Files.setText(_translate("MainWindow", "Help Files..."))
        self.actionContants.setText(_translate("MainWindow", "Contants"))
        self.ToolContants.setText(_translate("MainWindow", "Contants"))
        self.ToolContants.setToolTip(_translate("MainWindow", "<html><head/><body><p>Contants</p></body></html>"))
        self.ToolActionModelling.setText(_translate("MainWindow", "Forward"))
        self.ToolActionModelling.setToolTip(_translate("MainWindow", "<html><head/><body><p>Forward</p></body></html>"))
        #set frame name
        self.label_frame_View.setText(_translate('MainWindow','View Display Tools'))
        self.label_frame_Process.setText(_translate('MainWindow','Process Tools'))
        #set toolButton name
        self.toolButtonWigb.setText(_translate('MainWindow','Wiggle Style'))
        self.toolButtonPcolor.setText(_translate('MainWindow','Pseudo Color'))
        self.toolButtonScanLine.setText(_translate('MainWindow','Scan Line'))
        self.toolButtonColorMap.setText(_translate('MainWindow','Color Map'))
        self.toolButtonDisplayGain.setText(_translate('MainWindow','Display Gain'))
        self.toolButtonScaleOut.setText(_translate('MainWindow','Scale Out'))
        self.toolButtonModifiedHeadFile.setText(_translate('MainWindow','Modified Head File'))
        self.toolButtonAreaGain.setText(_translate('MainWindow','Area Gain'))
        self.toolButtonDeleteTrack.setText(_translate('MainWindow','Delete Track'))
        self.toolButtonExtractTrack.setText(_translate('MainWindow','Extract Track'))
        self.toolButtonZeroDrift.setText(_translate('MainWindow','Zero Drift'))
        self.toolButtonFilter.setText(_translate('MainWindow','Filter Process'))
        self.toolButtonMigrate.setText(_translate('MainWindow','Migrate'))
        self.toolButtonInversion.setText(_translate('MainWindow','Inversion'))
        #set toolButton tool tip
        self.toolButtonWigb.setToolTip(_translate('MainWindow','Wiggle Style'))
        self.toolButtonPcolor.setToolTip(_translate('MainWindow','Pseudo Color'))
        self.toolButtonScanLine.setToolTip(_translate('MainWindow','Scan Line'))
        self.toolButtonColorMap.setToolTip(_translate('MainWindow','Color Map'))
        self.toolButtonDisplayGain.setToolTip(_translate('MainWindow','Display Gain'))
        self.toolButtonScaleOut.setToolTip(_translate('MainWindow','Scale Out'))
        self.toolButtonModifiedHeadFile.setToolTip(_translate('MainWindow','Modified Head File'))
        self.toolButtonAreaGain.setToolTip(_translate('MainWindow','Area Gain'))
        self.toolButtonDeleteTrack.setToolTip(_translate('MainWindow','Delete Track'))
        self.toolButtonExtractTrack.setToolTip(_translate('MainWindow','Extract Track'))
        self.toolButtonZeroDrift.setToolTip(_translate('MainWindow','Zero Drift'))
        self.toolButtonFilter.setToolTip(_translate('MainWindow','Filter Process'))
        self.toolButtonMigrate.setToolTip(_translate('MainWindow','Migrate'))
        self.toolButtonInversion.setToolTip(_translate('MainWindow','Inversion'))
        #set toolButton statues tip
        self.toolButtonWigb.setStatusTip(_translate('MainWindow','Wiggle Style'))
        self.toolButtonPcolor.setStatusTip(_translate('MainWindow','Pseudo Color'))
        self.toolButtonScanLine.setStatusTip(_translate('MainWindow','Scan Line'))
        self.toolButtonColorMap.setStatusTip(_translate('MainWindow','Color Map'))
        self.toolButtonDisplayGain.setStatusTip(_translate('MainWindow','Display Gain'))
        self.toolButtonScaleOut.setStatusTip(_translate('MainWindow','Scale Out'))
        self.toolButtonModifiedHeadFile.setStatusTip(_translate('MainWindow','Modified Head File'))
        self.toolButtonAreaGain.setStatusTip(_translate('MainWindow','Area Gain'))
        self.toolButtonDeleteTrack.setStatusTip(_translate('MainWindow','Delete Track'))
        self.toolButtonExtractTrack.setStatusTip(_translate('MainWindow','Extract Track'))
        self.toolButtonZeroDrift.setStatusTip(_translate('MainWindow','Zero Drift'))
        self.toolButtonFilter.setStatusTip(_translate('MainWindow','Filter Process'))
        self.toolButtonMigrate.setStatusTip(_translate('MainWindow','Migrate'))
        self.toolButtonInversion.setStatusTip(_translate('MainWindow','Inversion'))
        
    def OpenHelpFile(self):
        timeLogManagement=QtCore.QDateTime.currentDateTime()
        timeDisplayLogManagement=timeLogManagement.toString('yyyy-MM-dd hh:mm:ss')
        self.textBrowserLogManagement.append('---------------------------------------------------')
        self.textBrowserLogManagement.append('%s:User Open Help Files'%timeDisplayLogManagement)
        os.popen('evince ./SourceFile/Help.pdf')
        # os.filestar(r'.\\SourceFile\\Help.pdf')
        
    def OpenContants(self,MainWindow):
        timeLogManagement=QtCore.QDateTime.currentDateTime()
        timeDisplayLogManagement=timeLogManagement.toString('yyyy-MM-dd hh:mm:ss')
        self.textBrowserLogManagement.append('---------------------------------------------------')
        self.textBrowserLogManagement.append('%s:User Open Contants'%timeDisplayLogManagement)
        MsgBox=QtWidgets.QMessageBox(MainWindow)  
        MsgBox.setWindowTitle("Contant")  
        MsgBox.setIconPixmap(QtGui.QPixmap('./SourceFile/contants.png'))
        MsgBox.addButton('Ok',QtWidgets.QMessageBox.ActionRole)
        MsgBox.exec_()  
        
    def NewFile(self,MainWindow):
        self.menuRecent_File.setEnabled(True)
        self.mdichildlist.append(MdiChild(MainWindow))
        self.mdiArea.addSubWindow(self.mdichildlist[-1])
        self.mdichildlist[-1].show()
        self.mdichildlist[-1].NewFile()
        MainWindow.actionClose.setEnabled(True)
        MainWindow.actionCloseAll.setEnabled(True)
        self.updateHeadersWithoutData(self.mdichildlist[-1].headers)
        MainWindow.dockWidgetTools.setEnabled(False)
        MainWindow.toolButtonScanLine.setChecked(False)
        MainWindow.actionScan_Line.setEnabled(False)
        
    def CloseFile(self,MainWindow):
        self.mdiArea.closeActiveSubWindow()
        
    def CloseAllFile(self,MainWindow):
        self.mdiArea.closeAllSubWindows()
    
    def OpenFile(self,MainWindow):
        FullFilePath,_=QtWidgets.QFileDialog.getOpenFileName(self,'Select File','./','GPR file (*.dzt)') 
        if FullFilePath:
            if not(FullFilePath in MainWindow.FileList):
                self.menuRecent_File.setEnabled(True)
                self.mdichildlist.append(MdiChild(MainWindow))
                self.mdiArea.addSubWindow(self.mdichildlist[-1])
                self.mdichildlist[-1].show()
                # self.mdichildlist[-1].OpenFile(FullFilePath)
                MainWindow.FileList.append(FullFilePath)
                MainWindow.actionSave.setEnabled(True)
                MainWindow.actionSave_as.setEnabled(True)
                MainWindow.actionPrint_Preview.setEnabled(True)
                MainWindow.actionPrint.setEnabled(True)
                MainWindow.actionClose.setEnabled(True)
                MainWindow.actionCloseAll.setEnabled(True)
                MainWindow.menuView.setEnabled(True)
                MainWindow.menuData_Process.setEnabled(True)
                MainWindow.menuInversion_2D.setEnabled(True)
                MainWindow.ToolActionSave.setEnabled(True)
                MainWindow.ToolActionSaveAs.setEnabled(True)
                MainWindow.ToolActionPrint.setEnabled(True)
                MainWindow.ToolActionPrintPreview.setEnabled(True)
                MainWindow.dockWidgetTools.setEnabled(True)
            
                with open(FullFilePath,'rb') as fileobject:
                    headers,data_array=DZTFileRead.DZT_read(fileobject)
                    headers['FullFilePath']=FullFilePath
                    self.updateHeadersWithData(headers)
                    self.mdichildlist[-1].OpenFile(FullFilePath,headers,data_array)
                    activeSubWindow=self.mdiArea.activeSubWindow()
                
                    self.RecentFigureCanvas=PlotCanvas(self,MainWindow,data=data_array,width=15, height=6)
                    activeSubWindow.widget().setWidget(self.RecentFigureCanvas)
                    activeSubWindow.widget().widget().PlotAsWiggle()
                    self.toolButtonWigb.setChecked(True)
                    self.toolButtonPcolor.setChecked(False)
                    self.toolButtonColorMap.setEnabled(False)
                    self.menuColor_Map.setEnabled(False)
                    self.toolButtonScanLine.setChecked(False)
                    self.UserAspect=8
                    self.UserCmap='cm.viridis'
    
    def ChangeCmap(self,cmap):
        activeSubWindow=self.mdiArea.activeSubWindow()
        activeSubWindow.widget().widget().ChangeCmap('cm.'+cmap)
        self.UserCmap='cm.'+cmap
    
    def ChangeAspect(self,aspect):
        activeSubWindow=self.mdiArea.activeSubWindow()
        aspect=float(aspect)
        activeSubWindow.widget().widget().ChangeAspect(aspect)
        self.UserAspect=aspect
        
    def ChangeGain(self,gain):
        activeSubWindow=self.mdiArea.activeSubWindow()
        gain=float(gain)
        
        if activeSubWindow.widget().tag=='wiggle':
            activeSubWindow.widget().widget().PlotAsWiggle(gain=gain)
            activeSubWindow.widget().widget().ChangeAspect(self.UserAspect)
        else:
            activeSubWindow.widget().widget().PlotAsPColor(gain=gain)
            activeSubWindow.widget().widget().ChangeAspect(self.UserAspect)
            activeSubWindow.widget().widget().ChangeCmap(self.UserCmap)
    
    def ChangeVertical(self,dtype):
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            try:
                child=window.widget()
                if child is self.mdiArea.activeSubWindow().widget():
                    
                    headers=child.headers
                    if dtype == 'Sample':
                        ylim=headers['rh_nsamp']
                        ytick=np.linspace(0,ylim,6)
                        child.widget().ChangeVertical(ylim,ytick,dtype)
                    elif dtype == 'Time':
                        dtype+=' (ns)'
                        ylim=headers['rh_nsamp']
                        ytick_=float(headers['rh_range'])
                        ytick=['%2.2f'%i for i in np.linspace(0,ytick_,6)]
                        child.widget().ChangeVertical(ylim,ytick,dtype)
                    elif dtype == 'Depth':
                        dtype+=' (m)'
                        ylim=headers['rh_nsamp']
                        ytick_=float(headers['rh_depth'])
                        ytick=['%2.2f'%i for i in np.linspace(0,ytick_,6)]
                        child.widget().ChangeVertical(ylim,ytick,dtype)
            except:
                pass
    
    
    def ActionScanLine(self):
        if self.toolButtonScanLine.isChecked():
            self.toolButtonScanLine.setChecked(False)
        else:
            self.toolButtonScanLine.setChecked(True)
    
    def SwitchingStateWigb(self):
        if self.toolButtonWigb.isChecked():
            # use wiggle
            activeSubWindow=self.mdiArea.activeSubWindow()
            activeSubWindow.widget().widget().PlotAsWiggle()
            self.toolButtonColorMap.setEnabled(False)
            self.menuColor_Map.setEnabled(False)
            self.toolButtonPcolor.setChecked(False)
            self.toolButtonWigb.setChecked(True)
            activeSubWindow.widget().tag='wiggle'
            self.UserAspect=8
        if not self.toolButtonWigb.isChecked():
            # use pcolor
            activeSubWindow=self.mdiArea.activeSubWindow()
            activeSubWindow.widget().widget().PlotAsPColor()
            self.toolButtonColorMap.setEnabled(True)
            self.menuColor_Map.setEnabled(True)
            self.toolButtonWigb.setChecked(False)
            self.toolButtonPcolor.setChecked(True)
            activeSubWindow.widget().tag='pcolor'
            self.UserAspect=1
            self.UserCmap='cm.viridis'
            
    def SwitchingStatePColor(self):
        if self.toolButtonPcolor.isChecked():
            # use pcolor
            activeSubWindow=self.mdiArea.activeSubWindow()
            activeSubWindow.widget().widget().PlotAsPColor()
            self.toolButtonColorMap.setEnabled(True)
            self.menuColor_Map.setEnabled(True)
            self.toolButtonPcolor.setChecked(True)
            self.toolButtonWigb.setChecked(False)
            activeSubWindow.widget().tag='pcolor'
            self.UserAspect=1
            self.UserCmap='cm.viridis'
        if not self.toolButtonPcolor.isChecked():
            # use wiggle
            activeSubWindow=self.mdiArea.activeSubWindow()
            activeSubWindow.widget().widget().PlotAsWiggle()
            self.toolButtonColorMap.setEnabled(False)
            self.menuColor_Map.setEnabled(False)
            self.toolButtonPcolor.setChecked(False)
            self.toolButtonWigb.setChecked(True)
            activeSubWindow.widget().tag='wiggle'
            self.UserAspect=8
            
    def ActionSwitchingStateWigb(self):
        self.toolButtonWigb.setChecked(True)
        # use wiggle
        activeSubWindow=self.mdiArea.activeSubWindow()
        activeSubWindow.widget().widget().PlotAsWiggle()
        self.toolButtonColorMap.setEnabled(False)
        self.menuColor_Map.setEnabled(False)
        self.toolButtonPcolor.setChecked(False)
        self.toolButtonWigb.setChecked(True)
        activeSubWindow.widget().tag='wiggle'
        self.toolButtonPcolor.setChecked(False)
        self.UserAspect=8
        
    def ActionSwitchingStatePColor(self):
        self.toolButtonPcolor.setChecked(True)
        # use pcolor
        activeSubWindow=self.mdiArea.activeSubWindow()
        activeSubWindow.widget().widget().PlotAsPColor()
        self.toolButtonColorMap.setEnabled(True)
        self.menuColor_Map.setEnabled(True)
        self.toolButtonPcolor.setChecked(True)
        self.toolButtonWigb.setChecked(False)
        activeSubWindow.widget().tag='pcolor'
        self.toolButtonWigb.setChecked(False)    
        self.UserAspect=1
        self.UserCmap='cm.viridis'
           
    def updateHeadersWithData(self,headers):
        pattern=re.compile(r'[^\//:*?"<>|\r\n]+$')
        FileName=pattern.findall(headers['FullFilePath'])[0]
        self.TreeViewOriginalFileName.setText(1,FileName)
        self.TreeViewCreateFileTime.setText(1,str(headers['rh_create']))
        self.TreeViewEditFileTime.setText(1,headers['rh_modif'])
        self.TreeViewNumberOfChannels.setText(1,str(headers['rh_nchan']))
        self.TreeViewScan_Seconds.setText(1,str(headers['rh_sps']))
        self.TreeViewScan_Unit.setText(1,str(headers['rh_spm']))
        self.TreeViewUnit_Mark.setText(1,str(headers['rh_mpm']))
        self.TreeViewSample_Scan.setText(1,str(headers['rh_nsamp']))
        self.TreeViewBit_Sample.setText(1,str(headers['rh_bits']))
        self.TreeViewDielectricConstant.setText(1,str(headers['rh_epsr']))
        self.TreeViewChannel.setText(1,str(headers['rh_chanmask']))
        self.TreeViewAntennaStyle.setText(1,headers['rh_antname'])
        self.TreeViewAntennaSerialNumber.setText(1,'-')
        self.TreeViewPostion.setText(1,str(headers['rh_position']))
        self.TreeViewRange.setText(1,str(headers['rh_range']))
        self.TreeViewTopSurface.setText(1,str(headers['rh_top']))
        self.TreeViewDepth.setText(1,str(headers['rh_depth']))
        self.TreeViewLowpass.setText(1,'-')
        self.TreeViewHighpass.setText(1,'-')
        self.TreeViewMigration.setText(1,'-')
        
    def updateHeadersWithoutData(self,headers):
        self.TreeViewOriginalFileName.setText(1,headers['FullFilePath'])
        self.TreeViewCreateFileTime.setText(1,str(headers['rh_create']))
        self.TreeViewEditFileTime.setText(1,headers['rh_modif'])
        self.TreeViewNumberOfChannels.setText(1,str(headers['rh_nchan']))
        self.TreeViewScan_Seconds.setText(1,str(headers['rh_sps']))
        self.TreeViewScan_Unit.setText(1,str(headers['rh_spm']))
        self.TreeViewUnit_Mark.setText(1,str(headers['rh_mpm']))
        self.TreeViewSample_Scan.setText(1,str(headers['rh_nsamp']))
        self.TreeViewBit_Sample.setText(1,str(headers['rh_bits']))
        self.TreeViewDielectricConstant.setText(1,str(headers['rh_epsr']))
        self.TreeViewChannel.setText(1,str(headers['rh_chanmask']))
        self.TreeViewAntennaStyle.setText(1,headers['rh_antname'])
        self.TreeViewAntennaSerialNumber.setText(1,'-')
        self.TreeViewPostion.setText(1,str(headers['rh_position']))
        self.TreeViewRange.setText(1,str(headers['rh_range']))
        self.TreeViewTopSurface.setText(1,str(headers['rh_top']))
        self.TreeViewDepth.setText(1,str(headers['rh_depth']))
        self.TreeViewLowpass.setText(1,'-')
        self.TreeViewHighpass.setText(1,'-')
        self.TreeViewMigration.setText(1,'-')
        
    def setActiveSubWindow(self, window):
        self.mdiArea.setActiveSubWindow(window)
    
    def updataToolButton(self,MainWindow):
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            try:
                child=window.widget()
                if child is self.mdiArea.activeSubWindow().widget():
                    headers=child.headers
                    if headers['FileType'] is 'New':
                        MainWindow.dockWidgetTools.setEnabled(False)
                    else:
                        MainWindow.dockWidgetTools.setEnabled(True)
                    if child.tag=='wiggle':
                        self.toolButtonWigb.setChecked(True)
                        self.toolButtonPcolor.setChecked(False)
                        self.toolButtonColorMap.setEnabled(False)
                        self.menuColor_Map.setEnabled(False)
                    else:
                        self.toolButtonWigb.setChecked(False)
                        self.toolButtonPcolor.setChecked(True)
                        self.toolButtonColorMap.setEnabled(True)
                        self.menuColor_Map.setEnabled(True)
            except:
                pass
    
    def updataHeaders(self):
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            try:
                child=window.widget()
                if child is self.mdiArea.activeSubWindow().widget():
                    
                    headers=child.headers
                    if headers['FileType'] is 'New':
                        self.updateHeadersWithoutData(headers)
                    else:
                        self.updateHeadersWithData(headers)
            except:
                pass
        
    # def activeMdiChild(self):
    #     activeSubWindow = self.mdiArea.activeSubWindow()
    #     if activeSubWindow:
    #         print(activeSubWindow.widget())
    #         return activeSubWindow.widget()
    #     return None
    
    def whenCloseAll(self):
        self.menuRecent_File.setEnabled(False)
        
    def updataRecentFile(self):
        self.menuRecent_File.clear()        
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            child=window.widget()
            text="%d %s"%(i+1,child.filename[:-3])
            if i<9:
                text='&'+text
            action=self.menuRecent_File.addAction(text)
            action.setCheckable(True)
            action.setChecked(child is self.mdiArea.activeSubWindow().widget())
            action.triggered.connect(self.windowMapper.map)
            self.windowMapper.setMapping(action, window)

    def ExitClose(self):
        self.close()
    
    def GetUiModelling(self,MainWindow):
        ModellingMainWindow=MainWindow_Modelling.MainForm()
        ModellingMainWindow.showMaximized()
        ModellingMainWindow.show()
        
        ModellingMainWindow.EndModellingSignal.connect(lambda: self.GetProfileData(ModellingMainWindow,MainWindow))
        
    def GetProfileData(self,ModellingMainWindow,MainWindow):
        self.UiGetProfileData=ModellingMainWindow.data
        self.OpenGetProfileData(MainWindow)
        
    def OpenGetProfileData(self,MainWindow):
        self.menuRecent_File.setEnabled(True)
        self.mdichildlist.append(MdiChild(MainWindow))
        self.mdiArea.addSubWindow(self.mdichildlist[-1])
        self.mdichildlist[-1].show()
        MainWindow.FileList.append('UserCreate')
        MainWindow.actionSave.setEnabled(True)
        MainWindow.actionSave_as.setEnabled(True)
        MainWindow.actionPrint_Preview.setEnabled(True)
        MainWindow.actionPrint.setEnabled(True)
        MainWindow.actionClose.setEnabled(True)
        MainWindow.actionCloseAll.setEnabled(True)
        MainWindow.menuView.setEnabled(True)
        MainWindow.menuData_Process.setEnabled(True)
        MainWindow.menuInversion_2D.setEnabled(True)
        MainWindow.ToolActionSave.setEnabled(True)
        MainWindow.ToolActionSaveAs.setEnabled(True)
        MainWindow.ToolActionPrint.setEnabled(True)
        MainWindow.ToolActionPrintPreview.setEnabled(True)
        MainWindow.dockWidgetTools.setEnabled(True)
        headers={"FileType":'UserCreate',
                 "FullFilePath":'UserCreate',
                 "rh_tag": '',
                 "rh_tag_bits": '',
                 "rh_tag_bytes": '',
                 "rh_data": '',
                 "rh_nsamp": '',
                 "rh_nsamp": '',
                 "rh_bits": '',
                 "rh_zero": '',
                 "rh_sps": '',
                 "rh_spm": '',
                 "rh_mpm": '',
                 "rh_position": '',
                 "rh_range": '',
                 "rh_npass": '',
                 "rh_create": '',
                 "rh_modif": '',
                 "rh_rgain": '',
                 "rh_nrgain": '',
                 "rh_text": '',
                 "rh_ntext": '',
                 "rh_proc": '',
                 "rh_nproc": '',
                 "rh_nchan": '',
                 "rh_epsr": '',
                 "rh_top": '',
                 "rh_depth": '',
                 "rh_reserved": '',
                 "rh_spp": '',
                 "rh_linemun": '',
                 "rh_start_x": '',
                 "rh_start_y": '',
                 "rh_end_x": '',
                 "rh_end_y": '',
                 "rh_lineorder": '',
                 "rh_dtype": '',
                 "rh_antname": '',
                 "rh_chanmask": '',
                 "rh_name": '',
                 "rh_chksum": '',
                 "rh_variable": '',
                 }
        self.mdichildlist[-1].OpenFile('UserCreate',headers,self.UiGetProfileData['Profile'])
        activeSubWindow=self.mdiArea.activeSubWindow()
                
        self.RecentFigureCanvas=PlotCanvas(self,MainWindow,data=self.UiGetProfileData['Profile'],width=15, height=6)
        activeSubWindow.widget().setWidget(self.RecentFigureCanvas)
        activeSubWindow.widget().widget().PlotAsWiggle()
        self.toolButtonWigb.setChecked(True)
        self.toolButtonPcolor.setChecked(False)
        self.toolButtonColorMap.setEnabled(False)
        self.menuColor_Map.setEnabled(False)
        self.toolButtonScanLine.setChecked(False)
        self.UserAspect=8
        self.UserCmap='cm.viridis'
        
class ScanMdiChild(QtWidgets.QScrollArea):
    sequenceNumber=0
    FileNumber=0
    def __init__(self):
        super(ScanMdiChild, self).__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.isUntitled=True
        self.tag=''
        
class MdiChild(QtWidgets.QScrollArea):
    sequenceNumber=0
    FileNumber=0
    def __init__(self,MainWindow):
        super(MdiChild, self).__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.isUntitled=True
        self.MainWindow=MainWindow
        self.tag=''
    def NewFile(self):
        self.isUntitled=True
        self.filename="Untitle%s"%MdiChild.sequenceNumber+"[*]"
        self.headers={"FileType":'New',
                      "FullFilePath":self.filename,
                      "rh_tag": '',
                      "rh_tag_bits": '',
                      "rh_tag_bytes": '',
                      "rh_data": '',
                      "rh_nsamp": '',
                      "rh_nsamp": '',
                      "rh_bits": '',
                      "rh_zero": '',
                      "rh_sps": '',
                      "rh_spm": '',
                      "rh_mpm": '',
                      "rh_position": '',
                      "rh_range": '',
                      "rh_npass": '',
                      "rh_create": '',
                      "rh_modif": '',
                      "rh_rgain": '',
                      "rh_nrgain": '',
                      "rh_text": '',
                      "rh_ntext": '',
                      "rh_proc": '',
                      "rh_nproc": '',
                      "rh_nchan": '',
                      "rh_epsr": '',
                      "rh_top": '',
                      "rh_depth": '',
                      "rh_reserved": '',
                      "rh_spp": '',
                      "rh_linemun": '',
                      "rh_start_x": '',
                      "rh_start_y": '',
                      "rh_end_x": '',
                      "rh_end_y": '',
                      "rh_lineorder": '',
                      "rh_dtype": '',
                      "rh_antname": '',
                      "rh_chanmask": '',
                      "rh_name": '',
                      "rh_chksum": '',
                      "rh_variable": '',
                      }
        MdiChild.sequenceNumber+=1
        MdiChild.FileNumber+=1
        self.setWindowTitle(self.filename)
        timeLogManagement=QtCore.QDateTime.currentDateTime()
        timeDisplayLogManagement=timeLogManagement.toString('yyyy-MM-dd hh:mm:ss')
        self.MainWindow.textBrowserLogManagement.append('---------------------------------------------------')
        self.MainWindow.textBrowserLogManagement.append('%s:User Create New File Named %s'%(timeDisplayLogManagement,self.filename[:-3]))  
        
    def OpenFile(self,FullFilePath,headers,data_array):
        self.tag='wiggle'
        self.isUntitled=True
        MdiChild.FileNumber+=1
        self.filename=FullFilePath+"[*]"
        self.headers=headers
        self.headers['FullFilePath']=FullFilePath
        self.headers['FileType']='Open'
        self.data_array=data_array
        self.setWindowTitle(self.filename)
        timeLogManagement=QtCore.QDateTime.currentDateTime()
        timeDisplayLogManagement=timeLogManagement.toString('yyyy-MM-dd hh:mm:ss')
        self.MainWindow.textBrowserLogManagement.append('---------------------------------------------------')
        self.MainWindow.textBrowserLogManagement.append('%s:User Open the File: %s'%(timeDisplayLogManagement,self.filename[:-3]))
        
    def PlotFileAsWiggle(self):
        self.isUntitled=False
        self.setWindowTitle(self.filename)
        self.setWindowModified(True)
        timeLogManagement=QtCore.QDateTime.currentDateTime()
        timeDisplayLogManagement=timeLogManagement.toString('yyyy-MM-dd hh:mm:ss')
        self.MainWindow.textBrowserLogManagement.append('---------------------------------------------------')
        self.MainWindow.textBrowserLogManagement.append('%s:User Has Plot the Figure As Wiggle %s'%(timeDisplayLogManagement,self.filename[:-3]))   
        
    def PlotFileAsPColor(self):
        self.isUntitled=False
        self.setWindowTitle(self.filename)
        self.setWindowModified(True)
        timeLogManagement=QtCore.QDateTime.currentDateTime()
        timeDisplayLogManagement=timeLogManagement.toString('yyyy-MM-dd hh:mm:ss')
        self.MainWindow.textBrowserLogManagement.append('---------------------------------------------------')
        self.MainWindow.textBrowserLogManagement.append('%s:User Has Plot the Figure As Pseudo Color %s'%(timeDisplayLogManagement,self.filename[:-3]))
        
    def closeEvent(self,event):
        timeLogManagement=QtCore.QDateTime.currentDateTime()
        MdiChild.FileNumber-=1
        # print(MdiChild.FileNumber)
        timeDisplayLogManagement=timeLogManagement.toString('yyyy-MM-dd hh:mm:ss')
        self.MainWindow.textBrowserLogManagement.append('---------------------------------------------------')
        self.MainWindow.textBrowserLogManagement.append('%s:User Close the File: %s'%(timeDisplayLogManagement,self.filename[:-3]))
        # print(self.MainWindow.FileList)
        try:
            self.MainWindow.FileList.remove(self.filename[:-3])
        except:
            pass
        if MdiChild.FileNumber==0:
            self.MainWindow.whenCloseAll()
        if self.MainWindow.FileList==[]:
            self.MainWindow.actionSave.setEnabled(False)
            self.MainWindow.actionSave_as.setEnabled(False)
            self.MainWindow.actionPrint_Preview.setEnabled(False)
            self.MainWindow.actionPrint.setEnabled(False)
            self.MainWindow.actionClose.setEnabled(False)
            self.MainWindow.actionCloseAll.setEnabled(False)
            self.MainWindow.menuView.setEnabled(False)
            self.MainWindow.menuData_Process.setEnabled(False)
            self.MainWindow.menuInversion_2D.setEnabled(False)
            self.MainWindow.ToolActionSave.setEnabled(False)
            self.MainWindow.ToolActionSaveAs.setEnabled(False)
            self.MainWindow.ToolActionPrint.setEnabled(False)
            self.MainWindow.ToolActionPrintPreview.setEnabled(False)
            self.MainWindow.dockWidgetTools.setEnabled(False)
            self.MainWindow.TreeViewOriginalFileName.setText(1,'')
            self.MainWindow.TreeViewCreateFileTime.setText(1,'')
            self.MainWindow.TreeViewEditFileTime.setText(1,'')
            self.MainWindow.TreeViewNumberOfChannels.setText(1,'')
            self.MainWindow.TreeViewScan_Seconds.setText(1,'')
            self.MainWindow.TreeViewScan_Unit.setText(1,'')
            self.MainWindow.TreeViewUnit_Mark.setText(1,'')
            self.MainWindow.TreeViewSample_Scan.setText(1,'')
            self.MainWindow.TreeViewBit_Sample.setText(1,'')
            self.MainWindow.TreeViewDielectricConstant.setText(1,'')
            self.MainWindow.TreeViewChannel.setText(1,'')
            self.MainWindow.TreeViewAntennaStyle.setText(1,'')
            self.MainWindow.TreeViewAntennaSerialNumber.setText(1,'')
            self.MainWindow.TreeViewPostion.setText(1,'')
            self.MainWindow.TreeViewRange.setText(1,'')
            self.MainWindow.TreeViewTopSurface.setText(1,'')
            self.MainWindow.TreeViewDepth.setText(1,'')
            self.MainWindow.TreeViewLowpass.setText(1,'')
            self.MainWindow.TreeViewHighpass.setText(1,'')
            self.MainWindow.TreeViewMigration.setText(1,'')

class PlotCanvas(FigureCanvas):
    def __init__(self,MainWindow,parent=None,data=None,width=15,height=6,dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.data=data
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.MainWindow=MainWindow
        
    def PlotAsPColor(self,tt=None,xx=None,gain=1):
        self.fig.clear()
        y_max,x_max=self.data.shape
        if tt==None:
            tt=np.arange(y_max)
        if xx==None:
            xx=np.arange(x_max)
        self.axes = self.fig.add_subplot(111)
        self.fig_=self.axes.imshow(self.data*gain,vmin=np.min(self.data),vmax=np.max(self.data))
        self.axes.set_aspect(1)
        self.axes.set_xlabel('Scan')
        self.axes.set_ylabel('Sample')
        self.draw()
        self.fig.canvas.mpl_connect('motion_notify_event', self.motion_call_back)
        self.fig.canvas.mpl_connect('button_press_event', self.press_call_back)
        self.MainWindow.dockWidgetDisplayGraphInfo.setEnabled(True)
    
    def motion_call_back(self,event):
        # print("x=%s,  z=%s"%(event.xdata,event.ydata))
        if event.xdata and event.ydata:
            self.MainWindow.statusbar.showMessage('x=%s,y=%s'%(event.xdata,event.ydata))
            self.draw()
            self.draw_idle()
        
    def press_call_back(self,event):
        if event.xdata and event.ydata:
            xdata_=int(event.xdata)
            ScanData=self.data[:,xdata_]
            if self.MainWindow.toolButtonScanLine.isChecked():
                self.MainWindow.graphicsViewScanLine.subWindowList()[0].widget().PlotScanLine(ScanData)
    
    def ChangeCmap(self,cmap):
        eval('self.fig_.set_cmap(%s)'%cmap)
        self.draw()
    
    def ChangeAspect(self,aspect):
        self.axes.set_aspect(1/aspect)
        self.draw()
    
    def ChangeVertical(self,ylim,ytick,ylabel):
        self.axes.set_yticks(np.linspace(0,ylim,6))
        self.axes.set_yticklabels(ytick)
        self.axes.set_ylabel(ylabel)
        self.draw()
    
    def PlotAsWiggle(self,tt=None,xx=None,gain=1):
        self.fig.clear()
        y_max,x_max=self.data.shape
        if tt==None:
            tt=np.arange(y_max)
        if xx==None:
            xx=np.arange(x_max)
        self.axes = self.fig.add_subplot(111)
        wigb.wiggle(self.axes,self.data,tt,xx,color='k',sf=0.1*gain)
        self.axes.set_aspect(0.125)
        self.axes.set_xlabel('Scan')
        self.axes.set_ylabel('Sample')
        self.draw()  
        self.fig.canvas.mpl_connect('motion_notify_event', self.motion_call_back)
        self.fig.canvas.mpl_connect('button_press_event', self.press_call_back)
        self.MainWindow.dockWidgetDisplayGraphInfo.setEnabled(True)

class ScanPlotCanvas(FigureCanvas):
    def __init__(self,MainWindow,parent=None,width=15,height=6,dpi=200):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.MainWindow=MainWindow
    def PlotScanLine(self,data):
        self.fig.clear()
        self.axes = self.fig.add_subplot(111)
        x=np.arange(len(data))
        self.fig_=self.axes.plot(data,x)
        self.axes.invert_yaxis()
        self.axes.axis('off')
        self.draw()
        



 

         

        
        
        
        
        