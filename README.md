# Unit-Tests
Trabalho feito para a disciplina de engenharia de software 1 - Testes de Unidade (Unit Tests).

Esse projeto consiste na implementação em Python de uma calculadora simples, com as funcionalidades de soma, subtração, multiplicação, divisão e exponenciação. Foram elaborados testes unitários automatizados com o pytest para garantir o funcionamento das funções.

Versão do python utilizado - 3.13.2

## Percurso do trabalho

### instalar o python: 
pip install pytest

### Implementar as funcionalidades da calculadora
As funcionalidades foram implementadas de forma simples, pois o foco está no aprendizado da ferramenta pytest.

### Implementar os testes para as classes
__Soma__

Teste de soma correta: 5 + 3 = 8
Teste de soma com erro intencional para ilustrar falha: 5 + 5 = 10

__Subtração__

Teste de subtração correta: 5 - (-8) = 13
Teste de subtração com erro intencional para ilustrar falha: 10 - 1 = 11

__Multiplicação__

Teste de multiplicação correta: 3 * -10 = -30
Teste de multiplicação com erro intencional para ilustrar falha: 20 * 2 = 10

__Divisão__

Teste de divisão inteira correta: 4 / 2 = 2
Teste de divisão decimal correta: 12 / 5 = 2.4
Teste de divisão inteira com erro intencional para ilustrar falha: 10 / 5 = 7
Teste de divisão decimal com erro intencional para ilustrar falha: 49 / 4 = 13
Teste de divisão inteiro com erro intencional para ilustrar falha: 10 / 0 = 7

__Exponenciação__

Teste de exponenciação correta: 2 ^ 3 = 8
Teste de exponenciação com erro intencional para ilustrar falha: 2 ^ 0 = 0
Teste de exponenciação com erro intencional para ilustrar falha: 2 ^ (-1) = 0

### Executar os testes
Os testes unitários foram escritos usando pytest. Para executá-los, utilize o comando:
__pytest__ ou __pytest --disable-warnings__

### Considerações
Num primeiro momento a calculadora foi feita tendo a possibilidade de selecionar a operação desejada e declarar os valores por input, porém o pytest deu um erro os inputs e foi necessário retirar essa parte do código.

Posteriormente foi notado que se deixar o arquivo __test_calculadora.py__ fora da pasta teste não haverá problemas nos comandos de execução de teste, porém se o arquivo estiver dentro da pasta __tests__ é necessário colocar um inicializador dentro da pasta, sendo o arquivo "__unit__.py""
