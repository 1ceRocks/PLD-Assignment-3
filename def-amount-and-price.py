#Rendered a welcoming greet to a user after the initialization of the program.
print("\nWelcome to Villariza Foods! Our available product for today is apple. \n")

#Added a docstring inside a def function so that the functionality of the system is accessible and easy to comprehend.
def apple_change(money, apple):
    """
    Input from user and store-return as money and apple variable. The if statement shows that the user can afford an
    apple based on the calculations that was inputted. However, else statement contradicts this estimate from the user.
    """
    if money >= apple:
        exchange = float(money) % float(apple)
        apple_maxQuantity = float(money) // float(apple)
        print(f"\nYou can buy {apple_maxQuantity:,.0f} apple/s and your change is {exchange:,.2f} PHP.\n")
        
    elif money < apple:
        moneyShortage = float(apple) - float(money)
        print(f"\nSorry, but you do not have enough money to buy an apple. You need {moneyShortage:,.2f} PHP in order to purchase a single apple.\n")

#Input string has added inside the defined function for a simpler collective method.
apple_change(money = input("How much cash do you possess right now? \n> PHP: "), apple = input("\nWhat is the cost of an apple per item? \n> PHP: "))