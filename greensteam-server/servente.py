import greensteam_pb2 as Game
import greensteam_pb2 as User
import greensteam_pb2 as Publisher
import greensteam_pb2 as Comment
import greensteam_pb2 as Reviews

user = User.User()
user.name = "Ataraxia"

game = Game.Game()
game.name = "Yario"

comment = Comment.Comment()
comment.content = "Bom demai"
comment.authorName = "hugo"
comment.recomendation = True

game.reviews.comments.append(comment)

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

games = []
games.append(game)
games.append(game2)

def getPublisher(game) -> Publisher:
    for publisher in publishers:
        if game.name in [x.name for x in publisher.games]:
            return publisher
    return None


def getLastPlayedGame(name) -> Game:
    for user in users:
        if(user.name == name):
            userGames = user.library
            return userGames[-1]
    return None           

def getReviews(name) -> Reviews:
    for game in games:
        if(name == game.name):
            return game.reviews
    return None