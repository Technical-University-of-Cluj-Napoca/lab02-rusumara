from collections import deque
import sys

def read_maze(filename):
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]
    return maze

def find_start_end(maze):
    start = end = None
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == 'S':
                start = (i, j)
            elif val == 'T':
                end = (i, j)
    return start, end

def get_neighbors(position, maze):
    neighbors = []
    x, y = position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#':
            neighbors.append((nx, ny))
    return neighbors

def reconstruct_path(came_from, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

def bfs(maze, start, end):
    queue = deque([start])
    visited = {start}
    came_from = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            return reconstruct_path(came_from, start, end)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)
    return None

def dfs(maze, start, end):
    stack = [start]
    came_from = {start: None}
    visited = {start}

    while stack:
        current = stack.pop()
        if current == end:
            return reconstruct_path(came_from, start, end)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                stack.append(neighbor)
    return None

def print_maze_with_path(maze, path):
    for (x, y) in path:
        if maze[x][y] not in ('S', 'T'):
            maze[x][y] = '\033[91m*\033[0m'
    for row in maze:
        print(''.join(row))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ex05.py <bfs|dfs> <maze_file>")
        sys.exit(1)

    algorithm = sys.argv[1].lower()
    maze_file = sys.argv[2]
    maze = read_maze(maze_file)
    start, end = find_start_end(maze)

    if start is None or end is None:
        print("Maze must have 'S' (start) and 'T' (target).")
        sys.exit(1)

    if algorithm == "bfs":
        path = bfs(maze, start, end)
    elif algorithm == "dfs":
        path = dfs(maze, start, end)
    else:
        print("Error: Algorithm must be 'bfs' or 'dfs'.")
        sys.exit(1)

    if path:
        print_maze_with_path(maze, path)
    else:
        print("No path found.")
