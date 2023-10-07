# Find LCM (Least Common Multiple) of two numbers. LCM of two numbers is the smallest
# number which can be divided by both numbers. For example, LCM of 15 and 20 is 60,
# and LCM of 5 and 7 is 35. A simple solution is to find all prime factors of both
# numbers, then find union of all factors present in both numbers.

def calculate_lcm(x, y):
    # Define the greater of 2 entered numbers as LCM can only be greater than or equal to the largest them
    if x>y:
        greater = x
    else:
        greater = y

    while (True):
        if (greater % x == 0) and (greater % y == 0): # Condition
            lcm = greater # If condition is true, assign greater value to new variable "lcm" and stop the program
            break
        greater += 1 # If condition is not true, increase the greater's value for 1 and re-iterate

    return lcm # Once the 


# ==========Main Menu=============
while True:
    number_one=float(input("Enter your 1st number: ")) # Enter the first number
    number_two=float(input("Enter your 2nd number: ")) # Enter the second number
    print (calculate_lcm(number_one, number_two)) # Print the calculated LCM
    break #All actions are done so stop the program
