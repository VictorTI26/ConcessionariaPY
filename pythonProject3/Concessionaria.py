class Veiculo:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def exibir_informacoes(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - R$ {self.preco:.2f}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, preco, num_portas, combustivel):
        super().__init__(marca, modelo, ano, preco)
        self.num_portas = num_portas
        self.combustivel = combustivel

    def exibir_informacoes(self):
        return super().exibir_informacoes() + f", {self.num_portas} portas, {self.combustivel}"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, preco, cilindrada, partida):
        super().__init__(marca, modelo, ano, preco)
        self.cilindrada = cilindrada
        self.partida = partida

    def exibir_informacoes(self):
        return super().exibir_informacoes() + f", {self.cilindrada}cc, {self.partida}"

class Cliente:
    def __init__(self, nome, sobrenome, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone

class Concessionaria:
    def __init__(self):
        self.veiculos_disponiveis = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos_disponiveis.append(veiculo)

    def remover_veiculo(self, veiculo):
        if veiculo in self.veiculos_disponiveis:
            self.veiculos_disponiveis.remove(veiculo)

    def listar_veiculos_disponiveis(self):
        return self.veiculos_disponiveis

    def vender_veiculo(self, veiculo, cliente):
        if veiculo in self.veiculos_disponiveis:
            self.veiculos_disponiveis.remove(veiculo)
            return f"Veículo {veiculo.modelo} vendido para {cliente.nome} {cliente.sobrenome}"
        else:
            return "Veículo não disponível"