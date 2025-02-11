from calculadora.Calculadora import Soma
from calculadora.Calculadora import Subtracao
from calculadora.Calculadora import Multiplicacao
from calculadora.Calculadora import Divisao
from calculadora.Calculadora import Elevado

def teste_Somar_para_dar_certo():
    assert Soma.soma(5,3) == 8

def teste_Somar_para_dar_errado():
    assert Soma.soma(5,5) == 9 #10

def teste_Subtrair_para_dar_certo():
    assert Subtracao.subtração(5,-8) == 13

def teste_Subtrair_para_dar_errado():
    assert Subtracao.subtração(10,1) == 11 #9

def teste_Multiplicar_para_dar_certo():
    assert Multiplicacao.multiplicação(3,-10) == -30

def teste_Multiplicar_para_dar_errado():
    assert Multiplicacao.multiplicação(20,2) == 10 #40

def teste_Dividir_inteiro_para_dar_certo():
    assert Divisao.divisão(4,2) == 2

def teste_Dividir_inteiro_para_dar_errado():
    assert Divisao.divisão(10,5) == 7 #2

def teste_Dividir_decimal_para_dar_certo():
    assert Divisao.divisão(12,5) == 2.4

def teste_Dividir_decimal_para_dar_errado():
    assert Divisao.divisão(49,4) == 13 #12,25