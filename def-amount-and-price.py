#Rendered a welcoming greet to a user after the initialization of the program.
print("\nWelcome to Villariza Foods! Our available product for today is apple. \n")

#Added a docstring inside a def function so that the functionality of the system is accessible and easy to comprehend.
def apple_change(money, apple):
    if money >=  apple:
        exchange = money % apple
        apple_maxQuantity = money // apple
        print(f"\nYou can buy {apple_maxQuantity:,.0f} apple/s and your change is {exchange:,.2f} PHP.\n")
    else:
        moneyShortage = apple - money
        print(f"\nSorry, but you do not have enough money to buy an apple. You need {moneyShortage:,.2f} PHP in order to purchase a single apple.\n")

#Input string has added inside the defined function for a simpler collective method.
apple_change(money = float(input("How much cash do you possess right now? \n> PHP: ")), apple = float(input("\nWhat is the cost of an apple per item? \n> PHP: ")))