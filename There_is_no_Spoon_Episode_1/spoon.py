import sys
import math


# Don't let the machines win. You are humanity's last hope...

class Node(object):
    def __init__(self, x_location, y_location):
        self.x = x_location
        self.y = y_location
        self.coordinate = f'{self.x}, {self.y}'
        self.x_right = -1
        self.y_right = -1
        self.x_bottom = -1
        self.y_bottom = -1
        self.used = False

    def right_neighbor(self, neighbor):
        if not neighbor:
            self.x_right = -1
            self.y_right = -1
        else:
            self.x_right = neighbor.x
            self.y_right = neighbor.y

    def bottom_neighbor(self, neighbor):
        if not neighbor:
            self.x_bottom = -1
            self.y_bottom = -1
        else:
            self.x_bottom = neighbor.x
            self.y_bottom = neighbor.y

    def __str__(self):
        return f'{self.x} {self.y} {self.x_right} {self.y_right} {self.x_bottom} {self.y_bottom}'


def find_nodes(grid):
    nodes = []

    # width = int(input())  # the number of cells on the X axis
    width = len(grid[0])
    # print(width, file=sys.stderr)
    # height = int(input())  # the number of cells on the Y axis
    height = len(grid)
    # max_x_distance = width
    # print(height, file=sys.stderr)
    for i in range(height):
        # line = input()  # width characters, each either 0 or .
        # for idx, val in enumerate(line):
            for idx, val in enumerate(grid[i]):
                if val == '0':
                    nodes.append(Node(idx, i))

    return nodes

def find_neighbors(nodes, max_x_distance, max_y_distance):
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    closest_x = []
    closest_y = []

    init_max_x = max_x_distance
    init_max_y = max_y_distance

    for item in nodes:
        node = item
        node.used = True
        for item in nodes:
            if not item.used:
                if item.y == node.y:
                    distance = item.x - node.x
                    if 0 < distance < max_x_distance:
                        closest_x = item
                        max_x_distance = distance
                if item.x == node.x:
                    distance = item.y - node.y
                    if 0 < distance < max_y_distance:
                        closest_y = item
                        max_y_distance = distance

        node.used = False
        node.right_neighbor(closest_x)
        node.bottom_neighbor(closest_y)
        # print(node, file=sys.stderr)
        closest_x = []
        closest_y = []
        max_x_distance = init_max_x
        max_y_distance = init_max_y

    return nodes
#
#
# # Three coordinates: a node, its right neighbor, its bottom neighbor
# for item in nodes:
#     print(item)
