#!/usr/bin/python

from sys import argv
from caesar_breaker import auto_decrypt_caesar, brute_force_caesar
from language_finder import find_language
from utils import sanitize

if __name__ == '__main__':
    ciphertext = [argv[x].upper() for x in range(1, len(argv))]
    ciphertext = ' '.join(ciphertext)
    print(brute_force_caesar(ciphertext))
