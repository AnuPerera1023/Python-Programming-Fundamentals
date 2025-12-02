print("Hello PYTHON")

length = 5
width = 10
area = length * width

import random

secret_number = 7
guess = 0

while guess != secret_number:      # keep guessing until it matches
    guess = random.randint(1, 10)
    print("Guessing:", guess)

print("I guessed the right number! It was", secret_number)


