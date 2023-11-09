package com.greensteam;

import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;
//import com.greensteam.objects.Game;
//import com.greensteam.objects.Publisher;
import com.greensteam.proto.MessageOuterClass.Message;
//import com.greensteam.proto.MessageOuterClass.Game;
import com.greensteam.proto.MessageOuterClass.Publisher;
import com.greensteam.proto.MessageOuterClass.Game.Builder;

public class GreenSteamProxy {
    int requestId = 0;

	// O ideal seria solicitar os dados de conexao ao cliente
	// através de um nome de domínio (ex: www.ufc.br)
	//UDPClient udpClient = new UDPClient("localhost", 7896);
	UDPClient udpClient = new UDPClient("localhost", 9090);

	/*
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
	*/

	public Publisher getPublisher(Builder game) throws InvalidProtocolBufferException{
		
		Publisher publisher = Publisher.parseFrom(doOperation("Publisher", "get_publisher", game.build().toByteArray()));
		
		return publisher;
	}

	public byte[] doOperation(String objectRef, String method, byte[] args) throws InvalidProtocolBufferException {
		byte[] data = empacotaMensagem(objectRef, method, args);

		// envio
		udpClient.sendRequest(data);

		// recebimento
		Message resposta = desempacotaMensagem(udpClient.getReply());

		return resposta.getArguments().toByteArray();

	}

	private byte[] empacotaMensagem(String objectRef, String method, byte[] args) {

		Message message = Message.newBuilder()
			.setType(0)
			.setId(0)
			.setObfReference(objectRef)
			.setMethodId(method)
			.setArguments(ByteString.copyFrom(args))
			.build();

        return message.toByteArray();

	}

	private Message desempacotaMensagem(byte[] resposta) throws InvalidProtocolBufferException {

		// desempacota a mensagem de resposta
		return Message.parseFrom(resposta);

	}

}
