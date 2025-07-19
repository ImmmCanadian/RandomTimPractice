import matplotlib.pyplot as plt
import numpy as np
import random
import queue
from curses import wrapper
import curses
import time

def create_maze(dim):
    shape = (dim*2 + 1, dim*2 + 1)
    maze = np.full(shape, "#", dtype=object)

    x, y = (0, 0)
    maze[2*x+1, 2*y+1] = " "

    stack = [(x, y)]
    while stack:
        x, y = stack[-1]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < dim and 0 <= ny < dim and maze[2*nx+1, 2*ny+1] == "#":
                maze[2*nx+1, 2*ny+1] = " "
                maze[2*x+1+dx, 2*y+1+dy] = " "
                stack.append((nx, ny))
                break
        else:
            stack.pop()

    # Add entrance and exit
    maze[1, 0] = "S"
    maze[-2, -1] = "E"

    return maze

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == " ":
                stdscr.addstr(i, j * 2, " ")
            elif value in ("S", "E"):
                stdscr.addstr(i, j * 2, value, RED)
            else:
                stdscr.addstr(i, j * 2, value, BLUE)

    for (x, y) in path:
        stdscr.addstr(x, y * 2, "X", RED)

def find_path(maze, stdscr):
    start = "S"
    end = "E"
    start_pos = find_start(maze, start)
    if not start_pos:
        return None

    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = set()
    visited.add(start_pos)

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        stdscr.refresh()
        time.sleep(0.02)

        if maze[row][col] == end:
            return path

        neighbors = find_valid_neighbours(maze, visited, row, col)
        for neighbor in neighbors:
            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)

    return None

def find_start(maze, target):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == target:
                return (i, j)

def find_valid_neighbours(maze, visited, r, c):
    neighbors = []
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 < nr < len(maze) and 0 < nc < len(maze[0]):
            if (nr, nc) not in visited and maze[nr][nc] != "#":
                neighbors.append((nr, nc))
    return neighbors

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.addstr(0, 0, "Enter maze size (e.g., 10): ")
    stdscr.refresh()

    # Input validation
    while True:
        try:
            key = stdscr.getkey()
            dim = int(key)
            if dim > 0:
                break
            else:
                stdscr.addstr(1, 0, "Must be > 0")
        except ValueError:
            stdscr.addstr(1, 0, "Invalid input. Try again.")

    maze = create_maze(dim)

    stdscr.clear()
    print_maze(maze, stdscr)
    stdscr.addstr(dim*2 + 3, 0, "Press any key to start pathfinding...")
    stdscr.refresh()
    stdscr.getch()

    stdscr.clear()
    path = find_path(maze, stdscr)
    if path:
        stdscr.addstr(dim*2 + 3, 0, "Path found! Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)