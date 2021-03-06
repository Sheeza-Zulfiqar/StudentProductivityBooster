# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(695, 523)
        LoginForm.setStyleSheet("background-color: rgb(144, 255, 246);")
        self.centralwidget = QtWidgets.QWidget(LoginForm)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 40, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(28, 206, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.le_email = QtWidgets.QLineEdit(self.centralwidget)
        self.le_email.setGeometry(QtCore.QRect(340, 150, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_email.setFont(font)
        self.le_email.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_email.setObjectName("le_email")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.le_password = QtWidgets.QLineEdit(self.centralwidget)
        self.le_password.setGeometry(QtCore.QRect(340, 220, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_password.setFont(font)
        self.le_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_password.setObjectName("le_password")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(270, 320, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("background-color: rgb(28, 206, 255);")
        self.btn_login.setObjectName("btn_login")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(156, 390, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cmdbtn_register = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.cmdbtn_register.setGeometry(QtCore.QRect(340, 390, 185, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.cmdbtn_register.setFont(font)
        self.cmdbtn_register.setObjectName("cmdbtn_register")
        LoginForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 695, 21))
        self.menubar.setObjectName("menubar")
        LoginForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginForm)
        self.statusbar.setObjectName("statusbar")
        LoginForm.setStatusBar(self.statusbar)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "MainWindow"))
        self.label.setText(_translate("LoginForm", "Configuration"))
        self.label_4.setText(_translate("LoginForm", "Email"))
        self.label_5.setText(_translate("LoginForm", "Password"))
        self.btn_login.setText(_translate("LoginForm", "Login"))
        self.label_2.setText(_translate("LoginForm", "Register as New Student"))
        self.cmdbtn_register.setText(_translate("LoginForm", "Register"))
