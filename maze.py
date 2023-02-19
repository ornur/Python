from typing import List, Tuple, Callable


def find_path(maze: List[List[str]]) -> List[Tuple[int, int]]:
    path = []

    def rec(x: int, y: int) -> int:
        print(f"{x} {y}")
        if maze[x][y] == 'E':
            path.append((x, y))
            return 1
        maze[x][y] = '#'
        res = 0
        if x > 0:
            if maze[x - 1][y] != '#':
                if rec(x - 1, y) == 1:
                    path.append((x, y))
                    return 1
        if x < len(maze)-1:
            if maze[x + 1][y] != '#':
                if rec(x + 1, y) == 1:
                    path.append((x, y))
                    return 1
        if y > 0:
            if maze[x][y - 1] != '#':
                if rec(x, y - 1) == 1:
                    path.append((x, y))
                    return 1
        if y < len(maze[0]) - 1:
            if maze[x][y + 1] != '#':
                if rec(x, y + 1) == 1:
                    path.append((x, y))
                    return 1
        return res

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                print(f"{i} {j}")
                rec(i, j)
    path.reverse()
    return path


maze = [
    ['S', '.', '.', '.', '#', 'E'],
    ['#', '.', '#', '.', '.', '.'],
    ['.', '.', '.', '.', '#', '#'],
    ['.', '#', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.']
]
print(find_path(maze))
