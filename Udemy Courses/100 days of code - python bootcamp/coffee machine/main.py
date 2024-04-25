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

is_on = True
money = 0.

def report():
    return print(f'water: {resources["water"]}ml\nmilk: {resources["milk"]}ml\ncoffee: {resources["coffee"]}g\nmoney: ${money}')

def resource_check(order:dict):
    check = True

while is_on:
    user_choice = input('What would you like? (espresso/latte/cappuccino): ')

    if user_choice == 'off':
        break
    elif user_choice == 'report':
        report()
    elif
