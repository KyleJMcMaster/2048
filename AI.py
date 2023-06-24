from Board import Board
from Input import Input
from typing import List
from itertools import chain
from numpy import ndarray


class MinMaxAI(Input):

    def __init__(self):
        pass


    def getInput(self, board: ndarray) -> int:
        # method returns move to play based on a given board state
        # TODO: optimizations to improve pruning, save already calculated values
        root_state = GameState(board)
        current_depth = 0

        root_state.generate_tree()
        current_children = root_state.children
        while len(current_children) < 50000:
            new_children = []
            # print(len(current_children))
            for child in current_children:
                new_children.append(child.generate_tree())
            current_children = list(chain.from_iterable(new_children))
            current_depth += 1

        # print(current_depth)
        mins = [4000000] * 4
        for child in current_children:
            score = child.get_board_score()
            if score < mins[child.move_made]:
                mins[child.move_made] = score
        # print(mins)
        max_move_score = -1
        max_move = -1
        for i in range(4):
            if mins[i] != 4000000 and mins[i] > max_move_score and max_move_score:
                max_move_score = mins[i]
                max_move = i
        # print(max_move_score)
        # print(max_move)
        return max_move


class MinMaxAI_v2(Input):

    def __init__(self, num_games: int = 20):
        self.num_games = num_games

    def getInput(self, board: ndarray) -> int:
        # method returns move to play based on a given board state
        scores = []
        root_state = GameState(board)

        root_state.generate_tree()
        children = root_state.children

        mins = [4000000] * 4
        for child in children:
            score = child.get_avg_score(self.num_games)
            if score < mins[child.move_made]:
                mins[child.move_made] = score

        #print(mins)
        max_move_score = -1
        max_move = -1
        for i in range(4):
            if mins[i] != 4000000 and mins[i] > max_move_score and max_move_score:
                max_move_score = mins[i]
                max_move = i
        #print(max_move_score)
        #print(max_move)
        return max_move


class GameState:

    def __init__(self, board: ndarray, move_made: int=-1, parent_state=None,first_child:bool=False):
        self.board = Board.get_copy(board)
        self.parent = parent_state
        if first_child or parent_state is None:
            self.move_made = move_made
        else:
            self.move_made = self.parent.move_made

        self.children = []

    def generate_tree(self) -> List:
        # expands game tree by generating all possible game states from this position
        states = []
        legal_moves = Board.get_legal_moves(self.board)
        for move in legal_moves:
            board = Board.get_copy(self.board)
            Board.move(board, move)
            empty_squares = Board.find_empty_squares(board)
            for empty_square in empty_squares:
                b = Board.get_copy(board)
                Board.set_tile_value(b,[empty_square], [2])
                states.append(GameState(b, move,  self, self.parent is None))
                Board.set_tile_value(b,[empty_square], [4])
                states.append(GameState(b, move, self, self.parent is None))
        self.children = states
        return states

    def print_tree(self):
        Board.display(self.board)
        for child in self.children:
            print(child.move_made)
            child.board.display()

    def get_board_score(self) -> int:
        return Board.get_score(self.board)

    def play_random_games(self, num_games) -> List[int]:
        scores = []
        for i in range(num_games):
            board = Board.get_copy(self.board)
            scores.append(Board.play_random_game(board))

        return scores

    def get_avg_score(self, num_games) -> float:
        return sum(self.play_random_games(num_games))/num_games
