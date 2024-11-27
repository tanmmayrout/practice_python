# Functions basics

def add_number(n1,n2): # Function definition similar to C
    result = n1+n2
    return result #return statement

number1=(int(input("Enter a number ")))
number2=(int(input("Enter a number ")))

result = add_number(number1,number2) #Calling function
print("The sum is ",result) # Displaying result