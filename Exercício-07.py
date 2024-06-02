def dados_cadastrais():
    nome = input("Digite o nome: ")
    cpf = int(input("Digite o CPF: "))
    idade = int(input("Digite a idade: "))
    renda = float(input("Digite a renda mensal: "))
    return [nome, cpf, idade, renda]


def media_idade(pessoas_cadastradas):
    soma_idades = 0
    for pessoas in pessoas_cadastradas:
        soma_idades += pessoas[2]
    media_idade = soma_idades/len(pessoas_cadastradas)
    return media_idade


def media_renda(pessoas_cadastradas):
    soma_rendas = 0
    for pessoas in pessoas_cadastradas:
        soma_rendas += pessoas[3]
    media_renda = soma_rendas/len(pessoas_cadastradas)
    return media_renda


def cadastro():
    pessoas_cadastradas = []
    while True:
        pessoas = dados_cadastrais()
        pessoas_cadastradas.append(pessoas)
        print(40*"-")
        print("Você deseja cadastrar uma pessoa novamente?")
        print("Digite 1 para sim")
        print("Digite 2 para Não")
        print(40*"-")
        cadastrar_novamente = int(input("Digite a sua escolha: "))
        if cadastrar_novamente == 1:
            continue
        elif cadastrar_novamente == 2:
            print(40*"-")
            print("Até logo...")
            break
        else:
            print(40*"-")
            print("Opção inválida, digite novamente: ")
            print("Você deseja cadastrar uma pessoa novamente?")
            print("Digite 1 para sim")
            print("Digite 2 para Não")
            print(40*"-")
            cadastrar_novamente = int(input("Digite a sua escolha: "))
            
    print("\n---------- Pessoas Cadastradas ----------")
    for pessoas in pessoas_cadastradas:
        print(pessoas)
    print(40*"-")
    print(f"A média da idade é: {media_idade(pessoas_cadastradas)}")
    print(f"A média da renda mensal é: {media_renda(pessoas_cadastradas)}")
    print(40*"-")


cadastro()