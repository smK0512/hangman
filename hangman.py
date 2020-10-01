import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Hey,lets start the game!!!")
    print(word_completion)
    print(display_hangman(tries))
    while not guessed and tries > 0:
        guess = input("Please guess a letter:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed the letter ",guess)
                print(display_hangman(tries))
            elif guess not in word:
                print(guess, "is not in the word!!")
                tries -= 1
                print("You have this many tries left:",tries)
                print(display_hangman(tries))
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is present in the word!")
                print(display_hangman(tries))
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
            print(word_completion)
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Sorry you have already guessed the word!try again! ",guess)
                print(display_hangman(tries))
            elif guess != word:
                print("sorry" ,guess, "is not the word")
                tries -= 1
                print("You have this many tries left:",tries)
                print(display_hangman(tries))
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else :
            print("please enter a alphabet or the whole word we do not accept substrings!!")
    if guessed:
            print('''Congrats, you have guessed the word!!
            Yeah you winnnnn!!!!''')
    else:
            print('''Sorry you ran out of tries!!
                      The word was:''',word)


def display_hangman(tries):
    stages = [
        """_____________
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            |
        """,

        """
         _____________
         |      |
         |      O
         |     \\|/
         |      |
         |     / 
         |
         """,

        """
         _____________
         |      |
         |      O
         |     \\|/
         |      |
         |      
         |
         """,

        """
         _____________
         |      |
         |      O
         |     \\|
         |      |
         |     
         |
         """,

        """
         _____________
         |      |
         |      O
         |      |
         |      |
         |    
         |
         """,

        """
         _____________
         |      |
         |      O
         |     
         |      
         |     
         |
         """,

        """
         _____________
         |      
         |      
         |     
         |      
         |     
         |
         """
    ]
    print(stages[tries])


def main():
    word = get_word()
    play(word)
    again = input("Do ypu want to play again(Y/N:)").upper()
    while again == 'Y':
        play(word)


main()