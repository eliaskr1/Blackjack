import random, os
# Klass för kort
class Card():
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
# Klass för kortlek
class Deck(list):
    def __init__(self):
        # Gör att objekt från denna klass automatiskt skapar en kortlek.
        super().__init__(self.construct_deck())
        self.name = "Deck"
    
    def construct_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        return [Card(suit, rank, value) for suit in suits for rank, value in zip(ranks, values)]
        
    def shuffle_deck(self):
        random.shuffle(self)

# Klass för hand
class Hand(list):
    def __init__(self, name):
        # Ärver alla metoder och egenskaper från "list" datatypen
        super().__init__()
        self.name = name
    
    def draw(self, deck: list):
        '''
        Drar översta kortet från angiven "deck"
        och ger till instans som anropar metoden
        '''
        self.append(deck.pop(0))
    
    def hand_value(self):
        total_value = 0
        num_aces = 0  # För att hantera ess som kan vara 14 eller 1

        for card in self:
            total_value += card.value
            if card.rank == "Ace":
                num_aces += 1

        # Justera essens värde om det är nödvändigt
        while num_aces > 0 and total_value > 21:
            total_value -= 13
            num_aces -= 1

        return total_value
'''
# Rensa terminal
if os.name == "nt": 
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

# Konstruktor för kortlek
deck = Deck()
Deck.shuffle_deck(deck)

# Konstruktorer för händer
player_hand = Hand("Player hand")
house_hand = Hand("House hand")

# Syntax för att dra kort
player_hand.draw(deck)
house_hand.draw(deck)
'''

