#importação de bibliotecas
import random
import string

#criação do laço de repetição
while True:
    
    #mensagem de boas vindas
    print('''================================================================      
          Bem vindo ao gerador de senha simples Vini.Pass\n
          
Apenas responda a pergunta abaixo, e automaticamente será gerada uma senha ExtForte para você.
Lembre- se de usar um Numeral inteiro para não haver erro no programa. Obrigado!! ^_^\n''')
    print('================================================================\n') 
    
    #criação de uma função para gerar senhas aleatórias
    def password_gen(len_pass = 8):
        letters_options = string.ascii_letters
        number_options = string.digits
        punct_options = string.punctuation
        options_pass = string.ascii_letters + string.digits + string.punctuation
    
        password_choice = ""
     
    #criação de um for para definição de cada caractére da senha de forma random
        for digit in range (0, len_pass):
            digit = random.choice(options_pass)
            password_choice += digit
        
        return password_choice
    
    #mensagem de interação com o usuário
    user_choice = input('Quantos digitos você deseja na sua senha?\n')
    
    #verificação simples do caractere digitado pelo usúario
    if user_choice.isdigit():
        user_choice = int(user_choice)
        main = password_gen(len_pass= user_choice)
        #mensagem final apresentada ao usuário SE ele passar na verifição
        print(f'\nSua senha é: \n{main}')
        print('\nObrigado por usar meu código/programa.')
        break
    else:
        #mensagem de erro SE NÃO houver hesito na verificação, fazendo o usuário voltar ao ínicio da interação
        print('Você digitou uma opção invalida, tente outra vez.')
    
    


          
    
