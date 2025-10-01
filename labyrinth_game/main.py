#!/usr/bin/env python3
from .utils import describe_current_room, solve_puzzle, attempt_open_treasure
from .player_actions import show_inventory, get_input, move_player, take_item, use_item

def main():
    game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов
    }

    print("Добро пожаловать в Лабиринт сокровищ!")  # Приветствие
    
    describe_current_room(game_state)   # Описание стартовой комнаты

    while not game_state["game_over"]:
        command = input("\nВведите команду: ").strip().lower()  # Считываем команду от пользователя
        process_command(game_state, command)


def process_command(game_state, command):
    parts = command.split(maxsplit=1)
    action = parts[0].lower()
    arg = parts[1].lower() if len(parts) > 1 else None

    match action:
        case "look":
            describe_current_room(game_state)

        case "go":
            if arg:
                move_player(game_state, arg)
            else:
                print("Укажите направление (например: go north)")

        case "take":
            if arg:
                take_item(game_state, arg)
            else:
                print("Укажите предмет (например: take torch)")

        case "use":
            if arg:
                # Особый случай: сундук в treasure_room
                if arg == "treasure_chest" and game_state["current_room"] == "treasure_room":
                    attempt_open_treasure(game_state)
                else:
                    use_item(game_state, arg)
            else:
                print("Укажите предмет для использования (например: use torch)")

        case "solve":
            # В treasure_room попытка открыть сундук
            if game_state["current_room"] == "treasure_room":
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)

        case "inventory":
            show_inventory(game_state)

        case "quit" | "exit":
            game_state["game_over"] = True

        case _:
            print(f"Неизвестная команда: {action}")

if __name__ == "__main__":
    main()