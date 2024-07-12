from aiohttp import ClientSession
from dotenv import load_dotenv
from os import getenv
load_dotenv()
TOKEN = getenv("TOKEN")

class Labaratory:
    """Класс, описывающий интерфейс взаимодействия с нашей лабараторией (на сервере организатора).
    Содержит методы, реализующие данное апи"""
    def get_info_1(self):
        pass
    def get_info_2(self):
        pass
    def post_info_1(self):
        pass