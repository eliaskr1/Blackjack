import os
from utils import *

# Konstruktor för kortlek
deck = Deck()
Deck.shuffle_deck(deck)

# Konstruktor för händer
player_hand = Hand("Player hand")
house_hand = Hand("House hand")

# Variabler
ui_width = 40
player_value = 0
house_value = 0
win_counter = 0
loss_counter = 0
while True:
    if os.name == "nt": # Rensa terminal
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    # Intro UI
    print("|" + "*" * ui_width + "|")
    print("|" + "TWENTYONE".center(ui_width) + "|")
    print("|" + "Version 1.2.3".center(ui_width) + "|")
    print("|" + "-" * ui_width + "|")
    print("| The point of this card game is         |")
    print("| to get as close to 21 as possible.     |")
    print("| If you go OVER you lose. If you        |")
    print("| go LOWER than the house you lose.      |")
    print("|" + "-" * ui_width + "|")
    print("| Start | Start the game                 |")
    print("| Exit  | Exit game                      |")
    print("|" + "-" * ui_width + "|")
    cmd = input("> ").lower()

    # Starta spelet
    if cmd == "start":
        while True:
            if os.name == "nt": # Rensa terminal
                os.system("cls")
            elif os.name == "posix":
                os.system("clear")

            # Ingame UI
            print("|" + "*" * ui_width + "|")
            print("|" + "TWENTYONE".center(ui_width) + "|")
            print("|" + "Version 1.2.3".center(ui_width) + "|")
            print("|" + "-" * ui_width + "|")
            print("| WINS:", win_counter, "| LOSSES:", loss_counter, "|".rjust(20))
            print("|" + "-" * ui_width + "|")
            print("| D    | Draw a card" + "|".rjust(22))
            print("| S    | Stay" + "|".rjust(29))
            print("| Menu | Return to main menu" + "|".rjust(14))
            print("|" + "-" * ui_width + "|")
            
            # Skriver ut spelarens hand
            print("- Player's Hand:")
            for card in player_hand:
                print("-", card)
            if player_value > 0:
                print(f"- Player value: {player_value}")
            
            print("-" * ui_width)
            choice = input("> ").lower()

            # Logik och UI för "Draw" alternativet
            if choice == "d":

                # Skriver ut vilket kort som drogs och räknar ut värdet på spelarens hand
                print("-" * ui_width)
                print(f"You drew {deck[0]}")
                print("-" * ui_width)
                player_hand.draw(deck)
                player_value = player_hand.hand_value()

                # Logik om spelaren drar för högt
                if player_value > 21:
                    loss_counter += 1
                    print(f"Bust! {player_value} is over 21. You lose.")
                    print("Press any key to play again!")
                    print("Type 'Menu' to return to main menu")

                    # Spelaren får välja om man vill spela igen eller stänga av
                    go_again = input("> ").lower()
                    if go_again == "menu":
                        print("Exiting game...")
                        break

                    # Resettar spelet
                    else:
                        # Flyttar kort från händer till kortlek
                        for card in player_hand:
                            deck.append(card)
                        player_hand.clear()
                        for card in house_hand:
                            deck.append(card)
                        house_hand.clear()

                        # Blandar kortlek
                        deck.shuffle_deck()

                        # Återställer värdet av händer efter händer är tomma
                        player_value = player_hand.hand_value()
                        house_value = house_hand.hand_value()
                elif player_value < 21:
                    input("Press enter to continue your turn..")
                
            # Logik och UI för "Stay" alternativet
            elif choice == "s":

                # Datorns logik för om den ska stanna eller ta ett till kort
                while house_value < 16:
                    house_hand.draw(deck)
                    house_value = house_hand.hand_value()
                
                # Skriver ut husets hand
                print("- House's hand:")
                for card in house_hand:
                    print("-", card)
                if house_value > 0:
                    print(f"- House value: {house_value}")
                print("-" * ui_width)

                # Logik för om huset eller spelaren vann efter spelaren valt att stanna
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
                print("Type 'Menu' to return to main menu")
                go_again = input("> ").lower()
                if go_again == "menu":
                    print("Exiting game...")
                    break
                else:

                    # Samma logik som när spelaren drar över 21
                    for card in player_hand:
                        deck.append(card)
                    player_hand.clear()
                    for card in house_hand:
                        deck.append(card)
                    house_hand.clear()
                    deck.shuffle_deck()
                    player_value = player_hand.hand_value()
                    house_value = house_hand.hand_value()

            elif choice == "menu":
                print("Exiting game...")
                break
            else:
                input("Invalid command. Please refer to menu for valid commands...")

    elif cmd == "exit":
        print("Exiting program...")
        break
    else:
        input("Invalid command. Please refer to menu for valid commands...")

