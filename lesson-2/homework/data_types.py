# data types question 1
number = float(input("Enter the float number: "))
rounded_number = round(number, 2)
print(f"Rounded number: {rounded_number}")
print("Please enter the float number")

# data types question 2
a1 = int(input("Enter the number: "))
a2 = int(input("Enter the number: "))
a3 = int(input("Enter the number: ")) 

largest = max(a1, a2, a3)
smallest = min(a1, a2, a3)
print(f"The largest number is : {largest}")
print(f"The smallest number is : {smallest}")

# data types question 3
km = float(input("Enter the kilometer: "))
m = km * 1000
cm = km * 100_000
print(f"\n{km} kilometers is equal to: ")
print(f"{m} meters")
print(f"{cm} centimeters")

# data types question 4
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number : "))
quotient = num1 // num2
remainder = num1 % num2
print(f"\nResults for dividing {num1} by {num2}:")
print(f"Quotient): {quotient}")
print(f"Remainder: {remainder}")

# data types question 5
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"\n{celsius}°C is equal to {fahrenheit}°F")

# data types question 6
num = int(input("Enter a number: "))
last_digit = abs(num) % 10
print(f"The last digit of {num} is: {last_digit}")

# data types question 7
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is and odd number")