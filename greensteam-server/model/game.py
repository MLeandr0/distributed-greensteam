from dataclasses import dataclass

@dataclass
class Game:
    name: str
    description: str
    downloadQuantity: int
    reviewsPercentage: int