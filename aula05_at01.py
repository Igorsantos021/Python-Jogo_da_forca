from os import system
system('cls')

def Soma(numero1, numero2):
    try:
        print('A soma dos numeros é {}'.format(float(numero1) + float(numero2)))
    except:
        print('Algo deu errado...')

def Subtrair(numero1, numero2):
    try:
        print('A subtrção dos numeros é {}'.format(float(numero1) - float(numero2)))
    except:
        print('Algo deu errado...')

def Multiplicacao(numero1, numero2):
    try:
        print('A Multiplicação dos numeros é {}'.format(float(numero1) * float(numero2)))
    except:
        print('Algo deu errado...')

def Divisao(numero1, numero2):
    try:
        print('A Divisão dos numeros é {}'.format(float(numero1) / float(numero2)))
    except ZeroDivisionError as error:
        print(error)    
    except:
        print('Algo deu errado ')


while True:
    num1 = (input('Digite o primeiro numero: '))
    num2 = (input('Digite o segundo numero: '))

    print('1. Soma')
    print('2. Subtrair')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Sair')

    opcao = int(input('Opçao: '))
    if opcao == 1:
        Soma(num1, num2)
    if opcao == 2:
        Subtrair(num1, num2)    
    if opcao == 3:
        Multiplicacao(num1, num2) 
    if opcao == 4:
        Divisao(num1, num2)
    if opcao == 5:
        break

