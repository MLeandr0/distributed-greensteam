import esqueleto
import greenssteam_pb2 as Message

class Despachante:
    def dispatch(self, request):
        msg = Message.Message()
        msg.ParseFromString(request)
        print("test")

        methodId = msg.methodId
        reply = Message.Message()
        reply.type = 1
        reply.id = msg.id
        reply.obfReference = msg.obfReference
        reply.methodId = msg.methodId
        if methodId == "get_publisher":
            reply.arguments = esqueleto.getPublisher(msg)
            return reply.SerializeToString()
        elif methodId == "get_last_played_game":
            reply.arguments = esqueleto.getLastPlayedGame
        else:
            raise ValueError("Método não encontrado")