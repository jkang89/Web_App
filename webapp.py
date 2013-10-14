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
def get_project():
    hackbright_app.connect_to_db()
    project_title = request.args.get("project")
    project = hackbright_app.get_project_by_title(project_title)
    return render_template("get_project.html", project = project)

if __name__ == "__main__":
    app.run(debug=True)