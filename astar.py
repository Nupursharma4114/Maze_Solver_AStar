import heapq
from utils import manhattan_distance


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent

        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


def a_star(maze, start, goal):

    print("A* algorithm started!")

    start_node = Node(start)
    goal_node = Node(goal)

    open_list = []
    closed_list = []

    heapq.heappush(open_list, start_node)

    while open_list:

        current_node = heapq.heappop(open_list)

        # Skip if already visited
        if current_node.position in closed_list:
            continue

        closed_list.append(current_node.position)

        print("\nCurrent Node:", current_node.position)

        # Goal found
        if current_node.position == goal:
            print("\nGoal Reached!")

            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent

            path.reverse()
            return path

        # Possible directions
        directions = [
            (-1, 0),   # Up
            (1, 0),    # Down
            (0, -1),   # Left
            (0, 1)     # Right
        ]

        for move in directions:

            new_row = current_node.position[0] + move[0]
            new_col = current_node.position[1] + move[1]

            # Boundary check
            if new_row < 0 or new_row >= len(maze):
                continue

            if new_col < 0 or new_col >= len(maze[0]):
                continue

            # Skip walls
            if maze[new_row][new_col] == "#":
                continue

            # Skip visited nodes
            if (new_row, new_col) in closed_list:
                continue

            # Create neighbor
            neighbor = Node((new_row, new_col), current_node)

            # Calculate costs
            neighbor.g = current_node.g + 1
            neighbor.h = manhattan_distance(neighbor.position, goal)
            neighbor.f = neighbor.g + neighbor.h

            print(
                "Neighbor:",
                neighbor.position,
                "g =", neighbor.g,
                "h =", neighbor.h,
                "f =", neighbor.f
            )

            heapq.heappush(open_list, neighbor)

    print("No path found!")
    return None