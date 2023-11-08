import servente
import greenssteam_pb2 as Game

def getPublisher(data):
    game = Game.Game()
    game.ParseFromString(data.arguments)

    print(game)

    reply = servente.getPublisher(game)
    reply.SerializeToString()
    return reply