def main():

    bitola = float(input("Qual a bitola do Arame em milimetros?  \n"))
    while (bitola < 0):
         bitola = float(input("O valor inserido é negativo, favor inserir um valor maior que 0 \nQual a bitola do Arame em milimetros?  \n"))

#Calcular area 
    pi=3.14159
    A = (pi*(bitola**2)/4)*0.0000001
    #A= bitola*bitola

    print ("Área em metros quadrados: \n", A)
    escoamento = float(input("Qual limite de escoamento dos Arames em MPa? \n"))
    while (escoamento<0):
        escoamento = float(input("O valor inserido é negativo, favor inserir um valor maior que 0 \n Qual limite de escoamento dos Arames em MPa? \n"))
    elasticidade = float(input("Qual o módulo de elasticidade em GPa ? \n"))
    while (elasticidade<0):
        elasticidade = float(input("O valor inserido é negativo, favor inserir um valor maior que 0 \nQual o módulo de elasticidade em GPa ? \n"))

    #DISTANCIAS
    L4 = float(input("Qual e a distancia BD em metros? \n"))
    while (L4<0):
        L4 = float(input("O valor inserido é negativo, favor inserir um valor maior que 0 \nQual e a distancia BD em metros? \n"))
    L5 = float(input("Qual e a distancia DF em metros? \n"))
    while (L5<0):
            L5 = float(input("O valor inserido é negativo, favor inserir um valor maior que 0 \nQual e a distancia DF em metros? \n"))
    L6 = float(input("Qual e a distancia FG em metros? \n"))
    while (L6<0):
            L6 = float(input("O valor inserido é negativo, favor inserir um valor maior que 0 \nQual e a distancia FG em metros? \n"))

    #COMPRIMENTOS
    L1 = float(input("Qual e o comprimento AB em metros? \n"))
    while  (L1<0):
        L1 = float(input("O valor inserido é negativo, favor inserir um valor maior que 0 \nQual e o comprimento AB em metros? \n"))
    L2 = float(input("Qual e o comprimento CD em metros? \n"))
    while (L2<0):
        L2 = float(input("O valor inserido é negativo, favor inserir um valor maior que 0 \nQual e o comprimento CD em metros? \n"))
    L3 = float(input("Qual e o comprimento EF em metros? \n"))
    while (L3<0):
         L3 = float(input("O valor inserido é negativo, favor inserir um valor maior que 0 \nQual e o comprimento EF em metros? \n"))

    #CARGA DISTRIBUIDORA
    W = float(input("Qual o valor da carga distribuida W em N/m? \n"))
    while (W<0):
        W = float(input("O valor inserido é negativo, favor inserir um valor maior que 0 \nQual o valor da carga distribuida W em N/m? \n"))

    Frup= escoamento*A*(10**6)
    Fadm = Frup/1.5

    print ("A tensão Admissível é: ",Fadm)
    F1 = (W*L2*L3*(L4+L5+L6)**2)/(2*L1*((L3*L4)+(L2*L4)+(L2*L5)))
    F2 = (W*L3*(L4+L5+L6)**2)/(2*((L3*L4)+(L2*L4)+(L2*L5)))
    F3 = (W*L2*(L4+L5+L6)**2)/(2*(L3*L4)+(L2*L4)+(L2*L5))
    print ("\t F1: ",F1)
    print ("\t F2: ",F2)
    print ("\t F3: ",F3)
    if ((F1 or F2 or F3)>Fadm):
        print("Um ou mais dos arames ultrapassam a tensão admissível, dado o fator de segurança 1,5 \n")
    else:
        print ("A reação em A é ",F1," N \n")
        print ("A reação em C é ",F2," N \n")
        print ("A reação em E é ",F3," N \n")
        s3 = ((F3*L3)/(A*elasticidade))*(10**-12)
        if (s3>3):
            print("O valor utilizado para carga, os arames ultrapassam o deslocamento admitido em 3 milimetros")
        else:
            print("Os arames tem uma deformação de",s3," milimetros e os pontos B,D,F E G se deslocam nesta medida também")

print (">>>>>>>>>>>>>>>>> PROJETO 02 - RESISTÊNCIA DOS MATERIAIS <<<<<<<<<<<<<<<<< \n")
print ("Alunos: \n Antônio Igor Rodrigues Dourado \n Eduardo Dias Melo \n Eduardo Peixoto Vieira \n")
main()      
while (True):  
    #input("pressione Enter para Sair \n") 
    botao= int(input("Pressione 1 para realizar um novo cálculo ou 2 para SAIR \n "))
    if (botao==1):
        print("\n\n >>>>>>>>>>>>>>>>> NOVO CÁLCULO <<<<<<<<<<<<<<<<<")
        main()
    elif(botao==2):
        break
