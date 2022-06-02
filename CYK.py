from Gramatica import Gramatica


def CYK(gramatica: Gramatica, palavra: str):
    tabela = [[set() for j in range(len(palavra) - i)] for i in range(len(palavra))]
    # passo 1
    for i in range(len(palavra)):
        if palavra[i] in gramatica.terminais:
            for regra in gramatica.regras:
                if regra[1] == palavra[i]:
                    tabela[0][i] = regra[0]
        else:
            print('não faz parte dos terminais')
    print(tabela)
