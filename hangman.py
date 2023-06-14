import random, sys

HANGMAN_PIGS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 0  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 0  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 0  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 0  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 0  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 0  |
/|\ |
/ \ |
    |
====="""]

CATEGORY = 'Animals'
WORDS = '''ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR
           COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT COOSE HAWK
           LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT
           PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK
           SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE
           WOLF WOMBAT ZEBRA'''.split()

def main():
    missedletters = []
    correctletters = []
    secretword = random.choice(WORDS)
    
    while True:
        drawHangman(missedletters, correctletters, secretword)
        
        guess = getPlayerGuess(missedletters + correctletters)
        
        if guess in secretword:
            correctletters.append(guess)
            foundallletters = True
            for secretwordletter in secretword:
                if secretwordletter not in correctletters:
                    foundallletters = False
                    break
            if foundallletters:
                print(f'Yes! The secret word is {secretword}')
                print('You won')
                break
        else:
            missedletters.append(guess)
            if len(missedletters) == len(HANGMAN_PIGS) - 1:
                drawHangman(missedletters, correctletters, secretword)
                print('You have run out of guesses')
                print(f'The word was {secretword}')
                break

def drawHangman(missedletters, correctletters, secretword):
    print(HANGMAN_PIGS[len(missedletters)])
    print(f'The category is {CATEGORY}')
    print()
    
    print('Missed letter: ', end='')
    for letter in missedletters:
        print(letter, end=' ')
    if len(missedletters) == 0:
        print('No missed letters yet. ')
    print()
    
    blanks = ['_'] * len(secretword)
    
    for i in range(len(secretword)):
        if secretword[i] in correctletters:
            blanks[i] = secretword[i]
    
    print(' '.join(blanks))

def getPlayerGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER. ')
        else:
            return guess


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()