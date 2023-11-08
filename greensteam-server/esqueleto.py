import servente
import greenssteam_pb2

def getPublisher(data):
    request = greenssteam_pb2.Message()
    request.ParseFromString(data)
    reply = servente.getPublisher(request)
    return reply