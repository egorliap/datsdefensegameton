from aiohttp import ClientSession
import requests
import asyncio
from validation import *
from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN = getenv("TOKEN")

url = "https://games-test.datsteam.dev/"

participate_endpoint = "play/zombidef/participate"
commands_endpoint = "play/zombidef/command"
units_endpoint = "play/zombidef/units"
world_endpoint = "play/zombidef/world"
rounds_endpoint = "rounds/zombidef"

class Labaratory:
    """Класс, описывающий интерфейс взаимодействия с нашей лабараторией (на сервере организатора).
    Содержит методы, реализующие данное апи"""
    
    def __init__(self,session:requests.Session):
        self.session:requests.Session = session
        self.session.headers.update({"X-Auth-Token":TOKEN})
        
    def commands(self,payload:CommandRequest):
        res = self.session.post(url=url+commands_endpoint,data=payload)
        if(res.status_code != 200):
            return Error.model_validate_json(res.content)
        return Commands.model_validate_json(res.content)
    
    def participate(self):
        res = self.session.put(url=url+participate_endpoint)
        if(res.status_code != 200):
            return Error.model_validate_json(res.content)
        return Participate.model_validate_json(res.content)
    
    def rounds(self):
        res = self.session.get(url=url+rounds_endpoint)
        if(res.status_code != 200):
            return Error.model_validate_json(res.content)
        return GameRounds.model_validate_json(res.content)
    
    def units(self):
        res = self.session.get(url=url+units_endpoint)
        if(res.status_code != 200):
            return Error.model_validate_json(res.content)
        return UnitsChanging.model_validate_json(res.content)

    def world(self):
        res = self.session.get(url=url+world_endpoint)
        if(res.status_code != 200):
            return Error.model_validate_json(res.content)
        return UnitsNotChanging.model_validate_json(res.content)
        
    

