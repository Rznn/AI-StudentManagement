# FOREGIN KEY, triger , cascade

import sqlite3

def studentData():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS student(usn TEXT PRIMARY KEY,
        name TEXT,
        mobileno TEXT,
        address TEXT,
        email TEXT)""")
    con.commit()
    con.close()
studentData()

def addstdrec(usn,name,mobileno,address,email):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""INSERT INTO student VALUES (:usn,:name,:mobileno,:address,:email)""",{'usn':usn,'name':name,'mobileno':mobileno,'address':address,'email':email})
    con.commit()
    con.close()

def viewdatastud():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    con.close()
    return rows

def deletestdrec(usn):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""PRAGMA foreign_keys = ON""")
    con.commit()
    cur.execute("DELETE FROM student WHERE usn=:usn",{'usn':usn})
    con.commit()
    con.close()


def updatestddata(usn,name,mobileno,address,email):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("UPDATE student SET name=:name,mobileno=:mobileno,address=:address,email=:email WHERE usn=:usn",{'name':name,'mobileno':mobileno,'address':address,'email':email,'usn' : usn})
    con.commit()
    con.close()

def moderatordata():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS moderator(usr TEXT PRIMARY KEY,
        namem TEXT,
        password TEXT,
        emailm TEXT,
        contactno TEXT)""")
    con.commit()
    con.close()

moderatordata()

def addmoderator(idm,namem,password,emailm,contactno):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""INSERT INTO moderator VALUES (:usr,:namem,:password,:emailm,:contactno)""",{'usr':idm,'namem':namem,'password':password,'emailm':emailm,'contactno':contactno})
    con.commit()
    con.close()

def viewmoderator():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM moderator")
    rows=cur.fetchall()
    con.close()
    return rows

def deleterecmoderator(idm):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("DELETE FROM moderator WHERE usr=:idm",{'idm':idm})
     con.commit()
     con.close()



def updaterecmoderator(idm,namem,password,emailm,contactno):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("UPDATE moderator SET namem=:namem,password=:password,emailm=:emailm,contactno=:contactno WHERE idm=:idm",{'namem':namem,'password':password,'emailm':emailm,'contactno':contactno,'idm':idm})
     con.commit()
     con.close()

def performancedata():
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("""PRAGMA foreign_keys = ON""")
     cur.execute("""CREATE TABLE IF NOT EXISTS performance(usn TEXT PRIMARY KEY,
     internal INTEGER,
     external INTEGER,
     attendance INTEGER,
     final TEXT,
     remark TEXT,
     foreign key (usn) references student(usn) ON DELETE CASCADE)""")
     con.commit()
     con.close()

performancedata()
def addmark(usn,internal,external,attendance,final, remark):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""INSERT INTO performance VALUES(:usn,:internal,:external,:attendance,:final,:remark)""",{'usn':usn,'internal':internal,'external':external,'attendance':attendance,'final':final,'remark':remark})
    con.commit()
    con.close()

def check_marks():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM performance")
    rows=cur.fetchall()
    con.close()
    return rows

def updatemark(usn,internal,external,attendance,final,remark):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("DELETE FROM performance WHERE usn=:usn",{'usn':usn})
    con.commit()
    con.close()
    addmark(usn,internal,external,attendance,final,remark)


