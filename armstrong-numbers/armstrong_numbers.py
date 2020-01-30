def is_armstrong_number(number):
    number_str = str(number)
    length = len(number_str)
    temp = 0
    for i in range(length):
        temp += int(number_str[i]) ** length
    return number == temp:
