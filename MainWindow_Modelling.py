# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Modelling.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
import numpy as np
import UiNewModel
import UiAddRectangle
import UiAddEllipse
import UiAddPolygon
import GetMask
import WriteModelParameters
import ReadModelParameters
from matplotlib import cm

import time
import Forward2D

class Ui_MainWindow(object):
    EndModellingSignal=QtCore.pyqtSignal()
    def setupUi(self, MainWindow):
        self.mdichildlist=[]
        self.data=dict()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UI_Ico/modelling.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.mdiArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.TabbedView)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setDocumentMode(True)
        self.mdiArea.setTabsMovable(True)
        self.horizontalLayout.addWidget(self.mdiArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCreate = QtWidgets.QMenu(self.menubar)
        self.menuCreate.setObjectName("menuCreate")
        self.menuCreate.setEnabled(False)
        MainWindow.setMenuBar(self.menubar)
        #MENU--->View
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuView.setEnabled(False)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget_Tree = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_Tree.setAutoFillBackground(True)
        self.dockWidget_Tree.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_Tree.setObjectName("dockWidget_Tree")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setContentsMargins(9, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.treeView = QtWidgets.QTreeWidget(self.dockWidgetContents)
        self.treeView.setObjectName("treeView")
        
        self.treeView.setColumnCount(2)
        self.treeView.setHeaderLabels(['Model','Parameters'])
        self.treeView.setIndentation(10)
        self.treeView.setColumnWidth(0,100)
        self.treeView.setColumnWidth(1,100)
        
        self.toolButtonCreate = QtWidgets.QToolButton(self.dockWidgetContents)
        ToolBtniconCreate = QtGui.QIcon()
        ToolBtniconCreate.addPixmap(QtGui.QPixmap("./UI_Ico/create.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonCreate.setIcon(ToolBtniconCreate)
        self.toolButtonCreate.setIconSize(QtCore.QSize(80, 30))
        self.toolButtonCreate.setObjectName("toolButtonCreate")
        self.toolButtonCreate.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.gridLayout.addWidget(self.toolButtonCreate, 0, 1, 1, 1)
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
        # Add Create Menu
        self.ToolButtonMenu = QtWidgets.QMenu(self)
        # Create--->Sigma
        self.CreateSigma = QtWidgets.QAction('sigma', self)
        self.CreateSigma.setEnabled(False)
        self.ToolButtonMenu.addAction(self.CreateSigma)
        self.CreateSigma.triggered.connect(lambda: self.PlotModel(self.CreateSigma.text(),MainWindow))
        # Create--->Epsilon
        self.CreateEpsilon = QtWidgets.QAction('epsilon', self)
        self.CreateEpsilon.setEnabled(False)
        self.ToolButtonMenu.addAction(self.CreateEpsilon)
        self.CreateEpsilon.triggered.connect(lambda: self.PlotModel(self.CreateEpsilon.text(),MainWindow))
        # Create--->Mu
        self.CreateMu = QtWidgets.QAction('mu', self)
        self.CreateMu.setEnabled(False)
        self.ToolButtonMenu.addAction(self.CreateMu)
        self.CreateMu.triggered.connect(lambda: self.PlotModel(self.CreateMu.text(),MainWindow))
        self.ToolButtonMenu.addSeparator()
        # Create--->Profile
        self.CreateProfile = QtWidgets.QAction('Profile', self)
        self.CreateProfile.setEnabled(False)
        self.ToolButtonMenu.addAction(self.CreateProfile)
        self.CreateProfile.triggered.connect(lambda: self.PlotModel(self.CreateProfile.text(),MainWindow))
        self.toolButtonCreate.setMenu(self.ToolButtonMenu)
        # self.toolButtonCreate.clicked.connect(lambda: self.PlotModel(MainWindow))
        self.toolButtonCreate.setEnabled(False)
        
        self.toolButtonClear = QtWidgets.QToolButton(self.dockWidgetContents)
        self.toolButtonClear.setEnabled(False)
        
        ToolBtniconClear = QtGui.QIcon()
        ToolBtniconClear.addPixmap(QtGui.QPixmap("./UI_Ico/clear.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonClear.setIcon(ToolBtniconClear)
        self.toolButtonClear.setIconSize(QtCore.QSize(80, 30))
        self.toolButtonClear.setObjectName("ToolBtniconClear")
        self.gridLayout.addWidget(self.toolButtonClear, 0, 0, 1, 1)
        
        self.gridLayout.addWidget(self.treeView, 2, 0, 1, 3)
        self.dockWidget_Tree.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_Tree)
        
        # Add Colormap Menu
        self.toolButtonColorMap = QtWidgets.QToolButton(self.dockWidgetContents)
        ToolBtniconColorMap = QtGui.QIcon()
        ToolBtniconColorMap.addPixmap(QtGui.QPixmap("./UI_Ico/colormap.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonColorMap.setIcon(ToolBtniconColorMap)
        self.toolButtonColorMap.setIconSize(QtCore.QSize(80, 30))
        self.toolButtonColorMap.setObjectName("toolButtonColorMap")
        self.toolButtonColorMap.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.gridLayout.addWidget(self.toolButtonColorMap, 0, 2, 1, 1)
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
        self.toolButtonColorMap.setEnabled(False)
        
        # Menu--->File--->New
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.triggered.connect(lambda: self.NewFile(MainWindow))
        # Menu--->File--->Open
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(lambda: self.OpenFile(MainWindow))
        # Menu--->File--->Save
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setEnabled(False)
        self.actionSave.triggered.connect(self.SaveFile)
        # Menu--->File--->Save as 
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave_as.setEnabled(False)
        self.actionSave_as.triggered.connect(self.SaveAsFile)
        # Menu--->File--->Exit
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        
        # Menu--->Create--->New Model
        self.actionNewModel = QtWidgets.QAction(MainWindow)
        self.actionNewModel.setObjectName("actionNewModel")
        self.actionNewModel.triggered.connect(self.GetUiNewModel)
        self.actionNewModel.setEnabled(False)
        # Menu--->Create--->Rectangle
        self.actionRectangle = QtWidgets.QAction(MainWindow)
        self.actionRectangle.setObjectName("actionRectangle")
        self.actionRectangle.triggered.connect(self.GetUiAddRectangle)
        self.actionRectangle.setEnabled(False)
        # Menu--->Create--->Ellipse
        self.actionEllipse = QtWidgets.QAction(MainWindow)
        self.actionEllipse.setObjectName("actionEllipse")
        self.actionEllipse.triggered.connect(self.GetUiAddEllipse)
        self.actionEllipse.setEnabled(False)
        # Menu--->Create--->Polygon
        self.actionPolygon = QtWidgets.QAction(MainWindow)
        self.actionPolygon.setObjectName("actionPolygon")
        self.actionPolygon.triggered.connect(self.GetUiAddPolygon)
        self.actionPolygon.setEnabled(False)
        
        # Tool--->NewFile
        self.ToolActionNewFile = QtWidgets.QAction(MainWindow)
        iconNew = QtGui.QIcon()
        iconNew.addPixmap(QtGui.QPixmap("./UI_Ico/new.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionNewFile.setIcon(iconNew)
        self.ToolActionNewFile.setObjectName("ToolActionNewFile")
        self.ToolActionNewFile.triggered.connect(lambda: self.NewFile(MainWindow))
        # Tool--->OpenFile
        self.ToolActionOpenFile = QtWidgets.QAction(MainWindow)
        iconNew = QtGui.QIcon()
        iconNew.addPixmap(QtGui.QPixmap("./UI_Ico/open.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionOpenFile.setIcon(iconNew)
        self.ToolActionOpenFile.setObjectName("ToolActionOpenFile")
        self.ToolActionOpenFile.triggered.connect(lambda: self.OpenFile(MainWindow))
        # Tool--->Save
        self.ToolActionSave = QtWidgets.QAction(MainWindow)
        iconNew = QtGui.QIcon()
        iconNew.addPixmap(QtGui.QPixmap("./UI_Ico/save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionSave.setIcon(iconNew)
        self.ToolActionSave.setObjectName("ToolActionSave")
        self.ToolActionSave.setEnabled(False)
        self.ToolActionSave.triggered.connect(self.SaveFile)
        # Tool--->Save as
        self.ToolActionSaveAs = QtWidgets.QAction(MainWindow)
        iconNew = QtGui.QIcon()
        iconNew.addPixmap(QtGui.QPixmap("./UI_Ico/save as.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionSaveAs.setIcon(iconNew)
        self.ToolActionSaveAs.setObjectName("ToolActionSaveAs")
        self.ToolActionSaveAs.setEnabled(False)
        self.ToolActionSaveAs.triggered.connect(self.SaveAsFile)
        # Tool--->New Model
        self.ToolActionNewModel = QtWidgets.QAction(MainWindow)
        iconNew = QtGui.QIcon()
        iconNew.addPixmap(QtGui.QPixmap("./UI_Ico/new model.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionNewModel.setIcon(iconNew)
        self.ToolActionNewModel.setObjectName("ToolActionNewModel")
        self.ToolActionNewModel.setEnabled(False)
        self.ToolActionNewModel.triggered.connect(self.GetUiNewModel)
        # Tool--->Rectangle
        self.ToolActionRectangle = QtWidgets.QAction(MainWindow)
        iconNew = QtGui.QIcon()
        iconNew.addPixmap(QtGui.QPixmap("./UI_Ico/rectangle.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionRectangle.setIcon(iconNew)
        self.ToolActionRectangle.setObjectName("ToolActionRectangle")
        self.ToolActionRectangle.triggered.connect(self.GetUiAddRectangle)
        self.ToolActionRectangle.setEnabled(False)
        # Tool--->Ellipse
        self.ToolActionEllipse = QtWidgets.QAction(MainWindow)
        iconNew = QtGui.QIcon()
        iconNew.addPixmap(QtGui.QPixmap("./UI_Ico/ellipse.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionEllipse.setIcon(iconNew)
        self.ToolActionEllipse.setObjectName("ToolActionEllipse")
        self.ToolActionEllipse.triggered.connect(self.GetUiAddEllipse)
        self.ToolActionEllipse.setEnabled(False)
        # Tool--->Polygon
        self.ToolActionPolygon = QtWidgets.QAction(MainWindow)
        iconNew = QtGui.QIcon()
        iconNew.addPixmap(QtGui.QPixmap("./UI_Ico/polygon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionPolygon.setIcon(iconNew)
        self.ToolActionPolygon.setObjectName("ToolActionPolygon")
        self.ToolActionPolygon.triggered.connect(self.GetUiAddPolygon)
        self.ToolActionPolygon.setEnabled(False)
        # Tool--->Modelling
        self.ToolActionModelling = QtWidgets.QAction(MainWindow)
        iconNew = QtGui.QIcon()
        iconNew.addPixmap(QtGui.QPixmap("./UI_Ico/modelling.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionModelling.setIcon(iconNew)
        self.ToolActionModelling.setObjectName("ToolActionModelling")
        self.ToolActionModelling.triggered.connect(lambda: self.Modelling2D(MainWindow))
        self.ToolActionModelling.setEnabled(False)
        
        # Add to Menu--->File
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionExit)
        
        # Add to Menu--->Create
        self.menuCreate.addAction(self.actionNewModel)
        self.menuCreate.addSeparator()
        self.menuCreate.addAction(self.actionRectangle)
        self.menuCreate.addAction(self.actionEllipse)
        self.menuCreate.addAction(self.actionPolygon)
        
        # Add to Menu
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.menubar.addAction(self.menuCreate.menuAction())
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
        
        # Add to Tool
        self.toolBar.addAction(self.ToolActionNewFile)
        self.toolBar.addAction(self.ToolActionOpenFile)
        self.toolBar.addAction(self.ToolActionSave)
        self.toolBar.addAction(self.ToolActionSaveAs)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ToolActionNewModel)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ToolActionRectangle)
        self.toolBar.addAction(self.ToolActionEllipse)
        self.toolBar.addAction(self.ToolActionPolygon)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ToolActionModelling)
        # Add Custom Context Menu
        self.dockWidget_Tree.widget().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.dockWidget_Tree.widget().customContextMenuRequested[QtCore.QPoint].connect(self.TreeWidgetContext)
        
        self.windowMapper=QtCore.QSignalMapper(self)
        self.windowMapper.mapped[QtWidgets.QWidget].connect(self.setActiveSubWindow)
        self.mdiArea.subWindowActivated.connect(self.updataModelData)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCreate.setTitle(_translate("MainWindow", "Create"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNewModel.setText(_translate("MainWindow", "New Model"))
        self.actionRectangle.setText(_translate("MainWindow", "Rectangle"))
        self.actionEllipse.setText(_translate("MainWindow", "Ellipse"))
        self.actionPolygon.setText(_translate("MainWindow", "Polygon"))
        
        self.ToolActionNewFile.setText(_translate("MainWindow", "NewFile"))
        self.ToolActionNewFile.setToolTip(_translate("MainWindow", "<html><head/><body><p>New File</p></body></html>"))
        self.ToolActionOpenFile.setText(_translate("MainWindow", "OpenFile"))
        self.ToolActionOpenFile.setToolTip(_translate("MainWindow", "<html><head/><body><p>Open File</p></body></html>"))
        self.ToolActionSave.setText(_translate("MainWindow", "Save"))
        self.ToolActionSave.setToolTip(_translate("MainWindow", "<html><head/><body><p>Save</p></body></html>"))
        self.ToolActionSaveAs.setText(_translate("MainWindow", "SaveAs"))
        self.ToolActionSaveAs.setToolTip(_translate("MainWindow", "<html><head/><body><p>Save as</p></body></html>"))
        self.ToolActionNewModel.setText(_translate("MainWindow", "NewModel"))
        self.ToolActionNewModel.setToolTip(_translate("MainWindow", "<html><head/><body><p>New Model</p></body></html>"))
        self.ToolActionRectangle.setText(_translate("MainWindow", "Rectangle"))
        self.ToolActionRectangle.setToolTip(_translate("MainWindow", "<html><head/><body><p>Rectangle</p></body></html>"))
        self.ToolActionEllipse.setText(_translate("MainWindow", "Ellipse"))
        self.ToolActionEllipse.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ellipse</p></body></html>"))
        self.ToolActionPolygon.setText(_translate("MainWindow", "Polygon"))
        self.ToolActionPolygon.setToolTip(_translate("MainWindow", "<html><head/><body><p>Polygon</p></body></html>"))
        self.ToolActionModelling.setText(_translate("MainWindow", "Modelling"))
        self.ToolActionModelling.setToolTip(_translate("MainWindow", "<html><head/><body><p>Modelling</p></body></html>"))
        self.toolButtonClear.setText(_translate("MainWindow", "Clear"))
        self.toolButtonClear.setToolTip(_translate("MainWindow", "<html><head/><body><p>Clear</p></body></html>"))
        self.toolButtonColorMap.setText(_translate("MainWindow", "ColorMap"))
        self.toolButtonColorMap.setToolTip(_translate("MainWindow", "<html><head/><body><p>Color Map</p></body></html>"))
        self.toolButtonCreate.setText(_translate("MainWindow", "Create"))
        self.toolButtonCreate.setToolTip(_translate("MainWindow", "<html><head/><body><p>Create</p></body></html>"))

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
    def setActiveSubWindow(self, window):
        self.mdiArea.setActiveSubWindow(window)
        
    def updataModelData(self):
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            try:
                child=window.widget()
                if child is self.mdiArea.activeSubWindow().widget():
                    self.treeView.clear()
                    ModelData=child.SetModelData
                    if hasattr(child.widget(),'fig_'):
                        self.toolButtonColorMap.setEnabled(True)
                    else:
                        self.toolButtonColorMap.setEnabled(False)
                    if 'NewModel' in ModelData.keys():
                        self.updataTreeview_NewModel(ModelData)
                        self.actionRectangle.setEnabled(True)
                        self.actionEllipse.setEnabled(True)
                        self.actionPolygon.setEnabled(True)
                        self.ToolActionRectangle.setEnabled(True)
                        self.ToolActionEllipse.setEnabled(True)
                        self.ToolActionPolygon.setEnabled(True)
                        self.ToolActionModelling.setEnabled(True)
                        self.toolButtonCreate.setEnabled(True)
                        self.toolButtonClear.setEnabled(True)
                        self.CreateSigma.setEnabled(True)
                        self.CreateEpsilon.setEnabled(True)
                        self.CreateMu.setEnabled(True)
                    else:
                        self.actionRectangle.setEnabled(False)
                        self.actionEllipse.setEnabled(False)
                        self.actionPolygon.setEnabled(False)
                        self.ToolActionRectangle.setEnabled(False)
                        self.ToolActionEllipse.setEnabled(False)
                        self.ToolActionPolygon.setEnabled(False)
                        self.ToolActionModelling.setEnabled(False)
                        self.toolButtonCreate.setEnabled(False)
                        self.toolButtonColorMap.setEnabled(False)
                        self.toolButtonClear.setEnabled(False)
                        self.CreateSigma.setEnabled(False)
                        self.CreateEpsilon.setEnabled(False)
                        self.CreateMu.setEnabled(False)
                    if 'AddPolygon' in ModelData.keys():
                        self.updataTreeview_NewPolygon(ModelData)
                    if 'AddEllipse' in ModelData.keys():
                        self.updataTreeview_NewEllipse(ModelData)
                    if 'AddRectangle' in ModelData.keys():
                        self.updataTreeview_NewRectangle(ModelData)
            except:
                pass
                pass
        self.data=child.SetModelData
        
    def ChangeCmap(self,cmap):
        activeSubWindow=self.mdiArea.activeSubWindow()
        activeSubWindow.widget().widget().ChangeCmap('cm.'+cmap)
    
    def ChangeAspect(self,aspect):
        activeSubWindow=self.mdiArea.activeSubWindow()
        aspect=float(aspect)
        activeSubWindow.widget().widget().ChangeAspect(aspect)
        self.UserAspect=aspect
            
    def updataTreeview_NewModel(self,data):
        root_headfile=QtWidgets.QTreeWidgetItem(self.treeView)
        root_headfile.setText(0,'Model Parameters')
        # x lim
        self.TreeViewXlim=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewXlim.setText(0,'x limit')
        self.TreeViewXlim.setText(1,str(data['NewModel']['xlim']))
        # z lim
        self.TreeViewZlim=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewZlim.setText(0,'z limit')
        self.TreeViewZlim.setText(1,str(data['NewModel']['zlim']))
        # dx
        self.TreeViewDx=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewDx.setText(0,'dx')
        self.TreeViewDx.setText(1,str(data['NewModel']['dx']))
        # dz
        self.TreeViewDz=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewDz.setText(0,'dz')
        self.TreeViewDz.setText(1,str(data['NewModel']['dz']))
        # dt
        self.TreeViewDt=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewDt.setText(0,'dt')
        self.TreeViewDt.setText(1,'%1.2e'%data['NewModel']['dt'])
        # Simulation Time
        self.TreeViewSimulationTime=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewSimulationTime.setText(0,'Simulation Time')
        self.TreeViewSimulationTime.setText(1,'%1.2e'%data['NewModel']['t'])
        # Freq
        self.TreeViewFreq=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewFreq.setText(0,'Frequency')
        self.TreeViewFreq.setText(1,'%1.2e'%data['NewModel']['Freq'])
        # Conductivity
        self.TreeViewConductivity=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewConductivity.setText(0,'Conductivity')
        self.TreeViewConductivity.setText(1,'%1.2e'%data['NewModel']['Single_sigma'])
        # Dielectric Constant
        self.TreeViewDielectricConstant=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewDielectricConstant.setText(0,'DielectricConstant')
        self.TreeViewDielectricConstant.setText(1,'%1.2e'%data['NewModel']['Single_epsilon'])
        # Magnetic Permeability
        self.TreeViewMagneticPermeability=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewMagneticPermeability.setText(0,'Magnetic Permeability')
        self.TreeViewMagneticPermeability.setText(1,'%1.2e'%data['NewModel']['Single_mu'])
        
        self.treeView.expandAll()
        
    def updataTreeview_NewPolygon(self,data):
        root_headfile=QtWidgets.QTreeWidgetItem(self.treeView)
        root_headfile.setText(0,'New Polygon')
        # xc
        self.TreeViewXAxis=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewXAxis.setText(0,'x axis')
        self.TreeViewXAxis.setText(1,str(data['AddPolygon']['xc']))
        # xz
        self.TreeViewZAxis=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewZAxis.setText(0,'z axis')
        self.TreeViewZAxis.setText(1,str(data['AddPolygon']['zc']))
        # Conductivity
        self.TreeViewRecConductivity=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewRecConductivity.setText(0,'Conductivity')
        self.TreeViewRecConductivity.setText(1,str(data['AddPolygon']['Single_sigma']))
        # Dielectric Constant
        self.TreeViewRecDielectricConstant=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewRecDielectricConstant.setText(0,'DielectricConstant')
        self.TreeViewRecDielectricConstant.setText(1,str(data['AddPolygon']['Single_epsilon']))
        # Magnetic Permeability
        self.TreeViewRecMagneticPermeability=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewRecMagneticPermeability.setText(0,'Magnetic Permeability')
        self.TreeViewRecMagneticPermeability.setText(1,str(data['AddPolygon']['Single_mu']))
        self.treeView.expandAll()
    
    def updataTreeview_NewEllipse(self,data):
        root_headfile=QtWidgets.QTreeWidgetItem(self.treeView)
        root_headfile.setText(0,'New Ellipse')
        # Center_x
        self.TreeViewCenterX=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewCenterX.setText(0,'left')
        self.TreeViewCenterX.setText(1,str(data['AddEllipse']['Center_x']))
        # Center_z
        self.TreeViewCenterZ=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewCenterZ.setText(0,'Center_z')
        self.TreeViewCenterZ.setText(1,str(data['AddEllipse']['Center_z']))
        # LongAxis
        self.TreeViewLongAxis=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewLongAxis.setText(0,'Long Axis')
        self.TreeViewLongAxis.setText(1,str(data['AddEllipse']['LongAxis_']))
        # ShortAxis
        self.TreeViewShortAxis=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewShortAxis.setText(0,'Short Axis')
        self.TreeViewShortAxis.setText(1,str(data['AddEllipse']['ShortAxis_']))
        # Conductivity
        self.TreeViewRecConductivity=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewRecConductivity.setText(0,'Conductivity')
        self.TreeViewRecConductivity.setText(1,str(data['AddEllipse']['Single_sigma']))
        # Dielectric Constant
        self.TreeViewRecDielectricConstant=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewRecDielectricConstant.setText(0,'DielectricConstant')
        self.TreeViewRecDielectricConstant.setText(1,str(data['AddEllipse']['Single_epsilon']))
        # Magnetic Permeability
        self.TreeViewRecMagneticPermeability=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewRecMagneticPermeability.setText(0,'Magnetic Permeability')
        self.TreeViewRecMagneticPermeability.setText(1,str(data['AddEllipse']['Single_mu']))
        self.treeView.expandAll()
    
    def updataTreeview_NewRectangle(self,data):
        root_headfile=QtWidgets.QTreeWidgetItem(self.treeView)
        root_headfile.setText(0,'New Rectangle')
        # left
        self.TreeViewLeft=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewLeft.setText(0,'left')
        self.TreeViewLeft.setText(1,str(data['AddRectangle']['Left']))
        # Bottom
        self.TreeViewBottom=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewBottom.setText(0,'bottom')
        self.TreeViewBottom.setText(1,str(data['AddRectangle']['Bottom']))
        # Width
        self.TreeViewWidth=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewWidth.setText(0,'width')
        self.TreeViewWidth.setText(1,str(data['AddRectangle']['Width']))
        # High
        self.TreeViewHigh=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewHigh.setText(0,'high')
        self.TreeViewHigh.setText(1,str(data['AddRectangle']['High']))
        # Conductivity
        self.TreeViewRecConductivity=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewRecConductivity.setText(0,'Conductivity')
        self.TreeViewRecConductivity.setText(1,str(data['AddRectangle']['Single_sigma']))
        # Dielectric Constant
        self.TreeViewRecDielectricConstant=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewRecDielectricConstant.setText(0,'DielectricConstant')
        self.TreeViewRecDielectricConstant.setText(1,str(data['AddRectangle']['Single_epsilon']))
        # Magnetic Permeability
        self.TreeViewRecMagneticPermeability=QtWidgets.QTreeWidgetItem(root_headfile)
        self.TreeViewRecMagneticPermeability.setText(0,'Magnetic Permeability')
        self.TreeViewRecMagneticPermeability.setText(1,str(data['AddRectangle']['Single_mu']))
        self.treeView.expandAll()
        
    def TreeWidgetContext(self,point):
        self.CreateTreeContext()
        self.TreeMenu.exec_(QtGui.QCursor.pos())
    
    def CreateTreeContext(self):
        self.TreeMenu=QtWidgets.QMenu()
        self.TreeMenuActionNewModel=QtWidgets.QAction('Add New Model',self)
        self.TreeMenuActionRectangle=QtWidgets.QAction('Add Rectangle',self)
        self.TreeMenuActionEllipse=QtWidgets.QAction('Add Ellipse',self)
        self.TreeMenuActionPolygon=QtWidgets.QAction('Add Polygon',self)
        self.TreeMenu.addAction(self.TreeMenuActionNewModel)
        self.TreeMenu.addSeparator()
        self.TreeMenu.addAction(self.TreeMenuActionRectangle)
        self.TreeMenu.addAction(self.TreeMenuActionEllipse)
        self.TreeMenu.addAction(self.TreeMenuActionPolygon)
    
    def NewFile(self,MainWindow):
        self.mdichildlist.append(MdiChild(MainWindow))
        self.mdiArea.addSubWindow(self.mdichildlist[-1])
        self.mdichildlist[-1].show()
        self.mdichildlist[-1].NewFile()
        self.actionNewModel.setEnabled(True)
        self.ToolActionNewModel.setEnabled(True)
        self.treeView.clear()
        self.menuCreate.setEnabled(True)
        
    def OpenFile(self,MainWindow):
        FileName,FileType=QtWidgets.QFileDialog.getOpenFileName(self,'Select File','./','GPR Files (*.csu);;GprMax File (*.in)')
        self.mdichildlist.append(MdiChild(MainWindow))
        self.mdiArea.addSubWindow(self.mdichildlist[-1])
        self.mdichildlist[-1].show()
        self.mdichildlist[-1].OpenFile(FileName)
        self.actionNewModel.setEnabled(False)
        self.ToolActionNewModel.setEnabled(False)
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            try:
                child=window.widget()
                if child is self.mdiArea.activeSubWindow().widget():
                    break
            except:
                pass
        if 'GPR File' in FileType:
            self.treeView.clear()
            FileOpenModule=ReadModelParameters.FileOpen_Read(FileName)
            FileOpenModule.ReadModelParameters()
            child.SetModelData['NewModel']=dict()
            SourceStart=FileOpenModule.SourceStart
            ReceiverStart=FileOpenModule.ReceierStart
            Step=FileOpenModule.Step
            Scan=int(FileOpenModule.Scan)
            child.SetModelData['NewModel']['zlim']=FileOpenModule.Z_Range
            child.SetModelData['NewModel']['xlim']=FileOpenModule.X_Range
            child.SetModelData['NewModel']['dz']=FileOpenModule.dz
            child.SetModelData['NewModel']['dx']=FileOpenModule.dx
            child.SetModelData['NewModel']['dt']=FileOpenModule.dt
            child.SetModelData['NewModel']['t']=FileOpenModule.SimulationTime
            child.SetModelData['NewModel']['k_max']=int(np.round(child.SetModelData['NewModel']['t']/child.SetModelData['NewModel']['dt'])+1)
            child.SetModelData['NewModel']['xl']=int(np.round(child.SetModelData['NewModel']['xlim']/child.SetModelData['NewModel']['dx'])+1)
            child.SetModelData['NewModel']['zl']=int(np.round(child.SetModelData['NewModel']['zlim']/child.SetModelData['NewModel']['dz'])+1)    
            child.SetModelData['NewModel']['Freq']=FileOpenModule.Frequence

            Source_z_idx=[int(round((SourceStart[0]+Step*i)/child.SetModelData['NewModel']['dx'])+10) for i in range(Scan)]
            Source_x_idx=[int(round(SourceStart[1]/child.SetModelData['NewModel']['dz'])+10) for i in range(Scan)]
            Source_x=[SourceStart[0]+Step*i for i in range(Scan)]
            Source_z=[SourceStart[1] for i in range(Scan)]
            child.SetModelData['NewModel']['SourcePosition_idx']=list(zip(Source_x_idx,Source_z_idx))
            child.SetModelData['NewModel']['SourcePosition']=list(zip(Source_x,Source_z))
            Receiver_x=[ReceiverStart[0]+Step*i for i in range(Scan)]
            Receiver_z=[ReceiverStart[1] for i in range(Scan)]
            Receiver_z_idx=[int(round((ReceiverStart[0]+Step*i)/child.SetModelData['NewModel']['dx'])+10) for i in range(Scan)]
            Receiver_x_idx=[int(round(ReceiverStart[1]/child.SetModelData['NewModel']['dx'])+10) for i in range(Scan)]
            child.SetModelData['NewModel']['ReceiverPosition_idx']=list(zip(Receiver_x_idx,Receiver_z_idx))
            child.SetModelData['NewModel']['ReceiverPosition']=list(zip(Receiver_x,Receiver_z))
            data_=np.ones((child.SetModelData['NewModel']['xl'],child.SetModelData['NewModel']['zl']))
            print(child.SetModelData['NewModel']['xl'])
            print(child.SetModelData['NewModel']['zl'])
            
            child.SetModelData['NewModel']['Single_sigma']=FileOpenModule.NM_Conductivity
            child.SetModelData['NewModel']['sigma']=child.SetModelData['NewModel']['Single_sigma']*data_
            child.SetModelData['NewModel']['Single_epsilon']=FileOpenModule.NM_DielectricConstant
            child.SetModelData['NewModel']['epsilon']=child.SetModelData['NewModel']['Single_epsilon']*data_
            child.SetModelData['NewModel']['Single_mu']=FileOpenModule.NM_MagneticPermeability
            child.SetModelData['NewModel']['mu']=child.SetModelData['NewModel']['Single_mu']*data_
            child.SetModelData['All_sigma']=child.SetModelData['NewModel']['Single_sigma']*data_
            child.SetModelData['All_epsilon']=child.SetModelData['NewModel']['Single_epsilon']*data_
            child.SetModelData['All_mu']=child.SetModelData['NewModel']['Single_mu']*data_
            print(child.SetModelData['All_epsilon'].shape)
            child.SetModelData['NewModel']['Step']=Step
            child.SetModelData['NewModel']['Scan']=Scan
            self.actionSave.setEnabled(True)
            self.actionSave_as.setEnabled(True)
            self.ToolActionSave.setEnabled(True)
            self.ToolActionSaveAs.setEnabled(True)
            self.actionRectangle.setEnabled(True)
            self.actionEllipse.setEnabled(True)
            self.actionPolygon.setEnabled(True)
            self.ToolActionRectangle.setEnabled(True)
            self.ToolActionEllipse.setEnabled(True)
            self.ToolActionPolygon.setEnabled(True)
            self.ToolActionModelling.setEnabled(True)
            self.toolButtonCreate.setEnabled(True)
            self.toolButtonClear.setEnabled(True)
            self.CreateSigma.setEnabled(True)
            self.CreateEpsilon.setEnabled(True)
            self.CreateMu.setEnabled(True)
            self.updataTreeview_NewModel(child.SetModelData)
            if hasattr(FileOpenModule, 'Rectangle'):
                Left=FileOpenModule.Left
                Bottom=FileOpenModule.Bottom
                Width=FileOpenModule.Width
                High=FileOpenModule.High
                child.SetModelData['AddRectangle']=dict()
                sigma=FileOpenModule.Re_Conductivity
                epsilon=FileOpenModule.Re_DielectricConstant
                mu=FileOpenModule.Re_MagneticPermeability
                rec_xlim=(int(np.round(Left/child.SetModelData['NewModel']['dx'])),int(np.round((Left+Width)/child.SetModelData['NewModel']['dx'])))
                rec_zlim=(int(np.round(Bottom/child.SetModelData['NewModel']['dz'])),int(np.round((Bottom+High)/child.SetModelData['NewModel']['dz'])))
                    
                sigma_=np.array(child.SetModelData['NewModel']['sigma'])
                epsilon_=np.array(child.SetModelData['NewModel']['epsilon'])
                mu_=np.array(child.SetModelData['NewModel']['mu'])
                All_sigma_=np.array(child.SetModelData['All_sigma'])
                All_epsilon_=np.array(child.SetModelData['All_epsilon'])
                All_mu_=np.array(child.SetModelData['All_mu'])
                    
                sigma_[rec_zlim[0]:rec_zlim[1]+1,rec_xlim[0]:rec_xlim[1]+1]=sigma
                epsilon_[rec_zlim[0]:rec_zlim[1]+1,rec_xlim[0]:rec_xlim[1]+1]=epsilon
                mu_[rec_zlim[0]:rec_zlim[1]+1,rec_xlim[0]:rec_xlim[1]+1]=mu
                All_sigma_[rec_zlim[0]:rec_zlim[1]+1,rec_xlim[0]:rec_xlim[1]+1]=sigma
                All_epsilon_[rec_zlim[0]:rec_zlim[1]+1,rec_xlim[0]:rec_xlim[1]+1]=epsilon
                All_mu_[rec_zlim[0]:rec_zlim[1]+1,rec_xlim[0]:rec_xlim[1]+1]=mu
                child.SetModelData['AddRectangle']['sigma']=sigma_
                child.SetModelData['AddRectangle']['epsilon']=epsilon_
                child.SetModelData['AddRectangle']['mu']=mu_
                child.SetModelData['AddRectangle']['Single_sigma']=sigma
                child.SetModelData['AddRectangle']['Single_epsilon']=epsilon
                child.SetModelData['AddRectangle']['Single_mu']=mu
                child.SetModelData['All_sigma']=All_sigma_
                child.SetModelData['All_epsilon']=All_epsilon_
                child.SetModelData['All_mu']=All_mu_
                
                child.SetModelData['AddRectangle']['Left']=Left
                child.SetModelData['AddRectangle']['Bottom']=Bottom
                child.SetModelData['AddRectangle']['Width']=Width
                child.SetModelData['AddRectangle']['High']=High
                self.updataTreeview_NewRectangle(child.SetModelData)
                # self.actionSave.setEnabled(True)
                # self.actionSave_as.setEnabled(True)
                # self.ToolActionSave.setEnabled(True)
                # self.ToolActionSaveAs.setEnabled(True)
                # self.actionRectangle.setEnabled(True)
                # self.actionEllipse.setEnabled(True)
                # self.actionPolygon.setEnabled(True)
                # self.ToolActionRectangle.setEnabled(True)
                # self.ToolActionEllipse.setEnabled(True)
                # self.ToolActionPolygon.setEnabled(True)
                # self.ToolActionModelling.setEnabled(True)
                # self.toolButtonCreate.setEnabled(True)
                # self.toolButtonClear.setEnabled(True)
                # self.CreateSigma.setEnabled(True)
                # self.CreateEpsilon.setEnabled(True)
                # self.CreateMu.setEnabled(True)
            if hasattr(FileOpenModule, 'Ellipse'):
                sigma=FileOpenModule.El_Conductivity
                epsilon=FileOpenModule.El_DielectricConstant
                mu=FileOpenModule.El_MagneticPermeability
                LongAxis=FileOpenModule.LongAxis
                ShortAxis=FileOpenModule.ShortAxis
                Center=FileOpenModule.Center
                child.SetModelData['AddEllipse']=dict()
                Center_x=int(np.round(Center[0]/child.SetModelData['NewModel']['dx']))
                Center_z=int(np.round(Center[1]/child.SetModelData['NewModel']['dz']))
                LongAxis_=int(np.round(LongAxis/child.SetModelData['NewModel']['dx']))
                ShortAxis_=int(np.round(ShortAxis/child.SetModelData['NewModel']['dz']))
                sigma_=np.array(child.SetModelData['NewModel']['sigma'])
                epsilon_=np.array(child.SetModelData['NewModel']['epsilon'])
                mu_=np.array(child.SetModelData['NewModel']['mu'])
                    
                All_sigma_=np.array(child.SetModelData['All_sigma'])
                All_epsilon_=np.array(child.SetModelData['All_epsilon'])
                All_mu_=np.array(child.SetModelData['All_mu'])
                    
                for i in range(sigma_.shape[0]):
                    for j in range(sigma_.shape[1]):
                        if (i-Center_x)**2/LongAxis_**2+(j-Center_z)**2/ShortAxis_**2<1:
                            sigma_[i,j]=sigma
                            epsilon_[i,j]=epsilon
                            mu_[i,j]=mu
                            All_sigma_[i,j]=sigma
                            All_epsilon_[i,j]=epsilon
                            All_mu_[i,j]=mu
                                
                child.SetModelData['AddEllipse']['sigma']=sigma_
                child.SetModelData['AddEllipse']['epsilon']=epsilon_
                child.SetModelData['AddEllipse']['mu']=mu_
                
                child.SetModelData['AddEllipse']['Center_x']=Center[0]
                child.SetModelData['AddEllipse']['Center_z']=Center[1]
                child.SetModelData['AddEllipse']['LongAxis_']=LongAxis
                child.SetModelData['AddEllipse']['ShortAxis_']=ShortAxis
                child.SetModelData['AddEllipse']['Single_sigma']=sigma
                child.SetModelData['AddEllipse']['Single_epsilon']=epsilon
                child.SetModelData['AddEllipse']['Single_mu']=mu
                child.SetModelData['All_sigma']=All_sigma_
                child.SetModelData['All_epsilon']=All_epsilon_
                child.SetModelData['All_mu']=All_mu_
                self.updataTreeview_NewEllipse(child.SetModelData)
                
            if hasattr(FileOpenModule, 'Polygon'):
                child.SetModelData['AddPolygon']=dict()
                sigma=FileOpenModule.Po_Conductivity
                epsilon=FileOpenModule.Po_DielectricConstant
                mu=FileOpenModule.Po_MagneticPermeability
                sigma_=np.array(child.SetModelData['NewModel']['sigma'])
                epsilon_=np.array(child.SetModelData['NewModel']['epsilon'])
                mu_=np.array(child.SetModelData['NewModel']['mu'])
                
                All_sigma_=np.array(child.SetModelData['All_sigma'])
                All_epsilon_=np.array(child.SetModelData['All_epsilon'])
                All_mu_=np.array(child.SetModelData['All_mu'])
                
                xc_=FileOpenModule.xc
                zc_=FileOpenModule.zc

                xc=[int(np.round(x/child.SetModelData['NewModel']['dx'])) for x in xc_]
                zc=[int(np.round(z/child.SetModelData['NewModel']['dz'])) for z in zc_]
                masked=GetMask.GetMask(sigma_,xc,zc)
                sigma_[masked]=sigma
                epsilon_[masked]=epsilon
                mu_[masked]=mu
                All_sigma_[masked]=sigma
                All_epsilon_[masked]=epsilon
                All_mu_[masked]=mu
                child.SetModelData['AddPolygon']['sigma']=sigma_
                child.SetModelData['AddPolygon']['epsilon']=epsilon_
                child.SetModelData['AddPolygon']['mu']=mu_
                child.SetModelData['AddPolygon']['Single_sigma']=sigma
                child.SetModelData['AddPolygon']['Single_epsilon']=epsilon
                child.SetModelData['AddPolygon']['Single_mu']=mu
                child.SetModelData['AddPolygon']['xc']=xc_
                child.SetModelData['AddPolygon']['zc']=zc_
                    
                child.SetModelData['All_sigma']=All_sigma_
                child.SetModelData['All_epsilon']=All_epsilon_
                child.SetModelData['All_mu']=All_mu_
                # print(child.SetModelData)
                self.updataTreeview_NewPolygon(child.SetModelData)
                    
        if 'GprMax' in FileType:
            print('Here is the .in file')
        
        
    def SaveFile(self):
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            try:
                child=window.widget()
                if child is self.mdiArea.activeSubWindow().widget():
                    break
            except:
                pass
        FileName,FileType=QtWidgets.QFileDialog.getSaveFileName(self,'Save','./','GPR Files (*.csu)')
        WriteModelParameters.WriteModelData(child.SetModelData,FileName)      
    
    def SaveAsFile(self):
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            try:
                child=window.widget()
                if child is self.mdiArea.activeSubWindow().widget():
                    break
            except:
                pass
        FileName,FileType=QtWidgets.QFileDialog.getSaveFileName(self,'Save as','./','GPR Files (*.csu);;GprMax Files (*.in)')
        if 'GprMax' in FileType:
            print('Here is the .in Files')
        if 'GPR Files' in FileType:
            WriteModelParameters.WriteModelData(child.SetModelData,FileName)
        
    def GetUiAddPolygon(self):
        AddPolygon=UiAddPolygon.Ui_AddPolygon(self)
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            try:
                child=window.widget()
                if child is self.mdiArea.activeSubWindow().widget():
                    break
            except:
                pass
        AddPolygon.show()
        if AddPolygon.exec_() == AddPolygon.Accepted:
            if (not isinstance(eval(AddPolygon.lineEdit_XAxisData.text()),tuple)) or \
            (not isinstance(eval(AddPolygon.lineEdit_ZAxisData.text()),tuple)) or \
            len(eval(AddPolygon.lineEdit_XAxisData.text()))<3 or \
            len(eval(AddPolygon.lineEdit_ZAxisData.text()))<3 or (AddPolygon.lineEdit_Conductivity.text=='') or \
            (AddPolygon.lineEdit_MagneticPermeability.text==''):
                QtWidgets.QMessageBox.warning(self,"Warning","Wrong data,Please try again !!!",QtWidgets.QMessageBox.Yes)
            else:
                child.SetModelData['AddPolygon']=dict()
                sigma=float(AddPolygon.lineEdit_Conductivity.text())
                epsilon=AddPolygon.doubleSpinBox_DielectricConstant.value()
                mu=float(AddPolygon.lineEdit_MagneticPermeability.text())
                sigma_=np.array(child.SetModelData['NewModel']['sigma'])
                epsilon_=np.array(child.SetModelData['NewModel']['epsilon'])
                mu_=np.array(child.SetModelData['NewModel']['mu'])
                
                All_sigma_=np.array(child.SetModelData['All_sigma'])
                All_epsilon_=np.array(child.SetModelData['All_epsilon'])
                All_mu_=np.array(child.SetModelData['All_mu'])
                
                xc_=eval(AddPolygon.lineEdit_XAxisData.text())
                zc_=eval(AddPolygon.lineEdit_ZAxisData.text())

                xc=[int(np.round(x/child.SetModelData['NewModel']['dx'])) for x in xc_]
                zc=[int(np.round(z/child.SetModelData['NewModel']['dz'])) for z in zc_]
                if [x for x in xc_ if x>child.SetModelData['NewModel']['xlim']] or [z for z in zc_ if z>child.SetModelData['NewModel']['zlim']]:
                    QtWidgets.QMessageBox.warning(self,"Warning","Out of range,Please try again !!!",QtWidgets.QMessageBox.Yes)
                else:
                    masked=GetMask.GetMask(sigma_,xc,zc)
                    sigma_[masked]=sigma
                    epsilon_[masked]=epsilon
                    mu_[masked]=mu
                    All_sigma_[masked]=sigma
                    All_epsilon_[masked]=epsilon
                    All_mu_[masked]=mu
                    child.SetModelData['AddPolygon']['sigma']=sigma_
                    child.SetModelData['AddPolygon']['epsilon']=epsilon_
                    child.SetModelData['AddPolygon']['mu']=mu_
                    child.SetModelData['AddPolygon']['Single_sigma']=sigma
                    child.SetModelData['AddPolygon']['Single_epsilon']=epsilon
                    child.SetModelData['AddPolygon']['Single_mu']=mu
                    child.SetModelData['AddPolygon']['xc']=xc_
                    child.SetModelData['AddPolygon']['zc']=zc_
                    
                    child.SetModelData['All_sigma']=All_sigma_
                    child.SetModelData['All_epsilon']=All_epsilon_
                    child.SetModelData['All_mu']=All_mu_
                    
                    root_headfile=QtWidgets.QTreeWidgetItem(self.treeView)
                    root_headfile.setText(0,'New Polygon')
                    # xc
                    self.TreeViewXAxis=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewXAxis.setText(0,'x axis')
                    self.TreeViewXAxis.setText(1,str(child.SetModelData['AddPolygon']['xc']))
                    # xz
                    self.TreeViewZAxis=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewZAxis.setText(0,'z axis')
                    self.TreeViewZAxis.setText(1,str(child.SetModelData['AddPolygon']['zc']))
                    # Conductivity
                    self.TreeViewRecConductivity=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewRecConductivity.setText(0,'Conductivity')
                    self.TreeViewRecConductivity.setText(1,'%1.2e'%child.SetModelData['AddPolygon']['Single_sigma'])
                    # Dielectric Constant
                    self.TreeViewRecDielectricConstant=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewRecDielectricConstant.setText(0,'DielectricConstant')
                    self.TreeViewRecDielectricConstant.setText(1,'%1.2e'%child.SetModelData['AddPolygon']['Single_epsilon'])
                    # Magnetic Permeability
                    self.TreeViewRecMagneticPermeability=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewRecMagneticPermeability.setText(0,'Magnetic Permeability')
                    self.TreeViewRecMagneticPermeability.setText(1,'%1.2e'%child.SetModelData['AddPolygon']['Single_mu'])
                    self.treeView.expandAll()
    
    def GetUiAddEllipse(self):
        AddEllipse=UiAddEllipse.Ui_AddEllipse(self)
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            try:
                child=window.widget()
                if child is self.mdiArea.activeSubWindow().widget():
                    break
            except:
                pass
        AddEllipse.show()
        if AddEllipse.exec_() == AddEllipse.Accepted:
            if (AddEllipse.lineEdit_LongAxis.text()=='') or (AddEllipse.lineEdit_ShortAxis.text()=='') or \
            (not isinstance(eval(AddEllipse.lineEdit_Center.text()),tuple)) or \
            (AddEllipse.lineEdit_Conductivity.text()=='') or (AddEllipse.lineEdit_MagneticPermeability.text()=='') :
                QtWidgets.QMessageBox.warning(self,"Warning","Wrong data,Please try again !!!",QtWidgets.QMessageBox.Yes)
            else:
                sigma=eval(AddEllipse.lineEdit_Conductivity.text())
                epsilon=AddEllipse.doubleSpinBox_DielectricConstant.value()
                mu=eval(AddEllipse.lineEdit_MagneticPermeability.text())
                LongAxis=float(AddEllipse.lineEdit_LongAxis.text())
                ShortAxis=float(AddEllipse.lineEdit_ShortAxis.text())
                Center=eval(AddEllipse.lineEdit_Center.text())
                if (Center[1]-ShortAxis)<0 or (Center[1]+ShortAxis)>child.SetModelData['NewModel']['xlim'] or \
                (Center[0]-LongAxis)<0 or (Center[0]+LongAxis)>child.SetModelData['NewModel']['zlim']:
                    QtWidgets.QMessageBox.warning(self,"Warning","Out of range,Please try again !!!",QtWidgets.QMessageBox.Yes)
                else:
                    child.SetModelData['AddEllipse']=dict()
                    Center_x=int(np.round(Center[1]/child.SetModelData['NewModel']['dx']))
                    Center_z=int(np.round(Center[0]/child.SetModelData['NewModel']['dz']))
                    ShortAxis_=int(np.round(LongAxis/child.SetModelData['NewModel']['dx']))
                    LongAxis_=int(np.round(ShortAxis/child.SetModelData['NewModel']['dz']))
                    sigma_=np.array(child.SetModelData['NewModel']['sigma'])
                    epsilon_=np.array(child.SetModelData['NewModel']['epsilon'])
                    mu_=np.array(child.SetModelData['NewModel']['mu'])
                    
                    All_sigma_=np.array(child.SetModelData['All_sigma'])
                    All_epsilon_=np.array(child.SetModelData['All_epsilon'])
                    All_mu_=np.array(child.SetModelData['All_mu'])
                    
                    for i in range(sigma_.shape[0]):
                        for j in range(sigma_.shape[1]):
                            if (i-Center_x)**2/LongAxis_**2+(j-Center_z)**2/ShortAxis_**2<1:
                                sigma_[i,j]=sigma
                                epsilon_[i,j]=epsilon
                                mu_[i,j]=mu
                                All_sigma_[i,j]=sigma
                                All_epsilon_[i,j]=epsilon
                                All_mu_[i,j]=mu
                                
                    child.SetModelData['AddEllipse']['sigma']=sigma_
                    child.SetModelData['AddEllipse']['epsilon']=epsilon_
                    child.SetModelData['AddEllipse']['mu']=mu_
                    
                    child.SetModelData['AddEllipse']['Center_x']=Center[0]
                    child.SetModelData['AddEllipse']['Center_z']=Center[1]
                    child.SetModelData['AddEllipse']['LongAxis_']=LongAxis
                    child.SetModelData['AddEllipse']['ShortAxis_']=ShortAxis
                    child.SetModelData['AddEllipse']['Single_sigma']=sigma
                    child.SetModelData['AddEllipse']['Single_epsilon']=epsilon
                    child.SetModelData['AddEllipse']['Single_mu']=mu
                    child.SetModelData['All_sigma']=All_sigma_
                    child.SetModelData['All_epsilon']=All_epsilon_
                    child.SetModelData['All_mu']=All_mu_
                    
                    root_headfile=QtWidgets.QTreeWidgetItem(self.treeView)
                    root_headfile.setText(0,'New Ellipse')
                    # Center_x
                    self.TreeViewCenterX=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewCenterX.setText(0,'Center_x')
                    self.TreeViewCenterX.setText(1,str(child.SetModelData['AddEllipse']['Center_x']))
                    # Center_z
                    self.TreeViewCenterZ=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewCenterZ.setText(0,'Center_z')
                    self.TreeViewCenterZ.setText(1,str(child.SetModelData['AddEllipse']['Center_z']))
                    # LongAxis
                    self.TreeViewLongAxis=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewLongAxis.setText(0,'Long Axis')
                    self.TreeViewLongAxis.setText(1,str(child.SetModelData['AddEllipse']['LongAxis_']))
                    # ShortAxis
                    self.TreeViewShortAxis=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewShortAxis.setText(0,'Short Axis')
                    self.TreeViewShortAxis.setText(1,str(child.SetModelData['AddEllipse']['ShortAxis_']))
                    # Conductivity
                    self.TreeViewRecConductivity=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewRecConductivity.setText(0,'Conductivity')
                    self.TreeViewRecConductivity.setText(1,'%1.2e'%child.SetModelData['AddEllipse']['Single_sigma'])
                    # Dielectric Constant
                    self.TreeViewRecDielectricConstant=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewRecDielectricConstant.setText(0,'DielectricConstant')
                    self.TreeViewRecDielectricConstant.setText(1,'%1.2e'%child.SetModelData['AddEllipse']['Single_epsilon'])
                    # Magnetic Permeability
                    self.TreeViewRecMagneticPermeability=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewRecMagneticPermeability.setText(0,'Magnetic Permeability')
                    self.TreeViewRecMagneticPermeability.setText(1,'%1.2e'%child.SetModelData['AddEllipse']['Single_mu'])
                    self.treeView.expandAll()
                                 
    def GetUiAddRectangle(self):
        AddRectangle=UiAddRectangle.Ui_AddRectangle(self)
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            try:
                child=window.widget()
                if child is self.mdiArea.activeSubWindow().widget():
                    break
            except:
                pass
        AddRectangle.show()
        if AddRectangle.exec_() == AddRectangle.Accepted:
            if (AddRectangle.lineEdit_Left.text()=='') or (AddRectangle.lineEdit_Bottom.text()=='') or \
            (AddRectangle.lineEdit_Width.text()=='') or (AddRectangle.lineEdit_High.text()=='') or \
            (AddRectangle.lineEdit_Conductivity.text()=='') or (AddRectangle.lineEdit_MagneticPermeability.text()==''):
                QtWidgets.QMessageBox.warning(self,"Warning","Wrong data,Please try again !!!",QtWidgets.QMessageBox.Yes)
            else:
                Left=float(AddRectangle.lineEdit_Left.text())
                Bottom=float(AddRectangle.lineEdit_Bottom.text())
                Width=float(AddRectangle.lineEdit_Width.text())
                High=float(AddRectangle.lineEdit_High.text())
                if Left<0 or Bottom<0 or (Left+Width)>child.SetModelData['NewModel']['xlim'] or (Bottom+High)>child.SetModelData['NewModel']['zlim']:
                    QtWidgets.QMessageBox.warning(self,"Warning","Out of range,Please try again !!!",QtWidgets.QMessageBox.Yes)
                else:
                    child.SetModelData['AddRectangle']=dict()
                    sigma=eval(AddRectangle.lineEdit_Conductivity.text())
                    epsilon=AddRectangle.doubleSpinBox_DielectricConstant.value()
                    mu=eval(AddRectangle.lineEdit_MagneticPermeability.text())
                    rec_xlim=(int(np.round(Left/child.SetModelData['NewModel']['dx'])),int(np.round((Left+Width)/child.SetModelData['NewModel']['dx'])))
                    rec_zlim=(int(np.round(Bottom/child.SetModelData['NewModel']['dz'])),int(np.round((Bottom+High)/child.SetModelData['NewModel']['dz'])))
                    
                    sigma_=np.array(child.SetModelData['NewModel']['sigma'])
                    epsilon_=np.array(child.SetModelData['NewModel']['epsilon'])
                    mu_=np.array(child.SetModelData['NewModel']['mu'])
                    All_sigma_=np.array(child.SetModelData['All_sigma'])
                    All_epsilon_=np.array(child.SetModelData['All_epsilon'])
                    All_mu_=np.array(child.SetModelData['All_mu'])
                    
                    sigma_[rec_zlim[0]:rec_zlim[1]+1,rec_xlim[0]:rec_xlim[1]+1]=sigma
                    epsilon_[rec_zlim[0]:rec_zlim[1]+1,rec_xlim[0]:rec_xlim[1]+1]=epsilon
                    mu_[rec_zlim[0]:rec_zlim[1]+1,rec_xlim[0]:rec_xlim[1]+1]=mu
                    All_sigma_[rec_zlim[0]:rec_zlim[1]+1,rec_xlim[0]:rec_xlim[1]+1]=sigma
                    All_epsilon_[rec_zlim[0]:rec_zlim[1]+1,rec_xlim[0]:rec_xlim[1]+1]=epsilon
                    All_mu_[rec_zlim[0]:rec_zlim[1]+1,rec_xlim[0]:rec_xlim[1]+1]=mu
                    child.SetModelData['AddRectangle']['sigma']=sigma_
                    child.SetModelData['AddRectangle']['epsilon']=epsilon_
                    child.SetModelData['AddRectangle']['mu']=mu_
                    child.SetModelData['AddRectangle']['Single_sigma']=sigma
                    child.SetModelData['AddRectangle']['Single_epsilon']=epsilon
                    child.SetModelData['AddRectangle']['Single_mu']=mu
                    child.SetModelData['All_sigma']=All_sigma_
                    child.SetModelData['All_epsilon']=All_epsilon_
                    child.SetModelData['All_mu']=All_mu_
                    
                    child.SetModelData['AddRectangle']['Left']=Left
                    child.SetModelData['AddRectangle']['Bottom']=Bottom
                    child.SetModelData['AddRectangle']['Width']=Width
                    child.SetModelData['AddRectangle']['High']=High
                    
                    root_headfile=QtWidgets.QTreeWidgetItem(self.treeView)
                    root_headfile.setText(0,'New Rectangle')
                    # left
                    self.TreeViewLeft=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewLeft.setText(0,'left')
                    self.TreeViewLeft.setText(1,str(child.SetModelData['AddRectangle']['Left']))
                    # Bottom
                    self.TreeViewBottom=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewBottom.setText(0,'bottom')
                    self.TreeViewBottom.setText(1,str(child.SetModelData['AddRectangle']['Bottom']))
                    # Width
                    self.TreeViewWidth=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewWidth.setText(0,'width')
                    self.TreeViewWidth.setText(1,str(child.SetModelData['AddRectangle']['Width']))
                    # High
                    self.TreeViewHigh=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewHigh.setText(0,'high')
                    self.TreeViewHigh.setText(1,str(child.SetModelData['AddRectangle']['High']))
                    # Conductivity
                    self.TreeViewRecConductivity=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewRecConductivity.setText(0,'Conductivity')
                    self.TreeViewRecConductivity.setText(1,'%1.2e'%child.SetModelData['AddRectangle']['Single_sigma'])
                    # Dielectric Constant
                    self.TreeViewRecDielectricConstant=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewRecDielectricConstant.setText(0,'DielectricConstant')
                    self.TreeViewRecDielectricConstant.setText(1,'%1.2e'%child.SetModelData['AddRectangle']['Single_epsilon'])
                    # Magnetic Permeability
                    self.TreeViewRecMagneticPermeability=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewRecMagneticPermeability.setText(0,'Magnetic Permeability')
                    self.TreeViewRecMagneticPermeability.setText(1,'%1.2e'%child.SetModelData['AddRectangle']['Single_mu'])
                    self.treeView.expandAll()

    def GetUiNewModel(self):
        NewModel=UiNewModel.Ui_NewModel(self)
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            try:
                child=window.widget()
                if child is self.mdiArea.activeSubWindow().widget():
                    break
            except:
                pass
                    
        NewModel.show()
        if NewModel.exec_() == NewModel.Accepted:
            if (NewModel.lineEdit_dx.text()=='') or (NewModel.lineEdit_dz.text()=='') or \
            (NewModel.lineEdit_dt.text()=='') or (NewModel.lineEdit_SimulationTime.text()=='') or \
            (not isinstance(eval(NewModel.lineEdit_SourceStart.text()),tuple)) or \
            (not isinstance(eval(NewModel.lineEdit_ReceiverStart.text()),tuple)) or \
            (NewModel.lineEdit_Step.text()=='') or (NewModel.lineEdit_Scan.text()=='') or \
            (NewModel.lineEdit_Conductivity.text()=='') or (NewModel.lineEdit_Conductivity.text()=='') or \
            (NewModel.lineEdit_MagneticPermeability.text()=='') or (NewModel.lineEdit_Frequency.text()==''):
                QtWidgets.QMessageBox.warning(self,"Warning","Wrong data,Please try again !!!",QtWidgets.QMessageBox.Yes)
            else:   
                self.treeView.clear()
                child.SetModelData['NewModel']=dict()
                SourceStart=eval(NewModel.lineEdit_SourceStart.text())
                ReceiverStart=eval(NewModel.lineEdit_ReceiverStart.text())
                Step=float(NewModel.lineEdit_Step.text())
                Scan=int(NewModel.lineEdit_Scan.text())
                if SourceStart[0]+Step*Scan>=NewModel.doubleSpinBox_xRange.value():
                    QtWidgets.QMessageBox.warning(self,"Warning","Out of bounds,Please try again !!!",QtWidgets.QMessageBox.Yes)
                else:
                    child.SetModelData['NewModel']['xlim']=NewModel.doubleSpinBox_xRange.value()
                    child.SetModelData['NewModel']['zlim']=NewModel.doubleSpinBox_zRange.value()
                    child.SetModelData['NewModel']['dx']=float(NewModel.lineEdit_dx.text())
                    child.SetModelData['NewModel']['dz']=float(NewModel.lineEdit_dz.text())
                    child.SetModelData['NewModel']['dt']=eval(NewModel.lineEdit_dt.text())
                    child.SetModelData['NewModel']['t']=eval(NewModel.lineEdit_SimulationTime.text())
                    child.SetModelData['NewModel']['k_max']=int(np.round(child.SetModelData['NewModel']['t']/child.SetModelData['NewModel']['dt'])+1)
                    child.SetModelData['NewModel']['xl']=int(np.round(child.SetModelData['NewModel']['xlim']/child.SetModelData['NewModel']['dx'])+1)
                    child.SetModelData['NewModel']['zl']=int(np.round(child.SetModelData['NewModel']['zlim']/child.SetModelData['NewModel']['dz'])+1)    
                    child.SetModelData['NewModel']['Freq']=eval(NewModel.lineEdit_Frequency.text())

                    Source_z_idx=[int(round((SourceStart[0]+Step*i)/child.SetModelData['NewModel']['dx'])+10) for i in range(Scan)]
                    Source_x_idx=[int(round(SourceStart[1]/child.SetModelData['NewModel']['dz'])+10) for i in range(Scan)]
                    Source_x=[SourceStart[0]+Step*i for i in range(Scan)]
                    Source_z=[SourceStart[1] for i in range(Scan)]
                    child.SetModelData['NewModel']['SourcePosition_idx']=list(zip(Source_x_idx,Source_z_idx))
                    child.SetModelData['NewModel']['SourcePosition']=list(zip(Source_x,Source_z))
                    Receiver_x=[ReceiverStart[0]+Step*i for i in range(Scan)]
                    Receiver_z=[ReceiverStart[1] for i in range(Scan)]
                    Receiver_z_idx=[int(round((ReceiverStart[0]+Step*i)/child.SetModelData['NewModel']['dx'])+10) for i in range(Scan)]
                    Receiver_x_idx=[int(round(ReceiverStart[1]/child.SetModelData['NewModel']['dx'])+10) for i in range(Scan)]
                    child.SetModelData['NewModel']['ReceiverPosition_idx']=list(zip(Receiver_x_idx,Receiver_z_idx))
                    child.SetModelData['NewModel']['ReceiverPosition']=list(zip(Receiver_x,Receiver_z))
                    data_=np.ones((child.SetModelData['NewModel']['xl'],child.SetModelData['NewModel']['zl']))
                    child.SetModelData['NewModel']['Single_sigma']=eval(NewModel.lineEdit_Conductivity.text())
                    child.SetModelData['NewModel']['sigma']=child.SetModelData['NewModel']['Single_sigma']*data_
                    child.SetModelData['NewModel']['Single_epsilon']=NewModel.doubleSpinBox_DielectricConstant.value()
                    child.SetModelData['NewModel']['epsilon']=child.SetModelData['NewModel']['Single_epsilon']*data_
                    child.SetModelData['NewModel']['Single_mu']=eval(NewModel.lineEdit_MagneticPermeability.text())
                    child.SetModelData['NewModel']['mu']=child.SetModelData['NewModel']['Single_mu']*data_
                    child.SetModelData['All_sigma']=child.SetModelData['NewModel']['Single_sigma']*data_
                    child.SetModelData['All_epsilon']=child.SetModelData['NewModel']['Single_epsilon']*data_
                    child.SetModelData['All_mu']=child.SetModelData['NewModel']['Single_mu']*data_
                    
                    
                    root_headfile=QtWidgets.QTreeWidgetItem(self.treeView)
                    root_headfile.setText(0,'Model Parameters')
                    # x lim
                    self.TreeViewXlim=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewXlim.setText(0,'x limit')
                    self.TreeViewXlim.setText(1,str(child.SetModelData['NewModel']['xlim']))
                    # z lim
                    self.TreeViewZlim=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewZlim.setText(0,'z limit')
                    self.TreeViewZlim.setText(1,str(child.SetModelData['NewModel']['zlim']))
                    # dx
                    self.TreeViewDx=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewDx.setText(0,'dx')
                    self.TreeViewDx.setText(1,str(child.SetModelData['NewModel']['dx']))
                    # dz
                    self.TreeViewDz=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewDz.setText(0,'dz')
                    self.TreeViewDz.setText(1,str(child.SetModelData['NewModel']['dz']))
                    # dt
                    self.TreeViewDt=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewDt.setText(0,'dt')
                    self.TreeViewDt.setText(1,'%1.2e'%child.SetModelData['NewModel']['dt'])
                    # Simulation Time
                    self.TreeViewSimulationTime=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewSimulationTime.setText(0,'Simulation Time')
                    self.TreeViewSimulationTime.setText(1,'%1.2e'%child.SetModelData['NewModel']['t'])
                    # Freq
                    self.TreeViewFreq=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewFreq.setText(0,'Frequency')
                    self.TreeViewFreq.setText(1,'%1.2e'%child.SetModelData['NewModel']['Freq'])
                    # Conductivity
                    self.TreeViewConductivity=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewConductivity.setText(0,'Conductivity')
                    self.TreeViewConductivity.setText(1,'%1.2e'%child.SetModelData['NewModel']['Single_sigma'])
                    # Dielectric Constant
                    self.TreeViewDielectricConstant=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewDielectricConstant.setText(0,'DielectricConstant')
                    self.TreeViewDielectricConstant.setText(1,'%1.2e'%child.SetModelData['NewModel']['Single_epsilon'])
                    # Magnetic Permeability
                    self.TreeViewMagneticPermeability=QtWidgets.QTreeWidgetItem(root_headfile)
                    self.TreeViewMagneticPermeability.setText(0,'Magnetic Permeability')
                    self.TreeViewMagneticPermeability.setText(1,'%1.2e'%child.SetModelData['NewModel']['Single_mu'])
                    
                    self.treeView.expandAll()
                    
                    self.actionRectangle.setEnabled(True)
                    self.actionEllipse.setEnabled(True)
                    self.actionPolygon.setEnabled(True)
                    self.ToolActionRectangle.setEnabled(True)
                    self.ToolActionEllipse.setEnabled(True)
                    self.ToolActionPolygon.setEnabled(True)
                    self.ToolActionModelling.setEnabled(True)
                    self.toolButtonCreate.setEnabled(True)
                    self.toolButtonClear.setEnabled(True)
                    self.CreateSigma.setEnabled(True)
                    self.CreateEpsilon.setEnabled(True)
                    self.CreateMu.setEnabled(True)
    
    def PlotModel(self,text,MainWindow):
        activeSubWindow=self.mdiArea.activeSubWindow()
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            try:
                child=window.widget()
                if child is self.mdiArea.activeSubWindow().widget():
                    break
            except:
                pass
        if 'All_sigma' in child.SetModelData.keys():
            if text=='sigma':
                self.RecentFigureCanvas=PlotCanvas(self,MainWindow,data=child.SetModelData['All_sigma'],params=child.SetModelData['NewModel'],width=15, height=8)
            elif text=='epsilon':
                self.RecentFigureCanvas=PlotCanvas(self,MainWindow,data=child.SetModelData['All_epsilon'],params=child.SetModelData['NewModel'],width=15, height=8)
            elif text=='mu':
                self.RecentFigureCanvas=PlotCanvas(self,MainWindow,data=child.SetModelData['All_mu'],params=child.SetModelData['NewModel'],width=15, height=8)
            else:
                self.RecentFigureCanvas=PlotCanvas(self,MainWindow,data=None,params=child.SetModelData['NewModel'],width=15, height=8)
            activeSubWindow.widget().setWidget(self.RecentFigureCanvas)
        
        if text=='Profile':
            TimeMax=child.SetModelData['NewModel']['dt']*(child.SetModelData['NewModel']['k_max']-1)
            xLabel=[]
            x_label=[indx[1] for indx in child.SetModelData['NewModel']['SourcePosition_idx']]
            xLabel.append((np.min(x_label)-10)*child.SetModelData['NewModel']['dx'])
            xLabel.append((np.max(x_label)-10)*child.SetModelData['NewModel']['dx'])
            extent=(0,1,0,1)
            activeSubWindow.widget().widget().PlotProfile(self.data[text])
            activeSubWindow.widget().widget().setProfileLabelAndTick(TimeMax,xLabel)
            self.toolButtonColorMap.setEnabled(True)
            self.menuView.setEnabled(True)
            
        else:
            xtick=child.SetModelData['NewModel']['xlim']
            ztick=child.SetModelData['NewModel']['zlim']
            extent=(0,ztick,xtick,0)
            activeSubWindow.widget().widget().PlotModel(extent)
            activeSubWindow.widget().widget().PlotParams()
            activeSubWindow.widget().widget().setTimeLabelAndTick()
            self.toolButtonColorMap.setEnabled(True)
            self.menuView.setEnabled(True)
        
        
    def Modelling2D(self,MainWindow):
        windows=self.mdiArea.subWindowList()
        for i,window in enumerate(windows):
            try:
                child=window.widget()
                if child is self.mdiArea.activeSubWindow().widget():
                    break
            except:
                pass
        if 'All_sigma' in child.SetModelData.keys():
            data=child.SetModelData
        print(data)
        self.Thread=ThreadModelling2D(data,MainWindow)
        self.Thread.started.connect(self.StartProgress)
        self.Thread.start()
        self.Thread.finished.connect(self.EndProgress)
    
    def StartProgress(self):
        self.Progress=Actions()
    
    def EndProgress(self):
        self.Progress.close()
        # self.data['Ey_data']=self.Thread.Ey_data
        self.data['Profile']=self.Thread.Profile
        self.CreateProfile.setEnabled(True)
        self.EndModellingSignal.emit()
            
class ThreadModelling2D(QtCore.QThread):
    # ModellingSignal=QtCore.pyqtSignal()
    def __init__(self,data,parent=None):
        super(ThreadModelling2D,self).__init__(parent)
        self.data_dict=data
        self.Profile=[]
        
    def run(self):
        if self.data_dict:
            # ModellingSignal.emit()
            # print(self.data_dict['NewModel']['xlim'])
            # print(self.data_dict['NewModel']['zlim'])
            # print(self.data_dict['NewModel']['xl'])
            # print(self.data_dict['NewModel']['zl'])
            # print(self.data_dict['NewModel']['dx'])
            # print(self.data_dict['NewModel']['dz'])
            # print(self.data_dict['NewModel']['dt'])
            # print(self.data_dict['NewModel']['k_max'])
            # print(self.data_dict['NewModel']['Freq'])
            # print(self.data_dict['All_epsilon'].shape)
            # print(self.data_dict['All_sigma'].shape)
            # print(self.data_dict['All_mu'].shape)
            # print(self.data_dict['NewModel']['SourcePosition_idx'])
            # print(self.data_dict['NewModel']['ReceiverPosition_idx'])
            self.Profile=Forward2D.Forward_2D(self.data_dict)  
            # print(self.Profile.shape)

class Actions(QtWidgets.QDialog):
    """
    Simple dialog that consists of a Progress Bar and a Button.
    Clicking on the button results in the start of a timer and
    updates the progress bar.
    """
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Progress Bar')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 30)
        self.progress.setMaximum(0)
        self.progress.setTextVisible(False)
        self.progress.setInvertedAppearance(True)
        self.show()        

class PlotCanvas(FigureCanvas):
    def __init__(self,MainWindow,parent=None,data=None,params=None,width=15,height=6,dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.data=data
        self.params=params
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.MainWindow=MainWindow
        
    def PlotParams(self):
        SourcePosition=self.params['SourcePosition']
        # print(SourcePosition)
        ReceiverPosition=self.params['ReceiverPosition']
        # print(ReceiverPosition)
        for idx in range(len(SourcePosition)):
            self.axes.plot(SourcePosition[idx][0],SourcePosition[idx][1],'rd')
        for idx in range(len(ReceiverPosition)):
            self.axes.plot(ReceiverPosition[idx][0],ReceiverPosition[idx][1],'k.')
    
    def PlotProfile(self,profile):
        self.fig.clear()
        self.axes = self.fig.add_subplot(111)
        self.fig_=self.axes.imshow(profile,vmin=0.1*np.min(profile),vmax=0.1*np.max(profile),extent=(0,1,0,1))
        # self.axes.set_aspect(1)
        # self.axes.set_xlabel('Scan')
        # self.axes.set_ylabel('Sample')
        self.draw()
        # self.fig.canvas.mpl_connect('motion_notify_event', self.motion_call_back)
        # self.fig.canvas.mpl_connect('button_press_event', self.press_call_back)
        # self.MainWindow.dockWidgetDisplayGraphInfo.setEnabled(True)
        
    def ChangeAspect(self,aspect):
        self.axes.set_aspect(1/aspect)
        self.draw()
        
    def PlotModel(self,extent):
        self.fig.clear()
        self.axes = self.fig.add_subplot(111)
        print(self.data.shape)
        self.fig_=self.axes.imshow(self.data,vmin=np.min(self.data),vmax=np.max(self.data),extent=extent)
        self.axes.set_aspect(1)
        # self.axes.set_xlabel('Scan')
        # self.axes.set_ylabel('Sample')
        self.draw()
        # self.fig.canvas.mpl_connect('motion_notify_event', self.motion_call_back)
        # self.fig.canvas.mpl_connect('button_press_event', self.press_call_back)
        # self.MainWindow.dockWidgetDisplayGraphInfo.setEnabled(True)
        
    def setProfileLabelAndTick(self,TimeLabel,PositionLabel):
        # print(TimeLabel)
        # print(PositionLabel)
        d_=np.linspace(0,TimeLabel,5)
        d_=np.flip(d_,0)
        self.axes.set_yticks(np.linspace(0,1,5))
        self.axes.set_yticklabels(d_)
        d_=np.linspace(PositionLabel[0],PositionLabel[1],5)
        self.axes.set_xticks(np.linspace(0,1,5))
        self.axes.set_xticklabels(d_)
        self.axes.set_xlabel('Scam (m)')
        self.axes.set_ylabel('Time (s)')
        
    def setTimeLabelAndTick(self):
        self.axes.set_xlabel('Scam (m)')
        self.axes.set_ylabel('Depth (m)')
    
    def ChangeCmap(self,cmap):
        eval('self.fig_.set_cmap(%s)'%cmap)
        self.draw()
        
class MdiChild(QtWidgets.QScrollArea):
    sequenceNumber=0
    FileNumber=0
    def __init__(self,MainWindow):
        super(MdiChild, self).__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.isUntitled=True
        self.MainWindow=MainWindow
        self.SetModelData=dict()
        
    def NewFile(self):
        self.filename="Untitle%s"%MdiChild.sequenceNumber+"[*]"
        MdiChild.sequenceNumber+=1
        MdiChild.FileNumber+=1
        self.setWindowTitle(self.filename)
    
    def OpenFile(self,filename):
        self.filename=filename+"[*]"
        MdiChild.sequenceNumber+=1
        MdiChild.FileNumber+=1
        self.setWindowTitle(self.filename)
        
class MainForm(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    try:
        app
    except:
        app=QtWidgets.QApplication(sys.argv)
    ex = MainForm()
    ex.showMaximized()
    ex.show()
    sys.exit(app.exec_())
