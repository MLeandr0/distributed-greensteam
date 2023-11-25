import servente
import greensteam_pb2 as Game

def getPublisher(data):
    game = Game.Game()
    game.ParseFromString(data.arguments)
    reply = servente.getPublisher(game)

    return reply.SerializeToString()