import esqueleto
import greenssteam_pb2 as Message

class Despachante:
    def dispatch(self, request):
        msg = Message.Message()
        msg.ParseFromString(request)

        methodId = msg.methodId
        if methodId == "get_publisher":
            return esqueleto.getPublisher(msg)
        else:
            raise ValueError("Método não encontrado")