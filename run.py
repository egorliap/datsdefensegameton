import asyncio
from client import Labaratory
import requests
import validation
import zombies
import build

import logic
session = requests.Session()

async def participate():
    lab = Labaratory(session)
    units = logic.get_units()
    while(True):
        res = lab.participate()
        if(isinstance(res,validation.Participate)):
            print(f"{res.start_in=}")
            await asyncio.sleep(res.start_in+0.4)
            units = logic.get_units()
            
            
        elif(units.base == None):
            print("Dead((((((((((*))))))))))")
            await asyncio.sleep(20)
            
            
            
            
        elif(res.err_code > 50):
            
            if(units):
                defender = zombies.Defender(logic.get_zombies_list(units),logic.get_base_info(units))
                attacking = defender.get_attacking_next_tick()
                #print(f"{attacking=}")
                heal = defender.heal()
                
                #print(f"{heal=}")
                base = units.base
                b = build.Build(base)
                result = lab.commands(validation.CommandRequest(attack=heal,build=b.get_outter(),move_base=validation.Coords(x=base[1].x,y=base[1].y)).model_dump_json(by_alias=True))

                print(result)
                
                await asyncio.sleep(units.turn_ends_in_ms/1000)
                units = logic.get_units()
                
                
                
            
            
        else:
            print(res.error)
            await asyncio.sleep(30)
try:
    asyncio.run(participate())
except KeyboardInterrupt:
    print("stoped")