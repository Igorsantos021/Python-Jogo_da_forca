import random
from os import system

def escolher_palavra():
    palavras = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'php']
    return random.choice(palavras)

def mostrar_palavra(palavra ,letras_escolhidas):
    exibicao = ''
    for letra in palavra:
        if letra in letras_escolhidas:
            exibicao += letra
        else:
            exibicao += '_'
        
    return exibicao



def jogar():
    system('cls')
    palavra_secreta = escolher_palavra()
    tentativas_restante = 6
    letras_escolhidas = []

    print('''
   __     ______     ______     ______        ______   ______     ______     ______     ______    
  /\ \   /\  __ \   /\  ___\   /\  __ \      /\  ___\ /\  __ \   /\  == \   /\  ___\   /\  __ \   
 _\_\ \  \ \ \/\ \  \ \ \__ \  \ \ \/\ \     \ \  __\ \ \ \/\ \  \ \  __<   \ \ \____  \ \  __ \  
/\_____\  \ \_____\  \ \_____\  \ \_____\     \ \_\    \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
\/_____/   \/_____/   \/_____/   \/_____/      \/_/     \/_____/   \/_/ /_/   \/_____/   \/_/\/_/ 
                                                                                                  ''')
    
    print('Bem vindo ao Jogo da forca Tropa ')
    print('Advinhe a palavra secreta ')
    print(mostrar_palavra(palavra_secreta, letras_escolhidas))

    while tentativas_restante > 0:
        letra = input('Digite uma letra: ').lower()

        if len(letra) != 1 or letra.isnumeric():
            print('Por favor, digite apenas uma letra. ')
            continue

        if letra in letras_escolhidas:
            print('voce ja tentou essa letra. Tente outra')
            continue

        letras_escolhidas.append(letra)

        if letra not in palavra_secreta:
            tentativas_restante = tentativas_restante -1 #tentativas_restantes -= 1
            print('Letra incorreta, Voce tem {} tentativas restantes. '.format(tentativas_restante))
        else:
            print('Letra correta!')

        palavra_mostrar = mostrar_palavra(palavra_secreta, letras_escolhidas)
        print(palavra_mostrar)


        if  palavra_mostrar == palavra_secreta:
             print('Voce acertou!!')
             break
        
    if(tentativas_restante ==0 ):
        print('Voce perdeu.')


        
# 1- Verificar se a LETRA ja foi digitado
# 2- Criar um laço para o usuario continuar a jogar     
           
op = ''
while op.lower() != ' s ':
    jogar()

    op = input(' digite S para sair ')

    