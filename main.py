import dearpygui.dearpygui as dpg
from models import *
import time

step = 5

rows = 180
cols = 180

game_board = GameBoard(rows, cols)
delay_between_steps = 0


def __draw_board(board: GameBoard, step: int) -> None:
    row_number = 0
    for i in range(step, board.rows * step, step):
        col_number = 0
        for j in range(step, board.cols * step, step):
            if board.board[row_number][col_number].state == CellState.DEAD:
                dpg.draw_rectangle(pmin=(i, j), pmax=(i + step, j + step), fill=(0, 0, 0), color=(162, 166, 166),
                                   parent=Tag.draw_list)
            else:
                dpg.draw_rectangle(pmin=(i, j), pmax=(i + step, j + step), fill=(12, 210, 232), color=(162, 166, 166),
                                   parent=Tag.draw_list)
            col_number += 1
        row_number += 1


def __clear_draw_list() -> None:
    dpg.delete_item(Tag.draw_list)
    dpg.add_drawlist(tag=Tag.draw_list, width=game_board.cols * step, height=game_board.rows * step,
                     parent=Tag.child_window)


def next_iteration() -> None:
    game_board.scan_board()
    __clear_draw_list()
    __draw_board(game_board, step)
    time.sleep(delay_between_steps)


def restart() -> None:
    global game_board
    game_board = GameBoard(rows=rows, cols=cols)


class Tag:
    main_window = "main_window"
    draw_list = "draw_list"
    child_window = "child_window"


if __name__ == '__main__':
    dpg.create_context()

    dpg.add_window(tag=Tag.main_window)
    dpg.add_button(label="RESTART", parent=Tag.main_window, callback=restart)
    dpg.add_child_window(tag=Tag.child_window, width=-2, height=-2, horizontal_scrollbar=True, parent=Tag.main_window)
    dpg.add_drawlist(tag=Tag.draw_list, width=game_board.cols * step, height=game_board.rows * step,
                     parent=Tag.child_window)

    dpg.create_viewport(title='The Game of Life', width=1000, height=1000)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(Tag.main_window, True)
    while dpg.is_dearpygui_running():
        next_iteration()
        dpg.render_dearpygui_frame()

    dpg.destroy_context()
