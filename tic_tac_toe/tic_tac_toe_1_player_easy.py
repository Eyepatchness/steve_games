import numpy as np

from tic_tac_toe import TicTacToeGame

class TicTacToe1Player(TicTacToeGame):
    
    def __init__(self):
        
        super(TicTacToe1Player, self).__init__()
        self.pick_first_player()
        
    def pick_first_player(self):
        
        picked = False
        
        while not picked:
            print("Would you like to go first? (yes or no)")
            first_player = input()
            if first_player == "yes":
                self.players = ["Human", "Computer"]
                picked = True
            elif first_player == "no":
                self.players = ["Computer", "Human"]
                picked = True
            else:
                print("Invalid input")
        
    def get_move(self, player):
        
        print("{0}, enter move:".format(player))
        if player == "Human":
            horiz_ref = int(input())
            vert_ref = int(input())
        if player == "Computer":
            horiz_ref = int(np.random.random()*3)
            vert_ref = int(np.random.random()*3)
        
        return horiz_ref, vert_ref
            
        
if __name__ == "__main__":
    
    tic_tac_toe = TicTacToe1Player()
    
    tic_tac_toe.play_game()