#Arranged the variables and the spacing between the input function into def function for lightweight coding to a program.
print("\nYour Personal Information")

def extract_Name():
    nameCredential = input("\nEnter your NAME here. \n> ")
    return nameCredential

def extract_Age():
    ageCredential = float(input("\nEnter your AGE here in numbers. \n> "))
    return ageCredential

def extract_Address():
    addressCredential = input("\nEnter your ADDRESS here. \n> ")
    return addressCredential

#Credential Variables are now set into def function.
def totalDetails():
    userName = extract_Name()
    userAge = extract_Age()
    userAddress = extract_Address()  
    extract_Details(_userName=userName, _userAge=userAge, _userAddress=userAddress)

def extract_Details(_userName, _userAge, _userAddress):
    print(f"\nHi, my name is {_userName}. I am {_userAge:.0f} years old and I live in {_userAddress}.")

totalDetails()