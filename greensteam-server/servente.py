import greensteam_pb2 as Game
import greensteam_pb2 as User
import greensteam_pb2 as Publisher


user = User.User()
game = Game.Game()
game.name = "The world of Yario"


#publisher1 = Publisher("Publisher 1", [user1, user2], [game1, game2])
publisher = Publisher.Publisher()
publisher.name = "Intendo"
publisher.followers = 200000
publisher.games.append(game)
# publisher3.name = "oi"
#publisher2 = Publisher("Publisher 2", [user2], [game3])

publishers = [publisher]

def getPublisher(game) -> Publisher:
    for publisher in publishers:
        if game.name in [x.name for x in publisher.games]:
            return publisher
    return None
            