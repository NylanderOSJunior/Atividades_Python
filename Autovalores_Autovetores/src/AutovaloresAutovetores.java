import java.util.ArrayList;
import java.util.List;

import Jama.Matrix;

public class AutovaloresAutovetores {

	
	/**
	 * Calcula o menor autovalor (em módulo) e o autovetor correspondente de uma matriz
	 * @param matriz
	 * @param autovetorInicial
	 * @param erro
	 * @return
	 */
	public static AutovalorAutovetor metodoPotenciaInverso(Matrix matriz, double[] autovetorInicial, double erro) {
		/**
		 * Poderiamos aplicar o método da potência regular utilizando a matriz inversa,
		 * porém, fazendo alguns alterações nos passos, eliminamos a necessidade de
		 * calcular a matriz inversa. 
		 * Passos da potencia inverso:
		 * 1) Normaliza x0 = V/|V|
		 * 2) Yi = M^(-1)*Xi-1  =>  M*yi = Xi-1 (Achamos yi resolvendo o sistema pelo método LU, pois o xi-1 muda a cada iteração)
		 * 3) Xi = Yi/|Yi|
		 * 4) li = (T(Xi) * M^(-1) * Xi) / (T(Xi) * Xi
		 * Repetir 2 à 4 enquanto li - li-1 < E
		 * OBS.: Xi é o autovetor correspondente ao autovalor li. Yi é um vetor.
		 */
		double avalorAnterior;
		double avalorNovo = 0;
		int i = 0;
		
		//Passo 1:
		Matrix matrizVetorInicial = MatrizUtil.vetorParaMatrix(autovetorInicial);
		Matrix avetorX = MatrizUtil.normalizar(matrizVetorInicial);
		//Prepara as matriz L e U reaproveitadas no passo 2:
		DecomposicaoLU luMatriz = MatrizUtil.getLU(matriz);
		Matrix lowerMatriz = luMatriz.getL();
		Matrix upperMatriz = luMatriz.getU();
		
		//Passo 2:
		/* M*yi = xi-1  =>  L*U*yi = xi-1
		 * a) Fazendo U*yi = Z, resolvemos primeiro L*Z = xi-1
		 * b) Obtido o vetor Z, resolvemos U*yi = Z
		 */
		Matrix vetorZ = MatrizUtil.resolverSubstituicao(lowerMatriz, avetorX);
		Matrix vetorY = MatrizUtil.resolverRetrosubstituicao(upperMatriz, vetorZ);
		do {
			avalorAnterior = avalorNovo;
			//Passo 3:
			avetorX = MatrizUtil.normalizar(vetorY);
			
			//Calcula yi+1:
			/* M*yi = xi-1  =>  L*U*yi = xi-1
			 * a) Fazendo U*yi = Z, resolvemos primeiro L*Z = xi-1
			 * b) Obtido o vetor Z, resolvemos U*yi = Z
			 */
			vetorZ = MatrizUtil.resolverSubstituicao(lowerMatriz, avetorX);
			vetorY = MatrizUtil.resolverRetrosubstituicao(upperMatriz, vetorZ);
			
			//Passo 4:
			//li = (T(Xi) * M^(-1) * Xi) / (T(Xi) * Xi  =>  li = (T(Xi) * yi+1) / (T(Xi) * Xi)
			Matrix matrixTranspostaAvetor = avetorX.transpose();
			double avalorNumerador = matrixTranspostaAvetor.times(vetorY).get(0, 0); 
			double avalorDenominador = matrixTranspostaAvetor.times(avetorX).get(0, 0);
			avalorNovo = avalorNumerador / avalorDenominador;
			i++;
		} while (i == 1 || Math.abs(avalorNovo - avalorAnterior) > erro);

		AutovalorAutovetor autovalorAutovetor = new AutovalorAutovetor();
		autovalorAutovetor.autovalor = 1.0 / avalorNovo;
		autovalorAutovetor.autovetor = MatrizUtil.matrizParaVetor(avetorX);
		return autovalorAutovetor;
	}
	
}
