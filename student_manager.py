
import csv
import os

filename = "student_dropout_behavior_dataset.csv"

def display_students():
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_student():
    student_id = input("Enter student ID to search: ")

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader, None)

        for row in reader:
            if row and row[0] == student_id:
                print("Student found:", row)
                return

    print("Student not found.")

while True:
    print("\n===== STUDENT DATA MANAGER =====")
    print("1. Display student records")
    print("2. Search student by ID")
    print("3. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            display_students()
        elif choice == "2":
            search_student()
        elif choice == "3":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Try again.")

    except FileNotFoundError:
        print("Dataset file not found. Check the filename.")
    except PermissionError:
        print("Permission denied while accessing the file.")