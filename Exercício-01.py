import random

def gerar_Matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            sorteio_de_elementos = random.randint(1, 21)
            linha.append(sorteio_de_elementos)
        matriz.append(linha)
    return matriz

linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))
matrizes = gerar_Matriz(linhas, colunas)

print("\n---------------------------MATRIZ---------------------------\n")
print(matrizes)
print(60*"-")