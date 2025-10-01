from .utils import describe_current_room
from .constants import ROOMS

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
    

def move_player(game_state, direction):
    """
        Функция перемещения.
    """
    current_room = ROOMS[game_state['current_room']]
    exits = current_room.get('exits', {})
    
    if direction in exits:
        game_state['current_room'] = exits[direction]   # Обновляем текущую комнату
        
        game_state['steps'] = game_state.get('steps', 0) + 1    # Увеличиваем шаг

        describe_current_room(game_state)   # Описание новой комнаты
    else:
        print("Нельзя пойти в этом направлении.")


def take_item(game_state, item_name):
    """
        Функция взятия предмета
    """
    urrent_room = ROOMS[game_state['current_room']]
    items = current_room.get('items', [])
    
    if item_name in items:
        game_state.setdefault('player_inventory', []).append(item_name) # Добавляем предмет в инвентарь
        items.remove(item_name) # Убираем предмет из комнаты
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")


def use_item(game_state, item_name):
    """
        Юзаем предметы из инвентаря игрока.
    """
    inventory = game_state.get('player_inventory', [])
    
    if item_name not in inventory:
        print("У вас нет такого предмета.")
        return

    # Обработка уникальных предметов
    if item_name == "torch":
        print("Вы зажгли фонарь. Стало светлее.")
    elif item_name == "sword":
        print("Вы держите меч, чувствуете себя более уверенно.")
    elif item_name == "bronze box":
        print("Вы открыли бронзовую шкатулку.")
        if "rusty key" not in inventory:
            inventory.append("rusty key")
            print("В инвентарь добавлен: rusty key")
    else:
        print("Вы не знаете, как использовать этот предмет.")
