# Codesnippets som kommer användas i programmet. Implementering än så länge är oklar

import random, os
# Klass för kort
class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"

#UI
ui_width = 35

# Skapar min kortlek
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Konstruktor för "Card" Klassen
deck = [Card(suit, rank, value) for suit in suits for rank, value in zip(ranks, values)]

# Blandar kortleken
random.shuffle(deck)

# Funktion för att dra ett kort till spelarens hand
# Drar det översta kortet från leken och ger till spelaren
player_hand = []
def player_draw():
    player_hand.append(deck.pop(0))
# Samma som ovan fast för huset
house_hand = []
def house_draw():
    house_hand.append(deck.pop(0))

# Räknar ut värdet i en hand
def hand_value(hand):
    total_value = 0
    num_aces = 0  # För att hantera ess som kan vara 14 eller 1

    for card in hand:
        total_value += card.value
        if card.rank == "Ace":
            num_aces += 1

    # Justera essens värde om det är nödvändigt
    while num_aces > 0 and total_value > 21:
        total_value -= 13
        num_aces -= 1

    return total_value


if os.name == "nt": # Rensa terminal
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

print("*" * ui_width)
print("TWENTYONE".center(ui_width))
print("Version 1.0.0".center(ui_width))
print("-" * ui_width)
print("- The point of this card game is")
print("- to get as close to 21 as possible.")
print("- If you go OVER you lose. If you")
print("- go LOWER than the house you lose.")
print("-" * ui_width)

player_value = hand_value(player_hand)
house_value = hand_value(house_hand)

