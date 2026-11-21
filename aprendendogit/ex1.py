from random import randint

sorte=randint(0,10)


try:

    usuario=int(input('digite um numero'))

    if usuario== sorte:
        print('voce ganhou')

    else:
        print('voce perdeu')

except ValueError:
    print('voce nao colocou um numero valido')