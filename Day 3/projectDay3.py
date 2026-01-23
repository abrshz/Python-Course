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