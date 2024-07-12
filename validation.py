"""Ответы от сервера приходят в json, для валидации используем датаклассы pydantic
    Экземпляры этих датаклассов идут в логику и там обрабатываются"""
import pydantic

class BaseRequest(pydantic.BaseModel):
    api_key:str = pydantic.Field(validation_alias="X-Auth-Token")
     
    
class Coords(pydantic.BaseModel):
    x:int
    y:int

class AttackCommand(pydantic.BaseModel):
    block_id:str = pydantic.Field(validation_alias='blockId')
    target:Coords

class AcceptedCommands(pydantic.BaseModel):
    attack:list[AttackCommand]
    build:list[Coords]
    move_base:Coords
    
class Commands(pydantic.BaseModel):
    accepted_commands:AcceptedCommands = pydantic.Field(validation_alias='acceptedCommands')
    errors:list[str|None]

class Participate(pydantic.BaseModel):
    start_in:int = pydantic.Field(validation_alias="startsInSec")

class Block(pydantic.BaseModel):
    attack:int
    health:int
    id:str
    range:int
    is_head:bool|None = pydantic.Field(validation_alias="isHead")
    last_attack:Coords|None = pydantic.Field(validation_alias="lastAttack")
    name:str|None
    x:int
    y:int
    
class EnemyBlock(pydantic.BaseModel):
    attack:int
    health:int
    is_head:bool = pydantic.Field(validation_alias="isHead")
    last_attack:Coords = pydantic.Field(validation_alias="lastAttack")
    name:str
    x:int
    y:int
    
class Player(pydantic.BaseModel):
    enemy_block_kills:int = pydantic.Field(validation_alias="enemyBlockKills")
    game_ended_at:str|None = pydantic.Field(validation_alias="gameEndedAt")
    gold:int
    name:str
    points:int
    zombie_kills:int = pydantic.Field(validation_alias="zombieKills")
        
class Zombie(pydantic.BaseModel):
    attack:int
    direction:str
    health:int
    id:str
    speed:int
    type:str
    wait_turns:int = pydantic.Field(validation_alias='waitTurns')
    x:int
    y:int

class Zpot(pydantic.BaseModel):
    x:int
    y:int
    type:str

class UnitsChanging(pydantic.BaseModel):
    base:list[Block]
    enemy_blocks:list[EnemyBlock] = pydantic.Field(validation_alias='enemyBlocks')
    player:Player
    realm_name:str = pydantic.Field(validation_alias="realmName")
    turn:int
    turn_ends_in_ms:int = pydantic.Field(validation_alias="turnEndsInMs")    
    zombies:list[Zombie]

class UnitsNotChanging(pydantic.BaseModel):
    realm_name:str = pydantic.Field(validation_alias="realmName")
    zpots:list[Zpot]
    
class Round(pydantic.BaseModel):
    duration:int
    end_at:str = pydantic.Field(validation_alias="endAt")
    name:str
    repeat:int
    start_at:str = pydantic.Field(validation_alias="startAt")
    status:str
    
class GameRounds(pydantic.BaseModel):
    game_name:str = pydantic.Field(validation_alias="gameName")
    now:str
    rounds:list[Round]
    
    
class BaseRequest(pydantic.BaseModel):
    api_key:str = pydantic.Field(validation_alias="X-Auth-Token")

class CommandRequest(pydantic.BaseModel):
    attack:list[AttackCommand]
    build:list[Coords]
    move_base:Coords = pydantic.Field(validation_alias="moveBase")
    
class Error(pydantic.BaseModel):
    err_code:int = pydantic.Field(validation_alias='errCode')
    error:str