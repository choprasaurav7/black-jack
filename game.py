from deck import Deck
from hand import Hand


class Game:
    def play(self):
        game_number = 0
        games_to_play = 0
        while games_to_play <=0:
            try:
                games_to_play = int(input("How many games do you want to play"))
                if games_to_play < 0 :
                    raise ValueError
            except ValueError:
                print("You must enter a number greater than 0")

        while game_number < games_to_play:
            game_number += 1
            deck = Deck()
            deck.shuffle()
            player_hand = Hand()
            dealer_hand = Hand(True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
            print()

            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()
            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s","stand"]:
                choice = input("Please choose hit or stand").lower()
                print()
                while choice not in ["h", "s", "stand", "hit"]:
                    choice = input("Please choose hit or stand").lower()
                    print()
                if choice in ['hit', 'h']:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your Hand: ", player_hand_value)
            print("Dealer Hand: ", dealer_hand_value )

            self.check_winner(player_hand,dealer_hand,True)
            print("*" * 30)
            print("\nThanks for playing!!")



    def check_winner(self, player_hand:Hand, dealer_hand:Hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("Dealer Wins!")
                return True
            elif dealer_hand.get_value() >21:
                print("You win!")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("It's a draw")
                return  True
            elif player_hand.is_blackjack():
                print("You win")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer Wins")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Tie")
            else:
                print("Dealer wins")
            return True

        return False
