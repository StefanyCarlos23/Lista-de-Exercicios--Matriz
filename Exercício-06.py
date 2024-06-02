import random

def gerar_Matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            if i < j:
                elemento = 2*i + 7*j
            elif i == j:
                elemento = 3*i**2 + 1
            else:
                elemento = 4*i**3 + 5*j**2 + 1
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimir_Matriz(matriz):
    for linha in matriz:
        print(linha)

matriz = gerar_Matriz(10, 10)

print("\n--------------------------MATRIZ--------------------------\n")
imprimir_Matriz(matriz)
print(60*"-")