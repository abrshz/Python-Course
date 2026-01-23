# Conditional Statement:- allow your code to make decisions. They act like a crossroads in a journey: depending on whether a condition is "True" or "False," the program will follow a specific path.

# # 1. The Core Syntax: if, elif, and else
# Python uses three main keywords to handle logic:

# if: The starting point. It checks a condition.

# elif (short for "else if"): Checks another condition if the previous ones were false. You can have as many of these as you need.

# else: The "catch-all." It runs if none of the above conditions are met.

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? \n"))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")

num = int(input("What is the number you want to check?  \n"))

if num % 2 == 0:
    print(num + " is even number.")
else:
    print(str(num) + " is odd number.")

print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ")

bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("You typed a wrong input.")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3 

extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")
if extra_cheese == "Y":
    bill += 1  

print(f"Your final bill is: ${bill}")  

# Module (%) code using what you have learnt about modulo operator and conditional checks in Python to check if the number in the input area area is odd or even. 

# Nested conditions:- is put if/else statement inside other if/else statements. 

# Logical operation:- 
#  AND both conditions must be True 
#  OR one of the conditions True 
#  NOT the conditions is False


  
