class DisplayEngine:

    def __init__(self, game):
        self.game = game

    def render(self):
        b = self.game.board
        formatted_board = f"""
          A   B   C
        1 {b[0]} | {b[1]} | {b[2]}
         -----------
        2 {b[3]} | {b[4]} | {b[5]}
         -----------
        3 {b[6]} | {b[7]} | {b[8]}
        """
        print(f"{'Your turn...' if self.game.turn == 'O' else 'What will the computer do?'}")
        print(formatted_board)
