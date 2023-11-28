import socket
import despachante
import greensteam_pb2 as Message

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
                connection.run()

        except Exception as e:
            print(f"Listen: {e}")

class Connection:    
    last_id = -1

    def __init__(self, server_socket, client_address, data):
        self.is_test_server = False
        self.incoming_data = data
        self.server_socket = server_socket
        self.client_address = client_address
        self.despachante = despachante.Despachante()

    def run(self):
        try:
            msg = Message.Message()
            msg.ParseFromString(self.incoming_data)
            if(Connection.last_id == msg.id):
                print("Duplicated Request")
            else:
                Connection.last_id = msg.id
                if(self.is_test_server): return
                resultado = self.despachante.dispatch(self.incoming_data)
                self.send_reply(resultado)

        except Exception as e:
            print(f"Connection: {e}")

    def get_request(self):
        data = self.server_socket.recv(1024).decode()
        self.lastRequest.append(data)
        return data


    def send_reply(self, response_data):
        self.server_socket.sendto(response_data, self.client_address)

if __name__ == "__main__":
    server_port = 9090
    server = UDPServer(server_port)
    server.start()