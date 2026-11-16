
class TicTacToe:

    def __init__(self):
        self.board = [""] * 9
        self.current_player = "X"

    def make_move(self, position):

        if self.board[position] == "":
            self.board[position] = self.current_player
            return True

        return False

    def check_winner(self):

        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for combination in winning_combinations:

            a, b, c = combination

            if (self.board[a] != "" and
                self.board[a] == self.board[b] == self.board[c]):

                return self.board[a]

        return None

    def check_draw(self):
        return "" not in self.board

    def switch_player(self):

        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"

    def get_board(self):
        return self.board
