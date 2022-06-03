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
        # print(f'valor de n: {n}')
        # print(f'valor de i: {i}')
        for j in range(n - i + 1):
            # print(f'valor de n: {n}')
            # print(f'valor de i: {j}')
            print(n - i + 1)
            for k in range(j - 1):
                for regra in gramatica.regras:
                    if re.match('^[A-Z]{2}$', regra[1]):
                        pass
                        # Y = tabela[k][j]
                        # Z = regra[i - k, j + k]
                        # r = Y + Z
                        # if r in gramatica.regras:
                        #     tabela[i][j] = r
                        # tabela[i][j] = '-'



