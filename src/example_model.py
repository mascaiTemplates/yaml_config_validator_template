from src.base_model import YamlModel

from pydantic import BaseModel
from typing import List
from enum import Enum 


class Owner(BaseModel): 
    age: int
    name: str

        
class Car(BaseModel): 
    name: str
    is_new: bool


class Config(YamlModel): 
    owner: Owner
    car: Car 
    
