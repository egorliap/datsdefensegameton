import math as m
from typing import List
import validation
class Build:
    def __init__(self,base) -> None:
    
        self.base:List[validation.Block] = base
    def get_ranges(self):
        ranges = dict()
        for block in self.base:
            if(block.y not in ranges.keys()):
                ranges[block.y] = [block.x]
            else:
                ranges[block.y].append(block.x)
        return ranges
    def get_outter(self):
        ranges = self.get_ranges()
        res = []
        for key in ranges.keys():
            res.append(validation.Coords(x=min(ranges[key])-1,y=key))
            res.append(validation.Coords(x=max(ranges[key])+1,y=key))
        return res
            
    def rebase(self):
        pass