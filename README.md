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
Soma

Teste de soma correta: 5 + 3 = 8
Teste de soma com erro intencional para ilustrar falha: 5 + 5 = 10

Subtração

Teste de subtração correta: 5 - (-8) = 13
Teste de subtração com erro intencional para ilustrar falha: 10 - 1 = 11

Multiplicação

Teste de multiplicação correta: 3 * -10 = -30
Teste de multiplicação com erro intencional para ilustrar falha: 20 * 2 = 10

Divisão

Teste de divisão inteira correta: 4 / 2 = 2
Teste de divisão decimal correta: 12 / 5 = 2.4
Teste de divisão inteira com erro intencional para ilustrar falha: 10 / 5 = 7
Teste de divisão decimal com erro intencional para ilustrar falha: 49 / 4 = 13
Teste de divisão inteiro com erro intencional para ilustrar falha: 10 / 0 = 7

Exponenciação

Teste de exponenciação correta: 2 ^ 3 = 8
Teste de exponenciação com erro intencional para ilustrar falha: 2 ^ 0 = 0
Teste de exponenciação com erro intencional para ilustrar falha: 2 ^ (-1) = 0

### Executar os testes
Os testes unitários foram escritos usando pytest. Para executá-los, utilize o comando:
pytest 

ou

pytest --disable-warnings

### Considerações
Num primeiro momento a calculadora foi feita tendo a possibilidade de selecionar a operação desejada e declarar os valores por input, porém o pytest deu um erro os inputs e foi necessário retirar essa parte do código.


