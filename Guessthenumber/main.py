#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import os
import random

go = "no"
while go == "no":
  os.system("cls")
  print (art.logo)
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100.")
  print("Please choose an existing difficulty.")
  difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    attempts = 10
    go = "yes"
  elif difficulty =="hard":
    attempts = 5
    go = "yes"
    

def play(number):
  guess=int(input("Make a guess: "))
  if guess > number:
    print("Too high.")
    return attempts-1
  elif guess < number:
    print("Too low.")
    return attempts-1
  elif guess == number:
    print(art.win_logo)
    return 11

number = random.randint(1 ,100)
while attempts > 0 and attempts !=11: 
  print(f"You have {attempts} remaining yo guess the number.")
  attempts = play(number)
  if attempts == 0:
    print("You lose")