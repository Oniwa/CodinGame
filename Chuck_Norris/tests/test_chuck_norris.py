import unittest

from Chuck_Norris.chuck_norris import chuck_norris, message_to_binary, binary_grouping


class TestMessageToBinary(unittest.TestCase):

    def test_message_to_binary_c(self):
        binary = message_to_binary('C')

        self.assertEqual(binary, '1000011')

    def test_message_to_binary_cc(self):
        binary = message_to_binary('CC')

        self.assertEqual(binary, '10000111000011')

    def test_message_to_binary_percent_sign(self):
        binary = message_to_binary('%')

        self.assertEqual(binary, '0100101')


class TestBinaryGrouping(unittest.TestCase):
    def test_binary_grouping_c(self):
        binary = list('1000011')

        grouped = binary_grouping(binary)

        self.assertEqual(grouped, ['1', '0000', '11'])

    def test_binary_grouping_cc(self):
        binary = list('10000111000011')

        grouped = binary_grouping(binary)

        self.assertEqual(grouped, ['1', '0000', '111', '0000', '11'])

    def test_binary_grouping_percent_sign(self):
        binary = list('0100101')

        grouped = binary_grouping(binary)

        self.assertEqual(grouped, ['0', '1', '00', '1', '0', '1'])

    def test_binary_grouping_alternating(self):
        binary = list('0101010101010101')

        grouped = binary_grouping(binary)

        self.assertEqual(grouped, ['0', '1', '0', '1', '0', '1', '0', '1',
                                   '0', '1', '0', '1', '0', '1', '0', '1'])


class TestChuckNorris(unittest.TestCase):

    def test_chuck_norris_c(self):
        unary = chuck_norris('C')

        self.assertEqual(unary, '0 0 00 0000 0 00')

    def test_chuck_norris_cc(self):
        unary = chuck_norris('CC')

        self.assertEqual(unary, '0 0 00 0000 0 000 00 0000 0 00')

    def test_chuck_norris_percent_sign(self):
        unary = chuck_norris('%')

        self.assertEqual(unary, '00 0 0 0 00 00 0 0 00 0 0 0')

    def test_chuck_norris_message_from_chuck_norris(self):
        unary = chuck_norris("Chuck Norris' keyboard has"
                             " 2 keys: 0 and white space.")

        self.assertEqual(unary, '0 0 00 0000 0 0000 00 0 0 0 00 000 0 000 00 '
                                '0 0 0 00 0 0 000 00 000 0 0000 00 0 0 0 00 0 '
                                '0 00 00 0 0 0 00 00000 0 0 00 00 0 000 00 0 0 '
                                '00 00 0 0 0000000 00 00 0 0 00 0 0 000 00 00 '
                                '0 0 00 0 0 00 00 0 0 0 00 00 0 0000 00 00 0 '
                                '00 00 0 0 0 00 00 0 000 00 0 0 0 00 00000 0 '
                                '00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 '
                                '00000 00 00 0 000 00 000 0 0 00 0 0 00 00 0 0 '
                                '000000 00 0000 0 0000 00 00 0 0 00 0 0 00 00 '
                                '00 0 0 00 000 0 0 00 00000 0 00 00 0 0 0 00 '
                                '000 0 00 00 0000 0 0000 00 00 0 00 00 0 0 0 '
                                '00 000000 0 00 00 00 0 0 00 00 0 0 00 00000 0 '
                                '00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 '
                                '00000 00 00 0 0000 00 00 0 00 00 0 0 000 00 0 '
                                '0 0 00 00 0 0 00 000000 0 00 00 00000 0 0 00 '
                                '00000 0 00 00 0000 0 000 00 0 0 000 00 0 0 00 '
                                '00 00 0 0 00 000 0 0 00 00000 0 000 00 0 0 '
                                '00000 00 0 0 0 00 000 0 00 00 0 0 0 00 00 0 '
                                '0000 00 0 0 0 00 00 0 00 00 00 0 0 00 0 0 0 '
                                '00 0 0 0 00 00000 0 000 00 00 0 00000 00 0000 '
                                '0 00 00 0000 0 000 00 000 0 0000 00 00 0 0 00 '
                                '0 0 0 00 0 0 0 00 0 0 000 00 0')
