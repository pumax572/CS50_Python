import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: No es un numero lo ingresado")
    sys.exit(1)
try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    sys.exit(1)

print(f"{x} / {y} = {result}")

