"""Faça um Programa que peça as quatro notas de 3 alunos, calcule e armazene num vetor 
a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."""

notas = []
total_alunos = []
for c in range (0,10):
    media = 0
    for i in range (0,4):
        notas.append(float(input(f"Insira a {i+1}º nota:")))
        media += notas[i]
        print(media)
    notas.clear()
    media = media/4
    total_alunos.append(media)

print("Notas maiores que 7.0")    
for c in total_alunos:
    if c >= 7:
        print(c)