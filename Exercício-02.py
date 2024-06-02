import random

#matriz criada no exercício 1
def gerar_Matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            sorteio_de_elementos = random.randint(1, 21)
            linha.append(sorteio_de_elementos)
        matriz.append(linha)
    return matriz


#função para imprimir matrizes
def imprimir_Matriz(matriz):
    for linha in matriz:
        print(linha)
        

linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))
matriz = gerar_Matriz(linhas,colunas)

print("\n------------MATRIZ------------")
imprimir_Matriz(matriz)
print(30*"-")