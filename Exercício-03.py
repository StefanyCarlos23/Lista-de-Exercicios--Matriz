import random
# Utilizei as funções criadas nos exercícios anteriores
# para fazer o teste da nova função
def gerar_Matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            sorteio_de_elementos = random.randint(1, 21)
            linha.append(sorteio_de_elementos)
        matriz.append(linha)
    return matriz


def imprimir_Matriz(matriz):
    for linha in matriz:
        print(linha)


#Função para retornar a soma dos elementos pares da matriz
def somaPar():
    soma = 0
    for linha in matriz:
        for elemento in linha:
            if elemento  %2 == 0:
                soma += elemento
    return soma


linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))
matriz = gerar_Matriz(linhas, colunas)

print("\n------------MATRIZ------------")
imprimir_Matriz(matriz)
print(30*"-")

somapar = somaPar()
print(50*"-")
print(f"O resultado da soma dos elementos pares é: {somapar}")
print(50*"-")