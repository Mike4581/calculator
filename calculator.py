# This function add two numbers
def add(x,y):                            #def to start the function
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y                         #return function to call scripts or complete its tasks

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

#Sentinel variable
check_choice = False

while (check_choice == False):
    # take input from user
    choice = input("Select operator (+,-,x,/): ")
    # check if choice is one of the four options
    if choice in ('+','-','x','/'):
        check_num1 = False
        check_num2 = False
        #while control flow which repeatedly excutes a block of code until conditions is satisfied
        while (check_num1 == False):
            #try lets you test a block of code for errors                   
            try:
                   #float covert values into a decimal number or fractional                                        
                num1 = float(input("Enter first number: "))
                #if checks s condition and execute it if the conditionholds true
                if isinstance(num1,float):                  
                    check_num1 = True
            #except allows you to catch and handle the exception that python encountered in the try clause         
            except:                                         
                print("Invalid input. Please enter a number.")

        while (check_num2 == False):
            try:
                num2 = float(input("Enter second number: "))
                if isinstance(num2,float):
                    check_num2 = True
            except:
                print("Invalid input. Please enter a number.")
           
        if choice == '+':
            print(num1, "+", num2, "=" , add(num1, num2))

        elif choice == '-':                                     #elif test multiple conditions
            print(num1, "-", num2, "=", subtract(num1, num2))
        
        elif choice == 'x':
            print(num1, "*", num2, "=", multiply(num1, num2))
        
        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        
    else:                                                       #Show error if invalid operator
        print("Invalid input. Please enter a valid operator.")