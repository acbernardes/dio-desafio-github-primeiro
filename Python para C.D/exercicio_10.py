"""Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores."""

vetor_1 = []
vetor_2 = []
vetor_3 = []

for i in range(0,10):
    vetor_1.append(int(input("Insira um numero no primeiro vetor:")))
    
for j in range(0,10):
    vetor_2.append(int(input("Insira um numero no segundo vetor:")))

for k in range(0,10):
    vetor_3.append(vetor_1[i])
    vetor_3.append(vetor_2[i])

print(vetor_1)
print(vetor_2)
print(vetor_3)