"""Ответы от сервера приходят в json, для валидации используем датаклассы pydantic
    Экземпляры этих датаклассов идут в логику и там обрабатываются"""
import datetime
import pydantic

class BaseRequest(pydantic.BaseModel):
    api_key:str = pydantic.Field(alias="X-Auth-Token")
     
class BaseResponse(pydantic.BaseModel):
    errors:list[str|None]
    
class Coords(pydantic.BaseModel):
    x:int
    y:int

class AttackCommand(pydantic.BaseModel):
    block_id:str = pydantic.Field(alias='blockId')
    target:Coords

class AcceptedCommands(pydantic.BaseModel):
    attack:list[AttackCommand]
    build:list[Coords]
    move_base:Coords
    
class Commands(BaseResponse):
    accepted_commands:AcceptedCommands = pydantic.Field(alias='acceptedCommands')

class Participate(pydantic.BaseModel):
    start_in:int = pydantic.Field(alias="startsInSec")

class Block(pydantic.BaseModel):
    attack:int
    health:int
    id:str
    range:int
    is_head:bool = pydantic.Field(alias="isHead")
    last_attack:Coords = pydantic.Field(alias="lastAttack")
    name:str
    x:int
    y:int
    
class EnemyBlock(pydantic.BaseModel):
    attack:int
    health:int
    is_head:bool = pydantic.Field(alias="isHead")
    last_attack:Coords = pydantic.Field(alias="lastAttack")
    name:str
    x:int
    y:int
    
class Player(pydantic.BaseModel):
    enemy_block_kills:int = pydantic.Field(alias="enemyBlockKills")
    game_ended_at:datetime = pydantic.Field(alias="gameEndedAt")
    gold:int
    name:str
    points:int
    zombie_kills:int = pydantic.Field(alias="zombieKills")
        
class Zombie(pydantic.BaseModel):
    attack:int
    direction:str
    health:int
    id:str
    speed:int
    type:str
    wait_turns:int = pydantic.Field(alias='waitTurns')
    x:int
    y:int

class Zpot(pydantic.BaseModel):
    x:int
    y:int
    type:str

class UnitsChanging(pydantic.BaseModel):
    base:list[Block]
    enemy_blocks:list[EnemyBlock] = pydantic.Field(alias='enemyBlocks')
    player:Player
    realm_name:str = pydantic.Field(alias="realmName")
    turn:int
    turn_ends_in_ms:int = pydantic.Field(alias="turnEndsInMs")    
    zombies:list[Zombie]

class UnitsNotChanging(pydantic.BaseModel):
    realm_name:str = pydantic.Field(alias="realmName")
    zpots:list[Zpot]
    
class Round(pydantic.BaseModel):
    duration:int
    end_at:datetime = pydantic.Field(alias="endAt")
    name:str
    repeat:int
    start_at:datetime = pydantic.Field(alias="startAt")
    status:str
    
class GameRounds(pydantic.BaseModel):
    game_name:str = pydantic.Field(alias="gameName")
    now:datetime
    rounds:list[Round]
    