import numpy as np

class TicTacToeGame(object):
    def __init__(self):
        self.players = ["Player 1", "Player 2"]
        self.grid = np.array(['_']*9).reshape(3,3)
        self.number_moves = 0
        self.max_number_moves = 9
        self.gameover = False
    
    def play_game(self):
               
        self.current_player = self.players[0]
        self.current_symbol = "X"
        
        while not self.gameover: 
            print(self.grid)
            self.make_move()
            self.switch_player()
        
        print(self.grid)
        print("Game Over")
 
    def make_move(self):
        
        print("{0}, please make move".format(self.current_player))
        
        invalid_move = True
        while invalid_move:
            try:
                horiz_ref, vert_ref = self.get_move(self.current_player)
                if self.grid[horiz_ref][vert_ref] != '_':
                    print("Invalid move, please try another.")
                else:
                    self.grid[horiz_ref][vert_ref] = self.current_symbol
                    invalid_move = False
            except (ValueError, IndexError, NameError, SyntaxError) as e:
                print(e)
        
        self.number_moves += 1
        win_value = self.check_win(horiz_ref, vert_ref, self.current_symbol)
        
        if win_value:
            print("{0} wins!".format(self.current_player))
            self.gameover = True
        elif self.number_moves == self.max_number_moves:
            print("No winner. Game is tied.")
            self.gameover = True
               
    def get_move(self, player):
        
        print("{0}, enter move:".format(player))
        horiz_ref = int(input())
        vert_ref = int(input())
        
        return horiz_ref, vert_ref
    
    def switch_player(self):
        
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]
        
        if self.current_symbol == "X":
            self.current_symbol = "O"
        else:
            self.current_symbol = "X"
    
    def check_win(self, horiz_ref, vert_ref, symbol):
        
        win_value = False
        if self.check_row(self.grid[horiz_ref], symbol):
            win_value = True
        elif self.check_row(self.grid[:, vert_ref], symbol):
            win_value = True
        elif self.check_row(np.diag(self.grid), symbol):
            win_value = True
        elif self.check_row(np.diag(np.fliplr(self.grid)), symbol):
            win_value = True
        
        return win_value
    
    def check_row(self, row, symbol):
        
        truth_value = True
        for elem in row:
            truth_value *= (elem==symbol)
        
        return truth_value
    
if __name__ == "__main__":
    
    tic_tac_toe = TicTacToeGame()
    
    tic_tac_toe.play_game()
    
    
#     first_number = int(input("Enter first number: "))
#     second_number = int(input("Enter second number: "))
#     
#     product = multiply_two_numbers(first_number, second_number)
#     
#     print("Product is {0}".format(product))