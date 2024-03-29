import random


class Card:
    rank = ''
    suit = ''

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'[{self.rank}, {self.suit}]'


class Deck:
    def __init__(self, ranks, suits):
        global cards
        cards = []
        for i in ranks:
            for j in suits:
                cards.append(Card(i, j))

    def get_deck(self):
        global cards
        random.shuffle(cards)
        return cards
