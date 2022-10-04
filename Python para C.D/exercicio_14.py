"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

 O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
 Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
 entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""


perguntas = ["Telefonou para a vítima?","Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?","Já trabalhou com a vítima?"]
respostas = []
for i in perguntas:
    print(i)
    resp = input("S/N:\n")
    respostas.append(resp.lower())

res_positiva = respostas.count("s")

if res_positiva == 2:
    print("Suspeita!")
elif res_positiva == 3 or res_positiva == 4:
    print("Cumplice!")
elif res_positiva == 5:
    print("Assassina!")
else:
    print("Inocente!")