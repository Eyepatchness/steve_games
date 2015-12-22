from tic_tac_toe import TicTacToeGame

class TicTacToe2Player(TicTacToeGame):
    
    def __init__(self):
        
        super(TicTacToe2Player, self).__init__()
        self.players = ["Player 1", "Player 2"]
        
if __name__ == "__main__":
    
    tic_tac_toe = TicTacToe2Player()
    
    tic_tac_toe.play_game()