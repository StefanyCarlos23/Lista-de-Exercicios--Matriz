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


#Função para somar os elementos da linha
def soma_linha(matriz, linha):
    soma = 0
    for elemento in matriz[linha]:
        soma += elemento
    return soma


linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))
matriz = gerar_Matriz(linhas, colunas)

print("\n------------MATRIZ------------")
imprimir_Matriz(matriz)
print(30*"-")

num_linha = int(input("Digite o número da linha que você deseja somar os elementos: "))  

while num_linha > linhas or num_linha <0:
    print(30*"-")
    print("O número da linha que você digitou é diferente do número de linhas existentes na matriz. Digite novamente! ")
    num_linha = int(input("Digite o número da linha que você deseja somar os elementos: "))  

somalinhas = soma_linha(matriz, num_linha)

print(30*"-")
print(f"O resultado é: {somalinhas}")
print(30*"-")