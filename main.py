#Calculadora de IMC

#Declarando a função da calculadora
def calculadoraimc():
    
#Condição para identificar se usuario deseja continuar
    while True:
        #Entrada de dados do usúario:
        print("Seja bem-vindo a Calculadora IMC")
        peso = float(input("Qual seu peso atual em kg ? "))
        altura = float(input("Qual sua altura em metros ? "))

        #Função de calculo da IMC
        def imc(peso,altura):     
            imc = peso/(altura*altura)
            imc = round(imc,2)
            return imc
            
            
        #Função para classificar o imc de acordo com resultado.
        def classificar_imc(imc):   
            print(f"O Imc é igual a:",imc)
            if (imc <18.5):
                print("Abaixo do Peso")
            elif(imc<=24.9):
                print("Peso Normal")
            elif(imc<=29.9):
                print("Sobrepeso")
            else:
                print("Obesidade")
            
        #Chamada da função de calculo do IMC   
        imc_user = imc(peso,altura)
        
        #Chamada da Função de Classificação
        classificar_imc(imc_user)

        #Função de finalização ou recomeço da calculadora
        resposta = input("Deseja calcular novamente o IMC (s/n)? ").lower()
        if resposta !="s":
            print("Obrigado por usar nossa calculadora")
            break
    

#Chamada da função imc -> 
calculadoraimc()
        



