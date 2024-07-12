"""Ответы от сервера приходят в json, для валидации используем датаклассы pydantic
    Экземпляры этих датаклассов идут в логику и там обрабатываются"""
import pydantic

class Unit1(pydantic.BaseModel):
    pos1:type
    pos2:type
    pos3:type
    
class Unit2(pydantic.BaseModel):
    pos1:type
    pos2:type
    pos3:type