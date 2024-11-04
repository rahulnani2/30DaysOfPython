import random
from BlackJackCardGame import Deck
from Deck import shufflecards, dealcards

deck1 = Deck()
print(deck1.cards)



shufflecards()
card = dealcards(1)[0]

print(card[1]["value"])

