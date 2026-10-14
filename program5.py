"""Lab 05: uniform-cost search using Dijkstra's priority queue."""
from heapq import heappop, heappush

def cheapest_route(graph: dict[str, dict[str, float]], start: str, goal: str) -> tuple[float, list[str]] | None:
    frontier = [(0.0, start, [start])]
    best: dict[str, float] = {start: 0.0}
    while frontier:
        cost, node, path = heappop(frontier)
        if cost > best[node]:
            continue
        if node == goal:
            return cost, path
        for nxt, weight in sorted(graph.get(node, {}).items()):
            if weight < 0:
                raise ValueError('Uniform-cost search requires nonnegative edge costs.')
            next_cost = cost + weight
            if next_cost < best.get(nxt, float('inf')):
                best[nxt] = next_cost
                heappush(frontier, (next_cost, nxt, path + [nxt]))
    return None

if __name__ == '__main__':
    roads = {'A': {'B': 2, 'C': 5}, 'B': {'C': 1, 'D': 4}, 'C': {'D': 1}, 'D': {}}
    print('Cheapest route from A to D:', cheapest_route(roads, 'A', 'D'))
