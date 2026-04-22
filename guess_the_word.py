# Nicholas Branson
# CIS256 26671 (Spring 2026)
# Exercise Assignment 4

# Imported Libraries 
import random
import string

# Get word list and sets parameters then calls the game reset function
class HangmanGame:
    def __init__(self, word_list, user_name, max_guesses=4):
        self.word_list = [w.upper() for w in word_list]
        self.user_name = user_name
        self.max_guesses = max_guesses
        self.last_word = ""
        self.reset_game()

    # Clear all variables and set new round then call pick new word function
    def reset_game(self):
        self.guess_count = 0
        self.available_letters = list(string.ascii_uppercase)
        self.guessed_letters = []
        self.pick_word()

    # Pick a random word that is not the same as the last one from word list.
    def pick_word(self):
        possible_words = [w for w in self.word_list if w != self.last_word]
        self.word = list(random.choice(possible_words))
        self.last_word = "".join(self.word)

    # Display word with letters and missing spaces
    def display_word(self):
        display = [letter if letter in self.guessed_letters else "_" for letter in self.word]
        print("Word: " + " ".join(display))
        print(f"Wrong Guesses: {self.guess_count} of {self.max_guesses}")

    # Guess a letter
    def guess(self, letter):
        letter = letter.upper()
        if letter not in self.available_letters or len(letter) != 1:
            return None  # Invalid guess
        self.available_letters.remove(letter)
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        else:
            self.guess_count += 1
            return False

    # Interactive guess method
    def make_guess(self):
        print("Please choose any letter in the alphabet that's still on this list:")
        print(" ".join(self.available_letters))
        user_guess = input("Then press enter: ").upper()
        result = self.guess(user_guess)
        if result is True:
            print(f"Good guess {self.user_name}! '{user_guess}' is in the word.\n")
        elif result is False:
            print(f"Sorry {self.user_name}, '{user_guess}' is not in the word.\n")
        else:
            print("Invalid guess or letter already used.\n")

# Run game loop
    def play(self):
        self.reset_game()
        while self.guess_count < self.max_guesses:
            self.display_word()
            self.make_guess()
            
            # Prompt winner
            if all(letter in self.guessed_letters for letter in self.word):
                print(f"\nCongratulations! {self.user_name.title()} you guessed the word:", "".join(self.word).title())
                return
        print(f"\nGame Over, {self.user_name.title()}! The word was:", "".join(self.word).title())


# Print Header and get user name then greeting
word_list = ["Apple", "Orange", "Banana", "Grape", "Watermelon", "Pineapple", "Cantaloupe", "Strawberry"]
user_name=""

# Main program to start HandmanGame class and gether user name
def main():
    print("--- Welcome to the game of hangman ---")
    user_name = input("Can I get your first name: ")
    print(f"Well it's nice meeting you, {user_name.title()}!\n--- Let's begin ---\nCategory is 'Fruits'")

    game = HangmanGame(word_list, user_name)

        # Loop to keep game going till user types 'N'
    while True:
        game.play()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing! Goodbye")
            break
# Allows when running tests to bypass name input
if __name__ == "__main__":
     main()
