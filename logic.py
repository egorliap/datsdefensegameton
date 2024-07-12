"""Тут логика: какие запросы мы отправляем, как обрабатываем данные и тд"""
from typing import List
from validation import *
from client import *
import requests

session = requests.Session()
lab = Labaratory(session)
def create_attack(block_id,coords)->AttackCommand:
    return AttackCommand(block_id=block_id,coords=coords)

def create_build(coords):
    payload = CommandRequest(attack=[],build=[coords],move_base=Coords(x=None,y=None))
    return lab.commands(payload)
    

def get_zombies_positions()->List[Coords]:
    units = lab.units()
    if(isinstance(units,UnitsChanging)):
        zombies = units.zombies
        if(zombies):
            return [Coords(x=item.x, y=item.y) for item in zombies]
        else:
            return []
    print(units.err_code,units.error)
    return None

print(create_build(Coords(x=1,y=15)))

    
