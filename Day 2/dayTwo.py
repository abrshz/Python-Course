# print("Number of letters in your name " + str(len(input("Enter your name \n"))))
# print(8 / 3)
# print(8/4)

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = float(input("How much tip would you like to give? 10 , 12 or 15? \n"))
split = int(input("How many people to split the bill? \n"))
tip_percentage = 1 +  (tip / 100)
total_tip = bill * tip_percentage
total_bill = total_tip / split
print(f"Each person should pay: ${round(total_bill, 2)}")

