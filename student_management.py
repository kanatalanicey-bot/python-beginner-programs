
import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def get_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def add_student(students):
    print("\n--- Add Student ---")
    roll = input("Enter roll number: ").strip()

    if not roll:
        print("Roll number cannot be empty.")
        return

    if roll in students:
        print("A student with this roll number already exists.")
        return

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    department = input("Enter department: ").strip()
    marks = get_marks()

    students[roll] = {
        "name": name,
        "department": department,
        "marks": marks,
        "grade": calculate_grade(marks)
    }

    save_students(students)
    print("Student added successfully!")


def view_students(students):
    print("\n--- All Students ---")

    if not students:
        print("No student records found.")
        return

    print("-" * 75)
    print(f"{'Roll No':<12}{'Name':<22}"
          f"{'Department':<18}{'Marks':<10}{'Grade'}")
    print("-" * 75)

    for roll, details in sorted(students.items()):
        print(
            f"{roll:<12}"
            f"{details['name']:<22}"
            f"{details['department']:<18}"
            f"{details['marks']:<10.1f}"
            f"{details['grade']}"
        )

    print("-" * 75)


def search_student(students):
    print("\n--- Search Student ---")
    roll = input("Enter roll number: ").strip()

    if roll not in students:
        print("Student not found.")
        return

    details = students[roll]
    print("\nStudent Details")
    print("Roll Number:", roll)
    print("Name:", details["name"])
    print("Department:", details["department"])
    print("Marks:", details["marks"])
    print("Grade:", details["grade"])


def update_student(students):
    print("\n--- Update Student ---")
    roll = input("Enter roll number: ").strip()

    if roll not in students:
        print("Student not found.")
        return

    details = students[roll]

    print("Press Enter to keep the existing value.")

    name = input(f"Name [{details['name']}]: ").strip()
    department = input(
        f"Department [{details['department']}]: "
    ).strip()

    if name:
        details["name"] = name

    if department:
        details["department"] = department

    change_marks = input("Update marks? (y/n): ").strip().lower()

    if change_marks == "y":
        details["marks"] = get_marks()
        details["grade"] = calculate_grade(details["marks"])

    save_students(students)
    print("Student updated successfully!")


def delete_student(students):
    print("\n--- Delete Student ---")
    roll = input("Enter roll number: ").strip()

    if roll not in students:
        print("Student not found.")
        return

    confirm = input(
        f"Delete {students[roll]['name']}? (y/n): "
    ).strip().lower()

    if confirm == "y":
        del students[roll]
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")


def show_statistics(students):
    print("\n--- Student Statistics ---")

    if not students:
        print("No records available.")
        return

    marks = [details["marks"] for details in students.values()]
    average = sum(marks) / len(marks)

    print("Total students:", len(students))
    print(f"Average marks: {average:.2f}")
    print(f"Highest marks: {max(marks):.2f}")
    print(f"Lowest marks: {min(marks):.2f}")

    passed = sum(mark >= 40 for mark in marks)
    print("Passed (40 or above):", passed)
    print("Below 40:", len(marks) - passed)


def main():
    students = load_students()

    while True:
        print("\n" + "=" * 38)
        print("   STUDENT MANAGEMENT SYSTEM")
        print("=" * 38)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. View Statistics")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_statistics(students)
        elif choice == "7":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
