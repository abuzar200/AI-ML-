"""Lab 06: greedy best-first search on a grid of blocked cells."""
from heapq import heappop, heappush
Cell = tuple[int, int]

def heuristic(a: Cell, b: Cell) -> int:
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def search(width: int, height: int, start: Cell, goal: Cell, walls: set[Cell]) -> list[Cell] | None:
    if start in walls or goal in walls:
        return None
    queue = [(heuristic(start, goal), start)]
    parent: dict[Cell, Cell | None] = {start: None}
    while queue:
        _, cell = heappop(queue)
        if cell == goal:
            route: list[Cell] = []
            current: Cell | None = cell
            while current is not None:
                route.append(current)
                current = parent[current]
            return route[::-1]
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nxt = (cell[0] + dr, cell[1] + dc)
            if not (0 <= nxt[0] < height and 0 <= nxt[1] < width):
                continue
            if nxt in parent or nxt in walls:
                continue
            parent[nxt] = cell
            heappush(queue, (heuristic(nxt, goal), nxt))
    return None

if __name__ == '__main__':
    obstacles = {(1, 1), (2, 1), (3, 1)}
    print('Greedy path:', search(5, 5, (0, 0), (4, 4), obstacles))
