import dearpygui.dearpygui as dpg
from models import *


class Tag:
    main_window = "main_window"


step = 15
game_board = GameBoard(rows=50, cols=50)


def draw_board(board: GameBoard, step: int) -> None:
    row_number = 0
    for i in range(step, board.rows * step, step):
        col_number = 0
        for j in range(step, board.cols * step, step):
            if board.board[row_number][col_number].state == CellState.DEAD:
                dpg.draw_rectangle(pmin=(i, j), pmax=(i + step, j + step), fill=(38, 34, 34))
            else:
                dpg.draw_rectangle(pmin=(i, j), pmax=(i + step, j + step), fill=(74, 205, 217))
            col_number += 1
        row_number += 1


if __name__ == '__main__':
    dpg.create_context()

    with dpg.window(tag=Tag.main_window):
        with dpg.child_window(width=-2, height=-2):
            with dpg.drawlist(width=game_board.cols * step, height=game_board.rows * step):
                draw_board(game_board, step)

    game_board.scan_board()

    dpg.create_viewport(title='Custom Title', width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(Tag.main_window, True)
    dpg.start_dearpygui()
    dpg.destroy_context()
