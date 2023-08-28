
def execute_action_with_magic(action, character, use_magic):
    global hero_health, enemy_health
    damage_multiplier = 2 if use_magic else 1

    if action == 'good_hit':
        damage = 10 * damage_multiplier
    elif action == 'normal_hit':
        damage = 8 * damage_multiplier
    elif action == 'low_hit':
        damage = 5 * damage_multiplier
    elif action == 'do_nothing':
        damage = 0
    elif action == 'self_hurt':
        damage = -10 * damage_multiplier
    elif action == 'both_hurt':
        damage = 5 * damage_multiplier

    if character == 'hero':
        enemy_health -= damage
        if action == 'self_hurt':
            hero_health += damage
        elif action == 'both_hurt':
            hero_health -= damage // 2
    else:
        hero_health -= damage
        if action == 'self_hurt':
            enemy_health += damage
        elif action == 'both_hurt':
            enemy_health -= damage // 2
