# Unit-Tests
Trabalho feito para a disciplina de engenharia de software 1 - Testes de Unidade (Unit Tests).
Esse projeto consiste na implementação em Python de uma calculadora simples, com as funcionalidades de soma, subtração, multiplicação, divisão e exponenciação. Foram elaborados testes unitários automatizados com o pytest para garantir o funionamento das funções.

Versão do python utilizado - 3.13.2

## Percurso do trabalho

### instalar o python: 
pip install pytest

Testes Implementados
Os seguintes cenários foram testados:

Soma
Teste de soma correta: 5 + 3 = 8
Teste de soma com erro intencional para ilustrar falha.
Subtração

Teste de subtração correta: 5 - (-8) = 13
Teste de subtração com erro intencional para ilustrar falha.
Multiplicação

Teste de multiplicação correta: 3 * -10 = -30
Teste de multiplicação com erro intencional para ilustrar falha.
Divisão

Teste de divisão inteira correta: 4 / 2 = 2
Teste de divisão decimal correta: 12 / 5 = 2.4
Testes com erros intencionais para ilustrar falhas.
Exponenciação

Teste de exponenciação correta (ex.: 2^3 = 8).
Teste com erro intencional para ilustrar falha.
Os testes unitários foram escritos usando pytest. Para executá-los, utilize o comando:
pytest --disable-warnings
