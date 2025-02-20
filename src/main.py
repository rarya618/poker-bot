from utils.card_utils import Deck
from utils.math_utils import evaluate_hand, convert_card
from core.decision_engine import decide_action

def main():
    # Initialize a deck
    deck = Deck()

    # Deal a hand and board
    hand = [deck.deal(), deck.deal()]
    board = [deck.deal() for _ in range(5)]

    # Display the cards
    print(f"Your hand: {hand}")
    print(f"Board: {board}")

    # Evaluate hand strength
    hand_strength = evaluate_hand(
        board=[f"{convert_card(card)}" for card in board],
        hand=[f"{convert_card(card)}" for card in hand]
    )
    print(f"Hand strength: {hand_strength}")

    # Decide action
    action = decide_action(hand_strength, pot_odds=0.5)
    print(f"Bot's evaluation: {action}")

if __name__ == "__main__":
    main()