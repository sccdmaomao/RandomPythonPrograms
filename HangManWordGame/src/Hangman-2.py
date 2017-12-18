class HangmanGame:
    def __init__(self):
        self.should_start = True
        while (self.should_start):
            self.missed_letters = []
            self.guessed_letters = []
            
            self.secret_word = raw_input("Please enter the secret word: \n\t")
            self.player_word = "_" * len(self.secret_word)
            print("\n\n\n")
            self.start_game(self.secret_word)


# Game Logic

    def start_game(self, word): 
        self.draw_board(word)
        while (not self.is_game_over()[0]):
            
            guessed_letter = raw_input("\nGuess a letter: \n")
            while (len(guessed_letter) != 1 and self.guessed_letters.count(guessed_letter) >= 1 ):
                guessed_letter = raw_input("\nYou've guessed that letter before, try another one: \n")
            self.update_game(guessed_letter)
            self.draw_board(word)
        print('Game Over! Winner is....' + self.is_game_over()[1])
        print("The secret word was:  " + self.secret_word)
        self.restart()

    def update_game(self, letter):
        self.guessed_letters.append(letter)
        if (self.secret_word.count(letter) == 0):
            self.missed_letters.append(letter)

        for index in range(len(self.secret_word)):
            secret_letter = self.secret_word[index]
            if (letter == secret_letter):
                self.player_word = self.player_word[0:index] + letter + self.player_word[index+1:]
                
    def restart(self):
        restart = raw_input("Would you like to play again? (yes/no) \n")
        if (restart != "yes"):
            self.should_start = False

# ASCII helpers

    def draw_board(self, word):
        board = self.get_current_board(len(self.missed_letters))

        missed_letters = ""
        for letter in self.missed_letters:
            missed_letters += letter + " "
        secret_word = "Secret word: " + self.player_word

        print(board)
        print("Missed Letters: " + missed_letters)
        print(secret_word)


    def get_current_board(self, missed_count):
        boards = ["""
        H A N G M A N
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        """
        H A N G M A N
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        """
        H A N G M A N
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        """
        H A N G M A N
          +---+
          |   |
         _O   |
          |   |
              |
              |
        =========
        """,
        """
        H A N G M A N
          +---+
          |   |
         _O_  |
          |   |
              |
              |
        =========
        """,
        """
        H A N G M A N
          +---+
          |   |
         _O_  |
          |   |
         /    |
              |
        =========
        """,
        """
        H A N G M A N
          +---+
          |   |
         _O_  |
          |   |
         / \  |
              |
        =========
        """]
        return boards[missed_count]
# Utility Functions

    # Return tuple: (game_over, Winner)
    def is_game_over(self):
        if (len(self.missed_letters) >= 6):
            return (True, "Player 1")
        elif (self.player_word == self.secret_word): 
            return (True, "Player 2")
        else:
            return (False, "")
        

# Begin!        
game = HangmanGame()