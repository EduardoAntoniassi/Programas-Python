from psutil import cpu_percent, virtual_memory
print('Ola Mundo')

# repetir olá mundo várias vezes
# print('Olá Mundo' * 20)
# end='x' -- para não quebrar linha... PAIA
# print(7 + 4, end=' ')
# print(8 + 4)
# print('7' + '4')

# print('Olá' , 5 + 4)

# metro = 2
# centimetro = 0.02
# nome1 = 'metal'
# print(metro , centimetro , nome1)

# nome = input('Qual é o seu nome? ')
# idade = input('Qual é a sua idade? ')
# peso = input('Qual é o seu peso? ')
# print(nome, idade, peso)
# print(f'Oi porra {nome:=^20}!')

# num1 = input('Qual o número um ')
# num2 = input('Qual o número dois ')
# sum = num1 + num2
# print(num1 + num2)
#Soma errada concatenando números pois não mostra o tipo primitivo antes do input

# num11 = int(input('Qual o numero um '))
# num22 = int(input('Qual o numero dois '))
# somma = num11 + num22
# print('A soma vale' ,somma)
# print('A soma vale {}'.format(somma))
# print('A soma entre {} e {} vale {}'.format(num11, num22, somma))
# print(f'A soma vale {somma}')

# bola = bool(input('Digite um valor '))
# print(bola)

# num1 = input('Digite x ')
# print(num1.isalpha())
# print(num1.isnumeric())
# print(num1.isalnum())

# Operadores Aritméticos
# adição = +
# subtração = -
# multiplicação = *
# divisão = /
# divisão inteira = // (número pré vírgula caso a divisão dê um número float)
# potência = **
# função pow = pow(x, y)
# função sqrt = sqrt(x) (Para fazer raiz de expoente diferente de 2, pode se usar pow ou ** de (1 / expoente dif))
# resto = %

# Ordem de Procedência
# 1 = () (Quando isola uma função -- (4 * (5 + 4) == 36))
# 2 = **
# 3 = *, /, //, %
# 4 = +, -