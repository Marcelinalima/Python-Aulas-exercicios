def teste(arg, *args):
    print('argumento normal: {}'.format(arg))
    for arg in args:
        print('outro argumento: {}'.format(arg))
teste("python","É",  "melhor que", "java")        