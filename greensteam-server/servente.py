from model.game import Game
from model.publisher import Publisher
from model.user import User

game1 = Game("Jogo 1", "Descrição do Jogo 1", 1000, 90)
game2 = Game("Jogo 2", "Descrição do Jogo 2", 500, 85)
game3 = Game("Jogo 3", "Descrição do Jogo 3", 2000, 95)

user1 = User("Usuário 1", "Bio do Usuário 1", [game1, game2], 10)
user2 = User("Usuário 2", "Bio do Usuário 2", [game2, game3], 5)

publisher1 = Publisher("Publisher 1", [user1, user2], [game1, game2])
publisher2 = Publisher("Publisher 2", [user2], [game3])

publishers = [publisher1, publisher2]

def getPublisher(game) -> Publisher:
    for publisher in publishers:
        if game in publisher.games:
            return publisher  
    return None
            