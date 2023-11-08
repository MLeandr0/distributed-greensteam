import socket
import despachante
import greenssteam_pb2

class UDPServer:
    def __init__(self, server_port):
        self.server_port = server_port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(("0.0.0.0", self.server_port))
        print("Servidor aguardando conexões na porta", self.server_port)

    def start(self):
        try:
            while True:
                data, client_address = self.server_socket.recvfrom(1024)
                print(f"Conexão de {client_address[0]}:{client_address[1]}")
                connection = Connection(self.server_socket, client_address, data)

        except Exception as e:
            print(f"Listen: {e}")

class Connection:
    def __init__(self, server_socket, client_address, data):
        self.incoming_data = data
        self.server_socket = server_socket
        self.client_address = client_address
        self.despachante = despachante.Despachante()

    def run(self):
        try:
            while True:
                requisicao = self.desempacota_requisicao(self.incoming_data)
                resultado = self.despachante.selecionaEqueleto(requisicao)
                response_data = self.empacota_resposta(resultado, requisicao.request_id)
                self.send_reply(response_data)

        except Exception as e:
            print(f"Connection: {e}")

    def send_reply(self, response_data):
        # Implemente a lógica para enviar uma resposta ao cliente
        self.server_socket.sendto(response_data, self.client_address)

if __name__ == "__main__":
    server_port = 9090
    server = UDPServer(server_port)
    server.start()
