import socket
import despachante

class UDPServer:
    def __init__(self, server_port):
        self.server_port = server_port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(("localhost", self.server_port))
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
                requisicao = self.get_request()
                resultado = self.despachante.dispatch(requisicao)
                self.send_reply(resultado)

        except Exception as e:
            print(f"Connection: {e}")

    def get_request(self):
        data = self.server_socket.recv(1024).decode()
        return data


    def send_reply(self, response_data):
        # Implemente a lógica para enviar uma resposta ao cliente
        self.server_socket.send(response_data.encode(), self.client_address)

if __name__ == "__main__":
    server_port = 9090
    server = UDPServer(server_port)
    server.start()
