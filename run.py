import asyncio
from client import Labaratory
import requests
import validation
import zombies
import build
import enemies
import logic
session = requests.Session()

async def participate():
    lab = Labaratory(session)
    units = logic.get_units()
    while(True):
        res = lab.participate()
        if(isinstance(res,validation.Participate)):
            print(f"{res.start_in=}")
            await asyncio.sleep(res.start_in+1)
            units = logic.get_units()
            
            
        elif(units.base == None):
            print("Dead((((((((((*))))))))))")
            await asyncio.sleep(20)
            
            
            
            
        elif(res.err_code > 50):
            
            if(units):
                units = logic.get_units()
                base = units.base
                zmbs = units.zombies
                enemy_blocks = units.enemy_blocks
                defender = zombies.Defender(zmbs,base)
                en_attacker = enemies.Enemy(enemy_blocks,base)
                builder = build.Build(base)
                
                result = lab.commands(validation.CommandRequest(attack=defender.heal()+en_attacker.attack(),build=builder.get_outter(),move_base=validation.Coords(x=base[1].x,y=base[1].y)).model_dump_json(by_alias=True))

                print(result)
                
                await asyncio.sleep(units.turn_ends_in_ms/1000)
                
        else:
            print(res.error)
            await asyncio.sleep(30)
try:
    asyncio.run(participate())
except KeyboardInterrupt:
    print("stoped")