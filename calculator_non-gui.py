#This function adds two numbers
def add(x, y): 
    return x+y

#This function subtracts two numbers
def subtract(x, y):
    return x-y

#This function multiply two numbers
def multiply(x, y):
    return x*y

#This function divide two numbers
def divide(x, y):
    return x/y

#This function returns absolute value of two numbers
def absolute(x, y):
    if x<0 and y<0:
        x=x*(-1)
        y=y*(-1)
        return x, y

    elif x<0 and y>=0:
        x=x*(-1)
        return x, y

    elif x>=0 and y<0:
        y=y*(-1)
        return x, y

    else:
        return x, y


# ==========Main Menu=============
while True:
    users_choice = input('''Enter your choice below: 
        1 - Add
        2 - Subtract
        3 - Multiply
        4 - Divide
        5 - Absolute
        ''')

    if users_choice in ('1', '2', '3', '4', '5'):
        try:
            number_one=float(input("Enter your 1st number: "))  
            number_two=float(input("Enter your 2nd number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue #Error handling in case the wrong data for numbers 1 and 2 was entered
        
        if users_choice == '1':
            print(number_one, "+", number_two, "=", add(number_one, number_two))
            break #All actions are done so stop the program

        elif users_choice == '2':
            print(number_one, "-", number_two, "=", subtract(number_one, number_two))
            break #All actions are done so stop the program

        elif users_choice == '3':
            print(number_one, "*", number_two, "=", multiply(number_one, number_two))
            break #All actions are done so stop the program

        elif users_choice == '4':
            print(number_one, "/", number_two, "=", divide(number_one, number_two))
            break #All actions are done so stop the program

        elif users_choice == '5':
            print ("Absolute value of ", number_one, " and ",number_two, " is ", absolute(number_one, number_two))
            break #All actions are done so stop the program
    else:
        print("Invalid input.") #Error handling in case the wrong data was entered-neither 1, 2, 3, 4 or 5
        
