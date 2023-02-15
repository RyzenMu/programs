import random
import time

# Initial Steps to invite in the game:

print("\nWelcome to Hangman game by DataFlair\n")
name = input("Enter your name : ")
print("Hello " + name + "! Best of Luck")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

#the parameters we require to execute the game
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "_" * length
    already_guessed = []
    play_game = ""


def play_loop() :
    global play_game
    play_game = input("Do you want to play again? y = yes, n = no \n")
    
    while play_game not in ["Y", "y", "N", "n"]:
        play_game = input("Do you want to play again? y = yes, n = no \n")

    if play_game == "Y" or play_game == "y":
        main()
    elif play_game == "N" or play_game == "n":
        print("Thanks for playing! We expect you back again!")
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5

    guess = input("This is the Hangman Word:" + display + "Enter Your guess: \n")
    guess = guess.strip()

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index+1:]
        display = display[:index] + guess + display[index + 1 :]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter. \n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("wrong guess" + str(limit-count) + "guess remaining\n")
        elif count == 2:
            time.sleep(1)
            print("wrong guess" + str(limit-count) + "guess remaining\n")
        elif count == 3:
            time.sleep(1)
            print("wrong guess" + str(limit-count) + "guess remaining\n")
        elif count == 4:
            time.sleep(1)
            print("wrong guess" + str(limit-count) + "guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("wrong guess" + str(limit-count) + "guess remaining\n")
            play_loop()

    if word == '-' * length:
        print("Congrats! you have guessed the word correctly")
        play_loop()

    elif count != limit:
        hangman()


main()

hangman()