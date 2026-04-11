# # Hangman project
# import random
# word_list = ['aardvar', 'baboon' , 'camel']
# i = 0 

# lives = 6

# chosen_word = random.choice(word_list);
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)

# for position in range (word_length):
#     placeholder += ""
# print(placeholder)

# game_over = False
# correct_letters = []

# while not game_over:
#     guess_word = input("Guess a letter: ").lower

#     display = ""

#     for letter in chosen_word:
#         if letter == guess_word:
#            display += letter
#            correct_letters.append(guess_word)
#         elif  letter in correct_letters:
#            display += letter           
#         else:
#            display += "_"
#            print("You chosen the word ins't there.")


#     print(display)

#     if guess_word not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             game_over = True
#             print ("You lose!!")

#     if "_" not in display:
#         game_over = True
#         print("You win!!")
  
 
#  Ai

# Hangman project
import random


word_list = ['aardvar', 'baboon', 'camel' , 'hangman' , 'hello']
lives = 6

chosen_word = random.choice(word_list)
# print(chosen_word)  # Uncomment for testing

# Initialize display with underscores
display = "_" * len(chosen_word)
print(display)

correct_letters = []
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()  # Fixed .lower()

    new_display = ""
    for letter in chosen_word:
        if letter == guess:
            new_display += letter
            # Add to correct_letters only once
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    # Update display
    display = new_display
    print(display)

    # Check if guess is incorrect
    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life. Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("You lose!!")

    # Check if all letters guessed
    if "_" not in display:
        game_over = True
        print("You win!!")






