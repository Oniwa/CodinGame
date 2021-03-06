import unittest
from ASCII_Art.ascii_art import ascii_art, word_to_numbers


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

    def test_manhattan(self):
        length = 4
        height = 5
        word_to_asciify = 'MANHATTAN'
        ASCIIbet = [' #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### ',
                    '# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # ',
                    '### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## ',
                    '# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       ',
                    '# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  ']

        ascii = ascii_art(length, height, word_to_asciify, ASCIIbet)

        self.assertEqual(ascii[0], '# #  #  ### # #  #  ### ###  #  ### ')
        self.assertEqual(ascii[1], '### # # # # # # # #  #   #  # # # # ')
        self.assertEqual(ascii[2], '### ### # # ### ###  #   #  ### # # ')
        self.assertEqual(ascii[3], '# # # # # # # # # #  #   #  # # # # ')
        self.assertEqual(ascii[4], '# # # # # # # # # #  #   #  # # # # ')

    def test_ManhAtTan(self):
        length = 4
        height = 5
        word_to_asciify = 'ManhAtTan'
        ASCIIbet = [' #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### ',
                    '# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # ',
                    '### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## ',
                    '# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       ',
                    '# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  ']

        ascii = ascii_art(length, height, word_to_asciify, ASCIIbet)

        self.assertEqual(ascii[0], '# #  #  ### # #  #  ### ###  #  ### ')
        self.assertEqual(ascii[1], '### # # # # # # # #  #   #  # # # # ')
        self.assertEqual(ascii[2], '### ### # # ### ###  #   #  ### # # ')
        self.assertEqual(ascii[3], '# # # # # # # # # #  #   #  # # # # ')
        self.assertEqual(ascii[4], '# # # # # # # # # #  #   #  # # # # ')

    def test_manhattan_with_special_characters(self):
        length = 4
        height = 5
        word_to_asciify = 'M@NH@TT@N'
        ASCIIbet = [' #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### ',
                    '# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # ',
                    '### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## ',
                    '# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       ',
                    '# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  ']

        ascii = ascii_art(length, height, word_to_asciify, ASCIIbet)

        self.assertEqual(ascii[0], '# # ### ### # # ### ### ### ### ### ')
        self.assertEqual(ascii[1], '###   # # # # #   #  #   #    # # # ')
        self.assertEqual(ascii[2], '###  ## # # ###  ##  #   #   ## # # ')
        self.assertEqual(ascii[3], '# #     # # # #      #   #      # # ')
        self.assertEqual(ascii[4], '# #  #  # # # #  #   #   #   #  # # ')

    def test_manhattan_with_different_ASCIIbet(self):
        length = 20
        height = 11
        word_to_asciify = 'MANHATTAN'
        ASCIIbet = [" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ",
                    "| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |",
                    "| |      __      | || |   ______     | || |     ______   | || |  ________    | || |  _________   | || |  _________   | || |    ______    | || |  ____  ____  | || |     _____    | || |     _____    | || |  ___  ____   | || |   _____      | || | ____    ____ | || | ____  _____  | || |     ____     | || |   ______     | || |    ___       | || |  _______     | || |    _______   | || |  _________   | || | _____  _____ | || | ____   ____  | || | _____  _____ | || |  ____  ____  | || |  ____  ____  | || |   ________   | || |    ______    | |",
                    "| |     /  \     | || |  |_   _ \    | || |   .' ___  |  | || | |_   ___ `.  | || | |_   ___  |  | || | |_   ___  |  | || |  .' ___  |   | || | |_   ||   _| | || |    |_   _|   | || |    |_   _|   | || | |_  ||_  _|  | || |  |_   _|     | || ||_   \  /   _|| || ||_   \|_   _| | || |   .'    `.   | || |  |_   __ \   | || |  .'   '.     | || | |_   __ \    | || |   /  ___  |  | || | |  _   _  |  | || ||_   _||_   _|| || ||_  _| |_  _| | || ||_   _||_   _|| || | |_  _||_  _| | || | |_  _||_  _| | || |  |  __   _|  | || |   / _ __ `.  | |",
                    "| |    / /\ \    | || |    | |_) |   | || |  / .'   \_|  | || |   | |   `. \ | || |   | |_  \_|  | || |   | |_  \_|  | || | / .'   \_|   | || |   | |__| |   | || |      | |     | || |      | |     | || |   | |_/ /    | || |    | |       | || |  |   \/   |  | || |  |   \ | |   | || |  /  .--.  \  | || |    | |__) |  | || | /  .-.  \    | || |   | |__) |   | || |  |  (__ \_|  | || | |_/ | | \_|  | || |  | |    | |  | || |  \ \   / /   | || |  | | /\ | |  | || |   \ \  / /   | || |   \ \  / /   | || |  |_/  / /    | || |  |_/____) |  | |",
                    "| |   / ____ \   | || |    |  __'.   | || |  | |         | || |   | |    | | | || |   |  _|  _   | || |   |  _|      | || | | |    ____  | || |   |  __  |   | || |      | |     | || |   _  | |     | || |   |  __'.    | || |    | |   _   | || |  | |\  /| |  | || |  | |\ \| |   | || |  | |    | |  | || |    |  ___/   | || | | |   | |    | || |   |  __ /    | || |   '.___`-.   | || |     | |      | || |  | '    ' |  | || |   \ \ / /    | || |  | |/  \| |  | || |    > `' <    | || |    \ \/ /    | || |     .'.' _   | || |    /  ___.'  | |",
                    "| | _/ /    \ \_ | || |   _| |__) |  | || |  \ `.___.'\  | || |  _| |___.' / | || |  _| |___/ |  | || |  _| |_       | || | \ `.___]  _| | || |  _| |  | |_  | || |     _| |_    | || |  | |_' |     | || |  _| |  \ \_  | || |   _| |__/ |  | || | _| |_\/_| |_ | || | _| |_\   |_  | || |  \  `--'  /  | || |   _| |_      | || | \  `-'  \_   | || |  _| |  \ \_  | || |  |`\____) |  | || |    _| |_     | || |   \ `--' /   | || |    \ ' /     | || |  |   /\   |  | || |  _/ /'`\ \_  | || |    _|  |_    | || |   _/ /__/ |  | || |    |_|       | |",
                    "| ||____|  |____|| || |  |_______/   | || |   `._____.'  | || | |________.'  | || | |_________|  | || | |_____|      | || |  `._____.'   | || | |____||____| | || |    |_____|   | || |  `.___.'     | || | |____||____| | || |  |________|  | || ||_____||_____|| || ||_____|\____| | || |   `.____.'   | || |  |_____|     | || |  `.___.\__|  | || | |____| |___| | || |  |_______.'  | || |   |_____|    | || |    `.__.'    | || |     \_/      | || |  |__/  \__|  | || | |____||____| | || |   |______|   | || |  |________|  | || |    (_)       | |",
                    "| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |",
                    "| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |",
                    " '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' "]

        ascii = ascii_art(length, height, word_to_asciify, ASCIIbet)

        self.assertEqual(ascii[0],  " .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.")
        self.assertEqual(ascii[1],  "| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
        self.assertEqual(ascii[2],  "| | ____    ____ | || |      __      | || | ____  _____  | || |  ____  ____  | || |      __      | || |  _________   | || |  _________   | || |      __      | || | ____  _____  | |")
        self.assertEqual(ascii[3],  "| ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | || | |_   ||   _| | || |     /  \     | || | |  _   _  |  | || | |  _   _  |  | || |     /  \     | || ||_   \|_   _| | |")
        self.assertEqual(ascii[4],  "| |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | || |   | |__| |   | || |    / /\ \    | || | |_/ | | \_|  | || | |_/ | | \_|  | || |    / /\ \    | || |  |   \ | |   | |")
        self.assertEqual(ascii[5],  "| |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | || |   |  __  |   | || |   / ____ \   | || |     | |      | || |     | |      | || |   / ____ \   | || |  | |\ \| |   | |")
        self.assertEqual(ascii[6],  "| | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | || |  _| |  | |_  | || | _/ /    \ \_ | || |    _| |_     | || |    _| |_     | || | _/ /    \ \_ | || | _| |_\   |_  | |")
        self.assertEqual(ascii[7],  "| ||_____||_____|| || ||____|  |____|| || ||_____|\____| | || | |____||____| | || ||____|  |____|| || |   |_____|    | || |   |_____|    | || ||____|  |____|| || ||_____|\____| | |")
        self.assertEqual(ascii[8],  "| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |")
        self.assertEqual(ascii[9],  "| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
        self.assertEqual(ascii[10], " '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ")


class TestWordToNumbers(unittest.TestCase):

    def test_word_to_numbers_manhattan(self):
        word = 'manhattan'

        num_word = word_to_numbers(word)

        self.assertEqual(num_word, [12, 0, 13, 7, 0, 19, 19, 0, 13])

    def test_word_to_numbers_e(self):
        word = 'e'

        num_word = word_to_numbers(word)

        self.assertEqual(num_word, [4])

    def test_word_to_numbers_manhattan_with_special_characters(self):
        word = 'm@nh@tt@n'

        num_word = word_to_numbers(word)

        self.assertEqual(num_word, [12, 26, 13, 7, 26, 19, 19, 26, 13])

    def test_word_to_numbers_ManhAtTan(self):
        word = 'ManhAtTan'

        num_word = word_to_numbers(word)

        self.assertEqual(num_word, [12, 0, 13, 7, 0, 19, 19, 0, 13])

    def test_word_to_numbers_dog(self):
        word = 'dog'

        num_word = word_to_numbers(word)

        self.assertEqual(num_word, [3, 14, 6])

    def test_word_to_numbers_pneumonoultramicroscopicsilicovolcanoconiosis(self):
        word = 'pneumonoultramicroscopicsilicovolcanoconiosis'

        num_word = word_to_numbers(word)

        self.assertEqual(num_word, [15, 13, 4, 20, 12, 14, 13, 14, 20, 11, 19, 17, 0, 12, 8, 2, 17, 14, 18, 2, 14, 15, 8, 2, 18, 8, 11, 8, 2, 14, 21, 14, 11, 2, 0, 13, 14, 2, 14, 13, 8, 14, 18, 8, 18])
