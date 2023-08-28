
def play_game_with_ml():
    global hero_health, enemy_health, hero_magic_stock, enemy_magic_stock
    hero_health = 100
    enemy_health = 100
    hero_magic_stock = 2
    enemy_magic_stock = 2
    action_box = reset_action_box()
    shuffle(action_box)
    
    while hero_health > 0 and enemy_health > 0:
        if not action_box:
            action_box = reset_action_box()
            shuffle(action_box)
        
        card_counts = get_card_counts(action_box)

        is_hero_magic = should_use_hero_magic(game_state) and hero_magic_stock > 0
        is_enemy_magic = random() < 0.2 and enemy_magic_stock > 0

        hero_action = action_box.pop()
        enemy_action = action_box.pop()

        execute_action_with_magic(hero_action, "hero", is_hero_magic)
        execute_action_with_magic(enemy_action, "enemy", is_enemy_magic)

        if is_hero_magic:
            hero_magic_stock -= 1
        if is_enemy_magic:
            enemy_magic_stock -= 1
