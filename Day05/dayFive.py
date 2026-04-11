import random

# fruits = ['Apple', 'Peach' , 'Pear']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)


# scores = [85, 92, 78, 90, 88 , 190]


# max_score = scores[0]

# for score in scores[1:]:
#     if score > max_score:
#         max_score = score  

# print("\nThe maximum score is:", max_score)

# for scores in range (0, 10 , 4):
#     print(scores)

# Quiz question

# for number in range (1 , 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g' , 'h' , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' , 'v', 'w', 'x' , 'y' , 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
symbols = ['!', '#', '$', '%', '&' , '(' , ')', '*', '']


print("Welcome to the PyPassword Generator!")
letter = int(input("How many letters would you like in your password? \n"))
sym = int(input(f"How many symbols would you like?\n"))
num = int(input(f"How many numbers would you like?\n"))


# Easy level

# password = ("")

# for lets in range(1, letter + 1):
#     password += random.choice(alphabet)

# for lets in range(1, num + 1):
#     password += random.choice(numbers)

# for lets in range(1, sym + 1):
#     password += random.choice(symbols)

# print(password)

# Hard level

password_list = []

for char in range(0, letter):
    password_list.append(random.choice(alphabet))

for char in range(0, num):
    password_list.append(random.choice(numbers))

for char in range(0, sym):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
 
 
