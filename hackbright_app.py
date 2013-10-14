import sqlite3

CONN = sqlite3.connect("hackbright.db")
DB = CONN.cursor()

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    return row



def get_project_by_title(title):
    query = """SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    return row

def get_grade_by_project(project_title):
    query = """SELECT student_github, project_title, grade FROM Grades WHERE project_title = ?"""
    DB.execute(query, (project_title,))
    row = DB.fetchone()
    print """\
Student: %s
Project: %s
Grade: %s""" %(row[0], row[1], row[2])

def show_grades(student_github):
    query = """SELECT student_github, project_title, grade FROM Grades WHERE student_github = ?"""
    DB.execute(query, (student_github,))
    rows = DB.fetchall()
    return rows 

def show_grades_by_project(project_title):
    query = """SELECT student_github, project_title, grade FROM Grades WHERE project_title = ?"""
    DB.execute(query, (project_title,))
    rows = DB.fetchall()
    return rows 

def make_new_project(title, description, max_grade):
    query = """INSERT into Projects values (?, ?, ?)"""
    DB.execute(query, (title, description, max_grade))

    CONN.commit()
    print "Successfully added project: %s" % title

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))

    CONN.commit()
    return "Success"

def make_grade(student_github, project_title, grade):
    query = """INSERT into Grades values (?, ?, ?)"""
    DB.execute(query, (student_github, project_title, grade))

    CONN.commit()
    print "Successfully added grade: %s" % (grade)


def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split(",")
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args)
        elif command == "project":
            get_project_by_title(*args)
        elif command == "new_student":
            make_new_student(*args)
        elif command == "new_project":
            make_new_project(*args)
        elif command == "get_grade":
            get_grade_by_project(*args)
        elif command == "make_grade":
            make_grade(*args)
        elif command == "show_grades":
            show_grades(*args)

    CONN.close()

if __name__ == "__main__":
    main()
