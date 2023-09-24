
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            'milk': 0,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

profit = 0
resources = {
    "water": 30000,
    "milk": 20000,
    "coffee": 10000,
}

def machine(order):
    global bill
    global resources
    global process
    for item in MENU[order]["ingredients"]: 
            if item == 'water':
                if MENU[order]["ingredients"][item] < resources["water"]:
                    continue
                else:
                    process = 'end'
            if item == 'coffee':
                if MENU[order]["ingredients"][item] < resources["coffee"]:
                    continue
                else:
                    process = 'end'
            if item == 'milk':
                if MENU[order]["ingredients"][item] < resources["milk"]:
                    continue
                else:
                    process =  'end'
    if process != 'end':
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
        resources["water"] -= MENU[order]["ingredients"]["water"]
        resources["milk"] -= MENU[order]["ingredients"]["milk"]
        bill += MENU[order]['cost'] 
        order_list.append(order)
    if process == 'end':
        print('insufficient ingredients')

process = ''

bill = 0
order_list = []
again = 'yes'
while again == 'yes':
    order = input("What do you want : 'cappuccino' , 'latte' , espresso'\n").lower()
    if order == "cappuccino" or order == "latte" or order == 'espresso':
        machine(order)
    if order == 'report':
        print(resources)

    again = input("Do you want anything else : 'Yes' or 'No'\n")
print(f'Your Order : {order_list}')    
print(f'Your Total Bill : {bill} Rs')
print(f"Enjoy Your Order.\nThank You Visit Again!")    