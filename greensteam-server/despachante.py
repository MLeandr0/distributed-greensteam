class Despachante:

    def __init__(self, game_path):
        self.game_path = game_path

    def dispatch(self, request):

        # Obtém o código do método da solicitação
        method_id = request.method_id

        # Chama o método apropriado
        if method_id == "add_game":
            return self.add_game(request)
        elif method_id == "add_publisher":
            return self.add_publisher(request)
        elif method_id == "get_publisher":
            return self.get_publisher(request)
        elif method_id == "get_last_played_game":
            return self.get_last_played_game(request)
        else:
            raise ValueError("Método não encontrado")