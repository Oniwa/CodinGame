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
    asciified_text = []

    num_word = word_to_numbers(word_to_asciify)
    for row in range(height):
        line =''
        for number in num_word:
            ASCII_letter_low = number * length
            ASCII_letter_high = (number * length) + length
            line += ASCIIbet[row][ASCII_letter_low:ASCII_letter_high]

        asciified_text.append(line)

    return asciified_text


def word_to_numbers(word):
    letters = string.ascii_lowercase + '?'
    num_word = []

    for letter in word.lower():
        if letter in letters:
            num_word.append(letters.index(letter))
        else:
            num_word.append(letters.index('?'))

    return num_word

def print_ASCII_art(length, height, word_to_asciify, ASCIIbet):
    for item in ascii_art(length, height, word_to_asciify, ASCIIbet):
        print(item)

if __name__ == "__main__":
    print_ASCII_art(4, 5, 'ASCIIART', ASCIIbet = [' #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### ',
                    '# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # ',
                    '### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## ',
                    '# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       ',
                    '# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  ']
)
