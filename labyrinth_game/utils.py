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