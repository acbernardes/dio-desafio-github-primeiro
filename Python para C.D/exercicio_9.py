"""Faça um Programa que leia um vetor A com 10 números inteiros,
 calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

""" vetor_a = []

for i in range(0,3):
    vetor_a.append(int(input(f"Insira o {i+1}º valor:"))**2)

print(f"quadrados {vetor_a}")
print(f"A soma dos quadrados:{sum(vetor_a)}") """

"""Faça um Programa que leia um vetor de 5 números inteiros,
 mostre a soma, a multiplicação e os números. """

vetor = []
multiplicacao = 1
for i in range(0,5):
    vetor.append(int(input("Insira um numero:")))
    multiplicacao *= vetor[i]

print(f"A soma {sum(vetor)}")
print(f"Multiplicação {multiplicacao}")
print(f"Os numeros {vetor}")


