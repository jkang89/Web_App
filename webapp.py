from flask import Flask, render_template, request 
import hackbright_app

app = Flask(__name__)

@app.route("/student")
def getstudent():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)
    grades = hackbright_app.show_grades(student_github)
    html = render_template("student_info.html", first_name = row[0],
                                                last_name = row[1],
                                                github = row[2],
                                                grades = grades)
    return html

@app.route("/")
def get_github():
    return render_template("get_github.html")

@app.route("/project")
# all students and their grades for a particular project 
def get_project():
    hackbright_app.connect_to_db()
    project_title = request.args.get("project")
    projects = hackbright_app.show_grades_by_project(project_title)
    html = render_template("get_project.html", projects = projects)

    return html

@app.route("/register")
def create_new_student():
    return render_template("register.html")

@app.route("/success")
def register_success():
    hackbright_app.connect_to_db()
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    student_github = request.args.get("github")
    message = hackbright_app.make_new_student(first_name, last_name, student_github)

    return render_template("success.html")

@app.route("/new_project")
def new_project():
    return render_template("new_project.html")

@app.route("/new_project_success")
def new_project_success():
    hackbright_app.connect_to_db()
    project_title = request.args.get("project_title")
    project_description = request.args.get("project_description")
    max_grade = request.args.get("max_grade")
    message = hackbright_app.make_new_project(project_title, project_description, max_grade)

    return render_template("new_project_success.html")

@app.route("/enter_grade")
def enter_grade():
    return render_template("enter_grade.html")

@app.route("/enter_grade_success")
def enter_grade_success():
    hackbright_app.connect_to_db()
    student_github = request.args.get("student_github")
    project_title = request.args.get("project_title")
    student_grade = request.args.get("student_grade")
    message = hackbright_app.make_grade(student_github, project_title, student_grade)

    return render_template("enter_grade_success.html")

if __name__ == "__main__":
    app.run(debug=True)