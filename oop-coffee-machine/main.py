from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    user_input = input(f"What would you like to order? ({menu.get_items()}): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(user_input)
        payment_successful = money_machine.make_payment(menu_item.cost)
        if coffee_maker.is_resource_sufficient(menu_item) and payment_successful:
            coffee_maker.make_coffee(menu_item)
