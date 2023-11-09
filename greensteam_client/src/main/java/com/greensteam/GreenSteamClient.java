package com.greensteam;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//import com.greensteam.objects.Game;
//import com.greensteam.objects.Publisher;

import com.greensteam.proto.MessageOuterClass.Game;

public class GreenSteamClient {
    
    GreenSteamProxy proxy;
	/*
	Publisher enixUI;
	Publisher Bancom;
	Game theAdventure;
	Game theFall;	
	*/

	
	public GreenSteamClient() {
		this.proxy = new GreenSteamProxy();
		//theAdventure = new Game("The adventure", 20000, "A game about an adventure", 75.9);
		//theFall = new Game("The Fall", 20159, "A game about an adventure", 80.1);
	}
	

    public String selecionaOperacao() throws IOException {

		BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
		String opt = null;
		do {
			opt = stdin.readLine();
		} while (opt.equals("\n") || opt.equals("") || opt.isEmpty());

		opt = "Encontrar desenvolvedora";

		switch (opt) {
		case "Checar atividade":

			// Interagir com o usuario via stdin.readLine() para setar
			// argumentos de entada
			// ex:
			// System.out.println("Digite seu nome: ");
			// person.setName(stdin.readLine());

			// Por fim, chamar metodo do proxy correspondente à operação
			// escolhida
			// proxy.addPerson(person.build());

			break;

		case "Encontrar desenvolvedora":

			System.out.println("\nDecide which game you want to check");
			System.out.println("1 - The Adventure");
			System.out.println("2 - The Fall\n");
			
			Game.Builder game = Game.newBuilder();

			game.setName("The world of Yario");
			game.setDescription("A game when a snake tries to kill the prince");
			game.setDownloadQuantity(32000);
			game.setReviewsPercentage(95);

			System.out.println(proxy.getPublisher(game));

			/*
			int gameChoice = Integer.parseInt(stdin.readLine());
			if(gameChoice == 1) {
				System.out.println("\nYeah");
				System.out.println(theAdventure.getName());
				proxy.getPublisher(theAdventure);
			} else if (gameChoice == 2) {
				System.out.println("\nHell yeah");
				System.out.println(theFall.getName());
				proxy.getPublisher(theFall);
			} else {
				System.out.println("\nJogo invalido ou inexistente, tente novamente.");
			}
			*/
			break;

		case "Obter avaliações":
			break;

		case "Finalizar":
			//proxy.finaliza();
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
		GreenSteamClient bookClient = new GreenSteamClient();
		//bookClient.startMockedDataBase();
		//bookClient.printMenu();
		String operacao = "empty";
		do {
			bookClient.printMenu();
			try {
				operacao = bookClient.selecionaOperacao();
			} catch (IOException ex) {
				System.out.println("Escolha uma das operações pelo número: " + ex);
			}
		} while (!operacao.equals("Finalizar"));
	}

}