import unittest
from There_is_no_Spoon_Episode_1.spoon import find_nodes, find_neighbors


class TestSpoon(unittest.TestCase):

    def test_can_find_nodes_example(self):
        grid = ['00', '0.']

        nodes = find_nodes(grid)

        self.assertEqual(len(nodes), 3)

    def test_can_find_nodes_complex(self):
        grid = ['00.0',
                '0.00',
                '.0.0',
                '000.']

        nodes = find_nodes(grid)

        self.assertEqual(len(nodes), 11)

    def test_example(self):
        grid = ['00', '0.']

        nodes = find_nodes(grid)

        nodes = find_neighbors(nodes, len(grid[0]), len(grid))

        self.assertEqual(str(nodes[0]), '0 0 1 0 0 1')
        self.assertEqual(str(nodes[1]), '1 0 -1 -1 -1 -1')
        self.assertEqual(str(nodes[2]), '0 1 -1 -1 -1 -1')

    def test_complex(self):
        grid = ['00.0',
                '0.00',
                '.0.0',
                '000.']

        nodes = find_nodes(grid)

        nodes = find_neighbors(nodes, len(grid[0]), len(grid))

        self.assertEqual(str(nodes[0]), '0 0 1 0 0 1')
        self.assertEqual(str(nodes[1]), '1 0 3 0 1 2')
        self.assertEqual(str(nodes[2]), '3 0 -1 -1 3 1')
        self.assertEqual(str(nodes[3]), '0 1 2 1 0 3')
        self.assertEqual(str(nodes[4]), '2 1 3 1 2 3')
        self.assertEqual(str(nodes[5]), '3 1 -1 -1 3 2')
        self.assertEqual(str(nodes[6]), '1 2 3 2 1 3')
        self.assertEqual(str(nodes[7]), '3 2 -1 -1 -1 -1')
        self.assertEqual(str(nodes[8]), '0 3 1 3 -1 -1')
        self.assertEqual(str(nodes[9]), '1 3 2 3 -1 -1')
        self.assertEqual(str(nodes[10]), '2 3 -1 -1 -1 -1')
