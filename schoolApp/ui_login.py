# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(460, 244)
        font = QtGui.QFont()
        font.setPointSize(14)
        login.setFont(font)
        login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(login)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(login)
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(190, 80, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.userEdit = QtWidgets.QLineEdit(self.groupBox)
        self.userEdit.setGeometry(QtCore.QRect(30, 30, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.userEdit.setFont(font)
        self.userEdit.setObjectName("userEdit")
        self.passEdit = QtWidgets.QLineEdit(self.groupBox)
        self.passEdit.setGeometry(QtCore.QRect(30, 80, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.passEdit.setFont(font)
        self.passEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passEdit.setObjectName("passEdit")
        self.loginBtn = QtWidgets.QPushButton(self.groupBox)
        self.loginBtn.setGeometry(QtCore.QRect(130, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.loginBtn.setFont(font)
        self.loginBtn.setObjectName("loginBtn")
        self.loginTryLable = QtWidgets.QLabel(self.groupBox)
        self.loginTryLable.setGeometry(QtCore.QRect(20, 120, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loginTryLable.setFont(font)
        self.loginTryLable.setStyleSheet("color: rgb(255, 0, 0);")
        self.loginTryLable.setText("")
        self.loginTryLable.setObjectName("loginTryLable")
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "?????????? ???????????? "))
        self.label_2.setText(_translate("login", "?????? ???????????????? : "))
        self.label_3.setText(_translate("login", "???????? ???????????? : "))
        self.loginBtn.setText(_translate("login", "????????"))
