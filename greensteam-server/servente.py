import greenssteam_pb2 as Game
import greenssteam_pb2 as User
import greenssteam_pb2 as Publisher


user = User.User()
user.name = "Ataraxia"
game = Game.Game()
game.name = "The world of Yario"
game2 = Game.Game()
game2.name = "RORR"
user.library.append(game)
user.library.append(game2)
userGames = user.library
users = [user]

publisher = Publisher.Publisher()
publisher.name = "Intendo"
publisher.followers = 200000
publisher.games.append(game)
publishers = [publisher]

def getPublisher(game) -> Publisher:
    for publisher in publishers:
        if game.name in [x.name for x in publisher.games]:
            return publisher
    return None


def getLastPlayedGame(name) -> Game:
    for user in users:
        if(user.name == name):
            userGames = user.library
            print(userGames[-1])
            return userGames[-1]
    return None            
            