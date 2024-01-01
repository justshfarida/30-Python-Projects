from random import choice
def run_game():
    word : str = choice(['apple','banana','secret'])
    username: str = input('What is your name? >> ')
    print(f"Welcome to the hangman {username}!")

    guessed: str=''
    tries: int=3
    while tries>0:
        blanks: int = 0
        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks+=1
        print()
        # If there are no blanks left, that means the user won the game!
        if blanks == 0:
            print('You got it!')
            break

        # Get user input
        guess: str = input('Enter a letter: ')
        
        if len(guess)==1:
            pass
        else:
            print('Enter 1 letter or full word')
            continue

        # Check that the user isn't just guessing the same letter again
        if guess in guessed:
            print(f'You already used: "{guess}". Please try with another letter!')
            continue

        # Add the guess to the guessed string
        guessed += guess

        # Check that the guess is in the word
        if guess not in word:
            tries -= 1
            print(f'Sorry, that was wrong... ({tries} tries remaining)')

            # Game-over if tries reaches 0
            if tries == 0:
                print('No more tries remaining... You lose.')
                break


if __name__ == '__main__':
    run_game() 
