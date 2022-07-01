def fibonacci(digito):
    primeiro_digito = 0
    segundo_digito = 1

    print(primeiro_digito, segundo_digito, end=' ')

    while segundo_digito < digito:
        soma_digitos = primeiro_digito + segundo_digito
        print(soma_digitos, end=' ')
        primeiro_digito = segundo_digito
        segundo_digito = soma_digitos
    if segundo_digito == digito:
        print()
        print('Digito informado pertence a sequencia')
    else:
        print('Nao pertence')


print('-=' * 20, '\nSEQUENCIA DE FIBONACCI', )
print('Verifica se o numero pertence a sequencia de FIBONACCI')
print('-=' * 20)

while True:
    try:
        digito = int(input('Digite o numero : '))
        fibonacci(digito)
        break
    except ValueError:
        print('Voce digitou um valor errado tente novamente')
