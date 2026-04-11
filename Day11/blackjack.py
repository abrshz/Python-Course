import random

def blackjack():
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(random.choice(card))
        computer_cards.append(random.choice(card))
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    while sum(user_cards) < 21:
        ask = input("Type 'y' to get another card, type 'n' to pass: ")
        if ask == 'y':
            user_cards.append(random.choice(card))
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
        else:
            break
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(card))
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    if sum(user_cards) > 21:
        print("You went over. You lose 😤")
    elif sum(computer_cards) > 21:
        print("Opponent went over. You win 😁")
    elif sum(user_cards) > sum(computer_cards):
        print("You win 😁")
    elif sum(user_cards) < sum(computer_cards):
        print("You lose 😤")
    else:
        print("It's a draw 🙃")
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    blackjack()


