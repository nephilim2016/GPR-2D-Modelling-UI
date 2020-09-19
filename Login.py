from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
import MainFile
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import hashlib
import time
import datetime
import os
import base64

class Ui_MainWindow(object):

    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setWindowIcon(QIcon('./Login_Ico/login.ico'))
        self.setupUi(self)
        self.retranslateUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500,250)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        MainWindow.setStyleSheet("#MainWindow{border-image:url(./Login_Ico/background.jpg);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(40, 12, 40, 12)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(18)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelAccount = QtWidgets.QLabel(self.widget)
        self.labelAccount.setObjectName("labelAccount")
        self.horizontalLayout_2.addWidget(self.labelAccount)
        self.lineEditAccount = QtWidgets.QLineEdit(self.widget)
        self.lineEditAccount.setObjectName("lineEditAccount")
        self.horizontalLayout_2.addWidget(self.lineEditAccount)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelPassword = QtWidgets.QLabel(self.widget)
        self.labelPassword.setObjectName("labelPassword")
        self.horizontalLayout_3.addWidget(self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(self.widget)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_3.addWidget(self.lineEditPassword)

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton_Ok = QtWidgets.QPushButton(self.widget)
        self.pushButton_Ok.setObjectName("pushButton_Ok")
        self.horizontalLayout_4.addWidget(self.pushButton_Ok)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton_Cancel = QtWidgets.QPushButton(self.widget)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.horizontalLayout_4.addWidget(self.pushButton_Cancel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage('Copyright@Central South University 2019')
        self.retranslateUi(MainWindow)
        
        self.pushButton_Ok.clicked.connect(self.CheckPassword)
        self.pushButton_Cancel.clicked.connect(self.CancelClose)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelAccount.setText(_translate("MainWindow", "Account"))
        self.labelPassword.setText(_translate("MainWindow", "Password"))
        self.pushButton_Ok.setText(_translate("MainWindow", "&Ok"))
        self.pushButton_Cancel.setText(_translate("MainWindow", "&Cancel"))
        
    def CheckPassword(self):
        login_user = self.lineEditAccount.text()
        login_password = self.lineEditPassword.text()
        AdminAccount='CSU'
        AdminPassword_PreEncode='Nephilim'
        AdminPassword=self._md5(AdminPassword_PreEncode)
        UserAccount=login_user
        Nowtime=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        UserPassword_PreEncoding=UserAccount+Nowtime
        UserPassword=self._md5GBK(UserPassword_PreEncoding)
        if login_user == AdminAccount and login_password == AdminPassword:
            with open('./CrackFile/log.csu','r') as f:
                results=f.readlines()
            try:
                result=results[-1]
            except IndexError:
                self._EmptyFileWrite()
            else:
                self._NotEmptyFileWrite(result)
            ui_MainWindow_GPR.show()
            ui_MainWindow_GPR.showMaximized()
            MainWindow.close()
        elif login_password==UserPassword:
            with open('./CrackFile/log.csu','r') as f:
                results=f.readlines()
            try:
                result=results[-1]
            except IndexError:
                self._EmptyFileWrite()
            else:
                self._NotEmptyFileWrite(result)
            ui_MainWindow_GPR.show()
            ui_MainWindow_GPR.showMaximized()
            MainWindow.close()
        else:
            QtWidgets.QMessageBox.warning(self,"Warning","Wrong account or wrong password,Please try again !!!",QtWidgets.QMessageBox.Yes)
            self.lineEditAccount.setFocus()
            
    def _EmptyFileWrite(self):
        StartDateString=datetime.datetime.strptime('2019-04-07','%Y-%m-%d')
        LastDateString=StartDateString.strftime('%Y-%m-%d')
            
        NowDate=datetime.datetime.now()
        NowDateString=NowDate.strftime('%Y-%m-%d')
                
        delta = datetime.timedelta(days=90)
        NextDate=NowDate+delta
        NextDateString=NextDate.strftime('%Y-%m-%d') 
        
        writecontent=LastDateString+NowDateString+NextDateString
        writecontentEncoding=base64Encoding(writecontent)
        with open('./CrackFile/log.csu', 'a') as f:
            f.write(writecontentEncoding+'\n')         
    def _NotEmptyFileWrite(self,result):
        resultDeconde=base64Decoding(result)
        LastDateString=resultDeconde[10:20]
        NowDate=datetime.datetime.now()
        NowDateString=NowDate.strftime('%Y-%m-%d')
        delta = datetime.timedelta(days=90)
        NextDate=NowDate+delta
        NextDateString=NextDate.strftime('%Y-%m-%d')
        writecontent=LastDateString+NowDateString+NextDateString
        writecontentEncoding=base64Encoding(writecontent)
        with open('./CrackFile/log.csu', 'a') as f:
            f.write(writecontentEncoding+'\n')         
            
    def _md5(self,str_):
        m = hashlib.md5()
        m.update(str_.encode("utf8"))
        return m.hexdigest()
 
    def _md5GBK(self,str_):
        m = hashlib.md5(str_.encode(encoding='gb2312'))
        return m.hexdigest()

    def CancelClose(self):
        self.close()
        
        
class MainForm(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()
        
    def center(self):
        screen=QtWidgets.QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

def base64Encoding(str_):
    bytesString = str_.encode(encoding="utf-8")
    encodestr = base64.b64encode(bytesString)
    encoderesult=encodestr.decode(encoding="utf-8")
    return encoderesult
def base64Decoding(encodestr):
    decodestr = base64.b64decode(encodestr)
    decodestrresult=decodestr.decode()
    return decodestrresult 
        
if __name__ == "__main__":
    import sys
    try:
        app
    except:                
        app=QtWidgets.QApplication(sys.argv)
        
    if os.path.exists('./CrackFile/log.csu'):
        with open('./CrackFile/log.csu','r') as f:
            results=f.readlines()
            try:
                result=results[-1]
            except IndexError:
                MainWindow=MainForm()
                ui_MainWindow_GPR = MainFile.MainForm()
                MainWindow.show()
                sys.exit(app.exec_())
            else:
                resultDeconde=base64Decoding(result)
                
                LastDateString=resultDeconde[10:20]
                LastDate=datetime.datetime.strptime(LastDateString,'%Y-%m-%d')
                
                NeedDateString=resultDeconde[20:None]
                NeedDate=datetime.datetime.strptime(NeedDateString,'%Y-%m-%d')
                
                NowDate=datetime.datetime.now()
                NowDateString=NowDate.strftime('%Y-%m-%d')
                delta = datetime.timedelta(days=90)
                
                if NowDate>=NeedDate:
                    MainWindow=MainForm()
                    ui_MainWindow_GPR = MainFile.MainForm()
                    MainWindow.show()
                    sys.exit(app.exec_())
                else:
                    ui_MainWindow_GPR = MainFile.MainForm()
                    ui_MainWindow_GPR.showMaximized()
                    ui_MainWindow_GPR.show()
                    sys.exit(app.exec_())
    else:
        with open('./CrackFile/log.csu','w+') as f:
            results=f.readlines()
            try:
                result=results[-1]
            except IndexError:
                MainWindow=MainForm()
                ui_MainWindow_GPR = MainFile.MainForm()
                MainWindow.show()
                sys.exit(app.exec_())
            else:
                resultDeconde=base64Decoding(result)
                
                LastDateString=resultDeconde[10:20]
                LastDate=datetime.datetime.strptime(LastDateString,'%Y-%m-%d')
                
                NeedDateString=resultDeconde[20:None]
                NeedDate=datetime.datetime.strptime(NeedDateString,'%Y-%m-%d')
                
                NowDate=datetime.datetime.now()
                NowDateString=NowDate.strftime('%Y-%m-%d')
                delta = datetime.timedelta(days=90)
                
                if NowDate>=NeedDate:
                    MainWindow=MainForm()
                    ui_MainWindow_GPR = MainFile.MainForm()
                    MainWindow.show()
                    sys.exit(app.exec_())
                else:
                    ui_MainWindow_GPR = MainFile.MainForm()
                    ui_MainWindow_GPR.showMaximized()
                    ui_MainWindow_GPR.show()
                    sys.exit(app.exec_())
        # print('ERROR')