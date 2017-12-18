
# ASCII helpers
def draw_board(word, missed_letters, player_word):
    board = get_current_board(len(missed_letters))

    missed_letters_message = ""
    for letter in missed_letters:
        missed_letters_message += letter + " "
    secret_word_message = "Secret word: " + player_word

    print(board)
    print("Missed Letters: " + missed_letters_message)
    print(secret_word_message)


def get_current_board(missed_count):
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
def is_game_over(missed_letters, player_word,secret_word):
    if (len(missed_letters) >= 6):
        return (True, "Player 1")
    elif (player_word == secret_word): 
        return (True, "Player 2")
    else:
        return (False, "")
    

# Begin!        
should_start = True
while (should_start):
    missed_letters = []
    guessed_letters = []
    
    secret_word = raw_input("Please enter the secret word: \n\t")
    player_word = "_" * len(secret_word)
    print("\n\n\n")
    

    draw_board(secret_word, missed_letters, player_word)
    while (not is_game_over(missed_letters, player_word,secret_word)[0]):
        
        guessed_letter = raw_input("\nGuess a letter: \n")
        while (len(guessed_letter) != 1 and guessed_letters.count(guessed_letter) >= 1 ):
            guessed_letter = raw_input("\nYou've guessed that letter before, try another one: \n")
        guessed_letters.append(guessed_letter)
        if (secret_word.count(guessed_letter) == 0):
            missed_letters.append(guessed_letter)

        for index in range(len(secret_word)):
            secret_letter = secret_word[index]
            if (guessed_letter == secret_letter):
                player_word = player_word[0:index] + guessed_letter + player_word[index+1:]
        draw_board(secret_word, missed_letters, player_word)
    print('Game Over! Winner is....' + is_game_over(missed_letters, player_word,secret_word)[1])
    print("The secret word was:  " + secret_word)
    restart = raw_input("Would you like to play again? (yes/no) \n")
    if (restart != "yes"):
        should_start = False

