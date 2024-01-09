from data import MENU, resources

profit = 0


# TODO: print report
def print_report():
    """Prints report of available resources and total money"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


# TODO: check if the resource is sufficient
def is_resources_sufficient(item):
    """Returns True if the resources are available"""
    for key in item:
        if item[key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


# TODO: process coins
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# TODO: check if the transaction is successful
def is_transaction_successful(item, money):
    """Returns True if the transaction is successful"""
    if money < item["cost"]:
        print("Sorry that's not enough money, Money refunded.")
        print(f"Required money: {item['cost']}")
        return False
    else:
        global profit
        profit += item["cost"]
        if money > item["cost"]:
            print(f"Here is ${round(money - item['cost'], 2)} dollars in change.")
        return True


# TODO: make coffee
def make_coffee(item_ingredients, choice):
    for key in item_ingredients:
        resources[key] -= item_ingredients[key]
    print(f"Here is your {choice}")


is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print_report()
    else:
        drink = MENU[user_choice]
        if is_resources_sufficient(drink['ingredients']):
            print(f"Your cost is {drink['cost']}")
            paid_amount = process_coins()
            if is_transaction_successful(drink, paid_amount):
                make_coffee(drink['ingredients'], user_choice)
