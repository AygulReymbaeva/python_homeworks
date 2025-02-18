#q1
def uncommon_elements(list1, list2):
    result = []
    for num in list1:
        if num not in list2:
            result.append(num)
    for num in list2:
        if num not in list1:
            result.append(num)
    return result
list1 = [1, 1, 2]
list2 = [2, 3, 4]
print(uncommon_elements(list1, list2))  

from collections import Counter

def uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)
    uncommon = []
    for num in list1:
        if num not in list2:
            uncommon.extend([num] * count1[num])
    for num in list2:
        if num not in list1:
            uncommon.extend([num] * count2[num])
    return uncommon
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(uncommon_elements(list1, list2))  

from collections import Counter

def uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)
    uncommon = []
    for num in count1:
        if num not in count2:
            uncommon.extend([num] * count1[num])
    for num in count2:
        if num not in count1:
            uncommon.extend([num] * count2[num])
    return uncommon
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
print(uncommon_elements(list1, list2))  

#q2
def print_squares(n):
    for i in range(1, n): 
        print(i * i)  
n = 5
print_squares(n)

#q3
def modify_text(txt):
    vowels = "aeiouAEIOU"
    result = []
    i = 0  
    while i < len(txt):
        result.append(txt[i])
        if (i + 1) % 3 == 0:
            result.append("_")
        if txt[i] in vowels and i + 1 < len(txt):
            result.append(txt[i + 1])
            result.append("_")
            i += 1  
        i += 1  
    if result and result[-1] == "_":
        result.pop()
    return "".join(result)
txt = "hello"
print(modify_text(txt))  

def modify_text(txt):
    vowels = "aeiouAEIOU"
    result = []
    i = 0  
    while i < len(txt):
        result.append(txt[i])
        if (i + 1) % 3 == 0:
            result.append("_")
        if txt[i] in vowels and i + 1 < len(txt):
            result.append(txt[i + 1])
            result.append("_")
            i += 1  
        i += 1  
    if result and result[-1] == "_":
        result.pop()
    return "".join(result)
txt = "assalom"
print(modify_text(txt)) 

def modify_text(txt):
    vowels = "aeiouAEIOU"
    result = []
    i = 0  
    while i < len(txt):
        result.append(txt[i])
        if (i + 1) % 3 == 0:
            result.append("_")
        if txt[i] in vowels and i + 1 < len(txt):
            result.append(txt[i + 1])
            result.append("_")
            i += 1  
        i += 1  
    if result and result[-1] == "_":
        result.pop()
    return "".join(result)
txt = "abcabcdabcdeabcdefabcdefg"
print(modify_text(txt)) 

#q4
import random
def number_guessing_game():
    while True:
        number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10
        print("Welcome to the Number Guessing Game!")
        print("I have selected a number between 1 and 100")
        print("You have 10 attempts to guess it")
        while attempts < max_attempts:
            guess = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: ")
            if not guess.isdigit():
                print("Please enter a valid number!")
                continue
            guess = int(guess)
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("You guessed it right!")
                break  
        if attempts == max_attempts and guess != number:
            print("You lost. Want to play again?")
        play_again = input("Type 'Y', 'YES',  or 'ok' to play again: ").lower()
        if play_again not in ['y', 'yes', 'ok']:
            print("Thanks for playing!")
            break  
number_guessing_game()

#q5
def password_checker():
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password is too short")
    elif not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter")
    else:
        print("Password is strong")
password_checker()

#q6
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
for num in range(1, 101):
    if is_prime(num):
        print(num)

#bonus-challenge
import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors! First to 5 points wins")
    while player_score < 5 and computer_score < 5:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            player_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!")
        print(f"Scores: You - {player_score}, Computer - {computer_score}")
    if player_score == 5:
        print("Congratulations, you won the match!")
    else:
        print("The computer won the match")
rock_paper_scissors()
