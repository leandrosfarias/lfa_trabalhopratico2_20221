def ler_gramatica(nome_arquivo: str) -> tuple:
    gramatica = open(f'{nome_arquivo}.txt', 'r')
    linhas = gramatica.readlines()
    variaveis = []
    terminais = []
    regras = []
    producoes = []
    for linha in linhas:
        variavel, producao = linha.split('=>')
        producoes.append(producao.strip().split('|'))
        variaveis.append(variavel)
        for c in producao:
            if str.islower(c):
                terminais.append(c)
        producao = producao.strip().split('|')
        for c in producao:
            regras.append([variavel, c])
    simbolo_inicial = variaveis[0]
    gramatica.close()
    return simbolo_inicial, variaveis, terminais, regras


gramatica = ler_gramatica('gramatica')


def print_info_gram(gramatica: tuple) -> None:
    print(f'Simbolo inicial: {gramatica[0]}')
    print(f'Variáveis: {gramatica[1]}')
    print(f'Terminais: {gramatica[2]}')
    print(f'Regras: {gramatica[3]}')


print_info_gram(gramatica)
