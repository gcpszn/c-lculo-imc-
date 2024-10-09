class Pessoa:
    def __init__(self, nome, peso, altura):
        """Inicializa uma pessoa com nome, peso e altura."""
        self.nome = nome
        self.peso = peso
        self.altura = altura
    
    def calcular_imc(self):
        """Calcula o IMC e retorna a classificação."""
        imc_valor = self.peso / (self.altura ** 2)
        
        # Classificação do IMC
        if imc_valor < 18.5:
            class_imc = 'Abaixo do peso'
        elif 18.5 <= imc_valor <= 24.9:
            class_imc = 'Peso normal'
        elif 25.0 <= imc_valor <= 29.9:
            class_imc = 'Sobrepeso'
        else:
            class_imc = 'Obesidade'
        
        return f'{self.nome}, o seu IMC é {imc_valor:.1f}, classificado como {class_imc}.'

def entrada_valor_positivo(mensagem):
    """Recebe um valor positivo do usuário, garantindo que a entrada seja válida."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print('Erro: insira um valor maior que zero.')
        except ValueError:
            print('Erro: insira um número válido.')

# Coleta as informações do usuário
nome = input('Digite seu nome: ')
peso = entrada_valor_positivo('Digite seu peso em kg: ')
altura = entrada_valor_positivo('Digite sua altura em metros (ex: 1.75): ')

# Cria um objeto da classe Pessoa
pessoa = Pessoa(nome, peso, altura)

# Exibe o resultado do cálculo do IMC
print(pessoa.calcular_imc())
