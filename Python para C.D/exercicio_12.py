"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos 
com mais de 13 anos possuem altura inferior à média de altura desses alunos."""

idades = [13, 14, 15, 13,15, 11, 12, 12, 13, 16]
alturas = [1.70, 1.50, 1.63, 1.56, 1.65, 1.70, 1.50, 1.63, 1.56, 1.65]

media_alturas = sum(alturas)/len(alturas)
print(media_alturas)
contador = 0
for i, valor in enumerate(idades):
    if valor >= 13 and alturas[i]<media_alturas:
        contador = contador + 1

print(f"Temos {contador} alunos menores que a média:{media_alturas}")

