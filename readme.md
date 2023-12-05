# Documentacao do jogo

## Objetivo

Jogo que interaja com o usuário com palavras sorteadas com base no tema escolhido pelo mesmo.

## Funcionalidade

O jogo foi desenvolvido com condições que validam o input do usuário para cada pergunta realizada pelo programa.
Caso o usuário digite um caracter inesperado, o programa retornará uma mensagem pedindo que realize novamente o input
do caracter certo.

Possui um MENU que informa os temas disponíveis. São eles: Estações do ano, meses do ano, times brasileiros de futebol,
países europeus e animais. Quando o usuário escolhe um dos temas, o programa randomicamente seleciona uma palavra que está
armazenada em um dicionário no arquivo temas.py

### Regra para cálculo das chances

O número de chances é definido com base no seguinte cálculo:

Caso o tamanho da palavra seja ímpar, o numero de chances será o (tamanho + 1) /2
Caso o tamanho da palavra seja par, o numero de chances será o tamanho /2 

O usuário perde suas chances caso erre as letras, do contrário, as chances não são alteradas.

No fim, se o usuário acertar todas as letras da palavra ele ganha o jogo. Caso contrário, ele perde.

## Executável

Foi disponibilizado um executável para que o usuário possa jogar em sua máquina sem precisar ter o python instalado.


