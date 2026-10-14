"""Lab 09: Tic-Tac-Toe using the minimax decision algorithm."""
from functools import lru_cache
Board = tuple[str, ...]
LINES = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

def winner(board: Board) -> str | None:
    for a,b,c in LINES:
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a]
    return None

@lru_cache(maxsize=None)
def minimax(board: Board, turn: str) -> int:
    """Score the game for X: win=+1, loss=-1, draw=0."""
    won = winner(board)
    if won == 'X':
        return 1
    if won == 'O':
        return -1
    if ' ' not in board:
        return 0
    scores = []
    for i, val in enumerate(board):
        if val == ' ':
            nxt = list(board)
            nxt[i] = turn
            scores.append(minimax(tuple(nxt), 'O' if turn == 'X' else 'X'))
    return max(scores) if turn == 'X' else min(scores)

def best_move(board: Board, turn: str = 'X') -> int | None:
    if winner(board) or ' ' not in board:
        return None
    options = []
    for i, value in enumerate(board):
        if value == ' ':
            nxt = list(board)
            nxt[i] = turn
            score = minimax(tuple(nxt), 'O' if turn == 'X' else 'X')
            options.append((score, i))
    return (max(options, key=lambda item: (item[0], -item[1])) if turn == 'X'
            else min(options, key=lambda item: (item[0], item[1])))[1]

if __name__ == '__main__':
    board: Board = ('X', 'X', ' ', 'O', 'O', ' ', ' ', ' ', ' ')
    print('Board:', board)
    print('Best move for X (index 0 to 8):', best_move(board, 'X'))
