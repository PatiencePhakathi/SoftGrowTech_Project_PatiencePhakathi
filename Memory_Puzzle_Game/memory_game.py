import random

# Simple memory game
cards = ['A', 'A', 'B', 'B', 'C', 'C']
random.shuffle(cards)

print("Welcome to the Memory Game!")
print("Cards are shuffled!")

# Show the shuffled cards (for simplicity)
print("Shuffled cards:", cards)

# Ask user to guess a pair
first_guess = input("Pick the index of the first card (0-5): ")
second_guess = input("Pick the index of the second card (0-5): ")

try:
    first = int(first_guess)
    second = int(second_guess)
    if cards[first] == cards[second] and first != second:
        print(f"Congrats! You found a match: {cards[first]}")
    else:
        print(f"No match. Cards were {cards[first]} and {cards[second]}")
except (ValueError, IndexError):
    print("Invalid input. Please enter a number between 0 and 5.")




