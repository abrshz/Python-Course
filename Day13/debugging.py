from random import randint
def my_function():
    for i in range (1,21):
        # print(i)
        if i == 20:
            # print(i)
            print('You got it!')
my_function()

dice_images = ['1', '2', '3', '4', '5', '6']
dice_num = randint(0, 5)
print(dice_images[dice_num])

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizz_buzz(35)
