print("Exercício 1")
num1 = int(input("escolha o número: "))
for i in range(1,num1+1): print(i)
print("------------------------------i")
print("Exercício 2")
num2 = float(input("escolha um número: "))
if float(25) < num2 <= float(50):
    print("(25,50]")
elif float(0) <= num2 <= float(25):
    print("[0,25]")
elif float(50) < num2 <= float(75):
    print("(50,75]")
elif float(75) <= num2 <= float(100):
    print("[75,100]")
else: print("Fora de intervalo")
print("------------------------------i")
print("Exercício 3")
raio = float(input("raio do círculo: "))
import math
print((raio ** 2) * (math.pi))
print("------------------------------i")
print("Exercício 4")
inteiro1 = int(input("escolha um número inteiro: "))
inteiro2 = int(input("escolha outro número inteiro: "))
real = float(input("escolha um número real: "))
print("a)", inteiro1 * (inteiro2 / 2))
print("b)", 3 * inteiro1 + real)
print("c)", real ** 3)
print("------------------------------i")
