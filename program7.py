"""Lab 07: optimal A* grid route using Manhattan distance."""
from heapq import heappop, heappush
from itertools import count
Cell = tuple[int, int]

def heuristic(a: Cell, b: Cell) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(width: int, height: int, start: Cell, goal: Cell, walls: set[Cell]) -> list[Cell] | None:
    if start in walls or goal in walls:
        return None
    tie = count()
    queue = [(heuristic(start, goal), 0, next(tie), start)]
    cost = {start: 0}
    parent: dict[Cell, Cell | None] = {start: None}
    while queue:
        _, g, _, current = heappop(queue)
        if g != cost[current]:
            continue
        if current == goal:
            result: list[Cell] = []
            node: Cell | None = current
            while node is not None:
                result.append(node)
                node = parent[node]
            return result[::-1]
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nxt = (current[0]+dr, current[1]+dc)
            if not (0 <= nxt[0] < height and 0 <= nxt[1] < width) or nxt in walls:
                continue
            ng = g + 1
            if ng < cost.get(nxt, float('inf')):
                cost[nxt], parent[nxt] = ng, current
                heappush(queue, (ng + heuristic(nxt, goal), ng, next(tie), nxt))
    return None

if __name__ == '__main__':
    blocked = {(1, 1), (2, 1), (3, 1)}
    route = a_star(5, 5, (0, 0), (4, 4), blocked)
    print('A* shortest route:', route)
    print('Steps:', len(route)-1 if route else 'unreachable')
