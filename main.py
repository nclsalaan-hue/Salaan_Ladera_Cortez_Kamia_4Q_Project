import sqlite3
import re

# Database
DB_NAME = "students.db"
def connect_db():
    return sqlite3.connect(DB_NAME)

# Add student
def add_student():
    return

# View students
def view_students():
    return

# Update student
def update_student():
    return

# Delete students
def delete_student():
    return

# Main
while True:
    print("""
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Terminating")
        break
    else:
        print("Invalid choice.")

def add_student():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            email TEXT
        )
    """)

    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")

    if not age.isdigit():
        print("Invalid age.")
        conn.close()
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email.")
        conn.close()
        return

    cursor.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
                   (name, int(age), email))

    conn.commit()
    conn.close()
    print("Student added.")


def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No students found.")
    else:
        for row in rows:
            print(row)

    conn.close()

def update_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = input("Enter ID to update: ")

    if not student_id.isdigit():
        print("Invalid ID.")
        conn.close()
        return

    name = input("Enter new name: ")
    age = input("Enter new age: ")
    email = input("Enter new email: ")

    if not age.isdigit():
        print("Invalid age.")
        conn.close()
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email.")
        conn.close()
        return

    cursor.execute("""
        UPDATE students
        SET name = ?, age = ?, email = ?
        WHERE id = ?
    """, (name, int(age), email, int(student_id)))

    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        print("Student updated.")

    conn.commit()
    conn.close()


def delete_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = input("Enter ID to delete: ")

    if not student_id.isdigit():
        print("Invalid ID.")
        conn.close()
        return

    cursor.execute("DELETE FROM students WHERE id = ?", (int(student_id),))

    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        print("Student deleted.")

    conn.commit()
    conn.close()


# final update before submission!!!!