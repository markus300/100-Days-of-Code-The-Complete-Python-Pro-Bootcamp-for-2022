from art import logo
from art import vs
from game_data import data
import random
import os
#Know the amount of data in "data"
# count = 0
# for x in data:
#   count += 1
# print (count)
# the print is 50 so is 49 the last index
person1 = random.randint(0,49)
def compare(person1,person2,guess):
  if data[person1]["description"]<data[person2]["description"]:
    compare = "a"
  elif data[person1]["description"]>data[person2]["description"]:
    compare = "b"
  else:
    return "True"
    
  if guess == compare:
    return "True"
  else:
    return "False"
  

def play(person1):
  win= "True"
  score = 0
  while win == "True":
    os.system("cls")
    person2 = random.randint(0,49)
    print (logo)
    if score >0:
      print(f"You're right! Current score: {score}.")
    print(f"Compare A: {data[person1]['name']}, {data[person1]['description']}, {data[person1]['country']}.")
    print(vs)
    print(f"Against B: {data[person2]['name']}, {data[person2]['description']}, {data[person2]['country']}.")
    guess = (input("Who has more followers? Type 'A' or 'B': ")).lower()
    win = compare(person1,person2,guess)
    if win == "True" and guess == "b":
      score += 1
      person1 = person2
    elif win == "True":
      score += 1
    else:
      print(""" \ \   /                  |               |   
  \   /  _ \   |   |      |   _ \    __|  __| 
     |  (   |  |   |      |  (   | \__ \  |   
    _| \___/  \__,_|     _| \___/  ____/ \__| 
                                              """)
  

play(person1)

  
  