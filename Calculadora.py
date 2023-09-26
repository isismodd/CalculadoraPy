

operacao = input("Por favor digite a operação que deseja realizar: \n digite '+' para adição \n digite '-' para subtração \n digite '*' para multiplicação \n digite '/' para divisão \n")

number_1 = int(input('Digite o primeiro número: '))
number_2 = int(input('Digite o segundo número: '))


if operacao == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operacao == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operacao == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operacao == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('Você não digitou um operador válido, por favor rode o programa novamente.')