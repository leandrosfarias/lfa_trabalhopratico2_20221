class Gramatica:
    def __init__(self, nome_arquivo: str):
        self.nao_terminais = []
        self.terminais = []
        self.regras = []
        with open(f'{nome_arquivo}.txt', 'r') as arquivo:
            arquivo = arquivo.read().splitlines()
        self.simbolo_inicial = arquivo[0][0]
        for linha in arquivo:
            variavel, producao = linha.split(' => ')
            self.nao_terminais.append(variavel)
            producao = producao.strip().split(' | ')
            for c in producao:
                if str.islower(c):
                    self.terminais.append(c)
                self.regras.append([variavel, c])

    def print_info(self):
        print(f'Simbolo incicial: {self.simbolo_inicial}')
        print(f'Não terminais: {self.nao_terminais}')
        print(f'Terminais: {self.terminais}')
        print(f'Regras: {self.regras}')


# g = Gramatica('gramatica')
# g.print_info()
