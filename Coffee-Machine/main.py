from data import MENU, resources


def money():
    print('Insert your coins: ')

    quarters = int(input('How many quarters 0.25: ')) / 4
    dimes = int(input('How many dimes 0.1: ')) / 10
    nickles = int(input('How many nickles 0.05: ')) * 0.05
    pennies = int(input('How many pennies 0.01: ')) / 100

    wallet = quarters + dimes + nickles + pennies

    print(f"Your money: ${wallet}")
    return wallet


def report():
    print('Resources in machine: ')
    for resource in resources:
        print(f'{resource.capitalize()}: {resources[resource]}ml')


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) or report: ")

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        report()
    elif choice in ['cappuccino', 'espresso', 'latte']:
        # wallet
        wallet = money()

    else:
        print('Only options available are (espresso/latte/cappuccino)')



