MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_questions(money):
        money += (int(input("How many quarters?: ")))*0.25
        money += (int(input("How many dimes?: ")))*0.10
        money += (int(input("How many nickles?: "))) * 0.05
        money += (int(input("How many pennies?: "))) * 0.01
        return money
def compare(cont,money):
    if cont == "espresso":
        if resources["water"] > MENU["espresso"]["ingredients"]["water"]:
            if resources["coffee"] > MENU["espresso"]["ingredients"]["coffee"]:
                money = print_questions(money)
                if money > MENU["espresso"]["cost"]:
                    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                    money -= MENU["espresso"]["cost"]
                    print(f"Here is ${round(money,2)} in change")
                    print(f"Here is your {cont} ☕ Enjoy!")
                    return round(money,2)
                else:
                    print("Sorry there is not enough money.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")
    else:
        if resources["water"] > MENU[cont]["ingredients"]["water"]:
            if resources["milk"] > MENU[cont]["ingredients"]["milk"]:
                if resources["coffee"] > MENU[cont]["ingredients"]["coffee"]:
                    money = print_questions(money)
                    if money > MENU[cont]["cost"]:
                        resources["water"] -= MENU[cont]["ingredients"]["water"]
                        resources["milk"] -= MENU[cont]["ingredients"]["milk"]
                        resources["coffee"] -= MENU[cont]["ingredients"]["coffee"]
                        money -= MENU[cont]["cost"]
                        print(f"Here is ${round(money,2)} in change")
                        print(f"Here is your {cont} ☕ Enjoy!")
                        return round(money,2)
                    else:
                        print("Sorry there is not enough money.")
                else:
                    print("Sorry there is not enough coffee.")
            else:
                print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough water.")


def run():
    cont =""
    money = 0.0

    while cont != "off":
        while cont != "espresso" or cont != "latte" or cont != "cappuccino":
            cont = input("What would you like? (espresso/latte/cappuccino): ")
            if cont == "report":
                print(f"water: {resources['water']}ml")
                print(f"milk: {resources['milk']}ml")
                print(f"coffee: {resources['coffee']}g")
                print(f"money: ${money}")
            elif cont == "espresso" or cont == "latte" or cont == "cappuccino" :
                money = compare(cont, money)



run()