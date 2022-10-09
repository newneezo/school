from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from openpyxl import workbook, load_workbook
import sys
import sqlite3
# from PyQt5.QtCore import *
from ui_main import Ui_MainWindow
from ui_admin import Ui_admin
from ui_login import Ui_login
from ui_student import Ui_student
from ui_teacher import Ui_teacher
from ui_add_action import Ui_add_action
from ui_add_class import Ui_add_class
from ui_add_exam import Ui_add_exam
from ui_add_sheen_form import Ui_addSeenForm
from ui_add_user import Ui_add_user
from ui_classes import Ui_classes
from ui_add_teacher import Ui_add_teacher
from ui_student_scores import Ui_stu_scores_win
from ui_add_student import Ui_add_student
from ui_edit_student import Ui_edit_student
from ui_edit_teacher import Ui_edit_teacher
from ui_edit_class import Ui_edit_class
from ui_show_stuEsalat import Ui_showEsalat
from ui_show_absent import Ui_showAbsent
from ui_add_teacher_lessons import Ui_add_teacher_lessons
from ui_show_teacher_lessons import Ui_show_teacher_lessons
from ui_add_teacher_absent import Ui_add_teacher_absent
from ui_show_teacher_absent import Ui_show_teacher_absent
from ui_edit_scores import Ui_edit_scores


# *****************************8 main app window *****************************

class MainAppWin(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle(" النذير للبرمجة ت - 0122411241")

        #   ******************* windows objects declaration   *************************
        # self.admin = Admin()
        # self.student = Student()
        # self.classes = Classes()
        # self.teacher = Teacher()
        # self.scores = StudentScores()
        # *********************  add pages to stacked widget ***************************
        # self.stackedWidget.addWidget(self.admin)
        # self.stackedWidget.addWidget(self.student)
        # self.stackedWidget.addWidget(self.classes)
        # self.stackedWidget.addWidget(self.scores)
        # self.stackedWidget.addWidget(self.teacher)
        # self.stackedWidget.setCurrentWidget(self.admin)
        # ************************ Bar Buttons   *********************************8
        self.adminBtn.clicked.connect(self.go_admin)
        self.teacherBtn.clicked.connect(self.go_teacher)
        self.studentBtn.clicked.connect(self.go_student)
        self.classesBtn.clicked.connect(self.go_classes)
        self.scoreBtn.clicked.connect(self.go_scores)
        # ********************************************************************8

    def go_teacher(self):
        self.teacher = Teacher()
        self.stackedWidget.addWidget(self.teacher)
        self.stackedWidget.setCurrentWidget(self.teacher)

    def go_student(self):
        self.student = Student()
        self.stackedWidget.addWidget(self.student)
        self.stackedWidget.setCurrentWidget(self.student)

    def go_admin(self):
        self.admin = Admin()
        self.stackedWidget.addWidget(self.admin)
        self.stackedWidget.setCurrentWidget(self.admin)

    def go_scores(self):
        self.scores = StudentScores()
        self.stackedWidget.addWidget(self.scores)

        self.stackedWidget.setCurrentWidget(self.scores)

    def go_classes(self):
        self.classes = Classes()
        self.stackedWidget.addWidget(self.classes)
        self.stackedWidget.setCurrentWidget(self.classes)


# *****************************8 add action *****************************

class AddAction(QWidget, Ui_add_action):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


# *****************************8 add class *****************************

class AddClass(QWidget, Ui_add_class):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.saveabtn.clicked.connect(self.go_save)
        self.naneEdit.clearMask()

    def go_save(self):
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        sql = f""" insert into classes(name, level, super) values('{self.naneEdit.text()}',
            '{self.levelComboBox.currentText()}', '{self.superEdit.text()}')"""

        try:
            c.execute(sql)
            conn.commit()
        except sqlite3.OperationalError as e:
            print(e)


# *****************************8 add exam *****************************

class AddExam(QWidget, Ui_add_exam):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        print("yes")
        self.pushButton.clicked.connect(self.go_save)

    def go_save(self):
        print("yes")

        try:
            conn = sqlite3.connect("newDB.db")
            c = conn.cursor()
            sql = f""" insert into exam(name, exam_date) values('{self.examEdit.text()}', '{self.dateEdit.text()}')"""
            print("yes")
            c.execute(sql)
            conn.commit()
            print("yes")
            QMessageBox.information(self, "مبروك", " تمت العملية بنجاح")
        except Exception as e:
            print(e)
            QMessageBox.information(self, "إنتبه!!", "لم تتم العملية")
        self.destroy(True, True)


# *****************************8 add sheen form *****************************

class AddSheenForm(QWidget, Ui_addSeenForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


# *****************************8 add student *****************************

class AddStudent(QWidget, Ui_add_student):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.go_save)
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        sql = "select id, name from classes"
        c.execute(sql)
        for row in c.fetchall():
            self.classCombobox.addItem(row[1], row[0])

    def go_save(self):
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        sql = f""" insert into student(name, address, birth, super, super_tel,
         super_job, base_school,score, class_id, payment )
         values('{self.name.text()}',
                    '{self.birth.text()}', '{self.sddress.text()}', '{self.super_2.text()}',
                    '{self.superTel.text()}',
                    '{self.superWork.text()}', '{self.baseSchool.text()}', '{self.score.text()}',
                     {self.classCombobox.currentData()}, '{self.payment.text()}')"""

        try:
            c.execute(sql)
            conn.commit()

        except sqlite3.OperationalError as e:
            print(e)


## ************************************* show absent *********************
class ShowAbsent(QWidget, Ui_showAbsent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.add.clicked.connect(self.go_add)
        self.edit.clicked.connect(self.go_edit)
        self.del1.clicked.connect(self.go_delete)

    # def refresh1(self, id2, name):
    #     conn = sqlite3.connect("newDB.db")
    #     c = conn.cursor()
    #     self.new = ShowAbsent()
    #     self.new.setWindowTitle(str(id2))
    #     self.new.label.setText(name)
    #     c.execute(f"select * from stu_absent_view WHERE id = '{id2}'")
    #     absent = c.fetchall()
    #
    #     for abs1 in absent:
    #         self.new.list.addItem(abs1[2])
    #
    #     self.new.show()
    #     self.destroy(True, True)

    def go_add(self):
        s_id = int(self.windowTitle())
        string, ok = QInputDialog.getText(self, "اضافة تاريخ غياب للطالب", "صيغة التاريخ mm/dd/yyyy")
        if ok and string is not None:
            conn = sqlite3.connect("newDB.db")
            c = conn.cursor()
            note = ""
            c.execute(f""" insert into stu_absent(stu_id, absent_date, note) values('{s_id}',
                    '{string}', '{note}')""")

            conn.commit()
            print("hh")

            c.execute(f"select * from stu_absent where stu_id = '{s_id}'")
            self.list.clear()
            print(len(self.list))
            for absent in c.fetchall():
                self.list.addItem(absent[1])

    def go_edit(self):
        s_id = int(self.windowTitle())
        row = self.list.currentRow()
        item = self.list.item(row)
        if item is not None:
            string, ok = QInputDialog.getText(self, "تعديل تاريخ الغياب", "صيغة التاريخ mm/dd/yyyy", QLineEdit.Normal,
                                              item.text())
            if ok and string is not None:
                print(string, item.text())

                conn = sqlite3.connect("newDB.db")
                c = conn.cursor()
                print("jj")
                c.execute(f"update stu_absent set absent_date = '{string}' where stu_id = '{s_id}' and"
                          f" absent_date = '{str(item.text())}'")
                conn.commit()
                print("hh")
                c.execute(f"select * from stu_absent where stu_id = '{s_id}'")
                self.list.clear()
                print(len(self.list))
                for absent in c.fetchall():
                    self.list.addItem(absent[1])

    def go_delete(self):
        s_id = int(self.windowTitle())
        row = self.list.currentRow()
        item = self.list.item(row)
        print(item.text())
        if item is not None:
            reply = QMessageBox.question(self, "حذف تاريخ غياب للطالب", "هل تريد حذف هذا التاريخ" + str(item.text()),
                                         QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:

                conn = sqlite3.connect("newDB.db")
                c = conn.cursor()
                print("jj")
                c.execute(f"delete from stu_absent where stu_id = '{s_id}' and absent_date = '{str(item.text())}'")
                conn.commit()
                print("hh")
                c.execute(f"select * from stu_absent where stu_id = '{s_id}'")
                self.list.clear()
                print(len(self.list))
                for absent in c.fetchall():
                    self.list.addItem(absent[1])


# *****************************8 add teacher *****************************

class AddTeacher(QWidget, Ui_add_teacher):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute("select * from subject")
        for row in c.fetchall():
            self.comboSubject.addItem(row[1], row[0])

        self.saveBtn.clicked.connect(self.go_save)

    def go_save(self):
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        sql = f""" insert into teacher(name, address, tel, subject) values('{self.name.text()}',
                    '{self.address.text()}', '{self.tel.text()}', '{self.comboSubject.currentData()}')"""

        try:
            c.execute(sql)
            conn.commit()
        except sqlite3.OperationalError as e:
            print(e)
        # Teacher.setTable(self)


# *************************** calendar  ************************************8
# class CalenderShow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("")
#
#         self.cal = QCalendarWidget()
#         vbox = QVBoxLayout()
#         btn = QPushButton("تم")
#         btn.clicked.connect(self.setDateValue)
#         vbox.addWidget(self.cal)
#         vbox.addWidget(btn)
#         self.setLayout(vbox)
#         self.myDate = ""
#
#     def setDateValue(self):
#         self.mydate = self.cal.selectedDate().toString(Di)


# ***************8**************** add esal  *******************************
class AddEsal(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(200, 200, 400, 200)

        self.id = 0
        self.money = QLineEdit()
        self.money.setPlaceholderText("ادخل المبلغ")
        self.esal_date = QDateEdit()
        # self.esal_date.setDate()
        self.note = QLineEdit()
        self.note.setPlaceholderText("تعليق")
        self.save = QPushButton("حفظ")
        self.save.clicked.connect(self.saveFunc)
        self.label = QLabel("")
        vbox = QVBoxLayout()
        vbox.addWidget(self.money)
        vbox.addWidget(self.esal_date)
        vbox.addWidget(self.note)
        vbox.addWidget(self.save)
        self.setLayout(vbox)

    def saveFunc(self):
        conn = sqlite3.connect("newDB.db")
        print(self.id)
        c = conn.cursor()
        sql = f""" insert into esalat(stu_id, esal_date, money, note) values('{self.id}',
                    '{self.esal_date.text()}', '{int(self.money.text())}', '{self.note.text()}')"""

        if int(self.id) > 0:
            try:
                c.execute(sql)
                conn.commit()
            except sqlite3.OperationalError as e:
                print(e)
        self.destroy(True, True)


## **************************** show esalat  ****************************

class ShowStuEsalat(QWidget, Ui_showEsalat):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def setTable(self):
        self.id1 = (self.windowTitle())

        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute(f"select id, esal_date, money, note from esalat where stu_id = '{self.id1}'")
        teach = c.fetchall()

        self.tableWidget.setRowCount(len(teach) + 1)
        i = 1
        for item in teach:
            for j in range(4):
                if item[j] is None:
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(""))
                else:
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(item[j])))

                if i % 2 == 0:
                    self.tableWidget.setAlternatingRowColors(1)
            i += 1
        self.tableWidget.resizeColumnsToContents()


# *****************************8 add user *****************************

class AddUser(QWidget, Ui_add_user):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


# *****************************8 edit class *****************************

class EditClass(QWidget, Ui_edit_class):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.id = 0
        self.saveabtn.clicked.connect(self.go_save)

    def go_save(self):
        print("ok", self.id)
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        sql = f""" update classes set name = '{self.naneEdit.text()}',
         level = '{self.levelComboBox.currentText()}',
          super = '{self.superEdit.text()}' where id = '{self.id}'"""
        if int(self.id) > 0:
            try:
                c.execute(sql)
                conn.commit()
            except sqlite3.OperationalError as e:
                print(e)
        self.destroy(True, True)


# *****************************8 edit student *****************************
class EditStudent(QWidget, Ui_edit_student):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.id = 0
        self.pushButton.clicked.connect(self.go_save)

        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        sql1 = "select id, name from classes"
        c.execute(sql1)
        for row in c.fetchall():
            self.classCombobox.addItem(row[1], row[0])

    def go_save(self):

        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        print("gg")
        sql = f""" update student set name = '{self.name.text()}',
         birth = '{self.birth.text()}', 
          address = '{self.sddress.text()}',
           super = '{self.super_2.text()}',
            super_tel = '{self.superTel.text()}',
             super_job = '{self.superWork.text()}',
              base_school = '{self.baseSchool.text()}',
               score = '{self.score.text()}',
                class_id = '{self.classCombobox.currentData()}',
                 payment = '{self.payment.text()}' where id = '{self.id}'"""

        if int(self.id) > 0:
            try:
                c.execute(sql)
                conn.commit()
            except sqlite3.OperationalError as e:
                print(e)
        self.destroy(True, True)


# *****************************8 edit teacher *****************************

class EditTeacher(QWidget, Ui_edit_teacher):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.id = 0
        print(self.id)
        self.saveBtn.clicked.connect(self.go_save)
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        print("hhhh")
        c.execute("select * from subject")
        for row in c.fetchall():
            self.comboSubject.addItem(row[1], row[0])
            print(row[1])

    def go_save(self):
        print("ok", self.id)
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        sql = f""" update teacher set name = '{self.name.text()}',
                 address = '{self.address.text()}',
                  tel = '{self.tel.text()}',
                   subject = '{self.comboSubject.currentData()}'where id = '{self.id}'"""
        if int(self.id) > 0:
            try:
                c.execute(sql)
                conn.commit()
            except sqlite3.OperationalError as e:
                print(e)

        self.destroy(True, True)


# *****************************8 admin *****************************

class Admin(QWidget, Ui_admin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


# *****************************8 classes *****************************

class Classes(QWidget, Ui_classes):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setTable()

    def classStudentNo(self, class_id):
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute(f"select COUNT(*) from student where class_id = {class_id}")
        return c.fetchone()[0]

    def contextMenuEvent(self, event):
        contexMenu = QMenu(self)
        addAction = contexMenu.addAction("اضافة صف")
        editAction = contexMenu.addAction("تحديث صف")
        deleteAction = contexMenu.addAction("حذف الصف")

        action = contexMenu.exec_(self.mapToGlobal(event.pos()))

        if action == addAction:
            self.addWin = AddClass()
            self.addWin.show()
        if action == editAction:
            if self.tableWidget.currentRow():
                i = self.tableWidget.currentRow()
                self.addWin = EditClass()
                self.addWin.id = self.tableWidget.item(i, 0).text()
                self.addWin.naneEdit.setText(self.tableWidget.item(i, 1).text())
                self.addWin.superEdit.setText(self.tableWidget.item(i, 3).text())
                print(self.addWin.id, "hh", self.tableWidget.item(i, 0).text())

                self.addWin.show()

        if action == deleteAction:
            if self.tableWidget.currentRow():
                i = self.tableWidget.currentRow()
                message = QMessageBox.critical(self, "إنتبه!!!!",
                                               " هل تريد حذف بيانات؟" + self.tableWidget.item(i, 1).text(),
                                               QMessageBox.Yes | QMessageBox.No)

                if message == QMessageBox.Yes:
                    conn = sqlite3.connect("newDB.db")
                    c = conn.cursor()
                    c.execute(f"delete from classes where name like '{self.tableWidget.item(i, 1).text()}'")
                    conn.commit()
                    self.setTable()

    def setTable(self):

        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute("select * from classes")
        teach = c.fetchall()
        self.tableWidget.setRowCount(len(teach) + 1)
        i = 1
        for item in teach:
            for j in range(4):
                if item[j] is None:
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(""))
                else:
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(item[j])))
                if i % 2 == 0:
                    self.tableWidget.setAlternatingRowColors(1)
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(self.classStudentNo(item[0]))))
            i += 1


# *****************************8 login *****************************

class Login(QWidget, Ui_login):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


# *****************************8 student *****************************

class Student(QWidget, Ui_student):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setTable()
        self.searchEdit.setPlaceholderText("ادخل اسم الطالب هنا للبحث عنه")
        self.searchEdit.textChanged.connect(self.search)
        self.setComboBox()
        self.comboBox.currentIndexChanged.connect(self.searchClass)
        self.searchBtn.clicked.connect(self.search)
        self.searchBtn.setText(" تحديث ")

    def setComboBox(self):
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute("select * from classes")
        self.comboBox.clear()
        for cl in c.fetchall():
            self.comboBox.addItem(cl[1], cl[0])

    def contextMenuEvent(self, event):
        contexMenu = QMenu(self)
        addAction = contexMenu.addAction("اضافة طالب")
        editAction = contexMenu.addAction("تخديث")
        deleteAction = contexMenu.addAction("حذف")
        add_esalAction = contexMenu.addAction("اضافة ايصال")
        show_esalAction = contexMenu.addAction("عرض الايصالات")
        add_absentAction = contexMenu.addAction("اضافة غياب")
        show_absentAction = contexMenu.addAction("عرض غياب الطالب")

        action = contexMenu.exec_(self.mapToGlobal(event.pos()))

        if action == addAction:
            self.addWin = AddStudent()
            self.addWin.show()

        if action == editAction:
            if self.tableWidget.currentRow():
                i = self.tableWidget.currentRow()
                self.addWin = EditStudent()
                self.addWin.id = int(self.tableWidget.item(i, 0).text())
                print(self.addWin.id, "jj")

                self.addWin.name.setText(self.tableWidget.item(i, 1).text())
                self.addWin.birth.setText(self.tableWidget.item(i, 2).text())

                self.addWin.sddress.setText(self.tableWidget.item(i, 3).text())
                self.addWin.super_2.setText(self.tableWidget.item(i, 4).text())

                self.addWin.superTel.setText(self.tableWidget.item(i, 5).text())
                self.addWin.superWork.setText(self.tableWidget.item(i, 6).text())

                self.addWin.baseSchool.setText(self.tableWidget.item(i, 7).text())
                self.addWin.score.setText(self.tableWidget.item(i, 8).text())

                self.addWin.classCombobox.setCurrentText(self.tableWidget.item(i, 9).text())
                self.addWin.payment.setText(self.tableWidget.item(i, 10).text())

                self.addWin.show()

        if action == deleteAction:
            if self.tableWidget.currentRow():
                i = self.tableWidget.currentRow()
                message = QMessageBox.critical(self, "إنتبه!!!!",
                                               " هل تريد حذف بيانات؟" + self.tableWidget.item(i, 1).text(),
                                               QMessageBox.Yes | QMessageBox.No)

                if message == QMessageBox.Yes:
                    conn = sqlite3.connect("newDB.db")
                    c = conn.cursor()
                    c.execute(f"delete from student where name like '{self.tableWidget.item(i, 1).text()}'")
                    conn.commit()
                    self.setTable()

        if action == add_esalAction:

            if self.tableWidget.currentRow():
                i = self.tableWidget.currentRow()
                winTitle = "اضافة ايصال مالي للطالب : " + self.tableWidget.item(i, 1).text()
                self.addWin = AddEsal()
                self.addWin.setWindowTitle(winTitle)

                self.addWin.id = int(self.tableWidget.item(i, 0).text())

                self.addWin.show()

        if action == show_esalAction:

            if self.tableWidget.currentRow():
                i = self.tableWidget.currentRow()
                s_name = self.tableWidget.item(i, 1).text()
                self.addWin = ShowStuEsalat()
                print("dd")
                self.addWin.stu_name.setText(s_name)
                dd = int(self.tableWidget.item(i, 0).text())
                print(dd, dd)
                self.addWin.setWindowTitle(str(dd))
                print(self.addWin.windowTitle())
                conn = sqlite3.connect("newDB.db")
                c = conn.cursor()

                c.execute(f"select SUM(money) from esalat where stu_id = '{dd}'")
                sum1 = c.fetchone()[0]
                self.addWin.sum_value.setText(str(sum1))

                self.addWin.id = dd
                if self.tableWidget.item(i, 10).text() == "":
                    self.addWin.rem_value.setText("")
                else:
                    self.addWin.sum_value.setText(str(sum1))
                    pp = int(self.tableWidget.item(i, 10).text())

                    if pp > sum1:
                        rem = pp - sum1
                        self.addWin.rem_value.setText(str(rem))
                    else:
                        self.addWin.rem_value.setText(" خالص")
                        self.addWin.tableWidget.setRowCount(10)
                        self.addWin.setTable()

                self.addWin.setTable()

                self.addWin.show()

        if action == add_absentAction:

            if self.tableWidget.currentRow():
                i = self.tableWidget.currentRow()
                s_name = self.tableWidget.item(i, 1).text()

                self.addWin = AddAbsent()
                name = self.tableWidget.item(i, 1).text()
                self.addWin.setWindowTitle(name)
                self.addWin.id1.setText(self.tableWidget.item(i, 0).text())

                self.addWin.show()

        if action == show_absentAction:
            if self.tableWidget.currentRow():
                i = self.tableWidget.currentRow()
                self.addWin = ShowAbsent()
                id1 = int(self.tableWidget.item(i, 0).text())
                self.addWin.label.setText(self.tableWidget.item(i, 1).text())
                self.addWin.setWindowTitle(self.tableWidget.item(i, 0).text())
                conn = sqlite3.connect("newDB.db")
                c = conn.cursor()
                c.execute(f"select * from stu_absent_view WHERE id = '{id1}'")
                absent = c.fetchall()
                for abs1 in absent:
                    self.addWin.list.addItem(abs1[2])

                self.addWin.show()

    def setTable(self):

        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute("select * from student_view")
        teach = c.fetchall()
        self.tableWidget.setRowCount(len(teach) + 1)
        i = 1
        for item in teach:
            for j in range(11):
                if item[j] is None:
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(""))
                else:
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(item[j])))

                if i % 2 == 0:
                    self.tableWidget.setAlternatingRowColors(1)
            i += 1
        self.tableWidget.resizeColumnsToContents()

    def search(self):
        self.tableWidget.children().clear()
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute(f"select * from student_view where name like '%" + self.searchEdit.text() + "%'")
        teach = c.fetchall()

        self.tableWidget.setRowCount(len(teach) + 1)
        i = 1
        for item in teach:
            for j in range(11):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(item[j])))

            i += 1
        self.tableWidget.resizeRowsToContents()

    def searchClass(self):
        self.tableWidget.children().clear()
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute(f"select * from student_view where name like '%" + self.searchEdit.text() + "%'" + f"""
                     and class = '{self.comboBox.currentText()}'""")
        teach = c.fetchall()

        self.tableWidget.setRowCount(len(teach) + 1)
        i = 1
        for item in teach:
            for j in range(11):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(item[j])))

            i += 1
        self.tableWidget.resizeRowsToContents()


## **************************** add abswnt *******************************
class AddAbsent(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" ")
        self.setGeometry(200, 200, 300, 100)
        self.id1 = QLabel("")
        self.absent_date = QDateEdit()
        self.note = QLineEdit()
        self.note.setPlaceholderText(" اكتب التعليق")
        self.save = QPushButton(" حفظ ")
        self.save.clicked.connect(self.goSave)
        vbox = QVBoxLayout()
        vbox.addWidget(self.id1)
        vbox.addWidget(self.absent_date)
        vbox.addWidget(self.note)
        vbox.addWidget(self.save)
        self.setLayout(vbox)

    def goSave(self):
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        sql = f""" insert into stu_absent(stu_id, absent_date, note) values('{self.id1.text()}',
                            '{self.absent_date.text()}', '{self.note.text()}')"""
        c.execute(sql)

        conn.commit()
        self.destroy(True, True)


## ****************************** edit scores   *****************************
class EditScores(QWidget, Ui_edit_scores):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.exam = 1
        self.stu = 1
        self.ides = []
        self.score_table = 1
        self.save.clicked.connect(self.go_save)

    def go_save(self):
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        col = 0
        try:
            for sub in self.ides:

                if self.tableWidget.item(0, col).text() is None:
                    score = 0
                else:
                    score = int(self.tableWidget.item(0, col).text())
                if self.score_table == 1:
                    sql1 = f""" update stu_scores1 set score = '{score}' where exam_id = '{self.exam}' and 
                            stu_id = '{self.stu}' and subject_id = '{sub}'"""
                    c.execute(sql1)
                else:
                    sql = f""" update stu_scores set score = '{score}' where exam_id = '{self.exam}' and 
                            stu_id = '{self.stu}' and subject_id = '{sub}'"""
                    c.execute(sql)
                col += 1
            QMessageBox.information(self, "", "تمت العملية بنجاح")
        except Exception as e:
            print(e)
            QMessageBox.information(self, "لم تتم العملية", str(e))
        conn.commit()
        self.destroy(True, True)


# 8******************************** add student to exam ************************
# *****************************8 student scores *****************************

class StudentScores(QWidget, Ui_stu_scores_win):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setCombo()
        self.check_class()
        self.combo_class.currentIndexChanged.connect(self.check_class)
        self.searchEdit.textChanged.connect(self.check_class)
        self.searchBtn.setVisible(False)
        self.combo_exam.currentIndexChanged.connect(self.check_class)

    def contextMenuEvent(self, event):
        contexMenu = QMenu(self)
        add_examAction = contexMenu.addAction("اضافة امتحان جديد")
        edit_examAction = contexMenu.addAction("تعديل امتحان")
        edit_subjectAction = contexMenu.addAction("تحديث المواد")
        edit_scoresAction = contexMenu.addAction("تحديث درجات الطالب")
        init_scoresAction = contexMenu.addAction("تفعيل الامتحان")
        add_stu_to_examAction = contexMenu.addAction("اضافة طالب للامتحان")
        excel_fileAction = contexMenu.addAction("اخراج النتيجة في ملف اكسل")

        action = contexMenu.exec_(self.mapToGlobal(event.pos()))

        if action == add_examAction:
            self.examWin = AddExam()
            self.examWin.show()

        if action == edit_scoresAction:

            if self.tableWidget.currentRow():
                self.editWin = EditScores()
                i = self.tableWidget.currentRow()
                self.editWin.label.setText(self.tableWidget.item(i, 1).text())
                conn = sqlite3.connect("newDB.db")
                c = conn.cursor()

                if self.tableWidget.columnCount() < 15:
                    c.execute(f"select level from classes where id = '{self.combo_class.currentData()}'")
                    level = "الثالث علمي"
                    if c.fetchone()[0] == level:
                        division = "علمي"
                    else:
                        division = "ادبي"

                    c.execute(f" select id, name from new_subject where division = '{division}' or division = 'مشترك'")
                    headers = []
                    ides = []
                    for ii in c.fetchall():
                        ides.append(ii[0])
                        headers.append(ii[1])
                    self.editWin.ides = ides
                    self.editWin.score_table = 0
                    self.editWin.tableWidget.setFont(QtGui.QFont("helvetica", 14))
                    self.editWin.tableWidget.setColumnCount(len(headers))
                    self.editWin.tableWidget.setRowCount(1)
                    self.editWin.tableWidget.setHorizontalHeaderLabels(headers)

                    for h in range(len(headers)):
                        item2 = self.tableWidget.item(i, h + 2).text()
                        self.editWin.tableWidget.setItem(0, h, QtWidgets.QTableWidgetItem(item2))
                        self.editWin.tableWidget.resizeColumnsToContents()
                else:
                    c.execute("select * from subject")
                    headers = []
                    ides = []
                    for ii in c.fetchall():
                        ides.append(ii[0])
                        headers.append(ii[1])
                    self.editWin.ides = ides
                    self.editWin.score_table = 1
                    self.editWin.tableWidget.setFont(QtGui.QFont("helvetica", 13))
                    self.editWin.tableWidget.setColumnCount(len(headers))
                    self.editWin.tableWidget.setRowCount(1)
                    self.editWin.tableWidget.setHorizontalHeaderLabels(headers)
                    for h in range(len(headers)):
                        item2 = self.tableWidget.item(i, h + 2).text()
                        self.editWin.tableWidget.setItem(0, h, QtWidgets.QTableWidgetItem(item2))
                        self.editWin.tableWidget.resizeColumnsToContents()
                self.editWin.setFixedWidth(1300)
                self.editWin.stu = self.tableWidget.item(i, 0).text()
                self.editWin.exam = self.combo_exam.currentData()
                self.editWin.show()

        if action == init_scoresAction:
            try:
                exam = self.combo_exam.currentData()
                conn = sqlite3.connect("newDB.db")
                c = conn.cursor()

                class_id = self.combo_class.currentData()
                c.execute(f"select id from student where class_id = '{class_id}'")
                student = c.fetchall()
                c.execute(f"select level from classes where id = '{class_id}'")
                x = c.fetchone()[0]
                print(student)

                print(x, "088000")
                level = "الثالث علمي"
                print("22")
                if x == level:
                    division = "علمي"
                    print(division)
                    try:
                        c.execute(f" select id from new_subject where division = '{division}' or"
                                  f" division = 'مشترك'")

                    except sqlite3.OperationalError as e:
                        print(e, "--0")
                    subjects = c.fetchall()
                    print(subjects)
                    z = 0
                    score = 0
                    for stu in student:
                        for sub in subjects:
                            try:
                                c.execute(f"""insert into stu_scores(exam_id, stu_id, subject_id, score) values(
                                            '{exam}', '{stu[0]}', '{sub[0]}', '{score}')""")

                            except Exception as e:
                                print(e, "-1")
                                z -= 2
                        z += 1
                    if z >= len(student):
                        QMessageBox.information(self, "", "تمت العملية بنجاح  ")
                        conn.commit()
                        self.tableWidget.clear()
                        self.setTable2(division)
                    if z < 0:
                        QMessageBox.information(self, "إنتبه!!!", "لم تتم العملية قد يكون الامتحان مفعل مسبقا ")
                else:
                    print("else1")
                    level2 = "الثالث ادبي"
                    if x == level2:
                        division = "ادبي"
                        c.execute(f" select id from new_subject where division = '{division}' or "
                                  f"division = 'مشترك'")
                        subject = c.fetchall()
                        z = 0
                        for stu in student:
                            print(stu[0])
                            for sub in subject:

                                try:
                                    c.execute(f""" insert into stu_scores (exam_id, stu_id, subject_id, score)
                                                                   values('{exam}', '{stu[0]}', '{sub[0]}', '0') """)

                                except Exception as e:
                                    print(e, "-2")
                                    z -= 2

                            z += 1
                        if z >= len(student):
                            QMessageBox.information(self, "", "تمت العملية بنجاح")
                            conn.commit()
                            self.tableWidget.clear()
                            self.setTable2(division)
                        if z < 0:
                            QMessageBox.information(self, "إنتبه!!!", "لم تتم العملية قد يكون الامتحان مفعل مسبقا ")
                    else:
                        print("else2")
                        c.execute(" select id from subject")
                        score = 0
                        z = 0
                        for stu in student:
                            for sub in c.fetchall():
                                try:
                                    c.execute(f""" insert into stu_scores1 (exam_id, stu_id, subject_id, score)
                                                            values('{exam}', '{stu[0]}', '{sub[0]}', '{score}')""")

                                except Exception as e:
                                    print(e, "-3")
                                    z -= 2

                            z += 1
                        if z >= len(student):
                            QMessageBox.information(self, "", "تمت العملية بنجاح")
                            conn.commit()
                            self.tableWidget.clear()
                            self.setTable()
                            print("pass")
                        if z < 0:
                            QMessageBox.information(self, "إنتبه!!!", "لم تتم العملية قد يكون الامتحان مفعل مسبقا ")
                conn.commit()
            except Exception as e:
                print(e, "00")

    def setCombo(self):
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute(" select * from exam")
        for row in c.fetchall():
            self.combo_exam.addItem(row[1], row[0])

        c.execute("select * from classes")
        for sub in c.fetchall():
            self.combo_class.addItem(sub[1], sub[0])

    def setTable(self):
        self.refreshBtn.setVisible(True)
        self.sybject_noEdit.setVisible(True)
        self.label_3.setVisible(True)
        self.tableWidget.clear()
        self.tableWidget.setFont(QtGui.QFont("helvetica", 13))
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute(f"select id, name from student where class_id = '{self.combo_class.currentData()}'"
                  f"and name like '%" + self.searchEdit.text() + "%'")
        stu = c.fetchall()
        c.execute(" select * from subject")
        headers = ["رقم الطالب", "اسم الطالب"]
        for sub in c.fetchall():
            headers.append(sub[1])
        headers.append("المجموع")
        headers.append("المعدل")
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setRowCount(len(stu) + 1)
        print(stu)
        self.tableWidget.setHorizontalHeaderLabels(headers)
        # self.tableWidget.setFont(QtGui.QFont("helvetica", 13))

        print(self.combo_class.currentData())
        # c.execute(f" select id, name from student where class_id = '{self.combo_class.currentData()}' and "
        #           f"name like '%" + self.searchEdit.text() + "%'")
        # stu = c.fetchall()
        self.tableWidget.setRowCount(len(stu) + 1)
        print(stu)
        i = 1
        for item in stu:
            try:
                c.execute(f"select score from stu_scores1 where exam_id = '{self.combo_exam.currentData()}' and"
                          f" stu_id = '{item[0]}'")

            except sqlite3.OperationalError as e:
                print(e, "***1-2")
            subject = c.fetchall()
            k = 2
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(item[0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item[1])))
            sum1 = 0
            for j in subject:
                sum1 += j[0]
                self.tableWidget.setItem(i, k, QtWidgets.QTableWidgetItem(str(j[0])))
                k += 1
                if i % 2 == 0:
                    self.tableWidget.setAlternatingRowColors(1)
            self.tableWidget.setItem(i, k, QtWidgets.QTableWidgetItem(str(sum1)))
            # mm = int(self.sybject_noEdit.text())
            m = sum1 / 6
            self.tableWidget.setItem(i, k + 1, QtWidgets.QTableWidgetItem(str(round(m, 1))))
            i += 1
        self.tableWidget.resizeColumnsToContents()

    def setTable2(self, division):
        self.refreshBtn.setVisible(False)
        self.sybject_noEdit.setVisible(False)
        self.label_3.setVisible(False)
        self.tableWidget.clear()
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.clear()
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute(f" select * from new_subject where division = '{division}' or division = 'مشترك'")
        headers = ["رقم الطالب", "اسم الطالب"]
        print(headers)
        for sub in c.fetchall():
            headers.append(sub[1])
        headers.append("المجموع")
        headers.append("المعدل")
        self.tableWidget.setColumnCount(len(headers))

        # self.tableWidget.setFont(QFont("helvetica", 14))
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.setFont(QtGui.QFont("helvetica", 14))
        print(self.combo_class.currentData())
        c.execute(f" select id, name from student where class_id = '{self.combo_class.currentData()}' and "
                  f"name like '%" + self.searchEdit.text() + "%'")
        stu = c.fetchall()
        self.tableWidget.setRowCount(len(stu) + 1)
        print(stu)
        i = 1
        for item in stu:
            try:
                c.execute(f"select score from stu_scores where exam_id = '{self.combo_exam.currentData()}' and"
                          f" stu_id = '{item[0]}'")
            except sqlite3.OperationalError as e:
                print(e, "***3")
            k = 2
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(item[0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item[1])))
            sum1 = 0
            for j in c.fetchall():
                sum1 += j[0]
                self.tableWidget.setItem(i, k, QtWidgets.QTableWidgetItem(str(j[0])))
                k += 1
                if i % 2 == 0:
                    self.tableWidget.setAlternatingRowColors(1)
            self.tableWidget.setItem(i, k, QtWidgets.QTableWidgetItem(str(sum1)))
            m = sum1 / 7
            self.tableWidget.setItem(i, k + 1, QtWidgets.QTableWidgetItem(str(round(m, 1))))
            i += 1
        self.tableWidget.resizeColumnsToContents()

    def check_class(self):
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute(f" select level from classes where id = '{self.combo_class.currentData()}'")
        cc = c.fetchone()[0]
        dev1 = "الثالث علمي"
        print(dev1)
        if cc == dev1:
            self.setTable2("علمي")
        else:
            dev2 = "الثالث ادبي"
            print(dev2)
            if cc == dev2:
                self.setTable2("ادبي")
            else:
                self.setTable()


# *****************************8 teachers *****************************
def t_lessons(t_id):
    conn = sqlite3.connect("newDB.db")
    c = conn.cursor()
    c.execute(f" select SUM(lessons_no) from teacher_lessons where teacher_id = '{t_id}'")
    return c.fetchone()[0]


class Teacher(QWidget, Ui_teacher):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setTable()
        self.searchBtn.clicked.connect(self.search)
        self.searchEdit.setPlaceholderText("ادخل الاسم هنا للبحث عن المعلم")
        self.searchEdit.textChanged.connect(self.search)

    def setTable(self):
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute("select * from teacher_view")
        teach = c.fetchall()
        self.tableWidget.setRowCount(len(teach) + 1)

        i = 1
        for item in teach:
            for j in range(5):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(item[j])))
                if i % 2 == 0:
                    self.tableWidget.setAlternatingRowColors(1)
            t_id = item[0]
            self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(t_lessons(t_id))))
            i += 1
        self.tableWidget.resizeColumnsToContents()

    def contextMenuEvent(self, event):
        contexMenu = QMenu(self)
        addAction = contexMenu.addAction("اضافة معلم")
        editAction = contexMenu.addAction("تحديث")
        deleteAction = contexMenu.addAction("حذف")
        addLessonsAction = contexMenu.addAction("اضافة حصص المعلم")
        showLessonsAction = contexMenu.addAction("عرض حصص المعلم")
        addAbsentsAction = contexMenu.addAction("اضافة غياب المعلم")
        showAbsentAction = contexMenu.addAction("عرض غياب المعلم")

        action = contexMenu.exec_(self.mapToGlobal(event.pos()))

        if action == addAction:
            self.addWin = AddTeacher()
            self.addWin.show()
        if action == editAction:
            if self.tableWidget.currentRow():
                print("yes")
                i = self.tableWidget.currentRow()
                print(i)
                self.editWin = EditTeacher()
                print("yes")
                self.editWin.id = int(self.tableWidget.item(i, 0).text())
                self.editWin.name.setText(self.tableWidget.item(i, 1).text())
                self.editWin.address.setText(self.tableWidget.item(i, 2).text())
                self.editWin.tel.setText(self.tableWidget.item(i, 3).text())
                self.editWin.comboSubject.setCurrentText(self.tableWidget.item(i, 4).text())
                print("yes")
                self.editWin.show()

        if action == deleteAction:
            if self.tableWidget.currentRow():
                i = self.tableWidget.currentRow()
                message = QMessageBox.critical(self, "إنتبه!!!!",
                                               " هل تريد حذف بيانات؟" + self.tableWidget.item(i, 1).text(),
                                               QMessageBox.Yes | QMessageBox.No)

                if message == QMessageBox.Yes:
                    conn = sqlite3.connect("newDB.db")
                    c = conn.cursor()
                    c.execute(f"delete from teacher where id = '{self.tableWidget.item(i, 0).text()}'")
                    conn.commit()
                    self.setTable()

        if action == addLessonsAction:
            if self.tableWidget.currentRow():
                print("yes")
                i = self.tableWidget.currentRow()
                self.addWin = AddTeacherLessons()
                t_id = self.tableWidget.item(i, 0).text()
                self.addWin.setWindowTitle(t_id)
                self.addWin.name.setText(self.tableWidget.item(i, 1).text())

                self.addWin.show()

        if action == showLessonsAction:
            if self.tableWidget.currentRow():
                i = self.tableWidget.currentRow()
                self.addWin = ShowTeacherLessons()
                self.addWin.setWindowTitle(self.tableWidget.item(i, 0).text())
                self.addWin.name.setText(self.tableWidget.item(i, 1).text())
                self.addWin.go()
                self.addWin.show()

        if action == addAbsentsAction:
            if self.tableWidget.currentRow():
                print("yes")
                i = self.tableWidget.currentRow()
                print(i)
                self.addWin = AddTeacherAbsent()
                self.addWin.setWindowTitle(self.tableWidget.item(i, 0).text())
                self.addWin.label.setText(self.tableWidget.item(i, 1).text())

                self.addWin.show()

        if action == showAbsentAction:
            if self.tableWidget.currentRow():
                print("yes")
                i = self.tableWidget.currentRow()
                print(i)
                self.addWin = ShowTeacherAbsent()
                self.addWin.setWindowTitle(self.tableWidget.item(i, 0).text())
                self.addWin.label.setText(self.tableWidget.item(i, 1).text())
                self.addWin.setTable()

                self.addWin.show()

    def search(self):
        self.tableWidget.children().clear()
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute(f"select * from teacher_view where name like '%" + self.searchEdit.text() + "%'")
        teach = c.fetchall()
        self.tableWidget.setRowCount(len(teach) + 1)
        for i, item in enumerate(teach):
            for j in range(5):
                self.tableWidget.setItem(i + 1, j, QtWidgets.QTableWidgetItem(str(item[j])))
                print(item[j])


## ******************************************** show teacher lessons ************************
class ShowTeacherLessons(QWidget, Ui_show_teacher_lessons):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setGeometry(200, 200, 300, 300)
        self.edit.clicked.connect(self.go_edit)
        self.del1.clicked.connect(self.go_delete)
        self.list_lessons.setCurrentRow(1)
        self.list_day.setCurrentRow(1)
        self.list_day.setSortingEnabled(True)
        self.list_lessons.setSortingEnabled(False)
        self.list_lessons.itemSelectionChanged.connect(
            lambda: self.list_day.setCurrentRow(self.list_lessons.currentRow()))
        self.list_day.itemSelectionChanged.connect(lambda: self.list_lessons.setCurrentRow(self.list_day.currentRow()))

    def go(self):
        t_id = int(self.windowTitle())
        print(t_id)
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute(f" select * from teacher_lessons where teacher_id = '{t_id}'")

        for row in c.fetchall():
            self.list_day.addItem(QListWidgetItem(str(row[1])))
            self.list_lessons.addItem(QListWidgetItem(str(row[2])))

    def go_edit(self):
        t_id = int(self.windowTitle())
        row = self.list_day.currentRow()
        item_day = self.list_day.item(row)
        item_lessons = self.list_lessons.item(row)
        if item_lessons is not None:
            string, ok = QInputDialog.getText(self, "تعديل حصص اليوم", "ادخل عدد الحصص", QLineEdit.Normal,
                                              item_lessons.text())
            if ok and string is not None:
                print(string, item_day.text())

                conn = sqlite3.connect("newDB.db")
                c = conn.cursor()
                print("jj")
                c.execute(f"""update teacher_lessons set lessons_no = '{string}' where teacher_id = '{t_id}' and
                            day_name = '{str(item_day.text())}'""")
                conn.commit()
                print("hh")
                c.execute(f"select * from teacher_lessons where teacher_id = '{t_id}'")
                self.list_day.clear()
                self.list_lessons.clear()
                print(len(self.list_day))
                for lessons in c.fetchall():
                    self.list_lessons.addItem(str(lessons[2]))
                    self.list_day.addItem(str(lessons[1]))

    def go_delete(self):
        print(self.list_lessons.currentRow())
        print(self.list_lessons.currentRow())
        if self.list_lessons.currentRow() < 0:
            return
        t_id = int(self.windowTitle())
        row = self.list_lessons.currentRow()
        item = self.list_day.item(row)
        print(item.text())
        if item is not None:
            reply = QMessageBox.question(self, "إنتبه !!!", "هل تريد حذف ليوم " + str(item.text()),
                                         QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:

                conn = sqlite3.connect("newDB.db")
                c = conn.cursor()
                c.execute(f""" delete from teacher_lessons where teacher_id = '{t_id}' and
                                                                                 day_name = '{str(item.text())}'""")
                conn.commit()
                print("hh")
                c.execute(f"select * from teacher_lessons where teacher_id = '{t_id}'")
                self.list_lessons.clear()
                self.list_day.clear()

                for lessons in c.fetchall():
                    self.list_lessons.addItem(str(lessons[2]))
                    self.list_day.addItem(str(lessons[1]))


## ****************************************** teacher--- add lessons *************************
class AddTeacherLessons(QWidget, Ui_add_teacher_lessons):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.go_save)

    def go_save(self):
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        t_id = int(self.windowTitle())
        sql = f""" insert into teacher_lessons(teacher_id, day_name, lessons_no) values('{t_id}',
                                    '{self.comboDay.currentText()}', '{self.comboLessonsNo.currentText()}')"""

        try:
            c.execute(sql)
            conn.commit()
            QMessageBox.information(self, "", "تمت الاضافة بنجاح")
        except sqlite3.Error as e:
            print(e)
            QMessageBox.information(self, "إنتبه!!", "لم تتم العملية ربما يكون اليوم مضاف فعلا")


# *************************************88 add teacher absent ****************************88***
class AddTeacherAbsent(QWidget, Ui_add_teacher_absent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.save.clicked.connect(self.goSave)

    def goSave(self):
        t_id = int(self.windowTitle())
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        sql = f""" insert into teacher_absent(teacher_id, absent_date, lessons_no, note) values('{t_id}',
                            '{self.dateEdit.text()}', '{self.lessons_no.text()}', '{self.note.text()}')"""
        try:
            c.execute(sql)
            conn.commit()
            QMessageBox.information(self, "", "تمت الاضافة بنجاح")
        except sqlite3.Error as e:
            print(e)
            QMessageBox.information(self, "إنتبه!!", "لم تتم العملية")
        self.destroy(True, True)


# ****************************************  show teacher absent *****************************
class ShowTeacherAbsent(QWidget, Ui_show_teacher_absent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def setTable(self):
        t_id = int(self.windowTitle())
        conn = sqlite3.connect("newDB.db")
        c = conn.cursor()
        c.execute(f"select * from teacher_absent where teacher_id = '{t_id}'")
        teach = c.fetchall()
        self.tableWidget.setRowCount(len(teach) + 1)

        i = 1
        for item in teach:

            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(item[1])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item[2])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item[3])))
            if i % 2 == 0:
                self.tableWidget.setAlternatingRowColors(1)
            t_id = item[0]
            self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(t_lessons(t_id))))
            i += 1
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainAppWin()

    win.showMaximized()

    sys.exit(app.exec_())
