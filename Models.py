from datetime import datetime
class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produto:
    def __init__(self, codigo, nome, preco, categoria: Categoria):
        self.codigo = codigo
        self.nome = nome 
        self.preco = preco 
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Pessoa:
    def __init__(self, nome, idade, cpf, endereco):
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf 
        self.endereco = endereco 

class Funcionario(Pessoa):
    def __init__(self, clt, nome, idade, cpf, endereco):
        self.clt = clt
        super().__init__(nome, idade, cpf, endereco)
        
class Fornecedor:
    def __init__(self, nome, cnpj, endereco):
        self.nome = nome 
        self.cnpj = cnpj 
        self.endereco = endereco 

class Venda:
    def __init__(self, produto: Produto, vendedor, cliente, quantidade_vendida, data = datetime.now()):
        self.produto = produto
        self.vendedor = vendedor 
        self.cliente = cliente
        self.quantidade_vendida = quantidade_vendida
        self.data = data