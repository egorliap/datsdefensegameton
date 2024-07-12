from aiohttp import ClientSession
import asyncio
from dotenv import load_dotenv
from os import getenv
from validation import *
load_dotenv()
TOKEN = getenv("TOKEN")

test_url = "https://games-test.datsteam.dev/"
participate_endpoint = "play/zombidef/participate"
commands_endpoint = "play/zombidef/command"
units_endpoint = "play/zombidef/units"
world_endpoint = "play/zombidef/world"
rounds_endpoint = "rounds/zombidef"

class Labaratory:
    """Класс, описывающий интерфейс взаимодействия с нашей лабараторией (на сервере организатора).
    Содержит методы, реализующие данное апи"""
    
    def __init__(self,session:ClientSession):
        self.session = session
        
    

