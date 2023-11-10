import esqueleto
import greenssteam_pb2 as Message

class Despachante:
    def dispatch(self, request):
        msg = Message.Message()
        msg.ParseFromString(request)

        methodId = msg.methodId
        if methodId == "get_publisher":
            reply = Message.Message()
            reply.type = 1
            reply.id = msg.id
            reply.obfReference = msg.obfReference
            reply.methodId = msg.methodId
            reply.arguments = esqueleto.getPublisher(msg)
            return reply.SerializeToString()
        else:
            raise ValueError("Método não encontrado")