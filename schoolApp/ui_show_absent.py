# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_absent.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_showAbsent(object):
    def setupUi(self, showAbsent):
        showAbsent.setObjectName("showAbsent")
        showAbsent.resize(404, 585)
        showAbsent.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(showAbsent)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(showAbsent)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.list = QtWidgets.QListWidget(showAbsent)
        self.list.setObjectName("list")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list.setFont(font)
        self.verticalLayout.addWidget(self.list)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add = QtWidgets.QPushButton(showAbsent)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.verticalLayout_3.addWidget(self.add)
        self.edit = QtWidgets.QPushButton(showAbsent)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit.setFont(font)
        self.edit.setObjectName("edit")
        self.verticalLayout_3.addWidget(self.edit)
        self.del1 = QtWidgets.QPushButton(showAbsent)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.del1.setFont(font)
        self.del1.setObjectName("del1")
        self.verticalLayout_3.addWidget(self.del1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(showAbsent)
        QtCore.QMetaObject.connectSlotsByName(showAbsent)

    def retranslateUi(self, showAbsent):
        _translate = QtCore.QCoreApplication.translate
        showAbsent.setWindowTitle(_translate("showAbsent", "Form"))
        self.label.setText(_translate("showAbsent", "TextLabel"))
        self.add.setText(_translate("showAbsent", "??????????"))
        self.edit.setText(_translate("showAbsent", "??????????"))
        self.del1.setText(_translate("showAbsent", "??????"))
