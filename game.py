from card import Deck

ranks = [i for i in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
suits = ['DIAMONDS', 'HEARTS', 'SPADES', 'CLUBS']
values = {
    'JACK': 11,
    'QUEEN': 12,
    'KING': 13,
    'ACE': 11,
    'ACE(1)': 1
}


def game():
    deck = Deck(ranks, suits)
    shuffled_deck = deck.get_deck()
    card_pos = 0
    wants_hit = False
    dealer_sum = 0
    player_sum = 0
    is_in = True

    print('Welcome to Blackjack! I wish you the best!')
    while card_pos < 49:
        dealer_hand = [shuffled_deck[card_pos], shuffled_deck[card_pos+1]]
        player_hand = [shuffled_deck[card_pos+2], shuffled_deck[card_pos+3]]
        card_pos += 4

        print(f'Your hand: [{player_hand[0]}, {player_hand[1]}]')
        player_sum = calc_total(player_hand)
        print(f"Dealer's hand: [{dealer_hand[0]}, HIDDEN]")
        dealer_sum = calc_total(dealer_hand)
        print('Hit? (y/n)')
        wants_hit = True if input() == 'y' else False

        while wants_hit and is_in:
            player_hand.append(shuffled_deck[card_pos])
            card_pos += 1

        if input() == 'y':
            player_hand.append(shuffled_deck)
        break  # For testing


def calc_total(hand):
    """
    :param list 'hand': list of Card objects
    """
    # Initial calculation of total
    total = 0
    for card in hand:
        total += values.get(card.rank, card.rank)
    # Check if bust & ACE
    indexes = aces(hand)
    if total > 21 and indexes:
        hand[indexes[0]].rank = 'ACE(1)'
        return calc_total(hand)
    else:
        return total, hand


def aces(hand):
    """
    :param list 'hand': list of Card objects
    """
    indexes = []
    for i, card in enumerate(hand):
        if card.rank == 'ACE':
            indexes.append(i)
    return indexes


# Test calc_total method
deck = Deck(ranks, suits)
shuffled_deck = deck.get_deck()
dealer_hand = [shuffled_deck[0], shuffled_deck[1]]
player_hand = [shuffled_deck[51], shuffled_deck[50]]
total, hand = calc_total(player_hand)
print(total)
print(hand[0].rank)
print(hand[1].rank)


# if __name__ == '__main__':
#     game()
