# Name : Mr Muhammad Ali
# Date 27-Sep-2019
# Description : A number guessing game !

import random

name = input("Hello what is your name? ")
number = random.randint(1, 100)
print("Hi " + name + ", I'm thinking of a number between 1 to 100.")
guessesTaken = 0

while guessesTaken < 5:
    guess = input ("Enter a guess: ")
    guess = int(guess)
    guessesTaken += 1
    
    if guess < number :
        print("That was too low")
    elif guess > number:
        print("That was too high")
    else:
        break

if guess == number:
    print("winner winner, Chicken dinner! Congrats " + name + " you guessed the correct number ! ")    
else:
    print("you loose, too bad. beter luck next time. The right number was", number)
