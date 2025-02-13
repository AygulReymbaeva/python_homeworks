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

# string q1
name = input("What's your name? ")
birth_year = int(input("What year were you born? "))
age = 2025-birth_year
print(f"{name}, you are {age} years old")

# string q2
txt = "LMaasleitbtui"
print("Car names are:", txt[0::2], txt[1::2])

# string q3
user_input = input("Please enter a word: ")
print(f"\nThe length of the word is: {len(user_input)}")
uppercase_string = user_input.upper()
print(f"The word in uppercase: {uppercase_string}")
lowercase_string = user_input.lower()
print(f"The word in lowercase: {lowercase_string}")

# string q4
user_input = input("Please enter a word: ")
formatted_input = user_input.replace(" ", "").lower()
if formatted_input == formatted_input[::-1]:
    print(f"The word '{user_input}' is a palindrome!")
else:
    print(f"The word '{user_input}' is not a palindrome.")

# string q5
word = input("Please enter the word: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in user_input:
        if char.isalpha():  
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
print(f"\nIn the word '{user_input}':")
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")

# string q6
word1 = input("Please enter the first word: ")
word2 = input("Please enter the second word: ")
if word2 in word1:
    print(f"The string '{word1}' contains '{word2}' ")
else:
    print(f"The string '{word1}' does not contain '{word2}' ")

# string q7
sentence = input("Please enter a sentence: ")
word_to_replace = input("Enter the word you want to replace: ")
replacement_word = input("Enter the word to replace it with: ")
modified_sentence = sentence.replace(word_to_replace, replacement_word)
print(f"\nModified sentence: {modified_sentence}")

# string q8
user_input = input("Please enter a word: ")
if len(user_input) > 0:
    first_char = user_input[0]
    last_char = user_input[-1]
    print(f"The first character is: {first_char}")
    print(f"The last character is: {last_char}")
else:
    print("The word is empty")

# string q9
user_input = input("Please enter a word: ")
reversed_word = user_input[::-1]
print(f"The reversed word is: {reversed_word}")

# string q10
