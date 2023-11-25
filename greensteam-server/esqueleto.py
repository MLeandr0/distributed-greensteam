import servente
import greensteam_pb2 as Game
import greensteam_pb2 as User
import greensteam_pb2 as Comment

def getPublisher(data):
    request = Game.Game()
    request.ParseFromString(data.arguments)
    reply = servente.getPublisher(request)
    return reply.SerializeToString()


def getLastPlayedGame(data):
    request = User.User()
    request.ParseFromString(data.arguments)
    reply = servente.getLastPlayedGame(request.name)
    return reply.SerializeToString()

def getReviews(data):
    request = Game.Game()
    request.ParseFromString(data.arguments)
    reply = servente.getReviews(request.name)
    return reply.SerializeToString()