package com.green_steam;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class GreenSteamClient {
    
    GreenSteamProxy proxy;

	public GreenSteamClient() {
		proxy = new GreenSteamProxy();
	}

    public int selecionaOperacao() throws IOException {

		int operacao = 0;

		BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
		String opt = null;
		do {
			opt = stdin.readLine();
		} while (opt.equals("\n") || opt.equals("") || opt.isEmpty());
		operacao = Integer.parseInt(opt);

		switch (operacao) {
		case 1:

			// Interagir com o usuario via stdin.readLine() para setar
			// argumentos de entada
			// ex:
			// System.out.println("Digite seu nome: ");
			// person.setName(stdin.readLine());

			// Por fim, chamar metodo do proxy correspondente à operação
			// escolhida
			// proxy.addPerson(person.build());

			break;

		case 2:

			break;

		case 3:
			break;

		case 0:
			//proxy.finaliza();
			break;

		default:
			System.out.println("Operação invalida, tente outra.");
			break;
		}
		return operacao;
	}

    public void printMenu() {
		System.out.println("\nDigite o n# da operação que deseja executar: ");
		System.out.println("1 - Consultar ultimo jogado");
		System.out.println("2 - Consultar empresa desenvolvedora");
		System.out.println("3 - Consultar avaliações");
		System.out.println("0 - Sair\n");
	}

    public static void main(String[] args) {
		GreenSteamClient bookClient = new GreenSteamClient();
		int operacao = -1;
		do {
			bookClient.printMenu();
			try {
				operacao = bookClient.selecionaOperacao();
			} catch (IOException ex) {
				System.out.println("Escolha uma das operações pelo número");
			}
		} while (operacao != 0);
	}

}