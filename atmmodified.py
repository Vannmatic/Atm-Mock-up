# Create account, bank operation,
import random

accountHolder = {} #dictionary
def init():

    isValidOptionSelected = False
    print("Welcome to Bank Of Matic")

    while isValidOptionSelected == False:
        
        haveAccount = int(input("Do you have an existing account?: 1(yes) 2(no)\n"))
        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            print(register())
        else:
            print("You have selected an invalid option")

def login():
    print(" Login ")
    isLoginSuccessful = False

    while isLoginSuccessful == False
        accountNumberFromUser = int(input("What is your account number?\n"))
         
    bankOperation()

def register():
    print("Create an account")

    email = input("Please enter your email address \n")
    first_name = input("Please enter your first name \n")
    last_name = input("Please enter your last name \n")
    password = input("Please enter your password \n")  
    
    accountNumber = generateAccountNumber()

    accountHolder[accountNumber] = [first_name,last_name,email,password]

    print(" Your account has been created")

    login()

def bankOperation():

    print("bank operations")

def generateAccountNumber():
    print("Account Number Here")
    return random.randrange(1111111111,9999999999)

#### BANKING SYSTEM ####

init()
    


