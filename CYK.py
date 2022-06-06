from Gramatica import Gramatica
import re


def CYK(gramatica: Gramatica, palavra: str):
    tabela = [[set() for j in range(len(palavra) - i)] for i in range(len(palavra))]
    n = len(palavra)
    # passo 1
    for j in range(n):
        if palavra[j] in gramatica.terminais:
            for regra in gramatica.regras:
                if regra[1] == palavra[j]:
                    tabela[0][j] = regra[0]
        else:
            print('Não faz parte do alfabeto.')
            break
    # print(tabela)
    #
    for i in range(1, n):
        # print(f'i == {i}')
        for j in range(n - 2 - i + 1):
            # print(f'n == {n}')
            # print(f'n - 2 - i + 1 == {n - 2 - i + 1}')
            for k in range(i - 1):
                for regra in gramatica.regras:
                    if re.match('^[A-Z]{2}$', regra[1]):
                        Y = tabela[k][j]
                        Z = tabela[i - k]
                        print(f'Y == {Y} e Z == {Z}')
