import sys
import math
import string

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# l = int(input())
# h = int(input())
# t = input()
# for i in range(h):
#     row = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# print("answer")

def ascii_art(length, height, word_to_asciify, ASCIIbet):
    letter_to_number = string.lowercase

    print(letter_to_number)
    return ['### ', "#   ", '##  ', '#   ', '### ']


def word_to_numbers(word):
    letters = string.ascii_lowercase + '?'
    num_word = []

    for letter in word.lower():
        if letter in letters:
            num_word.append(letters.index(letter))
        else:
            num_word.append(letters.index('?'))

    return num_word

