import unittest

# from window import Window #Uncomment for visual tests
# from cell import Point, Line, Cell #Uncomment for visual tests
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_create_cells_small(self):
        num_cols = 5
        num_rows = 3
        m = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(len(m._cells), num_cols)
        self.assertEqual(len(m._cells[0]), num_rows)

    def test_maze_create_cells_large(self):
        num_cols = 25
        num_rows = 30
        m = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(len(m._cells), num_cols)
        self.assertEqual(len(m._cells[0]), num_rows)

    def test_break_entrace_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(False, m1._cells[0][0].has_top_wall)
        self.assertEqual(False, m1._cells[-1][-1].has_bottom_wall)

    def test_reset_cells_visited(self):
        maze = Maze(50, 50, 8, 6, 70, 70)
        maze._break_entrance_and_exit()
        maze._break_walls_r(0, 0)
        maze._reset_cells_visited()
        self.assertEqual(True, all([not cell.visited for row in maze._cells for cell in row]))


def run_tests():
    win = Window(800, 600)
    # insert visual tests here
    visual_test_solve(win)
    win.wait_for_close()

def test_draw_line(win): # visual test
    point_a = Point(0, 0)
    point_b = Point(800, 600)
    point_c = Point(0, 600)
    point_d = Point(800, 0)
    line1 = Line(point_a, point_b)
    line2 = Line(point_c, point_d)
    win.draw_line(line1, "red")
    win.draw_line(line2, "black")

def test_draw_cells(win): # visual test
    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(0, 500, 100, 600)
    cell2 = Cell(win)
    cell2.has_bottom_wall = False
    cell2.draw(100, 400, 200, 500)
    cell3 = Cell(win)
    cell3.has_left_wall = False
    cell3.draw(200, 300, 300, 400)
    cell4 = Cell(win)
    cell4.has_top_wall = False
    cell4.draw(300, 200, 400, 300)

def test_draw_move(win): # visual test
    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(0, 500, 100, 600)
    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.draw(100, 500, 200, 600)
    cell1.draw_move(cell2, True)

def visual_test_maze_create_cells(win):
    maze = Maze(0, 0, 8, 6, 100, 100, win)

def visual_test_break_entrace_and_exit(win):
    maze = Maze(50, 50, 8, 6, 70, 70, win)
    maze._break_entrance_and_exit()

def visual_test_break_walls_r(win):
    maze = Maze(50, 50, 8, 6, 70, 70, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    
def visual_test_solve(win):
    maze = Maze(50, 50, 8, 6, 70, 70, win)
    print(maze.solve())

if __name__ == "__main__":
    # run_tests() # Uncomment to run visual tests
    # unittest.main() # Uncomment for logic tests