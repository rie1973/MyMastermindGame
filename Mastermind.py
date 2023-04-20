# Ann Smith
# June 25, 2022
#
# Python Program #1
#
# This program is for the game Mastermind, using letters. The player
# has 5 tries to guess the correct randomly generated color code. 
# The game will not count error entries against the 5 tries the player gets. The game
# will exit if the winner guesses correctly on the first try or within their 5 tries. It will also exit
# once all 5 tries with incorrect answers have been used.  


#generate random color code

legal_colors = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']


def generate_color_sequence():
    import random
    random.seed()

    sequence = random.sample(range(len(legal_colors)), 4)
    return [legal_colors[i] for i in sequence]

colors = generate_color_sequence()

### You Code Here

# print(colors) ##block to validate correct output

#welcome statement

print(f"\nPossible colors are {legal_colors}")

print("\nPlease enter your guess with no spaces between colors. Colors cannot be repeated.\n")

#initialize variables

tries = 0  
count = []
guess = ""
play_game = True           

#start game
while play_game:
    
    output_pegs = ""
    tries += 1
    noprint_pegs = False    
    
# validate user input
    validate = True
    while validate:

        color_issue = False
        length_issue = False
        unique_issue = False

        guess = input("\nGuess " + str(tries) + ": ")   #user input
        guess = guess.upper()

        if len(guess) != len(colors):   #too many/not enough letters
            length_issue = True
           
        match = [letter in legal_colors for letter in guess] 
        
        if all(match) == False:
            color_issue = True
        
        if color_issue:
            for i in range (4):
                if guess[i] not in legal_colors:   #not in color range
                    wrong_color = guess[i]
                    print (wrong_color + " is not a valid color. Please try again. ")             
        elif length_issue:
            print ("\nYou must enter 4 letters. Please try again.")

        else:
            for i in guess:
                if guess.count(i) > 1:   #duplicate letter
                    unique_issue = True
            if unique_issue:
                print("Colors can not be repeated. Please try again")
        if color_issue == False and length_issue == False and unique_issue == False:
            validate = False;

      
# places color pegs in proper positions based on user input

    if  output_pegs != "RRRR": 
        for i in range(4):
            if guess[i] == colors[i]:    #pegs for correct color, correct index  
                output_pegs += "R"

            elif guess[i] != colors[i] and guess[i] in colors: #pegs for correct color, wrong index 
                output_pegs += "W"
            
            else:       #not in colors at all
                output_pegs += "_"            


#allows game to print pegs only if all validation criteria is met/will not print out pegs along with error messages

    if noprint_pegs == False:
        print(output_pegs, end='')
    
#compare validated input to random color code
        
    if output_pegs == "RRRR":
        if tries == 1:
            print ("\nYou win =)!")
        else:
            print ("\nYou win =)!")
        play_game = False  #end game if correct on first try

    if tries >= 1 and tries <= 4 and output_pegs != "RRRR":  #continue to compare each guess against random color code
        continue
    
    elif tries >= 5 and output_pegs != "RRRR":
        print ("\nYou lose! =( ")
        play_game = False  #end game after 5 incorrect attempts
               
