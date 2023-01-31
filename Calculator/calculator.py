from functions import add,substract,multiplication,division
print("Welcome to Calcualtor Application")
print("Please enter your choice of operation from below list:")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter your choice:")
#print(choice)
if(choice == "1"):
    num1 = input("Enter firt number:")
    num2 = input("Enter second number:")
    print("Addition Result:", add(num1,num2))
if(choice == "2"):
    num1 = input("Enter firt number:")
    num2 = input("Enter second number:")
    print("Substraction Result:", substract(num1,num2))
if(choice == "3"):
    num1 = input("Enter firt number:")
    num2 = input("Enter second number:")
    print("Multiplication Result:", multiplication(num1,num2))
if(choice == "4"):
    num1 = input("Enter firt number:")
    num2 = input("Enter second number:")
    if(num2 == "0"):
        print("Cannot devide by Zero")
    else:     
        print("Division Result:", division(num1,num2))




