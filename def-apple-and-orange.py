#Rendered a welcoming greet to a user after the initialization of the program.
print("\nWelcome to Villariza Foods! \nThe Price of an Apple is 20 PHP, while the Price of an Orange is 25 PHP.")

#Synchronized every code into def function with parameters and added special variables for the program to run without errors.
def obtain_apple():
    apple = (input("\nPlease quantify how many apples you need to purchase... \n> Quantity: "))
    return apple 

def obtain_orange():
    orange = (input("\nPlease quantify how many oranges you need to purchase... \n> Quantity: "))
    return orange

def obtain_applePrice():
    price_apple = 25
    return price_apple

def obtain_orangePrice():
    price_orange = 25
    return price_orange

def obtain_totalPrice():
    apple = (obtain_apple() * obtain_applePrice())
    orange = (obtain_orange() * obtain_orangePrice())
    grand_total = (apple + orange)
    print_OutputReceipt(_grand_total=grand_total)

def print_OutputReceipt(_grand_total):
    print(f"\nThe total amount is {_grand_total:,.0f} PHP.\n")

obtain_totalPrice()