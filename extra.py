import random
from typing import Literal

def spawnGlider(arr, x=None, y=None):
    """
    Spawn a glider at random position (if position is not specified)
    """
    rows, cols = len(arr), len(arr[0])
    x, y = random.randrange(1, rows - 1), random.randrange(1, cols - 1)
    arr[x - 1][y - 1] = 1
    arr[x    ][y    ] = 1
    arr[x + 1][y    ] = 1
    arr[x    ][y + 1] = 1
    arr[x + 1][y - 1] = 1
    return arr


"""
Reference for pulsar

    0123456789012
  0 ..OOO...OOO..
  1 .............
  2 O....O.O....O
  3 O....O.O....O
  4 O....O.O....O
  5 ..OOO...OOO..
  6 .............
  7 ..OOO...OOO..
  8 O....O.O....O
  9 O....O.O....O
 10 O....O.O....O
 11 .............
 12 ..OOO...OOO..
"""


def spawnPulsar(arr:list[Literal[0, 1]], x=None, y=None):
    """
    Spawn a 3 period pulsar at random position (if position is not specified)
    """
    rows, cols = len(arr), len(arr[0])
    x, y = random.randrange(1, rows - 1), random.randrange(1, cols - 1)
    while x + 12 >= rows or y + 12 >= cols:
        x, y = random.randrange(rows), random.randrange(cols)

    for tmp_y in [y, y + 5, y + 7, y + 12]:
        arr[x + 2 ][tmp_y] = 1
        arr[x + 3 ][tmp_y] = 1
        arr[x + 4 ][tmp_y] = 1
        arr[x + 8 ][tmp_y] = 1
        arr[x + 9 ][tmp_y] = 1
        arr[x + 10][tmp_y] = 1

    for tmp_x in [x, x + 5, x + 7, x + 12]:
        for tmp_y in [y, y + 6]:
            arr[tmp_x][tmp_y + 2] = 1
            arr[tmp_x][tmp_y + 3] = 1
            arr[tmp_x][tmp_y + 4] = 1
    return arr