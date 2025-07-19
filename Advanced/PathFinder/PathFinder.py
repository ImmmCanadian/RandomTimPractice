import matplotlib.pyplot as plt
import numpy as np
import random
import queue
from curses import wrapper
import curses

def create_maze(dim):
    # Create a grid filled with walls
    shape = (dim*2+1, dim*2+1)
    maze = np.full(shape, "#", dtype=object)

    # Define the starting point
    x, y = (0, 0)
    maze[2*x+1, 2*y+1] = 0

    # Initialize the stack with the starting point
    stack = [(x, y)]
    while len(stack) > 0:
        x, y = stack[-1]

        # Define possible directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and nx < dim and ny < dim and maze[2*nx+1, 2*ny+1] == "#":
                maze[2*nx+1, 2*ny+1] = 0
                maze[2*x+1+dx, 2*y+1+dy] = 0
                stack.append((nx, ny))
                break
        else:
            stack.pop()
            
    # Create an entrance and an exit
    maze[1, 0] = "S"
    maze[-2, -1] = "E"
    
    return maze

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == 0:
                stdscr.addstr(i,j*2," ")
            else:
                stdscr.addstr(i,j*2,str(value), BLUE)
    if len(path)>0: 
        for x, row in enumerate(path):
            for y, _ in enumerate(row):
                stdscr.addstr(i,j*2,"X", RED)
    

def find_path(maze, stdscr):
    start = "S"
    end= "E"
    start_pos = find_start(maze,start)
    x,y = start_pos

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()
    visited.add(start_pos)

    while q.qsize() > 0:
        current_pos, path = q.get()
        row,col=current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        stdscr.refresh()

        if maze[row][col]==end:
            return path
        
        neighbours = find_valid_neighbours(maze, visited, row, col)

        for neighbour in neighbours:
            
            q.put((neighbour, path + neighbour))
            visited.add(neighbour)
    
def find_start(maze,start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return (i,j)

def find_valid_neighbours(maze, visited, current_row, current_column):
    neighbours = []
    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    for i,j in directions:
        #Checking if the neighbour is inside of the maze boundaries
        if current_row + i > 0 and current_row + i < len(maze) and current_column + j > 0 and current_column + j < len(maze[0]):
            #Checking if we already visited the neighbour and is not a wall
            if (current_row + i,current_column+j) not in visited and maze[current_row + i][current_column+j] != "#":
                neighbours.append((current_row + i,current_column+j))
    return neighbours




def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.addstr(0, 0, "Please enter how large you would like the maze to be: ")
    dim = int(stdscr.getkey())
    maze = create_maze(dim)

    stdscr.clear()
    print_maze(maze, stdscr)
    stdscr.addstr(dim+6,0,"Press any key to begin the shortest path finder.")
    stdscr.refresh()
    stdscr.getch()

    stdscr.clear()
    find_path(maze, stdscr)
    stdscr.refresh()
    stdscr.getch()


wrapper(main)