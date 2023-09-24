from ssl import Options
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mm = MoneyMachine()
cm = CoffeeMaker()
menu = Menu()

working = True

while working:
    options = menu.get_items()
    choice = input(f"Enter Your Choice ({options}) : ").lower()
    if choice == "off":
        working = False
    elif choice == "report":
        mm.report()
        cm.report()
    else:
        drink = menu.find_drink(choice)
        if cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
            cm.make_coffee(drink)
