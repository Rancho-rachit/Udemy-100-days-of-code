# DAY - 15
# COFFEE MACHINE

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

not_enough_resources = 'n'

exit_ = 'n'
money_earned = int('0')
while exit_ == 'n':

    # TODO: 1. Print report of all the coffee machine resources

    def report(water, milk, coffee, money_gg):
        print(f"water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}gm")
        print(f"Money: ${money_gg}")

    # TODO: 3. Process coins

    def ask_for_money():
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        money_to_be_given = round(float(quarters / 4) + float(dimes / 10) + float(nickels / 20) + float(pennies / 100), 2)
        return money_to_be_given


    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Check resources sufficient?

    if coffee_type == 'report':
        report(resources['water'], resources['milk'], resources['coffee'], money_earned)
    else:
        resources_avaialable = 'y'
        for resource in resources:
            if int(MENU[coffee_type]["ingredients"][resource]) > resources[resource]:
                print(f"Sorry there is not enough {resource}")
                resources_avaialable = 'n'

        if resources_avaialable != 'n':

            money_given = ask_for_money()

            # TODO: 4. Check transaction successful?

            if money_given < MENU[coffee_type]["cost"]:
                print(f"${money_given} is not enough to buy {coffee_type}")
            else:
                change = round(money_given - MENU[coffee_type]["cost"], 2)
                money_earned = float(MENU[coffee_type]["cost"])

                for wmc in resources:
                    resources[wmc] -= MENU[coffee_type]["ingredients"][wmc]

                # TODO: 5. Make Coffee
                print(f"Here is ${change} in change.")
                print(f"Here is your {coffee_type}. Enjoy!")

# _____________________ END ____________________________________                