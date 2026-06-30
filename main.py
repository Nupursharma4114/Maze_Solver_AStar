from maze import maze
from astar import a_star

start = None
goal = None

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            start = (i, j)
        elif maze[i][j] == "G":
            goal = (i, j)

print("Start:", start)
print("Goal:", goal)

path = a_star(maze, start, goal)

if path:
    print("\nShortest Path:")
    print(path)

    # Create a copy of the maze
    solved_maze = [row[:] for row in maze]

    # Mark the shortest path with *
    for row, col in path:
        if solved_maze[row][col] not in ("S", "G"):
            solved_maze[row][col] = "*"

    print("\nMaze with Shortest Path:\n")

    for row in solved_maze:
        print(" ".join(row))

else:
    print("No path found.")

