package com.green_steam;

public class GreenSteamProxy {
    int requestiId = 0;

	// O ideal seria solicitar os dados de conexao ao cliente
	// através de um nome de domínio (ex: www.ufc.br)
	UDPClient udpClient = new UDPClient("localhost", 7896);

	public AddressBook list(String nomeAgenda) {
		// (1) Empacota argumentos de entrada (ex: nomeAgenda)
		// (2) Chama doOperation
		// (3) Desempacota argumento de resposta (retorno de doOperation)
		// (4) Retorna reposta desempacotada
		// ex:
		// addressBook = AddressBook.parseFrom(doOperation("AddressBook",
		// "list", listPessoa.build().toByteArray()));
	}

	public String addPerson(Person person) {
		// (1) Empacota argumentos de entrada
		// (2) Chama doOperation
		// (3) Desempacota argumento de resposta (retorno de doOperation)
		// (4) Retorna reposta desempacotada
	}

	public String remove(int id, String nomeAgenda) {
		// (1) Empacota argumentos de entrada
		// (2) Chama doOperation
		// (3) Desempacota argumento de resposta (retorno de doOperation)
		// (4) Retorna reposta desempacotada
	}

	public byte[] doOperation(String objectRef, String method, byte[] args) {

		byte[] data = empacotaMensagem(objectRef, method, args);

		// envio
		udpClient.sendRequest(data);

		// recebimento
		Message resposta = desempacotaMensagem(udpClient.getReply());

		return resposta.getArguments().toByteArray();

	}

	public void finaliza() {
		udpClient.finaliza();
	}

	private byte[] empacotaMensagem(String objectRef, String method, byte[] args) {

		// empacota a Mensagem de requisicao

	}

	private Message desempacotaMensagem(byte[] resposta) {

		// desempacota a mensagem de resposta

	}

}
