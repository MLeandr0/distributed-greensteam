package com.greensteam;

import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;
import com.greensteam.proto.Greensteam.Game;
import com.greensteam.proto.Greensteam.Message;
import com.greensteam.proto.Greensteam.Publisher;
import com.greensteam.proto.Greensteam.Reviews;
import com.greensteam.proto.Greensteam.User;

public class GreenSteamProxy {

    int requestId = 0;

	// O ideal seria solicitar os dados de conexao ao cliente
	// através de um nome de domínio (ex: www.ufc.br)
	//UDPClient udpClient = new UDPClient("localhost", 7896);
	UDPClient udpClient = new UDPClient("localhost", 9090);

	public Game getLastPlayedGame(User.Builder profile) throws InvalidProtocolBufferException {

		Game game = Game.parseFrom(doOperation("Game", "get_last_played_game", profile.build().toByteArray()));

		return game;
	}

	public Publisher getPublisher(Game.Builder game) throws InvalidProtocolBufferException {
		
		Publisher publisher = Publisher.parseFrom(doOperation("Publisher", "get_publisher", game.build().toByteArray()));
		
		return publisher;
	}

	public Reviews getReviews(Game.Builder game) throws InvalidProtocolBufferException {
		
		Reviews reviews = Reviews.parseFrom(doOperation("Comment", "get_reviews", game.build().toByteArray()));
		
		return reviews;
	}

	public byte[] doOperation(String objectRef, String method, byte[] args) throws InvalidProtocolBufferException {
		byte[] data = empacotaMensagem(objectRef, method, args);

		// envio
		udpClient.sendRequest(data);

		// recebimento
		Message resposta = desempacotaMensagem(udpClient.getReply());

		// checagem de error
		if (!resposta.getError().getError().equals("")) {
			throw new RuntimeException(resposta.getError().getError());
		}

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

		return Message.parseFrom(resposta);
	}
}
