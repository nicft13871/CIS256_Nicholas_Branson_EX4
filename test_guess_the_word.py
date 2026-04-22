# Nicholas Branson
# CIS256 26671 (Spring 2026)
# Exercise Assignment 4

from guess_the_word import HangmanGame

def test_reset_game():
    game = HangmanGame(["Apple", "Banana"], "TestUser") 
    game.guessed_letters.append("A")
    game.reset_game()
    assert game.guessed_letters == [""]

