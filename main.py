#!/usr/bin/python3

"""
Julius Caesar protected his confidential information by encrypting it using a cipher.
Caesar's cipher shifts each letter by a number of letters. If the shift takes you
past the end of the alphabet, just rotate back to the front of the alphabet.
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      i love python
Alphabet rotated +3:    l oryh sbwkrq 
"""
def caesar_cipher(s):
    result = ""
    k = 3  # Default key value is 3
    for char in s:
        n = ord(char)
        if  n < 91:
            n = ((n + k) % 26) + 65
        if 96 < n < 123:
            n = ((n - 97 + k) % 26) + 97
        result = chr(n)
    return result

