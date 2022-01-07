from math import *
try:
    num1 = float(input("Masukin angkanya a:"))
    op = input("Masukin operasinya a:")
    if op == "\/":
        print(sqrt(num1))
    else:
        num2 = float(input("Masukin angkanya a:"))
        if op == "+":
            print(num1 + num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "^":
            print(num1**num2)
        else:
            print("invalid operator")
except ZeroDivisionError:
    print("undefined")
except ValueError:
    print("ga masuk akal a")




