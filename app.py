from flask import Flask, render_template, request, redirect, url_for, flash
from backend import *
from fuzzy import compute_fuzzy
import math
import webbrowser

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        x = request.form["username"]
        y = request.form["password"]
        if x == y and x == "admin":
            # Admin login
            return render_template("admin.html")
        else:
            # Check if user exist
            data = viewmoderator()
            for lst in data:
                if str(lst[0]) == str(x) and str(lst[2]) == str(y):
                    return render_template("moderator.html", mode=x)

            return render_template("index.html", status="error")
    return render_template("index.html", status="get")


@app.route("/admin", methods=["POST", "GET"])
def admin():
    return render_template("admin.html")


@app.route("/add_moderator", methods=["POST", "GET"])
def moderator():

    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        paswd = request.form["password"]
        email = request.form["email"]
        phone = request.form["phone"]

        if len(id) == 0:
            return render_template("add_moderator.html", msg="no-data")
        try:
            addmoderator(id, name, paswd, str(email), phone)
            return render_template("add_moderator.html", msg="success")
        except Exception as e:
            print(e)

            return render_template("add_moderator.html", msg="error")
        print(viewmoderator())

    return render_template("add_moderator.html", msg="GET")


@app.route("/add_student", methods=["POST", "GET"])
def add_student():
    if request.method == "POST":
        id = request.form["student_number"]
        name = request.form["name"]
        add = request.form["address"]
        email = request.form["email"]
        phone = request.form["phone"]

        if len(id) == 0:
            return render_template("add_student.html", status="no-data")

        try:
            addstdrec(id, name, phone, add, email)
            return render_template("add_student.html", status="ok")
        except Exception as e:
            print(e)
            return render_template("add_student.html", status="error")

    return render_template("add_student.html", status="success")

@app.route("/add_marks", methods=["POST", "GET"])
def addmarks():
    lst = viewdatastud()
    if request.method == "GET":
        return render_template(
            "add_marks.html", status="get", data=lst, lenght=len(lst)
        )
    try:
        usn = request.form["usnno"]
        internal = request.form["internal"]
        external = request.form["external"]
        attendance = request.form["attendance"]
        final =compute_fuzzy(int(internal), int(external),int(attendance))

        print(final)

        remark = ""
        
        if(float(final) < 50):
            remark = "Poor"
        elif(float(final) < 60):
            remark ="Average"
        elif(float(final) < 70):
            remark = "Good"
        elif(float(final) < 80):
            remark = "Very good"
        else:
            remark = "Exellent"

        addmark(usn, int(internal), int(external), int(attendance), final, remark)

        return render_template(
            "add_marks.html", status="added", data=lst, lenght=len(lst)
        )

    except Exception as e:
        print("Exception:", e)
        return render_template(
            "add_marks.html", status="error", data=lst, lenght=len(lst)
        )

@app.route("/update", methods=["GET", "POST"])
def update():
    lst = viewdatastud()
    try:
        usn = request.form["usnno"]
        internal = request.form["internal"]
        external = request.form["external"]
        attendance = request.form["attendance"]
        
        final = compute_fuzzy(int(internal) , int(external) , int(attendance))
        print(final)

        remark = ""

        if(float(final) < 50):
            remark = "Poor"
        elif(float(final) < 60):
            remark ="Average"
        elif(float(final) < 70):
            remark = "Good"
        elif(float(final) < 80):
            remark = "Very good"
        else:
            remark = "Exellent"

        updatemark(usn, int(internal), int(external), int(attendance), final, remark)
        return render_template(
            "add_marks.html", status="updated", data=lst, lenght=len(lst)
        )

    except Exception as e:
        print("Exception:", e)
        return render_template(
            "add_marks.html", status="error", data=lst, lenght=len(lst)
        )



@app.route("/moderator_section", methods=["POST", "GET"])
def modesection():
    nam = "Moderator"
    if request.method == "POST":
        nam = str(request.form["Uname"])
    return render_template("moderator.html", mode=nam)


@app.route("/performance")
def performance():
    lst = check_marks()
    return render_template("performance.html", data=lst, lenght=len(lst))


@app.route("/view_data")
def view_stud():
    return render_template("view.html")


@app.route("/view_std_data", methods=["POST", "GET"])
def view_std_data():

    if request.method == "POST":
        print(request.form)
        usn = request.form["usn_del"]
        deletestdrec(usn)
    lst = viewdatastud()
    return render_template("view_std_data.html", data=lst, lenght=len(lst))

@app.route("/viewmoddata", methods=["POST", "GET"])
def view_mod_data():

    if request.method == "POST":
        mod = request.form["mod_del"]
        deleterecmoderator(mod)

    lst = viewmoderator()
    return render_template("view_moderator.html", data=lst, lenght=len(lst))

@app.route("/view_sub_data", methods=["POST","GET"])
def view_subject():
    lst = viewsubject()

    if request.method == "POST":
        sub = request.form["deletesubject"]
        deletesub(sub)

    return render_template("view_subject.html", data=lst, lenght=len(lst))

if __name__ == "__main__":
    print("Opening web browser")
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True,host="0.0.0.0")
    
