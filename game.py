import random


class Game:

    SIZE = 3
    LETTERS = ["A", "B", "C"]
    PLAYER = "O"
    COMPUTER = "X"
    EMPTY = " "
    X = 0
    Y = 1
    LINES = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    PLAYER_LINE = PLAYER + PLAYER + PLAYER
    COMPUTER_LINE = COMPUTER + COMPUTER + COMPUTER

    def __init__(self, input_handler):
        self.board = []
        self.winner = None
        self.turn = self.PLAYER
        self.get_input = input_handler
        for count in range(9):
            self.board.append(self.EMPTY)

    def player_turn(self):
        coordinates = self.__process_move(self.get_input())
        index = self.__get_index(coordinates)
        if index is None:
            return
        if self.board[index] != self.EMPTY:
            print("This space is already taken")
            return
        self.board[index] = self.PLAYER
        self.turn = self.COMPUTER

    def computer_turn(self):
        made_move = False
        while not made_move:
            index = random.randint(0, 8)
            if self.board[index] is self.EMPTY:
                self.board[index] = self.COMPUTER
                made_move = True
        self.turn = self.PLAYER

    def check_for_win(self):

        board_full = True

        for line in self.LINES:
            line_value = ""
            for index in line:
                line_value += self.board[index]
            if line_value == self.PLAYER_LINE:
                self.winner = self.PLAYER
                return True
            if line_value == self.COMPUTER_LINE:
                self.winner = self.COMPUTER
                return True

        for value in self.board:
            if value == " ":
                board_full = False
        if board_full:
            self.winner = "Tie"
            return True

        return False

    def __get_coordinates(self, index):
        x = index % self.SIZE
        y = index / self.SIZE
        return x, y

    def __get_index(self, coordinates):
        if coordinates is None:
            return None
        index = coordinates[self.X] + self.SIZE * coordinates[self.Y]
        return index

    def __process_move(self, move):
        processed_move = None
        try:
            y = int(move[0]) - 1
            x = self.LETTERS.index(move[1])
        except:
            print("Sorry, the move was invalid...")
        else:
            processed_move = (x, y)
        finally:
            return processed_move
