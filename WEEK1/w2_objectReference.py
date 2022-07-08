class Carro:
    pass

meu_carro    = Carro()
carro_do_ime = Carro()

meu_carro.ano    = 1968
meu_carro.modelo = 'Fusca'
meu_carro.cor    = 'azul'

carro_do_ime.ano    = 1981
carro_do_ime.modelo = 'Brasília'
carro_do_ime.cor    = 'amarelo'


def myPrint(name, var):
    print("{} = {}".format(name, var))

myPrint('ano',    meu_carro.ano)
myPrint('modelo', meu_carro.modelo)
myPrint('cor',    meu_carro.cor)

myPrint('ano',    carro_do_ime.ano)
myPrint('modelo', carro_do_ime.modelo)
myPrint('cor',    carro_do_ime.cor)

novo_fusca      = meu_carro ## Duas varáveis apontando para o mesmo objeto
novo_fusca.ano += 10
myPrint('ano', meu_carro.ano)

