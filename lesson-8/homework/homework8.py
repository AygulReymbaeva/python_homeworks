#Q1
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
class Cow(Animal):
    def __init__(self, name, age, milk_production):
        super().__init__(name, age)
        self.milk_production = milk_production  
    def moo(self):
        print(f"{self.name} says Moo")
    def produce_milk(self):
        print(f"{self.name} produces {self.milk_production} liters of milk per day")
class Chicken(Animal):
    def __init__(self, name, age, egg_production):
        super().__init__(name, age)
        self.egg_production = egg_production  
    def cluck(self):
        print(f"{self.name} says paq-paq")
    def lay_eggs(self):
        print(f"{self.name} lays {self.egg_production} eggs per day")
class Horse(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed      
    def neigh(self):
        print(f"{self.name} says Nyeaah")
    def run(self):
        print(f"{self.name} runs at {self.speed} km/h")
cow = Cow("lucy", 5, 10)
chicken = Chicken("little ", 2, 5)
horse = Horse("Samo", 7, 50)
cow.eat()
cow.moo()
cow.produce_milk()
chicken.eat()
chicken.cluck()
chicken.lay_eggs()
horse.eat()
horse.neigh()
horse.run()

#Q2
import json
import random
class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")
    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}
class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    def create_account(self, name, initial_deposit):
        account_number = random.randint(10000, 99999)
        while account_number in self.accounts:
            account_number = random.randint(10000, 99999)
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}, Name: {account.name}, Balance: {account.balance}")
        else:
            print("Account not found")
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found")
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found")
    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            json.dump({acc: self.accounts[acc].to_dict() for acc in self.accounts}, file)
    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                data = json.load(file)
                self.accounts = {int(acc): Account(int(acc), val["name"], val["balance"]) for acc, val in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}
bank = Bank()
bank.create_account("Aygul", 500)
bank.view_account(10001)  
bank.deposit(10001, 200)
bank.withdraw(10001, 100)
