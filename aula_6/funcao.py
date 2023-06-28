def funcao(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
dicionario = {'none': 'joao', 'idade':30} 
funcao(**dicionario)       