#!/usr/bin/env python3
from .player_actions import show_inventory, get_input, move_player, take_item, use_item
from .utils import describe_current_room

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

if __name__ == "__main__":
    main()