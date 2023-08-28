
def get_card_counts(box):
    card_count = {
        "good_hit": 0,
        "normal_hit": 0,
        "low_hit": 0,
        "do_nothing": 0,
        "self_hurt": 0,
        "both_hurt": 0
    }
    for card in box:
        card_count[card] += 1
    return card_count
