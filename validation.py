"""Ответы от сервера приходят в json, для валидации используем датаклассы pydantic
    Экземпляры этих датаклассов идут в логику и там обрабатываются"""
import pydantic

class BaseRequest(pydantic.BaseModel):
    api_key:str = pydantic.Field(validation_alias="X-Auth-Token")
     
    
class Coords(pydantic.BaseModel):
    x:int|None
    y:int|None

class AttackCommand(pydantic.BaseModel):
    block_id:None|str = pydantic.Field(validation_alias='blockId',serialization_alias='blockId')
    target:Coords|None

class AcceptedCommands(pydantic.BaseModel):
    attack:list[AttackCommand|None]|None
    build:list[Coords|None]|None
    move_base:Coords|None = pydantic.Field(validation_alias='moveBase',serialization_alias='moveBase')
    
class Commands(pydantic.BaseModel):
    accepted_commands:AcceptedCommands|None = pydantic.Field(validation_alias='acceptedCommands')
    errors:list[str|None]|None

class Participate(pydantic.BaseModel):
    start_in:int = pydantic.Field(validation_alias="startsInSec")

class Block(pydantic.BaseModel):
    attack:int|None
    health:int|None
    id:str|None
    range:int|None
    #is_head:bool|None = pydantic.Field(validation_alias="isHead")
    last_attack:Coords|None = pydantic.Field(validation_alias="lastAttack")
    x:int|None
    y:int|None
    
class EnemyBlock(pydantic.BaseModel):
    attack:int|None
    health:int|None
    #is_head:bool|None = pydantic.Field(validation_alias="isHead")
    last_attack:Coords|None = pydantic.Field(validation_alias="lastAttack")
    #name:str|None
    x:int|None
    y:int|None
    
class Player(pydantic.BaseModel):
    enemy_block_kills:int|None = pydantic.Field(validation_alias="enemyBlockKills")
    game_ended_at:str|None = pydantic.Field(validation_alias="gameEndedAt")
    gold:int
    name:str
    points:int|None
    zombie_kills:int|None = pydantic.Field(validation_alias="zombieKills")
        
class Zombie(pydantic.BaseModel):
    attack:int
    direction:str
    health:int
    id:str
    speed:int
    type:str
    wait_turns:int|None = pydantic.Field(validation_alias='waitTurns')
    x:int
    y:int

class Zpot(pydantic.BaseModel):
    x:int|None
    y:int|None
    type:str|None

class UnitsChanging(pydantic.BaseModel):
    base:list[Block|None]|None
    enemy_blocks:list[EnemyBlock|None]|None = pydantic.Field(validation_alias='enemyBlocks')
    player:Player|None
    realm_name:str|None = pydantic.Field(validation_alias="realmName")
    turn:int|None
    turn_ends_in_ms:int|None = pydantic.Field(validation_alias="turnEndsInMs")    
    zombies:list[Zombie|None]|None

class UnitsNotChanging(pydantic.BaseModel):
    realm_name:str = pydantic.Field(validation_alias="realmName")
    zpots:list[Zpot|None]|None
    
class Round(pydantic.BaseModel):
    duration:int|None
    end_at:str|None = pydantic.Field(validation_alias="endAt")
    name:str|None
    
    start_at:str|None = pydantic.Field(validation_alias="startAt")
    status:str|None
    
class GameRounds(pydantic.BaseModel):
    game_name:str = pydantic.Field(validation_alias="gameName")
    now:str|None
    rounds:list[Round|None]|None
    
    
class BaseRequest(pydantic.BaseModel):
    api_key:str = pydantic.Field(serialization_alias="X-Auth-Token")

class CommandRequest(pydantic.BaseModel):
    attack:list[AttackCommand|None]|None
    build:list[Coords|None]|None
    move_base:Coords|None = pydantic.Field(serialization_alias="moveBase")
    
class Error(pydantic.BaseModel):
    err_code:int = pydantic.Field(validation_alias='errCode')
    error:str