import os
from utils import *

# Konstruktor för kortlek
deck = Deck()
Deck.shuffle_deck(deck)

# Konstruktor för händer
player_hand = Hand("Player hand")
house_hand = Hand("House hand")

player_value = 0
house_value = 0
win_counter = 0
loss_counter = 0
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
print("- Start | Start the game")
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
    print(f"WINS: {win_counter} LOSSES: {loss_counter}")
    print("- D    | Draw a card")
    print("- S    | Stay")
    print("- Exit | Exit game")
    print("-")
    
    # Skriver ut spelarens hand
    print("Player's Hand:")
    for card in player_hand:
        print(card)
    if player_value > 0:
        print(f"Player value: {player_value}")
    
    print("-")
    choice = input("> ").lower()

    if choice == "d":
        print(f"You drew {deck[0]}")
        player_hand.draw(deck)
        player_value = player_hand.hand_value()
        if player_value > 21:
            loss_counter += 1
            print("Bust! You lose.")
            print("Press any key to play again!")
            print("Type 'Exit' to exit program")
            go_again = input("> ").lower()
            if go_again == "exit":
                print("Exiting program...")
                break
            else:
                # Flyttar kort från händer till kortlek
                for card in player_hand:
                    deck.append(card)
                player_hand.clear()
                for card in house_hand:
                    deck.append(card)
                house_hand.clear()
                deck.shuffle_deck()
                player_value = player_hand.hand_value()
                house_value = house_hand.hand_value()
        elif player_value < 21:
            input("Press enter to continue your turn..")
        

    elif choice == "s":
        while house_value < 16:
            print(f"The house drew {deck[0]}")
            house_hand.draw(deck)
            house_value = house_hand.hand_value()
        
        # Skriver ut husets hand
        print("House's hand:")
        for card in house_hand:
            print(card)
        if house_value > 0:
            print(f"House value: {house_value}")
            
        if house_value > 21:
            win_counter += 1
            print("House busts! Congratulations, you win!")
        elif house_value >= player_value:
            loss_counter += 1
            print("The house wins!")
        elif player_value > house_value:
            win_counter += 1
            print("Congratulations! You win!")

        print("Press any key to play again!")
        print("Type 'Exit' to exit program")
        go_again = input("> ").lower()
        if go_again == "exit":
            print("Exiting program...")
            break
        else:
            # Flyttar kort från händer till kortlek
            for card in player_hand:
                deck.append(card)
            player_hand.clear()
            for card in house_hand:
                deck.append(card)
            house_hand.clear()
            deck.shuffle_deck()
            player_value = player_hand.hand_value()
            house_value = house_hand.hand_value()

    elif choice == "exit":
        print("Exiting program...")
        break
    else:
        input("Invalid command. Please refer to menu for valid commands...")
'''
elif cmd == "exit":
    break
else:
    input("Invalid command. Please refer to menu for valid commands...")
'''
