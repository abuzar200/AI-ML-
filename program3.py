"""Lab 03: breadth-first search, the shortest unweighted graph route."""
from collections import deque

def shortest_path(graph: dict[str, list[str]], start: str, goal: str) -> list[str] | None:
    if start == goal:
        return [start]
    queue = deque([start])
    parent: dict[str, str | None] = {start: None}
    while queue:
        current = queue.popleft()
        for nxt in graph.get(current, []):
            if nxt in parent:
                continue
            parent[nxt] = current
            if nxt == goal:
                path = [nxt]
                while parent[path[-1]] is not None:
                    path.append(parent[path[-1]])  # type: ignore[arg-type]
                return path[::-1]
            queue.append(nxt)
    return None

if __name__ == '__main__':
    graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}
    print('BFS shortest route A -> F:', shortest_path(graph, 'A', 'F'))
