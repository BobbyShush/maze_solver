class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_left_wall and self._win is not None:
            self._win.draw_line(left_wall, "black")
        elif self._win is not None:
            self._win.draw_line(left_wall, "white")

        if self.has_right_wall and self._win is not None:
            self._win.draw_line(right_wall, "black")
        elif self._win is not None:
            self._win.draw_line(right_wall, "white")

        if self.has_top_wall and self._win is not None:
            self._win.draw_line(top_wall, "black")
        elif self._win is not None:
            self._win.draw_line(top_wall, "white")

        if self.has_bottom_wall and self._win is not None:
            self._win.draw_line(bottom_wall, "black")
        elif self._win is not None:
            self._win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        point_a = Point((self._x1 + self._x2) // 2,  (self._y1 + self._y2) // 2)
        point_b = Point((to_cell._x1 + to_cell._x2) // 2,  (to_cell._y1 + to_cell._y2) // 2)
        move = Line(point_a, point_b)
        self._win.draw_line(move, "gray" if undo else "red")