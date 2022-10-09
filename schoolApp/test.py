import sqlite3

conn = sqlite3.connect("newDB.db")
c = conn.cursor()
# sql = f""" insert into stu_scores (exam_od, stu_id, subject_id, score) values(
#         '1', '{stu}', '{sub}', '0')"""

# sc_sql = f""" select id from new_subject where division = 'علمي' or division = 'مشترك'"""
at_sql = f""" select id from subject """
# c.execute(sc_sql)
#
# sc_subj = c.fetchall()
# print(sc_subj)
c.execute(at_sql)
at_subj = c.fetchall()
print(at_subj)
# c.execute(" select id from classes where level = 'الثالث علمي'")
# sc_classes = c.fetchall()
c.execute(" select id from classes where level = 'الثاني'")
at_classes = c.fetchall()
print(at_classes)

for c_it in at_classes:
    c.execute(f"select id from student where class_id = '{c_it[0]}'")
    for stu in c.fetchall():
        for sub in at_subj:
            sql = f""" insert into stu_scores1 (exam_id, stu_id, subject_id, score) values(
                    '1', '{stu[0]}', '{sub[0]}', '0')"""
            try:
                c.execute(sql)
                print("done")
            except sqlite3.Error as e:
                print(e)
                print("no")
    conn.commit()
# for c_it in at_classes:
#     c.execute(f"select id from student where class_id = '{c_it[0]}'")
#     for stu in c.fetchall():
#         for sub in at_subj:
#             sql = f""" insert into stu_scores (exam_id, stu_id, subject_id, score) values(
#                     '1', '{stu[0]}', '{sub[0]}', '0')"""
#             try:
#                 c.execute(sql)
#                 print("done")
#             except sqlite3.Error as e:
#                 print(e)
#                 print("no")
#
#     conn.commit()
