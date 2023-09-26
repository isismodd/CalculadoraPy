

def calculate():
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

    again()
    
    # Defina a função again() para perguntar ao usuario se ele quer usar novamente a calculadora
def again():

    # pegue o input do user
    calc_again = input('''
Você quer calcular de novo?
Por favor digite S para SIM ou N para NAO.
''')

    # Se o user digitar S, rode calculate() function
    if calc_again.upper() == 'S':
        calculate()

    # Se o user digitar N, diga adeus ao user e feche o programa
    elif calc_again.upper() == 'N':
        print('Muito bem, obrigado por usar a calculadora')

    # Se o user digitar outra letra, rode a function de novo
    else:
        again()
        
calculate()
