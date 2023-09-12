import random
# Klass för kort
class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Skapar min kortlek
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

# Konstruktor för "Card" Klassen
deck = [Card(suit, rank, value) for suit in suits for rank, value in zip(ranks, values)]

# Blandar kortleken
random.shuffle(deck)

for card in deck:
    print(card)


