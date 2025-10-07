from games import *
from collections import namedtuple


GameState = namedtuple('GameState', 'to_move, utility, board, moves')


class GameOfNim(Game):
    def __init__(self, board):
        actions = []
        for i in range(len(board)):
            for j in range(board[i] + 1):
                if (j == 0):
                    continue
                actions.append((i, j))

        self.initial = GameState(
            to_move="Max", utility=0, board=board, moves=actions)

    def result(self, state, move):
        board = state.board
        board[move[0]] -= move[1]

        actions = []
        for i in range(len(board)):
            for j in range(board[i] + 1):
                if (j == 0):
                    continue
                    actions.append((i, j))

        return GameState(
            to_move=self.to_move(state),
            utility=self.utility(state),
            board=board,
            moves=actions)

    def actions(self, state):
        return state.moves

    def terminal_test(self, state) -> bool:
        return all(row == 0 for row in state.board)

    def utility(self, state, player="Max"):
        if (self.terminal_test(state) is True):
            if (state.to_move == "Max"):
                return 1
            else:
                return -1
        return 0

    def to_move(self, state):
        if (state.to_move == "Max"):
            return "Min"
        return "Max"

    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == '__main__':
    # nim = GameOfNim([7, 5, 3, 1])
    nim = GameOfNim([0, 5, 3, 1])
    print(nim.initial.board)  # must be [0, 5, 3, 1]

    # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2,1), (2, 2), (2, 3), (3, 1)]
    print(nim.initial.moves)
    # nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.result(nim.initial, (1, 3)))

    # computer moves first
    utility = nim.play_game(alpha_beta_player, query_player)

    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
