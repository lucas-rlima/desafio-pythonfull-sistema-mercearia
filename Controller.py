from DAO import CategoriaDao, ProdutoDao, EstoqueDao
from Models import Categoria, Produto, Estoque


class EstoqueController:
    @classmethod
    def salvar(cls, produto, quantidade):
        if produto != '' and quantidade != 0:
            try:
                EstoqueDao.salvar(Estoque(produto, quantidade))
            except Exception as error:
                print('Erro ao Cadastrar produto no estoque')
                print(error)
        else:
            print('Digite corretamente o nome e quantidade')

    @classmethod
    def ler(cls):
        arq = EstoqueDao.ler()
        for item in arq:
            print(f'Produto: {" ".join(map(str, item.split()[0:-1])):<20} '
                  f'{f'Quantidade: {item.split()[-1]}':>15}')


def frase_completa (lines, alteracao, frase1 = 'n', frase2 = 'n', frase3 = 'n', frase4 = 'n'):
    f1, f2, f3, f4 = alteracao, alteracao, alteracao, alteracao
    if frase1 == 's':
        f1 = (f'{" ".join(map(str, lines.split()[0:1]))} ')
    if frase2 == 's':
        f2 = (f'{" ".join(map(str, lines.split()[1:-2]))} ')
    if frase3 == 's':
        f3 = (f'{" ".join(map(str, lines.split()[-2:-1]))} ')
    if frase4 == 's':
        f4 = (f'{lines.split()[-1]}')

    return f1+f2+f3+f4


class ProdutoController:
    @classmethod
    def salvar(cls, codigo, nome, preco, categoria: Categoria):
        ProdutoDao.salvar(Produto(codigo, nome, preco, categoria))

    @classmethod
    def ler(cls):
        arq = ProdutoDao.ler()
        for lines in arq:
            print(f'Código: {" ".join(map(str, lines.split()[0:1])):<13} '
                  f'Produto: {" ".join(map(str, lines.split()[1:-2])):<16}'
                  f'Valor: {" ".join(map(str, lines.split()[-2:-1])):<10}'
                  f'{f'Categoria: {lines.split()[-1]}':>15}')
            
    @classmethod
    def alterar(cls):
        opcao = input('Você deseja alterar qual produto? Digite o código do produto: ')
        arq = ProdutoDao.ler()
        counter = 0 
        for index, lines in enumerate(arq):
            if lines.split()[0] == opcao :
                counter += 1
                print('Quais das seguintes informações você deseja alterar? \n'
                      f'1- Código: {" ".join(map(str, lines.split()[0:1])):<13} '
                      f'2- Produto: {" ".join(map(str, lines.split()[1:-2])):<16}'
                      f'3- Valor: {" ".join(map(str, lines.split()[-2:-1])):<10}'
                      f'{f'4- Categoria: {lines.split()[-1]}':>15}\n'
                      '(DIGITE O NÚMERO CORRESPONDENTE DA OPÇÃO)'
                      )
                opcao = int(input(''))

                while  opcao < 1 or opcao > 4:
                    print('Opção incorreta! Tente Novamente digitar o número da opção:')
                    opcao = int(input(''))

                confirmar = False

                if opcao == 1:
                    alteracao = input('Digite o novo Código: ') + ' '
                    frase = frase_completa(lines, alteracao, frase2 = 's', frase3 = 's', frase4 = 's' )
                    print(frase)
                    if input('Confirmar? S/N  ').lower() == 's':
                        ProdutoDao.alterar(index, frase)
                        confirmar = True

                elif opcao == 2:
                    alteracao = input('Digite o novo nome: ')+ ' '
                    frase = frase_completa(lines, alteracao, frase1 = 's', frase3 = 's', frase4 = 's' )
                    print(frase)
                    if input('Confirmar? S/N  ').lower() == 's':
                        ProdutoDao.alterar(index, frase)
                        confirmar = True

                elif opcao == 3:
                    alteracao = input('Digite o novo valor: ')+ ' '
                    frase = frase_completa(lines, alteracao, frase2 = 's', frase1 = 's', frase4 = 's' )
                    print(frase)
                    if input('Confirmar? S/N  ').lower() == 's':
                        ProdutoDao.alterar(index, frase)
                        confirmar = True

                elif opcao == 4:
                    alteracao = input('Digite a nova categoria: ')+ ' '
                    frase = frase_completa(lines, alteracao, frase2 = 's', frase3 = 's', frase1 = 's' )
                    print(frase)
                    if input('Confirmar? S/N  ').lower() == 's':
                        ProdutoDao.alterar(index, frase)
                        confirmar = True
                if confirmar:
                    print('Alteração feita com sucesso!')
                else:
                    print('Alteração não efetuada.')

        
        if counter == 0:
            print('Nenhum produto encontrado com esse código')

        
