import random

def generate_random_binary_number():
    number_string = ""
    for i in range(4):
        random_number = random.randint(0,1)
        number_string += str(random_number)
    return number_string

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for num in binary:
        decimal += int(num) * (2 ** power)
        power -= 1
    return decimal

binary_number = generate_random_binary_number()
decimal_number = binary_to_decimal(binary_number)
print(decimal_number)