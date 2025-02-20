# Basic actions
def decide_action(hand_strength, pot_odds):
    if hand_strength <= 1000:
        return "strong"
    elif hand_strength <= 2500:
        return "mid"
    elif hand_strength <= 5000:
        return "weak"
    else:
        return "unplayable"