#task1
class BookNotFoundException(Exception):
    pass
class BookAlreadyBorrowedException(Exception):
    pass
class MemberLimitExceededException(Exception):
    pass
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed 3 books")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed")
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'")
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} didn't borrow '{book.title}'")
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title} by {book.author}")
    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member.name}")
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"The book '{title}' was not found in the library")
    def borrow_book(self, member_name, book_title):
        member = self.get_member(member_name)
        book = self.find_book(book_title)
        member.borrow_book(book)
    def return_book(self, member_name, book_title):
        member = self.get_member(member_name)
        book = self.find_book(book_title)
        member.return_book(book)
    def get_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        raise Exception(f"Member '{name}' not found")
    def show_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(book)
    def show_members(self):
        print("\nLibrary Members:")
        for member in self.members:
            print(f"{member.name} - Borrowed: {[book.title for book in member.borrowed_books]}")
library = Library()
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.add_member(Member("Aygul"))
library.add_member(Member("Ayziya"))
library.show_books()
library.show_members()
try:
    library.borrow_book("Aygul", "1984")
    library.borrow_book("Aygul", "The Great Gatsby")
    library.borrow_book("Aygul", "To Kill a Mockingbird")
    library.borrow_book("Aygul", "Nonexistent Book")
except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
    print(f"Error: {e}")
try:
    library.borrow_book("Ayziya", "The Midnight Library")
except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
    print(f"Error: {e}")
try:
    library.borrow_book("Ayziya", "1984")
except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
    print(f"Error: {e}")
library.return_book("Aygul", "1984")
try:
    library.borrow_book("Ayziya", "1984")
except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
    print(f"Error: {e}")
library.show_books()
library.show_members()

#task2
import csv
from collections import defaultdict
grades_data = [
    ["Name", "Subject", "Grade"],
    ["Aygul", "Math", "85"],
    ["Ayziya", "Science", "90"],
    ["Azizbek", "Math", "83"],
    ["Aziza", "History", "74"]
]
with open("grades.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(grades_data)
print("grades.csv file created.")
grades_list = []
with open("grades.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Grade"] = int(row["Grade"])  
        grades_list.append(row)
print("\nGrades Data:")
for row in grades_list:
    print(row)
subject_totals = defaultdict(list)
for row in grades_list:
    subject = row["Subject"]
    grade = row["Grade"]
    subject_totals[subject].append(grade)
average_grades = []
for subject, grades in subject_totals.items():
    avg = sum(grades) / len(grades)
    average_grades.append({"Subject": subject, "Average Grade": round(avg, 1)})
print("\nAverage Grades:")
for avg in average_grades:
    print(avg)
with open("average_grades.csv", mode="w", newline="") as file:
    fieldnames = ["Subject", "Average Grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(average_grades)
print("\naverage_grades.csv file created.")

#task3
import json
import csv
tasks_data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]
with open("tasks.json", "w") as file:
    json.dump(tasks_data, file, indent=4)
print("tasks.json file created")
def load_tasks():
    with open("tasks.json", "r") as file:
        return json.load(file)
def display_tasks(tasks):
    print("\nTasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print("\nChanges saved to tasks.json")
def task_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(task["completed"] for task in tasks)
    pending_tasks = total_tasks - completed_tasks
    average_priority = round(sum(task["priority"] for task in tasks) / total_tasks, 1) if total_tasks else 0
    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority}")
def convert_tasks_to_csv(tasks):
    with open("tasks.csv", "w", newline="") as file:
        fieldnames = ["ID", "Task", "Completed", "Priority"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                "ID": task["id"],
                "Task": task["task"],
                "Completed": task["completed"],
                "Priority": task["priority"]
            })
    print("\ntasks.csv file created")
tasks = load_tasks()
display_tasks(tasks)
task_statistics(tasks)
tasks[0]["completed"] = True
save_tasks(tasks)
convert_tasks_to_csv(tasks)
