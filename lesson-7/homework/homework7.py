#vectorclass
import math
class Vector:
    def __init__(self, *components):
        self.components = tuple(components)
    def __repr__(self):
        return f"Vector{self.components}"
    def __add__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))
    def __sub__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))
    def __mul__(self, other):
        if isinstance(other, (int, float)): 
            return Vector(*(a * other for a in self.components))
        elif isinstance(other, Vector):  
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for dot product")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Multiplication only supports scalars or dot product with another vector")
    def __rmul__(self, other):
        return self * other
    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cant normalize a zero vector")
        return Vector(*(a / mag for a in self.components))
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1)          
v3 = v1 + v2
print(v3)          
v4 = v2 - v1
print(v4)          
dot_product = v1 * v2
print(dot_product) 
v5 = 3 * v1
print(v5)          
print(v1.magnitude())  
v_unit = v1.normalize()
print(v_unit)      

#employeerecordsmanageroopversion
import os
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"
class EmployeeManager:
    FILE_NAME = "employees.txt"
    @staticmethod
    def add_employee(employee):
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully")
    @staticmethod
    def view_all_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("Records not found")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = file.readlines()
            if not records:
                print("Records not found")
            else:
                print("Employee Records:")
                for record in records:
                    print(record.strip())
    @staticmethod
    def search_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("Records not found")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for record in file:
                if record.startswith(employee_id + ","):
                    print("Employee Found:")
                    print(record.strip())
                    return
        print("Employee not found")
    @staticmethod
    def update_employee(employee_id, name=None, position=None, salary=None):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("Records not found")
            return
        updated = False
        records = []
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for record in file:
                data = record.strip().split(", ")
                if data[0] == employee_id:
                    if name:
                        data[1] = name
                    if position:
                        data[2] = position
                    if salary:
                        data[3] = salary
                    updated = True
                records.append(", ".join(data))
        if updated:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                for record in records:
                    file.write(record + "\n")
            print("Employee updated successfully")
        else:
            print("Employee not found")
    @staticmethod
    def delete_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("Records not found")
            return
        records = []
        deleted = False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for record in file:
                if not record.startswith(employee_id + ","):
                    records.append(record.strip())
                else:
                    deleted = True
        if deleted:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                for record in records:
                    file.write(record + "\n")
            print("Employee deleted successfully")
        else:
            print("Employee not found")
    @staticmethod
    def menu():
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                EmployeeManager.add_employee(Employee(emp_id, name, position, salary))
            elif choice == "2":
                EmployeeManager.view_all_employees()
            elif choice == "3":
                emp_id = input("Enter Employee ID to search: ")
                EmployeeManager.search_employee(emp_id)
            elif choice == "4":
                emp_id = input("Enter Employee ID to update: ")
                name = input("Enter new Name (press Enter to skip): ") or None
                position = input("Enter new Position (press Enter to skip): ") or None
                salary = input("Enter new Salary (press Enter to skip): ") or None
                EmployeeManager.update_employee(emp_id, name, position, salary)
            elif choice == "5":
                emp_id = input("Enter Employee ID to delete: ")
                EmployeeManager.delete_employee(emp_id)
            elif choice == "6":
                print("Finish")
                break
            else:
                print("Not found, please try again")

#bonuschallenge
import os
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"
class EmployeeManager:
    FILE_NAME = "employees.txt"
    @staticmethod
    def is_unique_employee_id(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            return True
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for record in file:
                if record.startswith(employee_id + ","):
                    return False
        return True
    @staticmethod
    def add_employee(employee):
        if not EmployeeManager.is_unique_employee_id(employee.employee_id):
            print("Error, employee ID must be unique")
            return
        try:
            with open(EmployeeManager.FILE_NAME, "a") as file:
                file.write(str(employee) + "\n")
            print("Employee added successfully")
        except IOError:
            print("Error, unable to write to file")
    @staticmethod
    def view_all_employees(sort_by=None):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("Records not found")
            return
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                records = [line.strip().split(", ") for line in file.readlines()]
                if not records:
                    print("Records not found")
                    return
                if sort_by == "salary":
                    records.sort(key=lambda x: float(x[3]))
                elif sort_by == "name":
                    records.sort(key=lambda x: x[1])
                print("Employee Records:")
                for record in records:
                    print(", ".join(record))
        except IOError:
            print("Error, unable to read file")
    @staticmethod
    def search_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("Records not found")
            return
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                for record in file:
                    if record.startswith(employee_id + ","):
                        print("Employee Found:")
                        print(record.strip())
                        return
            print("Employee not found")
        except IOError:
            print("Error, unable to read file")
    @staticmethod
    def update_employee(employee_id, name=None, position=None, salary=None):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("Records not found")
            return
        updated = False
        records = []
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                for record in file:
                    data = record.strip().split(", ")
                    if data[0] == employee_id:
                        if name:
                            data[1] = name
                        if position:
                            data[2] = position
                        if salary:
                            data[3] = salary
                        updated = True
                    records.append(", ".join(data))
            if updated:
                with open(EmployeeManager.FILE_NAME, "w") as file:
                    for record in records:
                        file.write(record + "\n")
                print("Employee updated successfully!")
            else:
                print("Employee not found")
        except IOError:
            print("Error, unable to update file")
    @staticmethod
    def delete_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("Records not found")
            return
        records = []
        deleted = False
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                for record in file:
                    if not record.startswith(employee_id + ","):
                        records.append(record.strip())
                    else:
                        deleted = True
            if deleted:
                with open(EmployeeManager.FILE_NAME, "w") as file:
                    for record in records:
                        file.write(record + "\n")
                print("Employee deleted successfully!")
            else:
                print("Employee not found")
        except IOError:
            print("Error")
    @staticmethod
    def menu():
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. View sorted employee records (by name or salary)")
            print("4. Search for an employee by Employee ID")
            print("5. Update an employee's information")
            print("6. Delete an employee record")
            print("7. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                EmployeeManager.add_employee(Employee(emp_id, name, position, salary))
            elif choice == "2":
                EmployeeManager.view_all_employees()
            elif choice == "3":
                sort_by = input("Sort by 'name' or 'salary': ")
                EmployeeManager.view_all_employees(sort_by)
            elif choice == "4":
                emp_id = input("Enter Employee ID to search: ")
                EmployeeManager.search_employee(emp_id)
            elif choice == "5":
                emp_id = input("Enter Employee ID to update: ")
                name = input("Enter new Name (press Enter to skip): ") or None
                position = input("Enter new Position (press Enter to skip): ") or None
                salary = input("Enter new Salary (press Enter to skip): ") or None
                EmployeeManager.update_employee(emp_id, name, position, salary)
            elif choice == "6":
                emp_id = input("Enter Employee ID to delete: ")
                EmployeeManager.delete_employee(emp_id)
            elif choice == "7":
                print("END")
                break
            else:
                print("Invalid choice! Please try again")

#todoapplication
import os
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name.strip()
        self.position = position.strip()
        self.salary = float(salary) if salary.replace('.', '', 1).isdigit() else 0.0
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"
class EmployeeManager:
    FILE_NAME = "employees.txt"
    @staticmethod
    def is_unique_employee_id(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            return True
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for record in file:
                if record.startswith(employee_id + ","):
                    return False
        return True
    @staticmethod
    def add_employee(employee):
        if not employee.employee_id.isdigit():
            print("Error, employee ID must be numeric")
            return
        if not EmployeeManager.is_unique_employee_id(employee.employee_id):
            print("Error, employee ID must be unique")
            return
        try:
            with open(EmployeeManager.FILE_NAME, "a") as file:
                file.write(str(employee) + "\n")
            print("Employee added successfully")
        except IOError:
            print("Error, unable to write to file")
    @staticmethod
    def view_all_employees(sort_by=None):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("Records not found")
            return
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                records = [line.strip().split(", ") for line in file.readlines()]
                if not records:
                    print("Records not found")
                    return
                if sort_by == "salary":
                    records.sort(key=lambda x: float(x[3]))
                elif sort_by == "name":
                    records.sort(key=lambda x: x[1])
                print("Employee Records:")
                for record in records:
                    print(", ".join(record))
        except IOError:
            print("Error, unable to read file")
    @staticmethod
    def search_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("Records not found")
            return
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                for record in file:
                    if record.startswith(employee_id + ","):
                        print("Employee Found:")
                        print(record.strip())
                        return
            print("Employee not found")
        except IOError:
            print("Error, unable to read file")
    @staticmethod
    def update_employee(employee_id, name=None, position=None, salary=None):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("Records not found")
            return
        updated = False
        records = []
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                for record in file:
                    data = record.strip().split(", ")
                    if data[0] == employee_id:
                        if name:
                            data[1] = name.strip()
                        if position:
                            data[2] = position.strip()
                        if salary:
                            try:
                                data[3] = str(float(salary))
                            except ValueError:
                                print("Error, salary must be a valid number")
                                return
                        updated = True
                    records.append(", ".join(data))
            if updated:
                with open(EmployeeManager.FILE_NAME, "w") as file:
                    for record in records:
                        file.write(record + "\n")
                print("Employee updated successfully")
            else:
                print("Employee not found")
        except IOError:
            print("Error, unable to update file")
    @staticmethod
    def delete_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("Records not found")
            return
        records = []
        deleted = False
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                for record in file:
                    if not record.startswith(employee_id + ","):
                        records.append(record.strip())
                    else:
                        deleted = True
            if deleted:
                with open(EmployeeManager.FILE_NAME, "w") as file:
                    for record in records:
                        file.write(record + "\n")
                print("Employee deleted successfully")
            else:
                print("Employee not found")
        except IOError:
            print("Error, unable to modify file") 
    @staticmethod
    def menu():
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. View sorted employee records (by name or salary)")
            print("4. Search for an employee by Employee ID")
            print("5. Update an employee's information")
            print("6. Delete an employee record")
            print("7. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                EmployeeManager.add_employee(Employee(emp_id, name, position, salary))
            elif choice == "2":
                EmployeeManager.view_all_employees()
            elif choice == "3":
                sort_by = input("Sort by 'name' or 'salary': ")
                EmployeeManager.view_all_employees(sort_by)
            elif choice == "4":
                emp_id = input("Enter Employee ID to search: ")
                EmployeeManager.search_employee(emp_id)
            elif choice == "5":
                emp_id = input("Enter Employee ID to update: ")
                name = input("Enter new Name (press Enter to skip): ") or None
                position = input("Enter new Position (press Enter to skip): ") or None
                salary = input("Enter new Salary (press Enter to skip): ") or None
                EmployeeManager.update_employee(emp_id, name, position, salary)
            elif choice == "6":
                emp_id = input("Enter Employee ID to delete: ")
                EmployeeManager.delete_employee(emp_id)
            elif choice == "7":
                print("END")
                break
            else:
                print("Please try again.")
