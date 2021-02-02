import sys
from enum import Enum
from utils import alphaindex, alphabet, count_chars
from language_finder import find_language


class LETTER_REFERENCE(Enum):
    PORTUGUESE = 'A'
    ESPERANTO = 'A'
    FINNISH = 'A'
    SWEDISH = 'E'
    ENGLISH = 'E'
    DANISH = 'E'
    ITALIAN = 'E'
    GERMAN = 'E'
    SPANISH = 'E'
    FRENCH = 'E'
    DUTCH = 'E'
    # ARABIC     =
    # HEBREW     =
    # JAPANESE   =
    # MALAYSIAN  =
    # RUSSIAN    =
    # SERBIAN    =
    # GREEK      =
    # NORWEGIAN  =


def plaintext_index(cipherchar, shift):
    return (alphaindex(cipherchar) + shift) % len(alphabet)


def auto_decrypt_caesar(ciphertext):
    base_char = LETTER_REFERENCE[find_language(ciphertext)].value
    char_count = count_chars(ciphertext)
    most_common = sorted(
        char_count, key=char_count.__getitem__, reverse=True
    )[0]
    shift = -(alphaindex(most_common) - alphaindex(base_char))
    return ''.join(
        [alphabet[plaintext_index(char, shift)] for char in ciphertext]
    )

def brute_force_caesar(ciphertext):
    for shift in range(len(alphabet)):
        plaintext = ""
        for char in ciphertext:
            if char == ' ':
                plaintext += ' '
            else:
                plaintext += alphabet[plaintext_index(char, shift)]
        print(shift, plaintext)
