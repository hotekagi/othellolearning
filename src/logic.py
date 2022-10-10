from enum import Enum
import pprint

class Stone(Enum):
    EMPTY = "_"
    LIGHT = "o"
    DARK = "x"

class Board:
    def __init__(self, size=8):
        stones = [[Stone.EMPTY for _ in range(size)] for _ in range(size)]
        lu = (size - 1) // 2
        stones[lu][lu] = Stone.LIGHT
        stones[lu + 1][lu + 1] = Stone.LIGHT
        stones[lu][lu + 1] = Stone.DARK
        stones[lu + 1][lu] = Stone.DARK
        self.stones = stones

if __name__ == '__main__':
    test = Board()
    pprint.pprint([[s.value for s in row] for row in test.stones])
