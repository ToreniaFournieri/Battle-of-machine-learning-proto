
def display_action_box(box):
    card_counts = get_card_counts(box)
    return f"Card(G{card_counts['good_hit']},N{card_counts['normal_hit']},L{card_counts['low_hit']},No{card_counts['do_nothing']},S{card_counts['self_hurt']},B{card_counts['both_hurt']})"
