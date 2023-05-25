# Cálculo de Pontuação de Boliche

Este código em Python realiza o cálculo da pontuação em uma partida de boliche, com base nas jogadas fornecidas como entrada.

## Como usar

1. Execute o código em um ambiente Python.
2. Insira as jogadas como entrada. As jogadas devem ser digitadas em uma única linha, separadas por espaços. Cada jogada representa o número de pinos derrubados em cada lançamento.
3. O código calculará a pontuação total da partida de boliche e exibirá a representação gráfica das jogadas.

## Regras de Pontuação

O código segue as regras básicas de pontuação do boliche:

- Cada frame consiste em até duas jogadas, exceto o último frame, que pode ter até três jogadas.
- Se o jogador derrubar todos os 10 pinos (strike), ele recebe uma pontuação de 10 mais a soma dos pinos derrubados nas próximas duas jogadas.
- Se o jogador derrubar todos os 10 pinos com as duas jogadas de um frame (spare), ele recebe uma pontuação de 10 mais a soma dos pinos derrubados na próxima jogada.
- Caso contrário, a pontuação de um frame é a soma do número de pinos derrubados nas duas jogadas.

## Limitações

Este código assume que as jogadas fornecidas como entrada são válidas e seguem as regras do jogo de boliche. Não há tratamento de erros para entradas inválidas, como valores negativos ou inválidos para o número de pinos derrubados.

Certifique-se de fornecer as jogadas corretas como entrada para obter o cálculo preciso da pontuação.
