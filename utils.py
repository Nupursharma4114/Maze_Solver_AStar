def manhattan_distance(current, goal):
    """
    Calculate Manhattan distance between two points.
    """

    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])