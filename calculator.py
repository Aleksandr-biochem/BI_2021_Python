# простейший калькулятор в формате число + операция + число
a = float(input())
p = input()
b = float(input())

if p == '+':
    print(a + b)
elif p == '-':
    print( a - b)
elif p == '*':
    print( a * b)
elif p == '/':
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')
elif p == 'mod':
    if b != 0:
        print(a % b)
    else:
        print('Деление на 0!')
elif p == 'pow':
    print(a ** b)
elif p == 'div':
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')
