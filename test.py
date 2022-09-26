from collections import deque
from queue import PriorityQueue


class State:
    goal: str = ''

    def __init__(self, board: str, moves: int = 0):
        self.board = board
        self.moves = moves

    def __lt__(self, other):
        return self.f() < other.f()

    def f(self):
        return self.g() + self.h()

    def g(self):
        return self.moves

    def h(self):
        """Manhattan"""
        dist = 0
        size = 3
        for i in range(9):
            goal_id = self.goal[i]
            g_x = i // size
            g_y = i - g_x * size
            p_x = self.board.index(goal_id) // size
            p_y = self.board.index(goal_id) - p_x * size
            dist += abs(g_x - p_x) + abs(g_y - p_y)
        return dist


def dfs(start: State, goal: str) -> dict:
    que = PriorityQueue()
    que.put(start)
    marked = {start.board: None}
    while que and (current := que.get()).board != goal:
        for state in expand(current):
            if state.board not in marked:
                marked[state.board] = current.board
                que.put(state)
    return marked


# def exchange(state: State, prev_pos: int, new_pos: int) -> State:
#     new_board = list(state.board)
#     new_board[prev_pos], new_board[new_pos] = new_board[new_pos], new_board[prev_pos]
#     return State(''.join(new_board), state.moves + 1)


# def expand(state: State) -> list:
#     result = []
#     position = state.board.index('0')
#     if position not in (0, 1, 2):
#         result.append(exchange(state, position, position - 3))
#     if position not in (0, 3, 6):
#         result.append(exchange(state, position, position - 1))
#     if position not in (2, 5, 8):
#         result.append(exchange(state, position, position + 1))
#     if position not in (6, 7, 8):
#         result.append(exchange(state, position, position + 3))
#     return result
def exchange(board: str, prev_pos: int, new_pos: int) -> str:
    new_board = list(board)
    new_board[prev_pos], new_board[new_pos] = new_board[new_pos], new_board[prev_pos]
    return ''.join(new_board)


def expand(board: str) -> list:
    result = []
    position = board.index('0')
    if position not in (0, 1, 2):
        result.append(exchange(board, position, position - 3))
    if position not in (0, 3, 6):
        result.append(exchange(board, position, position - 1))
    if position not in (2, 5, 8):
        result.append(exchange(board, position, position + 1))
    if position not in (6, 7, 8):
        result.append(exchange(board, position, position + 3))
    return result


def print_path(start: str, goal: str, marked):
    path = []
    node = goal
    print(marked, node)
    while node != start:
        path.append(node)
        node = marked[node]
    path.append(start)
    for each in path[::-1]:
        pprint(each)


def pprint(board: str):
    print(''.join(board[:3]))
    print(''.join(board[3:6]))
    print(''.join(board[6:]))
    print('--------')


def is_solvable(board: list) -> bool:
    if not board:
        return False
    inversion = 0
    for i in range(len(board) - 1):
        if board[i] == '0':
            continue
        for j in range(i + 1, len(board)):
            if board[j] == '0':
                continue
            if board[i] > board[j]:
                inversion += 1
    return inversion % 2 == 0


def bfs(start: str, goal: str) -> dict:
    que = deque()
    que.append(start)
    marked = {start: None}
    while que and (current := que.popleft()) != goal:
        for state in expand(current):
            if state not in marked:
                marked[state] = current
                que.append(state)
    return marked


if __name__ == '__main__':
    # start = State('283164705')
    # State.goal = '123456780'
    start = '283164705'
    goal = '123456780'
    marked = bfs(start, goal)
    print_path(start, goal, marked)
    print(start)
    # t = [2, 8, 3, 1, 6, 4, 7, 0, 5]
    # print(is_solvable(t))
    # marked = dfs(start, State.goal)
    # print_path(start.board, State.goal, marked)
    # print(start.board)
    # print(len(marked))
