from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 22, 16, 30, 30, win)
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()