# Trabalho feito por: Bruno Mascioli de Souza e Lucas Pereira dos Santos

jogadas = list(map(int, input().split()))

i = 0
soma = 0
while i < len(jogadas) - 3:
  if jogadas[i] == 10:
    print('X _ |', end=" ")
    soma += 10 + jogadas[i + 1] + jogadas[i + 2]
    i += 1
  elif jogadas[i] + jogadas[i + 1] == 10:
    print(jogadas[i], '/', '|', end=" ")
    soma += 10 + jogadas[i + 2]
    i += 2
  else:
    print(f'{jogadas[i]} {jogadas[i + 1]} |', end=" ")
    soma += jogadas[i] + jogadas[i + 1]
    i += 2

if len(jogadas) - i == 3:
  if jogadas[-3] == 10 and jogadas[-2] == 10 and jogadas[-1] == 10:
    soma += 30
    print('X X X')
  elif jogadas[-3] == 10:
    if jogadas[-2] == 10:
      soma += 20 + jogadas[-1]
      print(f'X X {jogadas[-1]}')
    else:
      if jogadas[-1] + jogadas[-2] == 10:
        soma += 20
        print(f'X {jogadas[-2]} /')
      else:
        soma += 10 + jogadas[-2] + jogadas[-1]
        print(f'X {jogadas[-2]} {jogadas[-1]}')
  else:
    if jogadas[-3] + jogadas[-2] == 10:
      if jogadas[-1] == 10:
        soma += 20
        print(f'{jogadas[-3]} / X')
      else:
        soma += 10 + jogadas[-1]
        print(f'{jogadas[-3]} / {jogadas[-1]}')

else:
  soma += jogadas[-2] + jogadas[-1]
  print(f'{jogadas[-2]} {jogadas[-1]}')
  

print(soma)
