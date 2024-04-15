from enum import Enum
from typing import List
import random


class CellState(Enum):
    ALIFE = 1
    DEAD = 0


class Cell:
    def __init__(self):
        if random.random() <= 0.7:
            self.state = CellState.DEAD
        else:
            self.state = CellState.ALIFE


Matrix = List[List[Cell]]
Vector = List[Cell]


class GameBoard:

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.board = [[Cell() for _ in range(cols)] for _ in range(rows)]

    def scan_board(self) -> None:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j])
