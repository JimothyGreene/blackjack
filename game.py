from card import Deck

ranks = [i for i in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
suits = ['DIAMONDS', 'HEARTS', 'SPADES', 'CLUBS']

deck = Deck(ranks, suits)
shuffled_deck = deck.get_deck
print(shuffled_deck)
