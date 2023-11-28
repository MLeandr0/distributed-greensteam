package com.greensteam;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import com.greensteam.proto.Greensteam.Game;
import com.greensteam.proto.Greensteam.User;

public class GreenSteamClient {
    
    GreenSteamProxy proxy;

	
	public GreenSteamClient() {
		this.proxy = new GreenSteamProxy();

	}
	
    public String selecionaOperacao() throws IOException {

		BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
		String opt = null;
		do {
			opt = stdin.readLine();
		} while (opt.equals("\n") || opt.equals("") || opt.isEmpty());
		switch (opt) {
		case "Checar atividade":

			User.Builder profile = User.newBuilder();
			System.out.print("\nDigite o nome do usuário: ");
			Game.Builder mockedGame = Game.newBuilder();

			profile.setName(stdin.readLine());

			//mocked input
			profile.setAchievements(10);
			profile.setBio("Empty");
			profile.addLibrary(mockedGame);

			try {
				System.out.println("\n" + proxy.getLastPlayedGame(profile));
			} catch (RuntimeException e) {
				System.out.println(e.getMessage());
			}
			
			break;

		case "Encontrar desenvolvedora":

			Game.Builder game = Game.newBuilder();
			System.out.print("\nDigite o nome do jogo: ");
			game.setName(stdin.readLine());
			
			//mocked input
			game.setDescription("A game when a snake tries to kill the prince");
			game.setDownloadQuantity(32000);
			game.setReviewsPercentage(95);

			try {
				System.out.println("\n" + proxy.getPublisher(game).getName());
			} catch (RuntimeException e) {
				System.out.println(e.getMessage());
			}

			break;

		case "Obter avaliações":

			Game.Builder gameReviews = Game.newBuilder();
			System.out.print("\nDigite o nome do jogo: ");

			gameReviews.setName(stdin.readLine());
			
			//mocked input
			gameReviews.setDescription("A game when a snake tries to kill the prince");
			gameReviews.setDownloadQuantity(32000);
			gameReviews.setReviewsPercentage(95);

			try {
				System.out.println("\n" + proxy.getReviews(gameReviews));
			} catch (RuntimeException e) {
				System.out.println(e.getMessage());
			}
			
			break;

		case "Finalizar":
			break;

		default:
			System.out.println("Operação invalida, tente outra.");
			break;
		}
		return opt;
	}

    public void printMenu() {
		System.out.println("\nDigite a operação que deseja executar: ");
		System.out.println("Checar atividade - Consulta o ultimo jogo jogado");
		System.out.println("Encontrar desenvolvedora - Consultar a empresa desenvolvedora do jogo");
		System.out.println("Obter avaliações - Consulta as avaliações do jogo");
		System.out.println("Finalizar - Encerrar contato com o servidor\n");
	}

    public static void main(String[] args) {
		GreenSteamClient greenSteamClient = new GreenSteamClient();
		String operacao = "empty";
		do {
			greenSteamClient.printMenu();
			try {
				operacao = greenSteamClient.selecionaOperacao();
			} catch (IOException ex) {
				ex.printStackTrace();
				System.out.println("Escolha uma das operações pelo número: " + ex);
			}
		} while (!operacao.equals("Finalizar"));
	}

}