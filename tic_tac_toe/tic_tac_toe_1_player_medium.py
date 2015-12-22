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
            horiz_ref, vert_ref = self.win_or_block()
        
        return horiz_ref, vert_ref 
    
    def win_or_block(self):
        
        symbol = self.current_symbol
        horiz_ref, vert_ref = self.pick_symbol_position(symbol)
        
        if horiz_ref == 3:
            if symbol == "X":
                symbol = "O"
            else:
                symbol = "X"
            horiz_ref, vert_ref = self.pick_symbol_position(symbol)
                  
        if horiz_ref == 3:
            horiz_ref = int(np.random.random()*3)
            vert_ref = int(np.random.random()*3)
        
        return horiz_ref, vert_ref
    
    def pick_symbol_position(self, symbol):
        
        for horiz_ref, row in enumerate(self.grid):
            if self.check_row_two_blank(row, symbol):
                vert_ref = np.where(row == "_")[0][0]
                return horiz_ref, vert_ref
        
        for vert_ref, column in enumerate(np.transpose(self.grid)):
            if self.check_row_two_blank(column, symbol):
                horiz_ref = np.where(column == "_")[0][0]
                return horiz_ref, vert_ref
            
        if self.check_row_two_blank(np.diag(self.grid), symbol):
            horiz_ref = np.where(np.diag(self.grid) == "_")[0][0]
            vert_ref = horiz_ref
            return horiz_ref, vert_ref
        
        if self.check_row_two_blank(np.diag(np.fliplr(self.grid)), symbol):
            horiz_ref = np.where(np.diag(np.fliplr(self.grid)) == "_")[0][0]
            vert_ref = 2 - horiz_ref
            return horiz_ref, vert_ref
        
        return 3, 3
        
        
    
    def check_row_two_blank(self, row, symbol):
        
        one_blank = np.array([["_", symbol, symbol],
                              [symbol, "_", symbol],
                              [symbol, symbol, "_"]])
        
        for control in one_blank:
            truth_value = True
            for i, elem in enumerate(row):
                truth_value *= (elem==control[i])
            if truth_value:
                return True
        
        return False
            
        
if __name__ == "__main__":
    
    tic_tac_toe = TicTacToe1Player()
    
    tic_tac_toe.play_game()