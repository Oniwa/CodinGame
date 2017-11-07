import unittest
from ASCII_Art.ascii_art import ascii_art


class TestASCIIArt(unittest.TestCase):

    def test_letter_e(self):
        length = 4
        height = 5
        word_to_asciify = 'E'
        ASCIIbet = [' #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### ',
                    '# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # ',
                    '### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## ',
                    '# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       ',
                    '# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  ']

        ascii = ascii_art(length, height, word_to_asciify, ASCIIbet)

        self.assertEqual(ascii[0], '### ')
        self.assertEqual(ascii[1], '#   ')
        self.assertEqual(ascii[2], '##  ')
        self.assertEqual(ascii[3], '#   ')
        self.assertEqual(ascii[4], '### ')
