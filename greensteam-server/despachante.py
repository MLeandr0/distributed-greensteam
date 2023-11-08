import esqueleto

class Despachante:

    def dispatch(self, request):

        methodId = request.methodId
        if methodId == "get_publisher":
            return esqueleto.getPublisher(request)
        else:
            raise ValueError("Método não encontrado")