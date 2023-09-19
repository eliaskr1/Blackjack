
import random, os
import utils as u
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

while True:
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
    print("-"*ui_width)
    print("- D    | Draw a card")
    print("- S    | Stay")
    print("- exit | Exit game")
    print("-"*ui_width)

    print("Player's hand:")
    for card in player_hand:
        print(card)
    player_value = hand_value(player_hand)
    print("Player value:", player_value)
    print("-"*ui_width)

    print("House's hand:")
    for card in house_hand:
        print(card)
    house_value = hand_value(house_hand)
    print("House value:", house_value)
    print("-"*ui_width)
    u_input = input("> ")
    
    if u_input == "d":
        player_draw()
        player_value = hand_value(player_hand)
        if player_value > 21:
            print("Player busts! You lose.")
            break
        
    elif u_input == "s":
        while house_value < player_value and house_value <= 21:
            house_draw()
            house_value = hand_value(house_hand)
        if house_value > 21:
            print("House busts! You win.")
            input("Press 'Enter' to continue")
        elif house_value == player_value:
            print("It's a tie!")
            input("Press 'Enter' to continue")
        elif house_value > player_value:
            print("House wins!")
            input("Press 'Enter' to continue")

    elif u_input == "exit":
        print("Exiting game...")
        break

    else:
        print("ERROR. Unknown command")
        input("Press enter to try again...")

        
