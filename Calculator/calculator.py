from art import logo
import os
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def print_operations():
    for symbol in operations:
      print(symbol)
      
def calculator():
  print (logo)
  print_operations()    
  y = "y"
  num1 = float(input("What's the first number?: "))
  while y=="y":
    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))
    calculation = operations[operation_symbol]
    num3= calculation(num1,num2)
    print (f"{num1} {operation_symbol} {num2} = {num3}")
    y = input(f"Type y to continue calculating with {num3}, or n to exit.: ")
    num1=num3
  os.system("clear")
  calculator()
  
calculator()
