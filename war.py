# create a list of cards and give them values +
# Ranking: Joker, Ace, King, Queen, Jack, 9, 8, 7, 6, 5, 4, 3, 2 +
# mix the cards in random position +
# deal out all the cards to two players + 
# player one and player two puts one card+
# create a new "face up" pile for both players +
# the player with highest value card takes both cards and puts in a new "face up pile"+
# each player drops one more card, untill list is empty+
##############========================>>>>>>>>>>>>>>>>>>>>>>>> SATURDAY

# - if player list of cards is empty, he collects all cards from "face up" list
# - then shuffles the cards, puts them in a player list and continues playing 

# If both players drop same value cards, then it initiates WAR
#    Both players draw 3 cards face down,
#    then each draws and flips one new card face up 
#    the player with highest ranking card takes all the cards
#    if it's a draw, then war initiates again

# if the player runs out of cards in any instance, then he looses the war



import random

def shuffle_dict(input_dict):
    cards = list(input_dict.keys())
    random.shuffle(cards)
    shuffled_dict = {key: input_dict[key] for key in cards}
    return shuffled_dict

class CardDeck:
    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = {"Joker1" : 15, "Joker2": 15}

    @classmethod
    def create_deck(cls):
        deck = cls()
        for rank in deck.ranks:
            for suit in deck.suits:
                card_name = f"{rank} of {suit}"
                if rank in "Jack":
                    card_value = 11
                elif rank in "Queen":
                    card_value = 12
                elif rank in "King":
                    card_value = 13
                elif rank == 'Ace':
                    card_value = 14
                else:
                    card_value = int(rank)
                deck.cards[card_name] = card_value
        return deck

    #def get_card_deck(self):
     #   card_dict = {card: value for card, value in self.cards.items()}
      #  return card_dict

def main():
    # Create a deck of cards using the class method
    deck = CardDeck.create_deck()

    # Shuffle the deck using the shuffle_dict function
    shuffled_card_dict = shuffle_dict(deck.cards)
    print("This is a shuffled card deck:")
    #print (shuffled_card_dict)
    player1_cards, player2_cards = distribute_cards(shuffled_card_dict)
    print("\nPlayer 1's hidden cards:")
    print(player1_cards)

    print("\nPlayer 2's hidden cards:")
    print(player2_cards)

   

    player1_face_up = {}
    player2_face_up = {}
    
    if not player1_cards:
        print("Player 1's deck is empty.")
    
    while player1_cards and player2_cards:
        card_player1, value_player1 = player1_cards.popitem()
        card_player2, value_player2 = player2_cards.popitem()
        
        if not player1_cards:
            print("Player 1's deck is empty.")
            player1_cards = player1_face_up 
        if not player1_cards:
            print("Player 2's deck is empty ")
            player2_cards = player2_face_up 
        elif value_player1 > value_player2:
            print("Player one wins the round and takes the cards")
            player1_face_up[card_player1] = value_player1
            player1_face_up[card_player2] = value_player2
        elif value_player1 < value_player2:
            print("Player 2 wins the round and takes the cards")
            player2_face_up[card_player1] = value_player1
            player2_face_up[card_player2] = value_player2
        else:
            print("War")

     


def distribute_cards(shuffled_dict):
    player1_cards = {}
    player2_cards = {}

    switch = True

    while shuffled_dict:
        card = list(shuffled_dict.keys())[0]
        if switch:
            player1_cards[card] = shuffled_dict[card]
        else:
            player2_cards[card] = shuffled_dict[card]
        del shuffled_dict[card]
        switch = not switch

    return player1_cards, player2_cards



if __name__ == "__main__":
    main()