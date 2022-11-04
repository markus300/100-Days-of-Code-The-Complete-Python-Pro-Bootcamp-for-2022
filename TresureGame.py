print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to find the Treasure.")
print("Your mission is to find the treasure. Remember to be patient but not to much") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("You are in the middle of a forest, you hear a sound on the left, where do you wanna go? right or left\n")
if direction == "left":
  action = input("You found a bear that is attacking a adventurer, what is your next action? fight, run or wait?\n")
  if action == "fight":
    print("You jump with a kick and push the bear, the adventurer use this opportunity to grab his sword and kill the bear stabbing it in the neck.")
    action = input("You noticed that the adventurer is about to die. What is your next action? Give the adventurer a potion of healing or kill him? g or k. \n")
    if action == "g":
      print("You help him, he drinks the potion and then gives you a map of a treasure, you two go to find the treasure.")
      print("You two find a dungeon and decide to enter, while you where in the front the adventurer stab and kill you.")
      print("YOU LOST")
    else:
      print("You kill the adventurer and loot all his belongings, found a treasure map and grab the sword.")
      print("You go to the location on the map and found a temple, you decide to enter and when you are at the entrance a trap is activated and you die.")
      print("YOU LOST.")
  elif action == "run":
    print("You run, but you step on a branch the bear noticed and start running towards you, the bear catch you and kill you \n YOU LOST.")
  else:
    print("You decide to wait, watching how the bear brutally kills the adventurer, then the bear left the adventurer.")
    action = input("What is your next action? loot, run, wait.\n")
    if action == "wait":
      print("The bear comes back to eat the corpse and a minute later goes inside the forest. ")
      action = input("What is your next action? loot, run, wait.\n")
      if action == "loot":
        print("You found a treasure map in his hand and another in his corpse.")
        action = input("What map you pick? hand or corpse.\n")
        if action == "corpse":
          print("You follow the map, go out of the forest at night, find a giant rock, move the rock and finally found the treasure")
          action = input("What is your next action? run, wait, open\n")
          if action == "wait":
            print("You wait until the sun rises, the sun purify the ominous spirit in the chest, you open it and finally found the treasure. \nYOU WON.")
          elif action == "run":
            print("The treasure chest wakes up from a branch that you step on it while running and launch a laser beam and hit you. \nYOU LOST.")
          else:
            print("You try to open the treasure chest, but the treasure chest eats you. \nYOU LOST.")
        else:
          print("You follow the treasured map, end up in a temple, enter the temple activate a trap and die.\nYOU LOST.")
      elif action == "wait":
        print("You waited to long and a snake bites you, you die because of poison. \nYOU LOST.")
      else:
        print("You run very fast but you don't realize the cliff, you fall and die. \nYOU LOST.")
    elif action == "loot":
      print("You approach the body but the bear comes back and attacks you, you die. \nYOU LOST.")
    else:
      print("You run very fast but you don't realize the cliff, you fall and die. \nYOU LOST.")
elif direction == "right":
  action=input("You found a lake. What is your next action? swim or not \n")
  if action == "swim":
    print("You go to swim but in the middle of the lake a water monster attacks you and kills you.\nYOU LOST.")
  else:
    print("Since you didn't jump into the water, a poisonous snake came and bit you and you died.\nYOU LOST.")

    

