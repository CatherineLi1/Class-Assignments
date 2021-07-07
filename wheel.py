# Catherine Li

import math
import random

def get_random_puzzle(puzzles):
    '''
    Parameter: puzzles, a list of string
    Return: random puzzle chosen from puzzles
    '''
    #generate a random number to represent the index for puzzles
    random_index = random.randint(1,len(puzzles))
    random_puzzle = puzzles[random_index-1]
    
    return random_puzzle


def count_occurrences_of_letter(puzzle, letter):
    '''
    Parameter: puzzle, letter (both strings)
    Return: number of times the letter occurs in puzzle
    '''
    count = 0
    for i in range(len(puzzle)):
        if letter in puzzle[i]:
            count += 1
    return count


def check_puzzle_compatibility(puzzle, blanks, puzzle2):
    '''
    Parameters: puzzle (string), blanks (list of booleans), puzzle2 (string, phrase to be swapped)
    Return: True if all letters are the same. False otherwis
    '''
    if len(puzzle) != len(puzzle2):
        return False
    
    #check if two puzzles are compatible
    for i in range(len(puzzle)):
        if blanks[i] == True:
            if puzzle[i] != puzzle2[i]:
                return False
            continue
    return True #code reaches this line if the two puzzles are compatible


def get_best_compatible_puzzle(puzzle, blanks, letter, puzzles):
    '''
    Parameters: puzzle (string), blanks (list of booleans)
                letter (string), puzzles (list of strings)
    Return: Hidden phrase in puzzles with fewest occurrences of letter.
            If no phrase is compatible, return None
    '''
    #check if there is another puzzle to switch
    original = puzzle
    for i in range(len(puzzles)):
        if puzzle != puzzles[i]:
            puzzle2 = puzzles[i]
            if check_puzzle_compatibility(puzzle, blanks, puzzle2):
                #puzzle2 is compatible
                occurrence_puzzle = count_occurrences_of_letter(puzzle, letter)
                occurrence_puzzle2 = count_occurrences_of_letter(puzzle2, letter)
                if occurrence_puzzle > occurrence_puzzle2:
                    #make puzzle2 into puzzle and continue searching other options
                    puzzle = puzzle2
    if original != puzzle:
        return puzzle
    return None #this line is reached, so no other puzzles are available


def get_starting_blanks(puzzle):
    '''
    Parameter: puzzle (string), represents the hidden phrase
    Return: list of boolean values, length of puzzle
    All values are False except spaces
    '''
    separated_list = list(puzzle)
    
    #check if character is a space
    for i in range(len(separated_list)):
        if separated_list[i] == ' ':
            separated_list[i] = True
        else:
            separated_list[i] = False
    return separated_list


def blanks_to_string(blanks, puzzle):
    '''
    Parameters: blanks (list of booleans), puzzle (string)
    Return: a string where only spaces and correct letters are shown
    All other characters are shown as _
    '''
    turn_to_string = blanks[:]
    
    #check if elements in blank are True or False and convert to letter or _ accordingly
    for i in range(len(blanks)):
        if blanks[i] == True:
            turn_to_string[i] = puzzle[i]
        else:
            turn_to_string[i] = '_'
    
    #change turn_to_string from a list to a string
    a = ''
    a_string = a.join(turn_to_string)
    return a_string


def update_blanks(blanks, puzzle, letter):
    '''
    Parameters: blanks (list of booleans), puzzle (string), and letter (string)
    Return: None
    Function changes blanks[i] to True if letter occurs. Rest of list is unchanged.
    '''
    #only change blanks[i] if it is the letter
    for i in range(len(blanks)):
        if letter == puzzle[i]:
            blanks[i] = True


def check_if_game_won(blanks):
    '''
    Parameters: blanks (list of booleans)
    Returns: True if hidden phrase is guessed. False otherwise
    '''
    #check that every element in blanks is True
    for i in range(len(blanks)):
        if blanks[i]:
            continue
        else:
            return False
    
    #if this line is reached, user has guessed the hidden phrase
    return True


def play(misfortune):
    '''
    Parameter: a boolean indicating whether or not the special variant should be played.
    This function will let the player play the game.
    '''
    puzzles = [
        "TO BE OR NOT TO BE",
        "TO ME NO CAT IS IN",
        "WALKING ON SUNSHINE",
        "TALKING ON IMESSAGE",
        "BE READY AT NOON",
        "HE READS AT CAMP",
        "NO SHADE ON MOON",
        "PIECE OF CAKE",
        "MONEY TO BURN",
        "TIME IS MONEY",
        "EASY AS HONEY",
        "ALL BARK AND NO BITE",
        "HER LOVE AND AN OMEN",
        "HAPPY AS A CLAM",
        "SAPPY AS A TREE",
        "HOLD YOUR HORSES",
        "STOP YOUR PONIES",
        "COOL BEAN",
        "TOOL HELP",
        "POLL TIME",
        "NICE MIME",
        "ROLL DICE",
        "VERY NEAT"
    ]
    
    num_correct_guesses, num_incorrect_guesses = 0, 0
    
    puzzle = get_random_puzzle(puzzles)
    puzzles.remove(puzzle)
    
    blanks = get_starting_blanks(puzzle)
    print("Here is your phrase:")
    print(blanks_to_string(blanks, puzzle))
        
    winner = False
    while not winner:
        letter = ''
        while not letter.isalpha():
            letter = input("Enter a letter (a - z or A - Z): ")
            letter = letter.upper()
        
        letter_present = count_occurrences_of_letter(puzzle, letter) > 0
        if letter_present and misfortune:
            new_puzzle = get_best_compatible_puzzle(puzzle, blanks, letter, puzzles)
            if new_puzzle not in [None, puzzle]:
                puzzles.remove(new_puzzle)
                puzzle = new_puzzle
                letter_present = count_occurrences_of_letter(puzzle, letter) > 0
                print("Muahaha.")
        
        if letter_present:
            update_blanks(blanks, puzzle, letter)
            num_correct_guesses += 1
        else:
            num_incorrect_guesses += 1
        
        print(blanks_to_string(blanks, puzzle))
        winner = check_if_game_won(blanks)
    
    print("Thanks for playing!")
    print("You had {} correct and {} incorrect guesses.".format(num_correct_guesses, num_incorrect_guesses))
    print("-------------")


def menu():
    '''
    Paramter: no parameters
    Return: none
    Function prints the introductory messages and list the options.
    Menu options will repeat until user decides to exit.
    '''
    #lines below this will repeat until 3) Exit is chosen
    while (True):
        print("Welcome to Wheel of (Mis)Fortune!")
        print("Guess the phrase, one letter at a time.")
        print("What would you like to do?")
        print("1) Play a game of Wheel of Fortune")
        print("2) Play a game of Wheel of Misfortune")
        print("3) Exit")
    
        user_input = input("> ")
        
        #choices depending on user's input
        if user_input == "1":
            misfortune = False #Wheel of Fortune is played
            play(misfortune)
        elif user_input == "2":
            misfortune = True #Wheel of Misfortune is played
            play(misfortune)
        elif user_input == "3":
            print("See ya!")
            break #program ends
        else:
            print("Invalid input.")

    
# Please do not alter anything below this line.
if __name__ == '__main__':
    menu()