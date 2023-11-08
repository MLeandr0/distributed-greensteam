import esqueleto

class Despachante:

    def dispatch(self, request):

        # Obtém o código do método da solicitação
        method_id = request.method_id

        # Chama o método apropriado
        if method_id == "get_publisher":
            return esqueleto.getPublisher(request)
        else:
            raise ValueError("Método não encontrado")