# Nicholas Branson
# CIS256 26671 (Spring 2026)
# Exercise Assignment 4

#Import HangmanGame Class from file
from guess_the_word import HangmanGame

# Test to make sure game resets and guessed letters are cleared
def test_reset_game():
    game = HangmanGame(["Apple", "Banana"], "TestUser") 
    game.guessed_letters.append("A")
    game.reset_game()
    assert game.guessed_letters == []
# Test to make sure when letter is guessed it is removed from available letters
def test_make_guess():
    game = HangmanGame(["Apple", "Banana"], "TestUser")
    game.word = "APPLE"
    game.guess("A")
    assert set(game.guessed_letters) == {"A"}
    assert "A" not in game.available_letters
    
# Test to make sure last word is not picked again
def test_pick_word():

    game = HangmanGame(["APPLE", "BANANA"], "TestUser")
    game.last_word = "APPLE" 
    game.pick_word()
    assert game.word == list("BANANA") 
    assert game.last_word == "BANANA"
    assert game.last_word != "APPLE"  
