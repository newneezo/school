# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_teacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edit_teacher(object):
    def setupUi(self, edit_teacher):
        edit_teacher.setObjectName("edit_teacher")
        edit_teacher.resize(378, 433)
        edit_teacher.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label = QtWidgets.QLabel(edit_teacher)
        self.label.setGeometry(QtCore.QRect(-50, 19, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(edit_teacher)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 70, 311, 308))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 20, 10, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name.setFont(font)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.address = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.address.setFont(font)
        self.address.setAlignment(QtCore.Qt.AlignCenter)
        self.address.setObjectName("address")
        self.verticalLayout.addWidget(self.address)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.tel = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tel.setFont(font)
        self.tel.setAlignment(QtCore.Qt.AlignCenter)
        self.tel.setObjectName("tel")
        self.verticalLayout.addWidget(self.tel)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.comboSubject = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboSubject.setFont(font)
        self.comboSubject.setObjectName("comboSubject")
        self.verticalLayout.addWidget(self.comboSubject)
        self.saveBtn = QtWidgets.QPushButton(edit_teacher)
        self.saveBtn.setGeometry(QtCore.QRect(160, 380, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.saveBtn.setFont(font)
        self.saveBtn.setObjectName("saveBtn")

        self.retranslateUi(edit_teacher)
        QtCore.QMetaObject.connectSlotsByName(edit_teacher)

    def retranslateUi(self, edit_teacher):
        _translate = QtCore.QCoreApplication.translate
        edit_teacher.setWindowTitle(_translate("edit_teacher", "Form"))
        self.label.setText(_translate("edit_teacher", "تعديل بيانات المعلم "))
        self.label_2.setText(_translate("edit_teacher", "الاسم : "))
        self.label_3.setText(_translate("edit_teacher", "العنوان : "))
        self.label_4.setText(_translate("edit_teacher", "رقم الهاتف : "))
        self.label_5.setText(_translate("edit_teacher", "المادة : "))
        self.saveBtn.setText(_translate("edit_teacher", "حفظ"))
