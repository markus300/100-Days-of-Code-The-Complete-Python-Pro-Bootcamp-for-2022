
import os
from art import logo
#HINT: You can call clear() to clear the output in the console.
auction={}

def new_bidder(new_name,new_bid):
  auction[new_name] = new_bid

def max_bidder():
  max_bid = 0
  max_name =""
  for bidders in auction:
    if auction[bidders] > max_bid:
      max_bid = auction[bidders]
      max_name = bidders
  print(f"The winner is {max_name} with the amount of {max_bid}")

def add_bidder():
  add= "yes"
  while add == "yes":
    print(logo)
    name = input("Your name is: ")
    bid = int(input("Your bid is: "))
    new_bidder(name, bid)
    add = input("You want to continue adding bidders?Yes or No? ").lower()
    os.system("cls")
    
add_bidder()
max_bidder()
  