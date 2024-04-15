import dearpygui.dearpygui as dpg
from enum import Enum
from typing import List


class Tag:
    main_window = "main_window"


class CellState(Enum):
    ALIFE = 1
    DEAD = 0


class Cell:
    def __init__(self):
        self.state = CellState.DEAD


class GameBoard:

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.board = [[Cell()] * cols] * rows


Matrix = List[List[Cell]]
Vector = List[Cell]

step = 20

game_board = GameBoard(rows=10, cols=10)


def draw_board() -> None:
    for i in range(0, game_board.rows * step, step):
        for j in range(0, game_board.cols * step, step):
            dpg.draw_rectangle(pmin=(i, j), pmax=(i + step, j + step))


def show_board(board: GameBoard) -> None:
    for row in board.board:
        print([cell.state.value for cell in row])


if __name__ == '__main__':
    dpg.create_context()

    with dpg.window(tag=Tag.main_window):
        with dpg.child_window(width=-2, height=-2):
            with dpg.drawlist(width=game_board.cols * step, height=game_board.rows * step):
                draw_board()

    show_board(game_board)

    dpg.create_viewport(title='Custom Title', width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(Tag.main_window, True)
    dpg.start_dearpygui()
    dpg.destroy_context()
