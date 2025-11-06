listaPessoas = []

def cadastraUseuario(usuario):
    listaPessoas.append(usuario)

def atenderUsuario():
    ultimo = len(listaPessoas)
    nomeUltimaPessoa = listaPessoas[ultimo]
    listaPessoas.remove(ultimo)

    return nomeUltimaPessoa

def mostraLista():
    contador = 1
    for i in listaPessoas:
        print(f'{contador}. {i} \n')
        contador +=1

