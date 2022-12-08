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


def is_sufficient(drink):

    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        sufficient = False
        print(ingredient, ingredients[ingredient], resources[ingredient])
        if ingredients[ingredient] <= resources[ingredient]:
            print('There is sufficient amount of ingredients')
            sufficient = True
            resources[ingredient] -= ingredients[ingredient]
        else:
            sufficient = False
            return sufficient
    return sufficient


def is_enough_money(wallet, drink):
    enough = False
    cost = MENU[drink]['cost']
    if wallet >= cost:
        enough = True
        return enough, cost
    else:
        return enough, cost


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) or report: ")

    if choice in ['cappuccino', 'espresso', 'latte']:
        sufficient = is_sufficient(choice)
        if sufficient:
            wallet = money()
            enough_money, drink_price = is_enough_money(wallet, choice)
            if enough_money:
                print(f'There you go: {choice} as you ordered')
                wallet -= drink_price
                print(f'Your change is ${wallet:.2f}')
            else:
                print('You dont have enough money')
        else:
            print('There is no ingredients in machine')
    elif choice == 'report':
        # report
        report()
    elif choice == 'off':
        is_on = False
    else:
        print('Only options available are (espresso/latte/cappuccino)')



