#zerocheckdec
def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper
@check
def div(a, b):
    return a / b
print(div(6, 2))  
print(div(6, 0))  

#employeerecords
#q1
def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee record added successfully!")
add_employee()
#q2
import os

def ensure_file():
    if not os.path.exists("employees.txt"):
        with open("employees.txt", "w") as file:
            pass 
def add_employee():
    ensure_file()
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ").strip()
        name = input("Enter Name: ").strip()
        position = input("Enter Position: ").strip()
        salary = input("Enter Salary: ").strip()
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print(" Employee record added successfully!\n")

def view_employees():
    ensure_file()
    if os.stat("employees.txt").st_size == 0:
        print(" No records found!\n")
        return
    print("\n Employee Records:")
    with open("employees.txt", "r") as file:
        for line in file:
            print(line.strip())
    print()

def search_employee():
    ensure_file()
    emp_id = input(" Enter Employee ID to search: ").strip()
    found = False
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                print("\n Employee Found:")
                print(line.strip())
                found = True
                break
    if not found:
        print(" Employee not found!\n")

def update_employee():
    ensure_file()
    emp_id = input(" Enter Employee ID to update: ").strip()
    updated_records = []
    found = False
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                print("\nCurrent Record: ", line.strip())
                name = input("Enter new Name: ").strip()
                position = input("Enter new Position: ").strip()
                salary = input("Enter new Salary: ").strip()
                updated_records.append(f"{emp_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                updated_records.append(line)
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)
        print(" Employee record updated successfully!\n")
    else:
        print(" Employee ID not found!\n")

def delete_employee():
    ensure_file()
    emp_id = input("Enter Employee ID to delete: ").strip()
    updated_records = []
    found = False
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                print("\nDeleting Record: ", line.strip())
                found = True
            else:
                updated_records.append(line)
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)
        print(" Employee record deleted successfully!\n")
    else:
        print(" Employee ID not found!\n")
def main():
    ensure_file()
    while True:
        print("\n Employee Records Manager")
        print(" Add new employee record")
        print(" View all employee records")
        print(" Search for an employee by Employee ID")
        print(" Update an employee's information")
        print(" Delete an employee record")
        print(" Exit")
        choice = input("➡ Enter your choice: ").strip()
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice! Please enter a number between 1 and 6.\n")
if __name__ == "__main__":
    main()


#wordfrequencycounter
#q1
import os
import string
from collections import Counter
def ensure_file():
    if not os.path.exists("sample.txt"):
        print(" 'sample.txt' not found. Please create one")
        text = input("Enter text to save in 'sample.txt':\n")
        with open("sample.txt", "w") as file:
            file.write(text)
        print(" File created successfully!\n")
def count_words():
    ensure_file()  
    with open("sample.txt", "r") as file:
        text = file.read().lower()  
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    word_counts = Counter(words)
    total_words = sum(word_counts.values())
    top_words = word_counts.most_common(5)
    print("\n Word Frequency Report")
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} time{'s' if count > 1 else ''}")
    with open("word_count_report.txt", "w") as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write("Top 5 Words:\n")
        for word, count in top_words:
            report.write(f"{word} - {count}\n")
    print("\n Report saved to 'word_count_report.txt'")
count_words()

#bonustask
import os
import string
from collections import Counter
def ensure_file():
    if not os.path.exists("sample.txt"):
        print(" 'sample.txt' not found. Please create one")
        text = input("Enter text to save in 'sample.txt':\n")
        with open("sample.txt", "w") as file:
            file.write(text)
        print(" File created successfully!\n")
def count_words():
    ensure_file()  
    word_counts = Counter()
    with open("sample.txt", "r") as file:
        for line in file:
            line = line.lower().translate(str.maketrans("", "", string.punctuation))  
            words = line.split()
            word_counts.update(words) 
    total_words = sum(word_counts.values())
    try:
        top_n = int(input("Enter how many top common words to display: "))
        if top_n <= 0:
            print(" Invalid number! Defaulting to top 5 words")
            top_n = 5
    except ValueError:
        print(" Invalid input! Defaulting to top 5 words")
        top_n = 5
    top_words = word_counts.most_common(top_n)
    print("\n Word Frequency Report")
    print(f"Total words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in top_words:
        print(f"{word} - {count} time{'s' if count > 1 else ''}")
    with open("word_count_report.txt", "w") as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write(f"Top {top_n} Words:\n")
        for word, count in top_words:
            report.write(f"{word} - {count}\n")
    print("\n Report saved to 'word_count_report.txt'")
count_words()
