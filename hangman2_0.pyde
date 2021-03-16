"""
This program implements the Hangman game.  Hangman is played by displaying a 'secret' word to the
player showing only the number of letters in the word.   The user guesses letters.  If the letter is
in the word, it is shown in it's correct location(s).  If the letter is not in the word, the user comes
one step closer to being hanged (indicated by a picture). 
Written By:  Wendy Powley
Date:  December, 2019
Modified by: Xinyu (Renee) Chen
"""

#GLOBAL VARIABLES
#These are visible to all functions
secretWord = ""
blank = ""
numWrongGuesses = 0
chosenLetters = [] #keeps track of all letters chosen by the user


def setup():
    """
    This function sets up the game - -drawing the initial picture, picking the secret word
    and displaying it on the screen.
    Parameters:  None
    Returns:  None
    """
    #secretWord and blank need to be global variables.  Since we change them here
    #we need to specify that they are globals.  This requirement is so that you do
    #not make changes to global variables without being aware that they are globals.  
    global secretWord, blank
    
    size(500, 500)
    background(0)
    stroke(255)
    drawGallows()
    
    #we'll define a list of potential words for the game - feel free to change them
    aListofWords = ["cat", "dog", "horse", "humster", "snake"]
    
    #choose the secret word.
    secretWord = chooseSecretWord(aListofWords)
    print secretWord
    
    #make a "blank" representation of the secret word and display it.
    blank = convertWordToBlanks(secretWord)
    displayWord(blank)

def displayWord(word):
    """
    This function displays a word on the screen.
    Parameters:  a string
    Returns:  None
    """
    textSize(40)
    text(word, 100, 350)
    

def drawGallows():
    """
    This function draws the gallows for the hangman game.
    Parameters:  None
    Returns:  None
    """
    #bottom
    line(100, 250, 300, 250)
    #perpendicular
    line(140, 250, 140, 30)
    #top
    line(140, 30, 230, 30)
    #small part
    line(230, 30, 230, 45)

def drawPerson(numWrongGuesses):
    """
    This function draws the person hanging from the gallows.
    Parameters: None
    Returns:  None
    """
    if numWrongGuesses == 1:
        #draw head
        ellipse(230, 60, 30, 30)
    elif numWrongGuesses == 2:
        #draw body
        line(230, 75, 230, 125)
    elif numWrongGuesses == 3:
        #draw arms
        line(200, 100, 260, 100)
    elif numWrongGuesses == 4: 
        #draw left leg
        line(230, 125, 220, 175)
    elif numWrongGuesses == 5:
        #draw right leg
        line(230, 125, 240, 175) 
        
def convertWordToBlanks(word):
    """
    This function takes a word and turns that word into a series of underscores each representing
    a letter of the word.
    Eg.  "snow" -->  "____"
    Parameters:  word - a string
    Return:  string (containing only underscores)
    """
    blank = ""
    for letter in word:
        blank = blank + "_"
    return blank
 
def chooseSecretWord(aListofWords):
    """ 
    This function chooses one word from a list of words at random and returns it.
    Parameters:  a list of strings
    Returns:  a string
    """
    pos = int(random(len(aListofWords)))
    return aListofWords[pos]

def updateRepresentation(secretWord, blank, guess):
    """
    This function 'inserts' guess into the blank word.
    Eg.  guess = 't', secretWord = "winter", blank = "__n__r" --> returns "__nt_r"
    Paramters:  secretWord, blank are strings, guess is a string, but a single letter.
    Returns:  a string
    """
    newBlank = ""
    for i in range(len(secretWord)):
        if secretWord[i] == guess:
            #insert the guessed letter into the new string
            newBlank = newBlank + guess
        else:
            #use the letter at blank[i]
            newBlank = newBlank + blank[i]
    return newBlank

def keyPressed():
    #this is what happens when I press a key
    #check to see if key is in the alphabet. 
    
    #show chosen letters
    global numWrongGuesses
    global blank
    global chosenLetters
        
        
    if key.isalpha():
        if key in secretWord:
            background(0)
            drawGallows()
            drawPerson(numWrongGuesses)
            chosenLetters.append(str(key))
            t = 5
            for i in range(len(chosenLetters)):
                textSize(20)
                text(chosenLetters[i], t, 400)
                t += 15
            blank = updateRepresentation(secretWord, blank, key)
            displayWord(blank)
            
            if blank == secretWord:
                numWrongGuesses = 0
                chosenLetters = []
                fill(255, 0, 0)
                text("YOU WIN", 200, 450)
                textSize(10)
                fill(255)
                text("to restart the game press space", 10, 480)
        
        else:
            numWrongGuesses += 1
            drawPerson(numWrongGuesses)
            chosenLetters.append(str(key))
            t = 5
            for i in range(len(chosenLetters)):
                textSize(20)
                text(chosenLetters[i], t, 400)
                t += 15
            if numWrongGuesses == 5:
                numWrongGuesses = 0
                chosenLetters = []
                setup()
                
    elif key == " ":
        numWrongGuesses = 0
        chosenLetters = []
        setup()
    
    else:
        background(0)
        drawGallows()
        drawPerson(numWrongGuesses)
        text("please choose a letter", 20, 420)
        

    
def draw():
    pass
