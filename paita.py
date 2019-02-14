'''
Objetivo: Gerar um numero aleatório e comparar com a entrada do usuario.
entrada: 3 numeros inteiros ( chutes ).
saida: Resultado.Acertando ou não.
'''

#jogo da advinhação


from random  import randint



print("!!!BEM VINDO AO JOGO DE ADVINHAÇÃO!!!")
print("*************************************")


def querer():

    escolha=input("Você deseja continuar? Y/N ") 
    quer= escolha == "y"
    nao_quer: escolha == "n"

    if (escolha == "y")or (escolha == "Y"):
        jogar()
      
        
    if (escolha == "n") or (escolha == "n"):
        print("Obrigado por jogar")
        input("Aperte qualquer tecla para sair")
     
            
   
def jogar():
    
    segredo=randint(1,100)
    pontuacao = 500
    score=0
    

    for tentativas in range (1,11):
        numero=101
        while numero>=100 or numero>=1:
            numero=int(input("Digite um numero de 1 a 10  Tentativa {} : " .format(tentativas) ) )

            if numero>100 or numero <0 :
                print("************************************")
                print("*********NUMERO INVÁLIDO************")
                print("************************************")



        
        acertou = numero == segredo
        acima   = numero > segredo
        abaixo  = numero < segredo
        invalido1 = numero < 1
        invalido2 = numero >100
            
        if(acertou):
            print("**************")
            print("Você acertou!!")
            print("**************")
            print("Sua pontuacao foi", pontuacao)
            break
        
        if (acima):
            score= numero-segredo
            pontuacao= pontuacao-score
            print("************************************")
            print("*Seu numero foi maior que o segredo*")
            print("************************************")
            
        if (abaixo):
            score= segredo-score
            pontuacao=pontuacao-score
            print("************************************")
            print("*Seu numero foi menor que o segredo*")
            print("************************************")

    if  (acertou == False):
        print("Seu numero era :",segredo)
        print("Você não pontuou")

    querer()
    

jogar()