# bool q1
username = input("Enter your username: ")
password = input("Enter your password: ")
if username and password:
    print("Both username and password are provided")
else:
    print("Username and password are not provided")

# bool q2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 == num2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

# bool q3
num = int(input("Enter the number: "))
if num > 0 and num % 2 == 0:
    print("The number is positive and even")
else:
    print("The number is either not positive or not even")

# bool q4
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 != num2 and num1 != num3 and num2 != num3:
    print("All the numbers are different")
else:
    print("At least two of the numbers are the same")

# bool q5
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) == len(string2):
    print("The strings have the same length")
else:
    print("The strings do not have the same length")

# bool q6
num = int(input("Enter the number: "))
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")

# bool q7
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 + num2 > 50.8:
    print("The sum of the numbers is greater than 50.8")
else:
    print("The sum of the numbers is not greater than 50.8")

# bool q8
num = float(input("Enter the number: "))
if 10 <= num <= 20:
    print("The number is between 10 and 20 (inclusive)")
else:
    print("The number is not between 10 and 20")






