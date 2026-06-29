import random

# List of words
words = ["apple", "banana", "mango", "grapes", "orange"]

# Choose a random word
word = random.choice(words)

guessed = []
tries = 6

print("🎮 Welcome to Hangman!")

while tries > 0:
    display = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if player won
    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess not in word:
        tries -= 1
        print("❌ Wrong guess!")
        print("Remaining tries:", tries)
    else:
        print("✅ Correct!")

if tries == 0:
    print("\n💀 Game Over!")
    print("The word was:", word)