import servente

def add_game(args):

    # (1) Desempacota argumento de entrada
    game = args.decode("utf-8")

    # (2) Chama o método do servente
    result = servente.add_game(game)

    # (3) Empacota resposta do método servente e retorna
    return result.encode("utf-8")