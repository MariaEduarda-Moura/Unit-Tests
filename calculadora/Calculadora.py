class Soma:
    def soma(num1,num2):
        som = float(num1)+float(num2)
        return som

class Subtracao:
    def subtração(num1,num2):
        sub = float(num1)-float(num2)
        return sub

class Multiplicacao:
    def multiplicação(num1, num2):
        mult = float(num1)*float(num2)
        return mult

class Divisao:
    def divisão(num1,num2):
        div = float(num1)/float(num2)
        return div

class Elevado:
    def elevado(num1,num2):
        elev = float(num1)**float(num2)
        return elev

#print("Qual operação você deseja fazer?\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Elevado")
#operação = int(input())
#if operação == 1:
#    print("Digite os valores:")
#    numero1 = float(input())
#    numero2 = float(input())
#    print(f"Soma de {numero1} e {numero2} = {Soma(numero1,numero2)}")
#elif operação == 2:
#    print("Digite os valores:")
#    numero1 = float(input())
#    numero2 = float(input())
#    print(f"Subtração de {numero1} e {numero2} = {Subtracao(numero1,numero2)}")
#elif operação == 3:
#    print("Digite os valores:")
#    numero1 = float(input())
#    numero2 = float(input())
#    print(f"Multiplicação de {numero1} e {numero2} = {Multiplicacao(numero1,numero2)}")
#elif operação == 4:
#    print("Digite os valores:")
#    numero1 = float(input())
#    numero2 = float(input())
#    print(f"Divisão de {numero1} e {numero2} = {Divisao(numero1,numero2):.2f}")
#elif operação == 5:
#    print("Digite o valor:")
#    numero1 = float(input())
#    numero2 = float(input())
#    print(f"{numero1} elevado a {numero2} = {Elevado(numero1,numero2)}")