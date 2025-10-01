#!/usr/bin/env python3
from . import constants
from . import player_actions
from . import utils

def main():
    print("Первая попытка запустить проект!")

if __name__ == "__main__":
    main()


game_state = {
    'player_inventory': [], # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False, # Значения окончания игры
    'steps_taken': 0 # Количество шагов
}