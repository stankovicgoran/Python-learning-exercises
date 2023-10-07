# Find GCD (greatest common divisor) of two numbers is the largest
# positive integer that perfectly divides the two given numbers.
# For example, the GCD of 12 and 14 is 2.

def calculate_gcd(x, y):
    # Define the smaller of 2 entered numbers
    if x<y:
        smaller=x
    else:
        smaller=y

    while(True):
        if((x % smaller == 0) and (y % smaller == 0)):
            gcd=smaller
            break
        smaller -= 1
            
    return gcd

# ==========Main Menu=============
while True:
    number_one=int(input("Enter your 1st number: ")) # Enter the first number
    number_two=int(input("Enter your 2nd number: ")) # Enter the second number
    print (calculate_gcd(number_one, number_two)) # Print the calculated GCD
    break #All actions are done so stop the program
