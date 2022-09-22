saque = 500
limite = 100

status = "Sucesso" if saque <= limite else "Falha"

print(f'{status} ao realizar o saque.')

#estrutura condicional
texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

#range

for c in range(0,5):
    print(c)

#while

dados = int(input("Insira um numero:"))

while dados != 3:
    dados = int(input("Opção invalida digite outro numero::"))

print('fim de codigo')