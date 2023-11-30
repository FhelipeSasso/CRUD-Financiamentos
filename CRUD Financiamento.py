class Financiamento:

    def __init__(self, valorImovel, prazoFinanciamento, taxaJurosAnual):
        self.valorImovel = valorImovel
        self.prazoFinanciamento = prazoFinanciamento * 12
        self.taxaJurosAnual = taxaJurosAnual


    def PagamentoMensal(self):
        PagamentoMensal = (self.valorImovel / self.prazoFinanciamento) * (1 + self.taxaJurosAnual / 12)
        return PagamentoMensal

    # falta implementar o pagamento total, taxa de juros e prazo de financiamento!
    
    def PagamentoTotal(self):
        pagamentoMensal = self.PagamentoMensal()
        pagamentoTotal = pagamentoMensal * self.prazoFinanciamento
        return pagamentoTotal

    
# subclasse Casa

class Casa(Financiamento):
    def __init__(self, valorImovel, prazoFinanciamento, taxaJurosAnual, taxaCasa):
          super().__init__(valorImovel, prazoFinanciamento, taxaJurosAnual)
          self._taxaCasa = taxaCasa

    def pgMensalCasa(self):
        PagamentoMensal = (self.valorImovel / self.prazoFinanciamento) * (1 + self.taxaJurosAnual / 12)
        return PagamentoMensal + self._taxaCasa
    
    def pgTotalCasa(self):
        PagamentoTotal = self.PagamentoMensal() * self.prazoFinanciamento
        return PagamentoTotal

# subclasse ap
class Apartamento(Financiamento):
    def __init__(self, valorImovel, prazoFinanciamento, taxaJurosAnual):
        super().__init__(valorImovel, prazoFinanciamento, taxaJurosAnual)

    def pgMensalApartamento(self):
        self._taxaMensal = self.taxaJurosAnual / 12
        self._numeroPagamentos = self.prazoFinanciamento * 12

        # Fórmula de pagamento mensal
        pagamentoMensal = (self.valorImovel * self._taxaMensal) / (1 - (1 + self._taxaMensal) ** -self._numeroPagamentos)
        return pagamentoMensal
    
    def pgTotalApartamento(self):
        PagamentoTotal = self.PagamentoMensal() * self.prazoFinanciamento
        return PagamentoTotal

# subclasse terreno
class Terreno(Financiamento):
    def __init__(self, valorImovel, prazoFinanciamento, taxaJurosAnual, taxaTerreno):
        super().__init__(valorImovel, prazoFinanciamento, taxaJurosAnual)
        self._taxaTerreno = 1.02
        
    def pgMensalTerreno(self):

        pagamentoMensal = self.PagamentoMensal() * self._taxaTerreno
        return pagamentoMensal
    
    def pgTotalTerreno(self):
        PagamentoTotal = self.PagamentoMensal() * self.prazoFinanciamento
        return PagamentoTotal

class InterfaceUsuario():
    @staticmethod
    def painel():
        print("\nOlá, bem-vindo ao sistema de financiamento de imóveis!")
        print("Qual operação deseja realizar hoje?")
        print("(1) Financiar Casa\n(2) Financiar Apartamento\n(3) Financiar Terreno")

    @staticmethod
    def operacoes(entrada):
        # dicionario
        armazenador = {}

        valor = float(input("Insira o valor do imóvel: \n"))
        prazo = int(input("Informe o prazo de financiamento: \n"))
        taxaJuros = float(input("Informe a taxa de Juros computada: \n"))

        # casa
        if entrada == 1:
            taxaCasa = 80
            financiamento = Casa(valor, prazo, taxaJuros, taxaCasa)
            armazenador['\nTipo do imóvel'] = 'Casa'
            armazenador['Valor do imóvel'] = f'R$ {valor}'
            armazenador['Prazo de Financiamento'] = f'R$ {prazo} anos'
            armazenador['Pagamento Mensal'] = f'R$ {financiamento.pgMensalCasa():.3f}'
            armazenador['Pagamento Total'] = f'R$ {financiamento.pgTotalCasa():.3f}'
            armazenador['Taxa fixa'] = taxaCasa

        # apartamento
        elif entrada == 2:
            # detalhe de pluralidade
            financiamento = Apartamento(valor, prazo, taxaJuros)
            armazenador['\nTipo do imóvel'] = 'Apartamento'
            armazenador['Valor do Imóvel'] = f'R$ {valor}'
            armazenador['Prazo de Financiamento'] = f'{prazo} anos'
            armazenador['Pagamento Mensal'] = f'R$ {financiamento.pgMensalApartamento():.3f}'
            armazenador['Pagamento Total'] = f'R$ {financiamento.pgTotalApartamento():.3f}'
            
        # terreno
        elif entrada == 3:
            taxaTerreno = 1.02
            financiamento = Terreno(valor, prazo, taxaJuros, taxaTerreno)
            armazenador['\Tipo do imóvel'] = 'Terreno'
            armazenador['Valor do imóvel'] = f'R$ {valor}'
            armazenador['Prazo de Financiamento'] = f'{prazo} anos'
            armazenador['Pagamento Mensal'] = f'R$ {financiamento.pgMensalTerreno():.3f}'
            armazenador['Pagamento Total'] = f'R$ {financiamento.pgTotalTerreno():.3f}'
            # detalhe de pluralidade

        # para o output sair referente a pluralidade

        if prazo == 1:
            prazo_str = f'{prazo} ano'
        else:
            prazo_str = f'{prazo} anos'
        armazenador['Prazo de Financiamento'] = prazo_str

        # output values

        for key, value in armazenador.items():
            print(f'{key}: {value}')

    @staticmethod
    def entrada():
        while True:
            entrada = int(input())
            if entrada <= 0 or entrada > 3:
                print("Entrada inválida. Por favor, tente novamente.")
            else:
                InterfaceUsuario.operacoes(entrada)
                break

class Main:
    interface = InterfaceUsuario()
    interface.painel()
    interface.entrada()
