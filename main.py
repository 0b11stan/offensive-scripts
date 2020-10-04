#!/usr/bin/python

import sys
from caesar_breaker import decrypt_caesar
from language_finder import find_language
from utils import sanitize

if __name__ == '__main__':
    ciphertext = sanitize(sys.argv[1])
    print(decrypt_caesar(ciphertext))
