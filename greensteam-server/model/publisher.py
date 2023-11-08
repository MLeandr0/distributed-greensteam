from dataclasses import dataclass
from model.game import Game

@dataclass
class Publisher:
    name: str
    followers: int
    library: list[Game]