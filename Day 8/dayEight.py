# def sample():
#     print("Hello world!")

# def say_hello():
#     print("Hello!")


# sample()
# say_hello()

# def life_in_weeks(age):
#     input_age = age * 52
#     years_week = 90 * 52
#     weeks_left = years_week - input_age
#     print(f"You have {weeks_left} weeks left.")
    
    
# life_in_weeks(20)

def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is this, {location}?")


greet_with("Jossy", "Addis")

# Shift function 

alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# shift = 13
# def encrypt(original_text, shift_amount):
#     cipher_text= ""

#     for letter in original_text:
#         shifted_position= alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]

#     print(f"Here is the encoded result: {cipher_text}")

# def decrypt(original_text, shifted_amount):
#     output_text= ""

#     for letter in original_text:
#         shifted_position= alphabet.index(letter) - shifted_amount
#         shifted %= len(alphabet)
#         output_text += alphabet[shifted_position]


def caesar(original_text, shift_amount, encode_or_decode):
    output_text= ""
    for letter in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position= alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the encoded decoded result: {output_text}")


caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)


