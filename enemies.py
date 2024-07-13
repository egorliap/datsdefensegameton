from typing import List
import math as m
from validation import *

def find_appropriate_blocks(x,y,blocks):
    pass
def dist(x1,y1,x2,y2):
    return m.sqrt((x2-x1)**2 + (y2-y1)**2)

class Enemy:
    def __init__(self,enemy_blocks,base_blocks) -> None:
        self.enemies:List[EnemyBlock] = enemy_blocks
        self.base:List[Block] = base_blocks

    def get_nearest_enemies(self):
        arr =[]
    
        for eblock in self.enemies:
                for block in self.base:
                    if(dist(eblock.x,eblock.y,block.x,block.y) <=5):
                        arr.append((eblock,block))
        return arr 
                    
    def attack(self):
        attack = []
        for attacker,block in self.get_nearest_enemies():
            attack.append(AttackCommand(blockId=block.id,target=Coords(x=attacker.x,y=attacker.y))) 
        return attack