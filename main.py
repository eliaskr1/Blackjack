import os
from utils import *

# Konstruktor för kortlek
deck = Deck()
Deck.shuffle_deck(deck)

# Konstruktor för händer
player_hand = Hand("Player hand")
house_hand = Hand("House hand")
'''
if os.name == "nt": # Rensa terminal
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

print("*")
print("TWENTYONE")
print("Version 1.0.0")
print("-")
print("- The point of this card game is")
print("- to get as close to 21 as possible.")
print("- If you go OVER you lose. If you")
print("- go LOWER than the house you lose.")
print("-")
print("- Start | Draw a card")
print("- Exit  | Exit game")
print("-")
cmd = input("> ").lower()
if cmd == "start":
'''
while True:
    if os.name == "nt": # Rensa terminal
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    print("*")
    print("TWENTYONE")
    print("Version 1.0.0")
    print("-")
    print("- D    | Draw a card")
    print("- S    | Stay")
    print("- exit | Exit game")
    print("-")
    
    # Skriver ut spelarens hand
    print("Player's Hand:")
    for card in player_hand:
        print(card)
    player_value = player_hand.hand_value()
    if player_value > 0:
        print(player_value)
        
    # Skriver ut husets hand
    print("House's hand:")
    for card in house_hand:
        print(card)
    house_value = house_hand.hand_value()
    if house_value > 0:
        print(house_value)
    
    choice = input("> ").lower()

    if choice == "d":
        print(deck[0])
        player_hand.draw(deck)
        input("enter")
    elif choice == "s":
        print(deck[0])