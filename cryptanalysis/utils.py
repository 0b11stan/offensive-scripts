import re
from string import ascii_uppercase as alphabet


def alphaindex(char):
    return alphabet.index(char)


def count_chars(ciphertext):
    result = {}
    for char in ciphertext:
        if char in result.keys():
            result[char] += 1
        else:
            result[char] = 1
    return result


def sanitize(ciphertext):
    return re.sub('[\s\W\d]*', '', ciphertext).upper()
