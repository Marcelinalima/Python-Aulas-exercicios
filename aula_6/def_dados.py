#função dados
#idade=None, quando o parametro é none é opcional nao vai receber nada 
def dados(nome, idade=None):
    if idade is not None:
     return('nome: {}\nidade: {} anos'.format(nome,idade))
    else:
        return('nome:{}\nidade não informada'.format(nome))
#chamamos a função dados      
print(dados('Marcelina','40'))      