import esqueleto
import greensteam_pb2 as Message
import greensteam_pb2 as Error

class Despachante:
    def dispatch(self, request):
        msg = Message.Message()
        msg.ParseFromString(request)
        methodId = msg.methodId
        reply = Message.Message()
        reply.type = 1
        reply.id = msg.id
        reply.obfReference = msg.obfReference
        reply.methodId = msg.methodId
        try:
            if methodId == "get_publisher":
                reply.arguments = esqueleto.getPublisher(msg)
                return reply.SerializeToString()
            elif methodId == "get_last_played_game":
                reply.arguments = esqueleto.getLastPlayedGame(msg)
                return reply.SerializeToString()
            elif methodId == "get_reviews":
                reply.arguments = esqueleto.getReviews(msg)
                return reply.SerializeToString()
        except ValueError as error:
            errorObj = Error.Error()
            errorObj.error = str(error)
            return errorObj.SerializeToString()

                    