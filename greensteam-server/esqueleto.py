import servente
import greenssteam_pb2

def getPublisher(data):
    request = greenssteam_pb2.Game()
    request.ParseFromString(data.arguments)
    reply = servente.getPublisher(request)
    reply.SerializeToString()
    return reply

def getLastPlayedGame(data):
    request = greenssteam_pb2.User()
    request.ParseFromString(data.arguments)
    reply = servente.getLastPlayedGame(request)
    reply.SerializeToString()
    return reply