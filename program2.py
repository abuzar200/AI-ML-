"""Lab 02: solve the 8-puzzle with an A* state-space search."""

from __future__ import annotations

from heapq import heappop, heappush
from itertools import count

State = tuple[int, ...]
GOAL: State = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def manhattan(state: State) -> int:
    """Lower bound on the number of remaining moves."""
    total = 0
    for index, tile in enumerate(state):
        if tile:
            goal_index = tile - 1
            total += abs(index // 3 - goal_index // 3) + abs(index % 3 - goal_index % 3)
    return total


def neighbors(state: State) -> list[State]:
    blank = state.index(0)
    r, c = divmod(blank, 3)
    options: list[State] = []
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            other = nr * 3 + nc
            nxt = list(state)
            nxt[blank], nxt[other] = nxt[other], nxt[blank]
            options.append(tuple(nxt))
    return options


def is_solvable(state: State) -> bool:
    if len(state) != 9 or set(state) != set(range(9)):
        raise ValueError('A state must contain the numbers 0 through 8 exactly once.')
    tiles = [x for x in state if x]
    inversions = sum(tiles[i] > tiles[j] for i in range(8) for j in range(i + 1, 8))
    return inversions % 2 == 0


def solve(start: State) -> list[State] | None:
    if not is_solvable(start):
        return None
    frontier: list[tuple[int, int, int, State]] = []
    serial = count()
    heappush(frontier, (manhattan(start), 0, next(serial), start))
    best_cost = {start: 0}
    parent: dict[State, State | None] = {start: None}
    while frontier:
        _, cost, _, state = heappop(frontier)
        if cost != best_cost[state]:
            continue
        if state == GOAL:
            path: list[State] = []
            current: State | None = state
            while current is not None:
                path.append(current)
                current = parent[current]
            return list(reversed(path))
        for nxt in neighbors(state):
            nc = cost + 1
            if nc < best_cost.get(nxt, float('inf')):
                best_cost[nxt] = nc
                parent[nxt] = state
                heappush(frontier, (nc + manhattan(nxt), nc, next(serial), nxt))
    return None


def display(state: State) -> str:
    return '\n'.join(' '.join(str(n) if n else '_' for n in state[i:i+3]) for i in (0, 3, 6))


if __name__ == '__main__':
    start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
    path = solve(start)
    if path is None:
        print('The puzzle is not solvable.')
    else:
        print(f'Solved in {len(path) - 1} moves.')
        for step, state in enumerate(path):
            print(f'\nStep {step}\n{display(state)}')
