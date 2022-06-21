import java.util.List;
import java.util.Scanner;

import Jama.Matrix;

public class Main {
	public static void main(String[] args) {
		try {
			Scanner scannerInt = new Scanner(System.in);
			Scanner scannerLine = new Scanner(System.in);
			System.out.println("Digite o arquivo da Matriz de entrada:");
			String caminhoArquivoMatriz = scannerLine.nextLine();
			System.out.println("Digite arquivo do Chute Inicial:");
			String caminhoArquivoAutovetorChute = scannerLine.nextLine();
			double erro = 0.001;
			
			Matrix matriz = new Matrix(MatrizUtil.lerMatrizDeArquivo(caminhoArquivoMatriz));
			double[] autovetorChute = MatrizUtil.matrizParaVetor(MatrizUtil.lerMatrizDeArquivo(caminhoArquivoAutovetorChute));

			System.out.println("Erro: " + erro);
			if (matriz.getRowDimension() <= 4) {
				System.out.println("Matriz de entrada:");
				MatrizUtil.exibirMatriz(matriz);
			}
			
			int opcao;
			do {
				System.out.println("--- Autovalores e Autovetores ---");
				System.out.println(" 1 - Potência Inverso");
				System.out.println(" 0 - Sair");
				
				System.out.print("Digite o número da opção: ");
				opcao = scannerInt.nextInt();
				System.out.println();
				
				switch (opcao) {
				case 1:
					System.out.println("---");
					metodoPotenciaInverso(matriz, autovetorChute, erro);
					if (opcao != 0) {
						break;
					}
				}
				if (opcao != 0) {
					System.out.println("=> Pressione ENTER para continuar");
					scannerLine.nextLine();
				}
			} while (opcao != 0);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void metodoPotenciaInverso(Matrix matriz, double[] autovetorChute, double erro) throws Exception {
		System.out.println("=> Metodo da potencia inversa (encontra o menor autovalor)");
		if (matriz.getRowDimension() <= 4) {
			System.out.println("Chute inicial: ");
			MatrizUtil.exibirVetor(autovetorChute);
		}
		
		AutovalorAutovetor autovalorAutovetor = AutovaloresAutovetores.metodoPotenciaInverso(matriz, autovetorChute, erro);
		System.out.println("Autovalor: " + autovalorAutovetor.autovalor);
		System.out.println("Autovetor:");
		MatrizUtil.exibirVetor(autovalorAutovetor.autovetor);
	}
	
	public static void testar(Matrix matriz, AutovalorAutovetor autovalorAutovetor) {
		System.out.println("Calcula: (M * Autovetor) / Autovalor). Resultado deve ser igual ao autovetor");
		MatrizUtil.exibirMatriz(matriz.times(MatrizUtil.vetorParaMatrix(autovalorAutovetor.autovetor)).times(1.0 / autovalorAutovetor.autovalor));
	}
}