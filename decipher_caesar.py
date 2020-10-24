#!/usr/bin/python

from sys import argv
from string import ascii_uppercase as alphabet

try:
    key = int(argv[1])
except:
    print("usage: {} KEY CIPHERTEXT".format(argv[0]))
    exit(1)

ciphertext = [argv[x].upper() for x in range(2, len(argv))]

plaintext = ""
for word in ciphertext:
    for character in word:
        cindex = alphabet.index(character)
        newindex = (cindex - key) % len(alphabet)
        plaintext += alphabet[newindex]
    plaintext += " "
print(plaintext)
