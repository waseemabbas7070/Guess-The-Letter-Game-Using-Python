import random as rd  # Import the random module for choosing a random word

# List of words for the game
words_list = ["Apple", "Banana", "Mango", "Grapes"]

# Number of lives the player has
lives = 6

# Randomly select a word from the list
chosen_word = rd.choice(words_list).lower()  # Convert to lowercase for consistency
print(chosen_word)  # Debugging: Print the chosen word (Remove this in the final version)

# Create a display list with underscores to represent unguessed letters
display = []
for letter in chosen_word:
    display += '_'  # Each letter is initially hidden as '_'

print(display)  # Display the initial blank word

# Variable to control the game loop
game_over = False

# Game loop: Runs until the player wins or loses
while not game_over:
    # Ask the user to guess a letter
    guessed_letter = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the chosen word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:  # If guessed letter matches a letter in the word
            display[position] = guessed_letter  # Reveal the letter in the display
            print(display)  # Show the updated word with guessed letters

    # If the guessed letter is NOT in the chosen word
    if guessed_letter not in chosen_word:
        lives -= 1  # Reduce a life
        print(f"Wrong guess! You have {lives} lives left.")  # Inform the player
        
        if lives == 0:  # If no lives are left, the player loses
            game_over = True
            print("You lose! The word was:", chosen_word)

    # Check if there are no more '_' left in display (meaning all letters are guessed)
    if '_' not in display:
        game_over = True
        print("Congrats!! You Won the game 🎉")
