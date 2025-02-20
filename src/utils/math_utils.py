from treys import Card, Evaluator

def convert_card(card):
    """Convert custom Card object to treys format."""
    rank_map = {'10': 'T', 'J': 'J', 'Q': 'Q', 'K': 'K', 'A': 'A'}
    rank = rank_map.get(card.rank, card.rank)  # Convert "10" to "T"
    suit = card.suit[0].lower()  # First letter of suit in lowercase (hearts -> 'h')
    return f"{rank}{suit}"

def evaluate_hand(board, hand):
    evaluator = Evaluator()
    board_cards = [Card.new(card) for card in board]
    hand_cards = [Card.new(card) for card in hand]
    return evaluator.evaluate(board_cards, hand_cards)