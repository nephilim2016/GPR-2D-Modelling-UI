# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_text.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1139, 852)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/UI_Ico/GPR.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.mdiArea = QtWidgets.QMdiArea(self.frame_3)
        self.mdiArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.TabbedView)
        self.mdiArea.setDocumentMode(True)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)
        self.mdiArea.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.mdiArea.setTabPosition(QtWidgets.QTabWidget.North)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout_6.addWidget(self.mdiArea, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1139, 19))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuData_Process = QtWidgets.QMenu(self.menubar)
        self.menuData_Process.setObjectName("menuData_Process")
        self.menuForward_2D_F = QtWidgets.QMenu(self.menubar)
        self.menuForward_2D_F.setObjectName("menuForward_2D_F")
        self.menuInversion_2D_I = QtWidgets.QMenu(self.menubar)
        self.menuInversion_2D_I.setObjectName("menuInversion_2D_I")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget_7 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_7.setEnabled(True)
        self.dockWidget_7.setObjectName("dockWidget_7")
        self.dockWidgetContents_8 = QtWidgets.QWidget()
        self.dockWidgetContents_8.setObjectName("dockWidgetContents_8")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_8)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.dockWidgetContents_8)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.frame = QtWidgets.QFrame(self.dockWidgetContents_8)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setObjectName("toolButton_3")
        self.verticalLayout_5.addWidget(self.toolButton_3)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout_2.addWidget(self.toolButton)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.toolButton_6 = QtWidgets.QToolButton(self.frame)
        self.toolButton_6.setObjectName("toolButton_6")
        self.verticalLayout_7.addWidget(self.toolButton_6)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 3, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.verticalLayout_3.addWidget(self.toolButton_2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.toolButton_4 = QtWidgets.QToolButton(self.frame)
        self.toolButton_4.setObjectName("toolButton_4")
        self.verticalLayout_6.addWidget(self.toolButton_4)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 2, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.toolButton_5 = QtWidgets.QToolButton(self.frame)
        self.toolButton_5.setWhatsThis("")
        self.toolButton_5.setObjectName("toolButton_5")
        self.verticalLayout_4.addWidget(self.toolButton_5)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 3, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 4, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.label_5 = QtWidgets.QLabel(self.dockWidgetContents_8)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.frame_2 = QtWidgets.QFrame(self.dockWidgetContents_8)
        self.frame_2.setEnabled(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 41, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 10, 41, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(70, 40, 59, 14))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(0, 40, 59, 14))
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 20)
        self.dockWidget_7.setWidget(self.dockWidgetContents_8)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_7)
        self.dockWidget_5 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_5.setObjectName("dockWidget_5")
        self.dockWidgetContents_5 = QtWidgets.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents_5)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents_5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1119, 192))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_5.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 1, 1, 1)
        self.dockWidget_5.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_5)
        self.dockWidget_6 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_6.setObjectName("dockWidget_6")
        self.dockWidgetContents_6 = QtWidgets.QWidget()
        self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dockWidgetContents_6)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.dockWidgetContents_6)
        self.treeWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.treeWidget.setMidLineWidth(0)
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.treeWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.treeWidget.setAutoExpandDelay(20)
        self.treeWidget.setIndentation(6)
        self.treeWidget.setExpandsOnDoubleClick(False)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setMinimumSectionSize(39)
        self.gridLayout_4.addWidget(self.treeWidget, 0, 1, 1, 1)
        self.dockWidget_6.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_6)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRecent_File = QtWidgets.QAction(MainWindow)
        self.actionRecent_File.setEnabled(False)
        self.actionRecent_File.setObjectName("actionRecent_File")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionPrint_Preview = QtWidgets.QAction(MainWindow)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrint_Setting = QtWidgets.QAction(MainWindow)
        self.actionPrint_Setting.setObjectName("actionPrint_Setting")
        self.actionExit_CSU_GPR = QtWidgets.QAction(MainWindow)
        self.actionExit_CSU_GPR.setObjectName("actionExit_CSU_GPR")
        self.ToolActionOpenFile = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../.designer/backup/open.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionOpenFile.setIcon(icon1)
        self.ToolActionOpenFile.setObjectName("ToolActionOpenFile")
        self.ToolActionNewFile = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../.designer/backup/new.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionNewFile.setIcon(icon2)
        self.ToolActionNewFile.setObjectName("ToolActionNewFile")
        self.ToolActionSave = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../.designer/backup/save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionSave.setIcon(icon3)
        self.ToolActionSave.setObjectName("ToolActionSave")
        self.ToolActionSaveAs = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../.designer/backup/save as.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionSaveAs.setIcon(icon4)
        self.ToolActionSaveAs.setObjectName("ToolActionSaveAs")
        self.ToolActionPrintPreview = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../.designer/backup/print preview.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionPrintPreview.setIcon(icon5)
        self.ToolActionPrintPreview.setObjectName("ToolActionPrintPreview")
        self.ToolActionPrint = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../.designer/backup/print.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionPrint.setIcon(icon6)
        self.ToolActionPrint.setObjectName("ToolActionPrint")
        self.ToolActionHelp = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../.designer/backup/help.icns"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionHelp.setIcon(icon7)
        self.ToolActionHelp.setObjectName("ToolActionHelp")
        self.actionHelp_Files = QtWidgets.QAction(MainWindow)
        self.actionHelp_Files.setObjectName("actionHelp_Files")
        self.actionContants = QtWidgets.QAction(MainWindow)
        self.actionContants.setObjectName("actionContants")
        self.ToolActionProcess = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../../.designer/backup/process.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionProcess.setIcon(icon8)
        self.ToolActionProcess.setObjectName("ToolActionProcess")
        self.ToolActionForward = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../../.designer/backup/forward.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionForward.setIcon(icon9)
        self.ToolActionForward.setObjectName("ToolActionForward")
        self.ToolActionInversion = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../../.designer/backup/inversion.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolActionInversion.setIcon(icon10)
        self.ToolActionInversion.setObjectName("ToolActionInversion")
        self.menuFIle.addAction(self.actionNew)
        self.menuFIle.addAction(self.actionOpen)
        self.menuFIle.addAction(self.actionRecent_File)
        self.menuFIle.addAction(self.actionClose)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionSave)
        self.menuFIle.addAction(self.actionSave_as)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionPrint_Preview)
        self.menuFIle.addAction(self.actionPrint)
        self.menuFIle.addAction(self.actionPrint_Setting)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionExit_CSU_GPR)
        self.menuHelp.addAction(self.actionHelp_Files)
        self.menuHelp.addAction(self.actionContants)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuData_Process.menuAction())
        self.menubar.addAction(self.menuForward_2D_F.menuAction())
        self.menubar.addAction(self.menuInversion_2D_I.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.ToolActionNewFile)
        self.toolBar.addAction(self.ToolActionOpenFile)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ToolActionSave)
        self.toolBar.addAction(self.ToolActionSaveAs)
        self.toolBar.addAction(self.ToolActionPrintPreview)
        self.toolBar.addAction(self.ToolActionPrint)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ToolActionProcess)
        self.toolBar.addAction(self.ToolActionForward)
        self.toolBar.addAction(self.ToolActionInversion)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ToolActionHelp)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "sadfasfsadf"))
        self.menuFIle.setTitle(_translate("MainWindow", "&File"))
        self.menuEdit.setTitle(_translate("MainWindow", " &Edit"))
        self.menuData_Process.setTitle(_translate("MainWindow", "&Data Process"))
        self.menuForward_2D_F.setTitle(_translate("MainWindow", "&GPR Forward 2D"))
        self.menuInversion_2D_I.setTitle(_translate("MainWindow", "&Inversion 2D"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.toolButton_6.setText(_translate("MainWindow", "..."))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.toolButton_5.setToolTip(_translate("MainWindow", "asfsdf"))
        self.toolButton_5.setStatusTip(_translate("MainWindow", "fasfsd"))
        self.toolButton_5.setText(_translate("MainWindow", "..."))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfgdfg</p></body></html>"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "1"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "2"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "1"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "asd"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "11asd"))
        self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("MainWindow", "sdaf"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "12asd"))
        self.treeWidget.topLevelItem(0).child(1).setText(1, _translate("MainWindow", "asdf"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "13asd"))
        self.treeWidget.topLevelItem(0).child(2).setText(1, _translate("MainWindow", "asdf"))
        self.treeWidget.topLevelItem(0).child(2).child(0).setText(0, _translate("MainWindow", "131asd"))
        self.treeWidget.topLevelItem(0).child(2).child(0).setText(1, _translate("MainWindow", "asdf"))
        self.treeWidget.topLevelItem(0).child(2).child(0).child(0).setText(0, _translate("MainWindow", "1311asd"))
        self.treeWidget.topLevelItem(0).child(2).child(0).child(0).setText(1, _translate("MainWindow", "asf"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "2"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "3"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open ..."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionRecent_File.setText(_translate("MainWindow", "Recent File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
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
        self.ToolActionProcess.setText(_translate("MainWindow", "Process"))
        self.ToolActionProcess.setToolTip(_translate("MainWindow", "<html><head/><body><p>Process</p></body></html>"))
        self.ToolActionForward.setText(_translate("MainWindow", "Forward"))
        self.ToolActionForward.setToolTip(_translate("MainWindow", "<html><head/><body><p>Forward</p></body></html>"))
        self.ToolActionInversion.setText(_translate("MainWindow", "Inversion"))
        self.ToolActionInversion.setToolTip(_translate("MainWindow", "<html><head/><body><p>Inversion</p></body></html>"))

