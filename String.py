def inverte_palavra(palavra):
    novapalavra =''
    for silabas in range(len(palavra)-1, -1, -1):
        novapalavra = novapalavra + palavra[silabas]
    print(f'Palavra invertida é : {novapalavra}')


palavra = str(input('Digite algo : '))


inverte_palavra(palavra)




