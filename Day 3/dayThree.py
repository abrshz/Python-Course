# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? \n"))

# if height >= 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# num = int(input("What is the number you want to check?  \n"))

# if num % 2 == 0:
#     print(num + " is even number.")
# else:
#     print(str(num) + " is odd number.")

# print("Welcome to Python Pizza Deliveries")
# size = input("What size pizza do you want? S, M or L: ")

# bill = 0
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25
# else:
#     print("You typed a wrong input.")

# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3 

# extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")
# if extra_cheese == "Y":
#     bill += 1  

# print(f"Your final bill is: ${bill}")  

# print("Welcome to Treasure Island.")
# print("Your mission is to find the hidden treasure.")
# choose = input("You are standing at a crossroad. \n Type 'left' or 'right' ")

# if choose == "left":    
#    word = input("You've come to a lake. There is an island in the middle of the lake.  \n Type 'wait' to wait foa a boat or Type 'swim' to swim across")
# if word == "wait":
#    survive = input("You arrive at the island save.\n Choose color to get price 'Red' or 'Blue' or 'Yellow'")
# if survive == "Red":
#     print("Burned by fire.\n Game over!!")
# elif survive == "Blue":
#     print("Eaten by beasts.\n Game over!!")
# else: 
#     print("You win!")
# else:
#     print("Attacked by trout.\n Game over!!")
# else: 
#     print("You've come to a dark cave. You can't see anything. Game over.")

print("Welcome to Treasure Island.")
print("Your mission is to find the hidden treasure.")

choice = input("You are standing at a crossroad. \nType 'left' or 'right': ").lower()

if choice == "left":
    action = input("You've come to a lake. There's an island in the middle. \nType 'wait' to wait for a boat or 'swim' to swim across: ")
    
    if action == "wait":
        color = input("You arrive at the island safely. \nChoose a color to get prize: 'Red', 'Blue', or 'Yellow': ")
        
        if color == "Red":
            print("Burned by fire.\nGame over!!")
        elif color == "Blue":
            print("Eaten by beasts.\nGame over!!")
        else:
            print("You win!")
    else:
        print("Attacked by trout.\nGame over!!")
else:
    print("Fail into a hole.\n Game over.")



  
