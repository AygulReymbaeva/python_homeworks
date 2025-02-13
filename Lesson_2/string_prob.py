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
sentence = input("Please enter a sentence: ")
words = sentence.split()
num_words = len(words)
print("The number of words in the sentence is: ", num_words)

# string q11
string = input("Please enter: ")
if any(char.isdigit() for char in string):
    print("The string contains digits")
else:
    print("The string does not contain digits")

# string q12
words = input("Please enter your words: ")
separator = ","
result = separator.join(words)
print(result)

# string q13
string = input("Please enter a string: ")
no_spaces = string.replace(" ", "")
print("String without spaces:", no_spaces)

# string q14
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string1 == string2:
    print("The strings are equal")
else:
    print("The strings are not equal") 
    
# string q15
sentence = input("Enter the sentence: ")
words = sentence.split()
acronym = ''.join(word[0].upper() for word in words)
print("Acronym:", acronym) 

# string q16
string = input("Enter the string: ")
char_to_remove = input("Enter the character to remove: ")
final_string = string.replace(char_to_remove, "")
print("Final string:", final_string) 

# string q17
string = input("Enter the string: ")
symbol = "*"
vowels = "aeiouAEIOU"
final_string = "".join(symbol if char in vowels else char for char in string)
print("Final string:", final_string) 

# string q18
string = input("Enter the string: ")
start_word = input("Enter the word to check if the string starts with: ")
end_word = input("Enter the word to check if the string ends with: ")

if string.startswith(start_word) and string.endswith(end_word):
    print("The string starts with '{}' and ends with '{}' ".format(start_word, end_word))
else:
    print("Sentence doesn't start and end with these words")
