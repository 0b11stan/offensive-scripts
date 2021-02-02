import sys
from enum import Enum
from utils import alphabet, alphaindex, count_chars


class IC_REFERENCE(Enum):
    FRENCH      = 0.0778
    ENGLISH     = 0.0667
    #RUSSIAN    = 0.0529
    #SERBIAN    = 0.0643
    #SWEDISH    = 0.0644
    #ESPERANTO  = 0.0690
    #GREEK      = 0.0691
    #NORWEGIAN  = 0.0694
    #DANISH     = 0.0707
    #FINNISH    = 0.0737
    #ITALIAN    = 0.0738
    #PORTUGUESE = 0.0745
    #ARABIC     = 0.0758
    #GERMAN     = 0.0762
    #HEBREW     = 0.0768
    #SPANISH    = 0.0770
    #JAPANESE   = 0.0772
    #DUTCH      = 0.0798
    #MALAYSIAN  = 0.0852


def compute_char_ic(char_count, ciphertext_len):
    return (char_count * (char_count - 1)) / \
           (ciphertext_len * (ciphertext_len - 1))


def compute_coincidence_index(ciphertext):
    chars = count_chars(ciphertext)
    ics = [
        compute_char_ic(chars.get(char, 0), len(ciphertext))
        for char in alphabet
    ]
    return sum(ics)


def find_language(ciphertext):
    gap = list(IC_REFERENCE)[0]
    ic = compute_coincidence_index(ciphertext)
    for ic_reference in IC_REFERENCE:
        tmp = abs(ic - ic_reference.value)
        gap = ic_reference if tmp < abs(ic - gap.value) else gap
    return gap.name
