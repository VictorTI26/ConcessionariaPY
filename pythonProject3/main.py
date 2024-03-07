from Concessionaria import Carro, Moto, Cliente,Concessionaria

carro1 = Carro("Toyota", "Corolla", 2022, 85000, 4, "Gasolina")
moto1 = Moto("Honda", "CB 500F", 2021, 30000, 500, "Elétrica")

cliente1 = Cliente("Alice", "Silva", "9999-9999")

concessionaria = Concessionaria()
concessionaria.adicionar_veiculo(carro1)
concessionaria.adicionar_veiculo(moto1)

print("Veículos disponíveis para venda:")
for veiculo in concessionaria.listar_veiculos_disponiveis():
    print(veiculo.exibir_informacoes())

print(concessionaria.vender_veiculo(carro1, cliente1))
print(concessionaria.vender_veiculo(moto1, cliente1))