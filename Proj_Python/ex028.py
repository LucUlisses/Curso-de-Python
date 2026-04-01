from random import randint
from time import sleep
print('-=-' * 20) #opicional
computador = randint(0, 5)
print('Tente adivinhar um numero entre 0 e 5...caso você erre terá que dar o seu caneco precioso e caso acerte eu darei meu caneco')
print('-=-' * 20) #opicional
jogador = int(input("Em que número pensei? "))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Ai que merda você você acertou...')
else:
    print('Você perdeu!!!! Eu pensei no numero {}, VAI ROLAR CANECOOOOO'.format(computador))

