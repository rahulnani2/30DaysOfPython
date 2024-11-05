from Deck import Deck
from Card import Card
class Hand:
    def __init__(self, dealer = False):
        self.cards =  []
        self.value =0 
        self.dealer = dealer
    
    def addcard(self, card_list):
        self.cards.extend(card_list)

hand = Hand()
hand.addcard(Deck.dealcards(Deck , 2))
print(hand.cards[0])