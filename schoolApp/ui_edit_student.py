# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_student.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edit_student(object):
    def setupUi(self, edit_student):
        edit_student.setObjectName("edit_student")
        edit_student.resize(486, 498)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(edit_student)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(edit_student)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(edit_student)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_personalData = QtWidgets.QWidget()
        self.tab_personalData.setObjectName("tab_personalData")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_personalData)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 19, 451, 358))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.name.setFont(font)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.sddress = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.sddress.setFont(font)
        self.sddress.setAlignment(QtCore.Qt.AlignCenter)
        self.sddress.setObjectName("sddress")
        self.verticalLayout.addWidget(self.sddress)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.birth = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.birth.setFont(font)
        self.birth.setAlignment(QtCore.Qt.AlignCenter)
        self.birth.setObjectName("birth")
        self.verticalLayout.addWidget(self.birth)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.super_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.super_2.setFont(font)
        self.super_2.setAlignment(QtCore.Qt.AlignCenter)
        self.super_2.setObjectName("super_2")
        self.verticalLayout.addWidget(self.super_2)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.superWork = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.superWork.setFont(font)
        self.superWork.setAlignment(QtCore.Qt.AlignCenter)
        self.superWork.setObjectName("superWork")
        self.verticalLayout.addWidget(self.superWork)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.superTel = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.superTel.setFont(font)
        self.superTel.setAlignment(QtCore.Qt.AlignCenter)
        self.superTel.setObjectName("superTel")
        self.verticalLayout.addWidget(self.superTel)
        self.tabWidget.addTab(self.tab_personalData, "")
        self.tab_school_data = QtWidgets.QWidget()
        self.tab_school_data.setObjectName("tab_school_data")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_school_data)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 451, 271))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.baseSchool = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.baseSchool.setFont(font)
        self.baseSchool.setAlignment(QtCore.Qt.AlignCenter)
        self.baseSchool.setObjectName("baseSchool")
        self.verticalLayout_2.addWidget(self.baseSchool)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.score = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.score.setFont(font)
        self.score.setAlignment(QtCore.Qt.AlignCenter)
        self.score.setObjectName("score")
        self.verticalLayout_2.addWidget(self.score)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.classCombobox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.classCombobox.setFont(font)
        self.classCombobox.setObjectName("classCombobox")
        self.verticalLayout_2.addWidget(self.classCombobox)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.payment = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.payment.setFont(font)
        self.payment.setAlignment(QtCore.Qt.AlignCenter)
        self.payment.setObjectName("payment")
        self.verticalLayout_2.addWidget(self.payment)
        self.tabWidget.addTab(self.tab_school_data, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.pushButton = QtWidgets.QPushButton(edit_student)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)

        self.retranslateUi(edit_student)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(edit_student)

    def retranslateUi(self, edit_student):
        _translate = QtCore.QCoreApplication.translate
        edit_student.setWindowTitle(_translate("edit_student", "Form"))
        self.label.setText(_translate("edit_student", "تعديل بيانات الطالب "))
        self.label_2.setText(_translate("edit_student", "الاسم : "))
        self.label_3.setText(_translate("edit_student", "العنوان : "))
        self.label_4.setText(_translate("edit_student", "تاريخ الميلاد : "))
        self.label_5.setText(_translate("edit_student", "اسم ولي الامر : "))
        self.label_6.setText(_translate("edit_student", "عمل ولي الامر : "))
        self.label_7.setText(_translate("edit_student", "هاتف ولي الامر : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_personalData), _translate("edit_student", "البيانات الشخصية"))
        self.label_8.setText(_translate("edit_student", "مدرسة الاساس : "))
        self.label_9.setText(_translate("edit_student", "المجموع : "))
        self.label_10.setText(_translate("edit_student", "الصف : "))
        self.label_11.setText(_translate("edit_student", "الرسوم الدراسية : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_school_data), _translate("edit_student", "البيانات المدرسية"))
        self.pushButton.setText(_translate("edit_student", "حفظ"))