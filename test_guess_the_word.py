# Nicholas Branson
# CIS256 26671 (Spring 2026)
# Exercise Assignment 4
#Testsss
import unittest
from guess_the_word import HangmanGame  # Import your class file

class TestHangmanGame(unittest.TestCase):
    
# Setup Test values
    def setUp(self):
        self.words = [
            "Apple", "Orange", "Banana", "Grape",
            "Watermelon", "Pineapple", "Cantalouse", "Strawberry"]
        self.game = HangmanGame(self.words, "TestUser", max_guesses=4)

# Checks the words match preset words
    def test_selected_word_from_list(self):
        for _ in range(10): 
            self.game.reset_game()
            selected_word = "".join(self.game.word)  # Convert list of letters to string
            self.assertIn(selected_word, [w.upper() for w in self.words])

# Checks the guessing process
    def test_guess_processing(self):
        """Check that correct and incorrect guesses are processed correctly."""
        self.game.word = list("APPLE")  # Force known word

        # Correct guess
        result_correct = self.game.guess('P')
        self.assertTrue(result_correct)
        self.assertIn('P', self.game.guessed_letters)
        self.assertEqual(self.game.guess_count, 0)  # No wrong guesses yet

        # Incorrect guess
        result_incorrect = self.game.guess('Z')
        self.assertFalse(result_incorrect)
        self.assertNotIn('Z', self.game.available_letters)  # Letter removed from available letters
        self.assertEqual(self.game.guess_count, 1)

if __name__ == "__main__":
    unittest.main()
