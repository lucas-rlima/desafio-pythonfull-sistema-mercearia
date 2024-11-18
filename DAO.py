from Models import Produto, Estoque, Categoria

class CategoriaDao:
    @classmethod
    def salvar(cls, categoria: Categoria):
        with open('categorias.txt', 'a') as arq:
            arq.write(categoria.categoria + '\n')
    
    @classmethod
    def ler(cls):
        with open('categorias.txt', 'r') as arq:
            return arq.readlines()
    @classmethod   
    def excluir(cls, line):
        with open('categorias.txt', 'r') as arq:
            content = arq.readlines()
        
        content[line] = ''

        with open('categorias.txt', 'w') as arq:
            arq.writelines(content)

    @classmethod
    def alterar(cls,newcontent, index):
        with open('categorias.txt', 'r') as arq:
            content = arq.readlines()
        
        content[index] = newcontent + '\n'
        with open('categorias.txt', 'w') as arq:
            arq.writelines(content)

class ProdutoDao:

    @classmethod
    def salvar(cls, produto: Produto):
        with open('produtos.txt', 'a') as arqprod:
            arqprod.write(str(produto.codigo) + ' ' + produto.nome + ' ' 
                          + str(produto.preco) + ' ' + str(produto.categoria) +' \n')
    

    @classmethod
    def ler(cls):
        with open('produtos.txt', 'r') as arqprod:
            return arqprod.readlines()
        
    @classmethod
    def alterar(cls, index, conteudo):
        with open('produtos.txt', 'r') as arqprod:
            temporario = arqprod.readlines()

        temporario[index] = conteudo + '\n'

        with open('produtos.txt', 'w') as arq:
            arq.writelines(temporario)

    @classmethod
    def remover(cls, index):
        with open('produtos.txt', 'r') as arq:
            temporario = arq.readlines()
        
        temporario[index] = ''

        with open('produtos.txt', 'w') as arq:
            arq.writelines(temporario)




class EstoqueDao:
    @classmethod
    def salvar(cls, estoque: Estoque):
        with open('estoque.txt', 'a') as arq:
            arq.write(estoque.produto + ' ' + str(estoque.quantidade)+ '\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            return arq.readlines()

    @classmethod
    def alterar(cls, estoque: Estoque):
        with open('estoque.txt', 'w') as arq:
            arq.write(estoque.produto + ' ' + str(estoque.quantidade))

