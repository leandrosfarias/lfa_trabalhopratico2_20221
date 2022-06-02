def ler_gramatica(nome_arquivo: str) -> tuple:
    gramatica = open(f'{nome_arquivo}.txt', 'r')
    linhas = gramatica.readlines()
    nao_terminais = []
    terminais = []
    regras = []
    producoes = []
    for linha in linhas:
        variavel, producao = linha.split('=>')
        producoes.append(producao.strip().split('|'))
        nao_terminais.append(variavel)
        for c in producao:
            if str.islower(c):
                terminais.append(c)
        producao = producao.strip().split('|')
        for c in producao:
            regras.append([variavel, c])
    simbolo_inicial = nao_terminais[0]
    gramatica.close()
    return simbolo_inicial, nao_terminais, terminais, regras


gramatica = ler_gramatica('gramatica')


def print_info_gram(gramatica: tuple) -> None:
    print(f'Simbolo inicial: {gramatica[0]}')
    print(f'nao_terminais: {gramatica[1]}')
    print(f'Terminais: {gramatica[2]}')
    print(f'Regras: {gramatica[3]}')


print_info_gram(gramatica)
