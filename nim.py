from games import Game
from tpying import Tuple, List, Boolean
from collections import namedtuple


GameState = namedtuple('GameState', 'to_move, utility, board, moves')


class GameOfNim(Game):
    def __init__(self, board: List[int]):
        super().__init__(board)

        actions = List[Tuple[int, int]]
        for i in range(board.length):
            for j in range(board[i]):
                if (j == 0):
                    continue
                actions.append((i, j))

        self.initial = GameState(
            to_move="Max", utility=0, board=board, moves=actions)

    def result(self, state, move: Tuple[int, int]) -> GameState:
        state.board[move[0]] -= move[1]

        actions = List[Tuple[int, int]]
        for i in range(state.length):
            for j in range(state[i]):
                if (j == 0):
                    continue
                    actions.append((i, j))

        return GameState(
            to_move=self.to_move(),
            utility=state.utility,
            board=state.board,
            moves=actions)

    def actions(self, state: GameState) -> List[Tuple[int, int]]:
        return state.actions

    def terminal_test(state: List[int]) -> Boolean:
        return all(p == 0 for p in state)

    def utility(state: GameState, player):
        if (state.to_move == "Max"):
            return 1
        return -1

    def to_move(state):
        if (state.to_move == "Max"):
            return "Min"
        return "Max"
