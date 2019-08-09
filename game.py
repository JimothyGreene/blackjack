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
    wants_play = True
    win_count = 0

    print('Welcome to Blackjack! I wish you the best!')
    while card_pos < 49 and wants_play:  # For each given deck of cards
        dealer_hand = [shuffled_deck[card_pos], shuffled_deck[card_pos+1]]
        player_hand = [shuffled_deck[card_pos+2], shuffled_deck[card_pos+3]]
        card_pos += 4

        # Print the current hands
        print(f'Your hand: [{player_hand[0]}, {player_hand[1]}]')
        player_sum = calc_total(player_hand)
        print(f"Dealer's hand: [{dealer_hand[0]}, HIDDEN]")
        dealer_sum = calc_total(dealer_hand)

        # Ask for hit
        print('Hit? (y/n)')
        wants_hit = True if input() == 'y' else False

        # While the player wants to be hit
        num_hits = 0
        while wants_hit and is_in:
            card_pos = hit(player_hand, shuffled_deck, card_pos)
            num_hits += 1
            player_sum = calc_total(player_hand)
            is_in = True if player_sum < 22 else False
            if is_in:
                print('Hit? (y/n)')
                wants_hit = True if input() == 'y' else False
            else:
                print('Bust! Better luck next round!')

        if is_in:
            # Dealer's Turn
            print("Dealer's hand: ")
            show_hand(dealer_hand)
            hit(dealer_hand, shuffled_deck, card_pos, num_hits)
            dealer_sum = calc_total(dealer_hand)

            # Compare values
            print(f"Your total: {player_sum}")
            print(f"Dealer's total: {dealer_sum}")
            if player_sum >= dealer_sum:
                win_count += 1
                print(f'You win! You now have {win_count} wins')
            else:
                print(f'Dealer wins! You still have {win_count} wins')

        # Asks if player still wants to play
        print('Would you like to play another round? (y/n)')
        if input() == 'y':
            wants_play = True
            print("That's what we like to hear!")
        else:
            wants_play = False
            print(f"See ya! You finished with {win_count} wins")


def show_hand(hand):
    for card in hand:
        print(card)


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
        return total


def aces(hand):
    """
    :param list 'hand': list of Card objects
    """
    indexes = []
    for i, card in enumerate(hand):
        if card.rank == 'ACE':
            indexes.append(i)
    return indexes


def hit(hand, deck, pos, max_hits=None):
    if max_hits is None:  # For the player hitting
        hand.append(deck[pos])
        print('Your hand: ')
        show_hand(hand)
        pos += 1
        return pos
    else:
        if calc_total(hand) < 17:
            for i in range(0, max_hits):
                hand.append(deck[pos])
                print("Dealer's hand: ")
                show_hand(hand)
                pos += 1
                if calc_total(hand) > 17:
                    break
        return pos


if __name__ == '__main__':
    game()
