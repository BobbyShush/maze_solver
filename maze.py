import time
import random

from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_cols,
        num_rows,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._create_cells()
        if seed:
            self.seed = random.seed(seed)

    def _create_cells(self):
        self._cells = []
        for i in range(self.__num_cols):
            self._cells.append([])
            for j in range(self.__num_rows):
                self._cells[i].append(Cell(self.__win))
                self._draw_cell(i, j)           

    def _draw_cell(self, i, j):
        x1 = self.__x1 + (self.__cell_size_x * i)
        y1 = self.__y1 + (self.__cell_size_y * j)
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.__win is not None:
            self.__win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        last_row = len(self._cells[0]) - 1
        last_col = len(self._cells) - 1
        self._cells[last_col][last_row].has_bottom_wall = False
        self._draw_cell(last_col, last_row)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            tbv = []
            for dir, coords in self._get_neighbors(i, j).items():
                if coords:
                    if not self._cells[coords[0]][coords[1]].visited:
                        tbv.append((dir, coords))
            if len(tbv) == 0:
                self._draw_cell(i, j)
                return
            rand_dir_index = random.randrange(len(tbv))
            rand_dir = tbv[rand_dir_index]
            self._travel(i, j, rand_dir)

    def _get_neighbors(self, i, j):
        neighbors = {}
        neighbors["north"] = (i, j-1) if j > 0 else None
        neighbors["south"] = (i, j+1) if j < len(self._cells[0]) - 1 else None
        neighbors["east"] = (i+1, j) if i < len(self._cells) - 1 else None
        neighbors["west"] = (i-1, j) if i > 0 else None
        return neighbors

    def _travel(self, i, j, dir):
        current = self._cells[i][j]
        going_to = self._cells[dir[1][0]][dir[1][1]]
        wall_pairs = {
            "north": ("has_top_wall", "has_bottom_wall"),
            "south": ("has_bottom_wall", "has_top_wall"),
            "east": ("has_right_wall", "has_left_wall"),
            "west": ("has_left_wall", "has_right_wall")
        }
        has_wall = wall_pairs[dir[0]]
        setattr(current, has_wall[0], False)
        setattr(going_to, has_wall[1], False)
        self._draw_cell(i, j)
        self._draw_cell(dir[1][0], dir[1][1])
        self._break_walls_r(dir[1][0], dir[1][1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False    
