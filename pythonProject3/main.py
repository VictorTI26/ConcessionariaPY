from Concessionaria import Concessionaria, Cliente, Carro, Moto
while True:
    print("Bem-vindo à concessionária")
    print("1- Carro\n2- Moto\n3- Cadastro de usuário")
    escolha = int(input("Digite o número correspondente à sua escolha: "))

    if escolha == 0:
        exit()

    def adicionarCarro():
        print("-------------------------------------Carro-------------------------------------")

        marca_carro = input("Digite a marca do carro: ")
        modelo_carro = input("Digite o modelo do carro: ")
        ano_carro = int(input("Digite o ano do carro: "))
        preco_carro = float(input("Digite o preço do carro: "))
        num_portas_carro = int(input("Digite o número de portas do carro: "))
        combustivel_carro = input("Digite o tipo de combustível do carro: ")

        carro1 = Carro(marca_carro, modelo_carro, ano_carro, preco_carro, num_portas_carro, combustivel_carro)
        return carro1
    def adicionarMoto():
        print("-------------------------------------Moto-------------------------------------")

        marca_moto = input("Digite a marca da moto: ")
        modelo_moto = input("Digite o modelo da moto: ")
        ano_moto = int(input("Digite o ano da moto: "))
        preco_moto = float(input("Digite o preço da moto: "))
        cilindrada_moto = int(input("Digite a cilindrada da moto: "))
        partida_moto = input("Digite o tipo de partida da moto: ")

        moto1 = Moto(marca_moto, modelo_moto, ano_moto, preco_moto, cilindrada_moto, partida_moto)
        return moto1

    def cadastrarUsuario():
        print("-------------------------------------Usuário-------------------------------------")

        nome_cliente = input("Digite o nome do cliente: ")
        sobrenome_cliente = input("Digite o sobrenome do cliente: ")
        telefone_cliente = input("Digite o telefone do cliente: ")

        cliente1 = Cliente(nome_cliente, sobrenome_cliente, telefone_cliente)
        return cliente1

    switch_case = {
        1: adicionarCarro,
        2: adicionarMoto,
        3: cadastrarUsuario,
    }

    if escolha in switch_case:
        item_selecionado = switch_case[escolha]()
    else:
        print("Opção inválida.")

    if isinstance(item_selecionado, (Carro, Moto)):
        concessionaria = Concessionaria()
        concessionaria.adicionar_veiculo(item_selecionado)

        print("\nVeículos disponíveis para venda:")
        for veiculo in concessionaria.listar_veiculos_disponiveis():
            print(veiculo.exibir_informacoes())

        print(concessionaria.vender_veiculo(item_selecionado, cadastrarUsuario()))
