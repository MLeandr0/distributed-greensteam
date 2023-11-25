from dataclasses import dataclass
from model.game import Game

@dataclass
class User:
    name: str
    bio: str
    library: list[Game]
    reviewsPercentage: int