rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choices = [rock, paper, scissors]
choice_human = int(input("What's your choice 1 for rock, 2 for paper or 3 for scissors? \n"))
choice_human = choices[choice_human-1]
choice_robot = random.choice(choices)
print("You choose")
print (choice_human)
print("The robot choose")
print (choice_robot)

if choice_human == choice_robot:
  print("It's a TIE")
elif (choice_human == scissors and choice_robot == paper)or(choice_human == paper and choice_robot == rock)or(choice_human == rock and choice_robot == scissors):
  print("You WON!.")
else:
  print("You LOST.")