programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again", 
    "Loop": "The action of doing something over and over again."
}

# Add existing key 
# programming_dictionary["Bug"] = "A moth in your computer"

for thing in programming_dictionary:
    print(programming_dictionary[thing])




student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if (score >= 91):
        student_grades[student] = "Outstanding"
    elif (score >= 81):
        student_grades[student] = "Exceeds Expectations"
    elif (score >= 71):
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# student_grades =

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log= {
    "France": {"name": "Paris", "visits": 2, "cities": ["Paris", "Lille", "Dijon"] },
    "Germany" : ["Stuttgart", "Berlin"]
}

# print(travel_log["France"]["name"])

# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# print(dict["c"])


bids = {}
continue_bidding = True

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

            
    print(f"The winner is {winner} with a bid of ${highest_bid}")



while continue_bidding:
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n$")
    )
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if should_continue == "No":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n * 20")
 



