def show_inventory(game_state):
    inventory = game_state.get('player_inventory', [])

    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("Ваш инвентарь пуст!")

def get_input(prompt="> "):
    try:
        return input(prompt).strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"