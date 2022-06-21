import json
def gaussJacobi(valorIn, maxInte, tol):
    if (maxInte == 0):
        for i in valorIn:
            print(i)
    aux = []
    for i in range(len(valorMatriz)):
        aux.append(0)
    for L in range(len(valorMatriz)):
        # Pega o ultimo item de cada linha do Vetor.
        for C in range(len(valorMatriz)):
            if (L != C):
                aux[L] = aux[L] + (valorMatriz[L][C] * valorIn[C])
    for L in range(len(valorMatriz)):
        for C in range(len(valorMatriz)):
            if (L == C):
                # Divide o valor pela diagonal
                aux[L] = ((valorMatriz[L][len(valorMatriz)] - aux[L]) /
                          valorMatriz[L][C])  
    tolerancia = True
    aux2 = 0
    for L in range(len(aux)):
        print("|",'X{:>2d} = {:>9.4f}  ||  E{:>2d} = {:>9.4f}'.format(
            L + 1, aux[L], L + 1, abs(aux[L] - valorIn[L])),"|")
        if (abs(aux[L] - valorIn[L]) >= aux2):
            aux2 = abs(aux[L] - valorIn[L])
    if (aux2 <= tol):
        tolerancia = False
    print('-----------------------------------')
    if (tolerancia == True):
        gaussJacobi(aux, maxInte - 1, tol)
    else:
        print("Valores Finais")
        for I in range(len(aux)):
            print('X{:>2d} = {:>9.4f}'.format(I + 1, aux[I]))
nomeArquivo = input("Digite o arquivo da Matriz: ")
try:
    with open(nomeArquivo) as f:
        arquivo = json.load(f)
except:
    print("\n\n Arquivo não encontrado ou com erro \n\n")
    exit()
valorIn = []
valorMatriz = arquivo['matriz']
tole = input("Digite o valor da tolerancia: ")
tol = float(tole)
MaxIn = input("Digite o maximo de interacoes: ")
MaxInte= int(MaxIn)
for i in range(len(valorMatriz)):
    valorIn.append(0)
verificador = True
# Verifica se cumpre o criterio da convergencia
for L in range(len(valorMatriz) - 1):
    soma = 0
    diagonal = 0
    for C in range(len(valorMatriz)):
        if (L != C):
            soma += abs(valorMatriz[L][C])
        if (L == C):
            diagonal = valorMatriz[L][C]
    if (soma > diagonal):
        verificador = False
if verificador == True:
    gaussJacobi(valorIn, MaxInte, tol)
else:
    print("Matriz não tem garantia de convergencia")
