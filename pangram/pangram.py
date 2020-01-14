from string import ascii_lowercase


def is_pangram(sentence):
    alphabet = list(ascii_lowercase)
    sentence = sentence.lower()
    for letter in sentence:
        if letter in alphabet:
            alphabet.remove(letter)
    if not alphabet:
        return True
    else:
        return False

