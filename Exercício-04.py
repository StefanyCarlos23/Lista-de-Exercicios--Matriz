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


#Funcão para somar os elementos da coluna
def soma_coluna(matriz, coluna):
    soma = 0
    for linha in matriz:
        soma += linha[coluna]
    return soma


linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))
matriz = gerar_Matriz(linhas, colunas)

print("\n------------MATRIZ------------")
imprimir_Matriz(matriz)
print(30*"-")

num_coluna = int(input("Digite o número da coluna que você deseja somar os elementos: "))

while num_coluna > colunas or num_coluna <0:
    print(30*"-")
    print("O número da coluna que você digitou é diferente do número de colunas existentes na matriz. Digite novamente! ")
    num_coluna = int(input("Digite o número da coluna que você deseja somar os elementos: "))

somacolunas = soma_coluna(matriz, num_coluna)

print(30*"-")
print(f"O resultado é: {somacolunas}")
print(30*"-")