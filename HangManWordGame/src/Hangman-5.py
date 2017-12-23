
# ASCII helpers
def draw_board(word, missed_letters, player_word):
    draw_hangman(len(missed_letters))

    missed_letters_message = ""
    for letter in missed_letters:
        missed_letters_message += letter + " "
    guess_word_message = "guess_word: " + player_word

    print("Missed Letters: " + missed_letters_message)
    print(guess_word_message)

def draw_hangman(level):#Draw method/Fcn
    if level == 1:#if and elif statement
        print('    +---+')
        print('    |   |')
        print('        |')
        print('        |')
        print('        |')
        print('        |')        
        print('=========')
    elif level == 2:
        print('    +---+')
        print('    |   |')
        print('    o   |')
        print('        |')
        print('        |')
        print('        |')        
        print('=========')
    elif level == 3:
        print('    +---+')
        print('    |   |')
        print('    o   |')
        print('    |   |')
        print('        |')
        print('        |')        
        print('=========')
    elif level == 4:
        print('    +---+')
        print('    |   |')
        print('    o   |')
        print('   /|   |')
        print('        |')
        print('        |')        
        print('=========')
    elif level == 5:
        print('    +---+')
        print('    |   |')
        print('    o   |')
        print('   /|\  |')
        print('        |')
        print('        |')        
        print('=========')
    elif level == 6:
        print('    +---+')
        print('    |   |')
        print('    o   |')
        print('   /|\  |')
        print('   /    |')
        print('        |')        
        print('=========')
    elif level == 7:
        print('    +---+')
        print('    |   |')
        print('    o   |')
        print('   /|\  |')
        print('   / \  |')
        print('        |')        
        print('=========DEAD!')

# Utility Functions

    # Return tuple: (game_over, Winner)
def is_game_over(missed_letters, player_word,guess_word):
    if (len(missed_letters) >= 7):
        return (True, "Player 1")
    elif (player_word == guess_word): 
        return (True, "Player 2")
    else:
        return (False, "")
    
import random
# Begin!        
should_start = True
while (should_start):
    missed_letters = []
    guessed_letters = []
    
    words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
    guess_word = words[random.randint(0, len(words)-1)]
    player_word = "_" * len(guess_word)
    draw_board(guess_word, missed_letters, player_word)
    while (not is_game_over(missed_letters, player_word,guess_word)[0]):
        
        guessed_letter = input("\nGuess a letter: \n")
        while (len(guessed_letter) != 1 or guessed_letters.count(guessed_letter) >= 1 ):
            guessed_letter = input("\nYou've guessed that letter before, try another one: \n")
        guessed_letters.append(guessed_letter)
        if (guess_word.count(guessed_letter) == 0):
            missed_letters.append(guessed_letter)

        for index in range(len(guess_word)):
            secret_letter = guess_word[index]
            if (guessed_letter == secret_letter):
                player_word = player_word[0:index] + guessed_letter + player_word[index+1:]
        draw_board(guess_word, missed_letters, player_word)
    print('Game Over! Winner is....' + is_game_over(missed_letters, player_word,guess_word)[1])
    print("The secret word was:  " + guess_word)
    restart = input("Would you like to play again? (yes/no) \n")
    if (restart != "yes"):
        should_start = False

