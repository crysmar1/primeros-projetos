# Cálculos raizes formula de Bhaskara
import math

# Função Cálculo do Delta
def delta(a, b, c):
    return b**2 - 4*a*c

# Função Entrada de dados
def main():
    a = float(input("Digite a variável a. "))
    b = float(input("Digite a variável b. "))
    c = float(input("Digite a variável c. "))
    imprime_raizes(a, b, c)

#Resolução da Equação
def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        print ("esta equação não possui raízes reais")
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
    if d == 0:
        print("a raiz dupla desta equação é:", x1)
    else:
        if x1 > x2:
            print("as raízes da equação são",x2,"e",x1)
        else:
            print("as raízes da equação são",x1,"e",x2)
