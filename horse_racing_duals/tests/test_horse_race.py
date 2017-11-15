import unittest


class TestHorseRace(unittest.TestCase):

    def test_simple_case(self):
        input_ = [5, 8, 9]

        result = horse_race(input_)

        self.assertEqual(result, 1)

    def test_horses_in_any_order(self):
        input_ = [15, 17, 3, 8, 11, 28, 6, 55, 7]

        result = horse_race(input_)

        self.assertEqual(result, 1)

    def test_result_not_one(self):
        input_ = [15, 17, 3, 8, 11, 28, 6, 55]

        result = horse_race(input_)

        self.assertEqual(result, 2)
