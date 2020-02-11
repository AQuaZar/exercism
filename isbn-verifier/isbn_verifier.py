import re


def is_valid(isbn):
    isbn = "".join(isbn.split("-"))
    if bool(re.match("[0-9]{9}[0-9xX]{1}", isbn)):
        checksum = 0
        for i, e in enumerate(isbn[:-1]):
            checksum += int(e) * (10 - i)
        if isbn[-1] == "X" or isbn[-1] == "x":
            checksum += 10
        else:
            checksum += int(isbn[-1])
        return checksum % 11 == 0
    else:
        return False
