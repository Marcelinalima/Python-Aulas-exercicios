def teste_args_kwargs(arg1, arg2, arg3):
    print("arg1", arg1)
    print("arg2", arg2)
    print("arg3", arg3)

dicionario ={'arg3': 6, 'arg1':'dois','arg2':2 }
teste_args_kwargs(**dicionario)
 