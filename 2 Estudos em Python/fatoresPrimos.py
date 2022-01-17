n = int(input("Digite um número inteiro maior que 1: "))

fator = 2
multiplicidade = 0
# Condição de execução para n maior que 1. Pois o 1 não decompoe.
while n > 1:
    while n % fator == 0:  # Enquanto o resto da divisão for 0, faz a divisão e muda a multiplicidade.
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print("fator ", fator, "multiplicidade = ", multiplicidade)
    fator = fator + 1
    multiplicidade = 0
    
