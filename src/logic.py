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
        self.turn = Stone.DARK

    def refresh(self, size=8):
        self.__init__(size=size)

    def change_turn(self):
        if self.turn == Stone.DARK:
            self.turn = Stone.LIGHT
        else:
            self.turn = Stone.DARK

    def put_stone(self, idx0, idx1):
        self.stones[idx0][idx1] = self.turn

    def is_empty(self, idx0, idx1):
        return self.stones[idx0][idx1] == Stone.EMPTY

if __name__ == '__main__':
    test = Board()
    pprint.pprint([[s.value for s in row] for row in test.stones])
