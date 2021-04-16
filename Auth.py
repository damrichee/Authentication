#register
# - first name, lastname, password, email
# - generate user id


#login
# - account number and password


#bank operations

#intializing the system

import random 

database = {} #dictionanry

def init():

    isValidOptionSelected = False
    print("Welcome to Bank Damatosine")

    while isValidOptionSelected == False:
        
        haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no)"))

        if (haveAccount == 1):
            isValidOptionSelected == True  
            login()
        elif(haveAccount == 2):
            isValidOptionSelected == True
            (register())
            
        else:
            print("You have selected invalid option")


def login():

    print("Login to your account \n")

    isLoginSuccesful = False

    while isLoginSuccesful == False:

        accountNumberFromUser = int(input("What is your account number? \n"))
        password = input("What is your password \n")

        for accountNumber,userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    isLoginSuccesful = True

        print("Invalid account or password")

    bankOperation(userDetails)

def register():
    print("Register")
    email = input("What is your email address? \n")
    first_name = input("What is your first name \n")
    last_name = input("What is your last name \n")
    password = input("Create a Password \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password ]

    print("Your account has been created")
    print("===== ===== ====")
    print("Your account number is %d" % accountNumber)
    print("Please do not share it")
    print("******* ****** ******")


    login()

def bankOperation(user):

    print("Welcome %s %s" % (user [0], user[1] ) )
   
    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Complain (4) Logout") )

    if (selectedOption == 1):
            
        depositOperation()
    elif(selectedOption == 2):
            
        withdrawalOperation()
    elif(selectedOption == 3):
            
        complainOperation()
    elif(selectedOption == 4):
        
        logout()
    else:
        
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
    print("Withdrawal")

def depositOperation():
    print("Deposit")

def complainOperation():
    print("Complain ")




    

def generationAccountNumber():

    print("Generating Account Number")
    return random.randrange(1111111111.9999999999)

def logout():
    print("Logout")



#### ACTUAL BANKING SYSTEM ####

init() 