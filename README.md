# Unit-Tests
Trabalho realizado para a disciplina de engenharia de software 1 - Testes de Unidade (Unit Tests).

Esse projeto consiste na implementação de uma calculadora simples em Python com as funcionalidades de soma, subtração, multiplicação, divisão e exponenciação. Foram elaborados testes unitários automatizados com o pytest para garantir o funcionamento correto das funções.

Versão do python utilizado - 3.13.2

## Percurso do trabalho

### Baixar e instalar o python: 
Baixar o python pelo site https://www.python.org/ ou pela Microsoft Store.

Durante a instalação, certifique-se de marcar a opção "Add Python to PATH".

Logo após, execute o seguinte comando no terminal para instalar o pytest: 
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
__pytest__ ou __pytest --disable-warnings__ (Desativa os avisos)

### Considerações
Num primeiro momento a calculadora foi imlementada tendo interatividade, permitindo ao usuário inserir valores via input(), No entanto, essa funcionalidade foi removida porque o pytest não suporta interações durante os testes.

Posteriormente foi notado que, se o arquivo __test_calculadora.py__  for deixado fora da pasta testes, os comandos de execução funcionam sem problemas. Porém se o arquivo estiver dentro da pasta __tests__ , será necessário adicionar um inicializador na pasta, criando o arquivo "_._unit__.py"(Tire o ponto depois do primeiro underline).

## Referências
Documentação oficial do pytest - [Get Started] {https://docs.pytest.org/en/stable/getting-started.html)

https://www.youtube.com/watch?v=H2jDPK3HVzw&t=181s

https://www.youtube.com/watch?v=uVM9vPu2z0g
