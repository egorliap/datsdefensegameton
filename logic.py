"""Тут логика: какие запросы мы отправляем, как обрабатываем данные и тд"""
from typing import List
from validation import *
from client import *
import requests
from zombies import Defender

session = requests.Session()
lab = Labaratory(session)


def get_zombies_list(units:UnitsChanging)->List[Coords]:
    zombies = units.zombies
    if(zombies):
        return [item for item in zombies]
    else:
        return []

def get_base_info(units: UnitsChanging)->List[Block]:
    blocks = units.base
    return blocks

def get_enemy_base_info(units: UnitsChanging)->List[EnemyBlock]:
    return units.enemy_blocks


def get_units()->UnitsChanging:
    units = lab.units()
    if(isinstance(units,UnitsChanging)):
        return units

