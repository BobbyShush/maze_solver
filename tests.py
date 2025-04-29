from window import Window
from cell import Point, Line, Cell

def run_tests():
    win = Window(800, 600)
    test_draw_cells(win)
    win.wait_for_close()

def test_draw_line(win):
    point_a = Point(0, 0)
    point_b = Point(800, 600)
    point_c = Point(0, 600)
    point_d = Point(800, 0)
    line1 = Line(point_a, point_b)
    line2 = Line(point_c, point_d)
    win.draw_line(line1, "red")
    win.draw_line(line2, "black")

def test_draw_cells(win):
    cell1 = Cell(0, 100, 500, 600, win)
    cell1.has_right_wall = False
    cell1.draw()
    cell2 = Cell(100, 200 ,400, 500, win)
    cell2.has_bottom_wall = False
    cell2.draw()
    cell3 = Cell(200, 300 ,300, 400, win)
    cell3.has_left_wall = False
    cell3.draw()
    cell4 = Cell(300, 400, 200, 300, win)
    cell4.has_top_wall = False
    cell4.draw()
    

if __name__ == "__main__":
    run_tests()