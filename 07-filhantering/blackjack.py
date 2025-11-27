import random
import sys

CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11  # Aces handled specially in value calculation
}

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def create_deck():
    return [f"{r}{s}" for s in SUITS for r in RANKS]


def shuffle_deck(deck):
    random.shuffle(deck)


def card_value(card):
    # card like 'A♠' or '10♥' -> rank is all but last char unless 10
    rank = card[:-1]
    return CARD_VALUES[rank]


def hand_value(hand):
    # Sum values, treat A as 11 initially and reduce to 1 as needed
    value = 0
    aces = 0
    for c in hand:
        rank = c[:-1]
        if rank == 'A':
            aces += 1
            value += 11
        else:
            value += CARD_VALUES[rank]
    # Reduce Aces from 11 to 1 as long as over 21
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value


def show_hands(player_hand, dealer_hand, hide_dealer_first=True):
    print("---")
    if hide_dealer_first:
        print(f"Dealer: [?, {dealer_hand[1]}]")
    else:
        print(f"Dealer: {dealer_hand} (värde: {hand_value(dealer_hand)})")
    print(f"Player: {player_hand} (värde: {hand_value(player_hand)})")
    print("---")


def deal_initial(deck):
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]
    return player, dealer


def player_turn(deck, player_hand, dealer_hand):
    while True:
        show_hands(player_hand, dealer_hand, hide_dealer_first=True)
        if hand_value(player_hand) == 21:
            print("Blackjack! (21)")
            break
        if hand_value(player_hand) > 21:
            print("Du gick över 21!")
            break
        action = input("(H)it eller (S)tand? ").strip().lower()
        if action in ('h', 'hit'):
            player_hand.append(deck.pop())
            print("Du drog:", player_hand[-1])
            continue
        elif action in ('s', 'stand', 'st'):
            break
        else:
            print("Skriv 'h' för hit eller 's' för stand.")
    return player_hand


def dealer_turn(deck, dealer_hand):
    # Dealer must hit until 17 or higher. Soft 17 rule: dealer stands on 17 (including soft 17) for simplicity.
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print("Dealer drar:", dealer_hand[-1])
    return dealer_hand


def compare_hands(player_hand, dealer_hand):
    p = hand_value(player_hand)
    d = hand_value(dealer_hand)
    print(f"Slutresultat -- Player: {p}, Dealer: {d}")
    if p > 21:
        return 'dealer'
    if d > 21:
        return 'player'
    if p > d:
        return 'player'
    if d > p:
        return 'dealer'
    return 'push'


def play_round():
    deck = create_deck()
    shuffle_deck(deck)
    player_hand, dealer_hand = deal_initial(deck)

    # Check immediate blackjack
    if hand_value(player_hand) == 21:
        show_hands(player_hand, dealer_hand, hide_dealer_first=False)
        print("Du fick Blackjack! Du vinner! (om inte dealern också har blackjack)")
        if hand_value(dealer_hand) == 21:
            print("Push: båda fick Blackjack")
        return

    player_hand = player_turn(deck, player_hand, dealer_hand)
    if hand_value(player_hand) > 21:
        show_hands(player_hand, dealer_hand, hide_dealer_first=False)
        print("Dealer vinner (spelare över 21)")
        return

    print("\nDealer spelar...")
    dealer_hand = dealer_turn(deck, dealer_hand)
    show_hands(player_hand, dealer_hand, hide_dealer_first=False)
    result = compare_hands(player_hand, dealer_hand)
    if result == 'player':
        print("Spelaren vinner!")
    elif result == 'dealer':
        print("Dealern vinner!")
    else:
        print("Push (oavgjort)")


def main():
    print("=== Enkel Blackjack (textläge) ===")
    while True:
        play_round()
        again = input("Spela igen? (j/n): ").strip().lower()
        if again not in ('j', 'ja', 'y', 'yes'):
            print("Tack för spelet!")
            break


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nAvslutar spelet.")
        sys.exit(0)
