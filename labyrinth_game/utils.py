from .constants import ROOMS

def describe_current_room(game_state):
    current_room_key = game_state['current_room']
    
    room = ROOMS.get(current_room_key)  # Получаем данные о комнате из константы ROOMS


    print(f"== {current_room_key.upper()} ==")  # Выводим название комнаты
    
    print(room['description'])  # Описание комнаты
    
    # Список предметов
    if room.get('items'):
        print("Заметные предметы:", ", ".join(room['items']))
    
    print("Выходы:", ", ".join(room.get('exits', [])))  # Доступные выходы
    
    # Проверка на загадку
    if room.get('puzzle'):
        print("Кажется, здесь есть загадка (используйте команду solve).")


def solve_puzzle(game_state):
    from .player_actions import get_input

    current_room_key = game_state['current_room']
    room = ROOMS.get(current_room_key)
    
    if not room or not room.get('puzzle'):
        print("Загадок здесь нет.")
        return
    
    question, answer = room['puzzle']
    print(question)
    
    user_answer = get_input("Ваш ответ: ")
    
    if user_answer.lower() == answer.lower():
        print("Правильно! Вы успешно решили загадку.")
        room['puzzle'] = None   # Убираем загадку, чтобы нельзя было решать дважды
        reward = room.get('reward') # Можно добавить награду, например предмет
        if reward:
            game_state.setdefault('player_inventory', []).append(reward)
            print(f"Вы получили: {reward}")
    else:
        print("Неверно. Попробуйте снова.")


def attempt_open_treasure(game_state):
    """
    Попытка открыть сундук с сокровищем в treasure_room.
    Можно открыть ключом, решить загадку или ввести код вручную.
    """
    from .player_actions import get_input
    from .utils import solve_puzzle

    current_room_key = game_state['current_room']
    room = ROOMS.get(current_room_key)

    if not room:
        print("Ошибка: комната не найдена.")
        return

    # Проверка наличия сундука
    if "treasure_chest" not in room.get("items", []):
        print("Сундук уже открыт или отсутствует.")
        return

    inventory = game_state.get("player_inventory", [])

    # Если есть ключ — открываем
    if "treasure_key" in inventory or "rusty_key" in inventory:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        room["items"].remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
        return

    # Если ключа нет — предлагаем решить загадку
    if room.get("puzzle"):
        print("У сундука есть загадка. Можно попробовать решить её или ввести код.")
        solve_puzzle(game_state)
        # Если сундук убран после решения загадки
        if "treasure_chest" not in room.get("items", []):
            print("Сундук открыт! В нём сокровище! Вы победили!")
            game_state["game_over"] = True
            return

    # Если загадки нет или игрок не решил — предлагаем ввести код
    choice = get_input("Сундук заперт. Хотите попробовать ввести код? (да/нет): ")
    if choice.lower() in ["да", "yes", "y"]:
        user_code = get_input("Введите код: ")
        # Проверяем правильный ответ из puzzle, если она есть
        puzzle = room.get("puzzle")
        if puzzle and user_code.strip().lower() == puzzle[1].lower():
            print("Правильно! Сундук открыт!")
            room["items"].remove("treasure_chest")
            print("В сундуке сокровище! Вы победили!")
            game_state["game_over"] = True
        else:
            print("Неверный код. Сундук остался закрыт.")
    else:
        print("Вы отступаете от сундука.")


def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение") 