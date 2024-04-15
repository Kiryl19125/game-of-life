from enum import Enum
from typing import List
import random


class CellState(Enum):
    ALIFE = 1
    DEAD = 0


class Cell:
    def __init__(self):
        if random.random() <= 0.9:
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
                alife_counter = 0
                neighbors = self.__get_neighbors(i, j)
                for neighbor in neighbors:
                    if neighbor.state == CellState.ALIFE:
                        alife_counter += 1
                if self.board[i][j].state == CellState.DEAD and alife_counter == 3:
                    self.board[i][j].state = CellState.ALIFE
                if self.board[i][j].state == CellState.ALIFE and (alife_counter < 2 or alife_counter > 3):
                    self.board[i][j].state = CellState.DEAD

    def __get_neighbors(self, row: int, col: int):
        neighbors = []
        rows = len(self.board)
        cols = len(self.board[0])

        # Define the range for neighboring cells
        row_range = range(max(0, row - 1), min(rows, row + 2))
        col_range = range(max(0, col - 1), min(cols, col + 2))

        # Iterate over neighboring cells
        for i in row_range:
            for j in col_range:
                if (i, j) != (row, col):
                    neighbors.append(self.board[i][j])

        return neighbors
