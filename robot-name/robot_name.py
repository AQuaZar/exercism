import random
from string import ascii_uppercase


class Robot:
    def __init__(self):
        self.name = generate_name()

    def reset(self):
        random.seed("new seed")
        self.name = generate_name()


def generate_name():
    name = ""
    letters = list(ascii_uppercase)
    for _ in range(2):
        x = random.randint(0, 25)
        name += letters[x]
    digits = str(random.randint(0, 999))
    if len(digits) != 3:
        digits = "0" * (3 - len(digits)) + digits
    return name + digits

