#, add, div, mul, sub, pow, sqrt
from mathOperators import operators

print("-" * 80)

num1 = int(input("Введите первое число: "))
while True:
    oper = input("Введите операцию: ")
    # if oper == "+":
    #     num2 = int(input("Введите второе число: "))
    #     print(f'{num1} {oper} {num2} = {num1 + num2}')
    #     num1 += num2
    # if oper == "C":
    #     num1 = int(input("Введите первое число: "))

    num2 = int(input("Введите второе число: "))
    rez = operators[oper](num1, num2)

    print(f'{num1} {oper} {num2} = {operators[oper](num1, num2)}')
