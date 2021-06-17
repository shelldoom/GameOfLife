import random
from p5 import *
from logger import logging
from pprint import pprint
from extra import *

screen_width, screen_height = 600, 600
resolution = 20
rows, cols = screen_height // resolution, screen_width // resolution

def populateRegion(arr: list[Literal[0, 1]], regions: int = 1):
    rows, cols = len(arr), len(arr[0])
    for _ in range(regions):
        r, c = random.randrange(1, rows), random.randrange(1, cols)
        for i in range(-2, 3):
            for j in range(-2, 3):
                if 0 <= r + i < rows and 0 <= c + j < cols:
                    arr[r + i][c + j] = random.randint(0, 1)
    return arr


def make2DArray(rows: int, cols: int, empty: bool=False):
    arr = [[0]*cols for _ in range(rows)]
    if not empty:
        arr = [random.choices([0, 1], k=cols, weights=[0.8, 0.2]) for _ in range(rows)]
        # arr = populateRegion(arr, 3)
    logging.debug(f'Array created with rows:{rows}, cols:{cols}, arr:{arr}')
    return arr


def draw2DArray(arr: list[Literal[0, 1]], resolution: int) -> None:
    rows, cols = len(arr), len(arr[0])
    offset = 0
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 1:
                x = j * resolution
                y = i * resolution
                fill(0)
                stroke(150)
                rect(x, y, resolution - offset, resolution - offset)


def getAliveNeighbors(arr: list[Literal[0, 1]], r: int, c: int) -> int:
    rows, cols = len(arr), len(arr[0])
    assert r < rows and c < cols
    neighborCount = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Pass thru
            neighborCount += arr[(r + i + rows) % rows][(c + j + cols)%cols]
            # Wall of Death/Life
            #  if 0 <= r + i < rows and 0 <= c + j < cols:
                # neighborCount += arr[r + i][c + j]
    neighborCount -= arr[r][c]
    return neighborCount


def newGeneration(arr: list[Literal[0, 1]]) -> list[Literal[0, 1]]:
    rows, cols = len(arr), len(arr[0])
    new_arr = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighborCount = getAliveNeighbors(arr, i, j)
            if neighborCount == 3:
                new_arr[i][j] = 1
            if neighborCount <= 1 or neighborCount >= 4:
                new_arr[i][j] = 0
            if arr[i][j] == 1 and 2 <= neighborCount <= 3:
                new_arr[i][j] = arr[i][j]
    return new_arr


arr = None
def setup():
    size(screen_width, screen_height)
    global arr
    # arr = make2DArray(rows, cols)
    arr = make2DArray(rows, cols, empty=False)
    # arr = spawnPulsar(arr)
    # Spawn 3 gliders
    # for _ in range(3):
        # arr = spawnGlider(arr)
    

def draw():
    global arr
    background(255)
    draw2DArray(arr, resolution)
    arr = newGeneration(arr)


if __name__ == "__main__":
    run(frame_rate=10)