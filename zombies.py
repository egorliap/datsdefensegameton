from typing import List

from validation import *

def evaluate_direction(z: Zombie):
    if z.direction == "up":
        return Coords(x=z.x,y=z.y + z.speed)
    if z.direction == "down":
        return Coords(x=z.x,y=z.y - z.speed)
    if z.direction == "left":
        return Coords(x=z.x - z.speed,y=z.y)
    if z.direction == "right":
        return Coords(x=z.x + z.speed,y=z.y)
    

class Defender:
    def __init__(self,zombies,base_blocks) -> None:
        self.zombies:List[Zombie] = zombies
        self.base:List[Block] = base_blocks
    def get_attacking_next_tick(self):
        arr =[]
        for zombie in self.zombies:
            for block in self.base:
                if(abs(evaluate_direction(zombie).x - block.x)<=3 and abs(evaluate_direction(zombie).y - block.y)<=3):
                    arr.append( (zombie,block))
        return arr
                    
    def heal(self):
        attack = []
        for attacker,block in self.get_attacking_next_tick():
            attack.append(AttackCommand(blockId=block.id,target=Coords(x=attacker.x,y=attacker.y))) 
        return attack
