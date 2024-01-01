import random
import sys
class RPS():
    def __init__(self):
        print("Welcome to RPS 9000")

        self.moves: dict={'rock':'r','paper':'p','scissors':'✂️'}
        self.valid_moves: list=list(self.moves.keys())
        self.ai_score: int=0
        self.user_score: int=0
    def play_game(self):
        self.user_move: str = input("Enter rock/paper/scissors: ").lower()

        if self.user_move=='exit':
            print("Thanks for playing!")
            sys.exit()
        if self.user_move not in self.valid_moves:
            print("Invalid move...")
            return self.play_game()
        
        
        self.ai_move: str= random.choice(self.valid_moves)
        self.display_game()
        self.check_moves()
    def display_game(self):
        print("---")
        print(f"You played {self.moves[self.user_move]}")
        print(f"AI played {self.moves[self.ai_move]}")
    def check_moves(self):
     
        if self.user_move==self.ai_move:
            print('It is a tie!')
        elif self.user_move=='rock' and self.ai_move=='scissors':
            print('You won!')
            self.user_score+=1
        elif self.user_move=='scissors' and self.ai_move=='paper':
            print('You won!')
            self.user_score+=1
        elif self.user_move=='paper' and self.ai_move=='rock':
            print('You won!')
            self.user_score+=1
        else:
            print("AI won...")
            self.ai_score+=1

        print(f"You have {self.user_score} points.")
        print(f"AI has {self.ai_score} points.")


if __name__=='__main__':
    rps=RPS()
    while True:
        rps.play_game()
