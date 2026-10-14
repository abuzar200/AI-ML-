"""Lab 08: hill climbing, a local-search optimization algorithm."""

def score(x: int) -> int:
    """Concave toy objective with a maximum at x = 3."""
    return 20 - (x - 3) ** 2

def hill_climb(start: int, lower: int = -10, upper: int = 10) -> tuple[int, list[tuple[int, int]]]:
    if not lower <= start <= upper:
        raise ValueError('Start must be within the allowed range.')
    x = start
    history = [(x, score(x))]
    while True:
        neighbors = [n for n in (x-1, x+1) if lower <= n <= upper]
        if not neighbors:
            break
        best = max(neighbors, key=lambda n: (score(n), -abs(n-x)))
        if score(best) <= score(x):
            break
        x = best
        history.append((x, score(x)))
    return x, history

if __name__ == '__main__':
    optimum, history = hill_climb(-3)
    print('Search history:', history)
    print('Best x:', optimum, 'Best score:', score(optimum))
