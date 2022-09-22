modo iterativo
- consigo ver o resultado do codigo em tempo real
 no terminal chamo por python, para sair digito exit()

posso chamar um programa no terminal
python

função dir - sem argumentos, retorna a lista de nomes no escopo local atual. com argumento retorna lista de atributos válidos para o objeto
- lista de metodos q podemos utilizar no objetos
dir()
dir(100)

função help - ajuda integrado, me tras forma de utilizar a função

help()
help(100)
para encerrar a documentação -k

-------------------------------
-------------------------------
Variáveis e constantes

definir valores que podem sofrer alterações no decorrer da execução do programa.

constantes- os valores são imutaveis (nao existe palavra em python reservada para constante)
-em convenção cria-se a variavel com o nome em letras maiusculas

boas práticas
-escrever em snake case
-escolher nomes sugestivos
-nome de constantes todo em maiusculo
-------------------------------
-------------------------------
### conversão de tipos

float(variavel)
int(variavel)
str(variavel)

não consigo converter qualquer tipo de dados
por exemplo, letra pra float ou int

-------------------------------
-------------------------------
### funções de entrada e saida

-receber e exibir informações para o usuário

input() - recebe dados da entrada padrão (recebe em formato string)
print() -exibo dados na tela (elementos opcionais sep, end, file, flush)-convertido em string
end '...\n' (finaliza o print)
sep="#" (separador das strings)
\n - quebro linha

/////////////////////////////

*Tipos de Operadores com Python*

-> Operadores aritméticos
#Adição print(1+1)
#subtração print(1-1)
#multiplicação 1*1
#Divisão 12/3 (retorno um float)
#divisao inteira 12//4 (retorno um int)
#modulo (resto da divisão) -> 10%3 -sobra 1
#exponencial (elevado)-> print (2**3) -return 8

->Igual na matematica ele resolve as operações por regra de qual deverá ser executada primeiro.
-Parentesis, expoentes, multiplicação, divisões, somas e subtrações 

-------------------------------
-------------------------------
-> Operadores de comparação

São operadores utilizados para comparar dois valores
variavel_1==variavel_2
(Se verdadeiro retorna True, se falso retorna False)
variavel_1!=variavel_2
(Se verdadeiro retorna True, se falso retorna False)
variavel_1>variavel_2 - serve para maior e menor tb
(Se verdadeiro retorna True, se falso retorna False)
-------------------------------
-------------------------------

-> Operadores de atribuição
-São utilizados para definir o valor inicial ou sobrescrever um valor

Atribuição simples
saldo = 500

Atribuição de soma
saldo += 200 (como se fosse saldo = saldo +200) adiciono valor

Atribuição de multiplicação / divisão
saldo *= 2 (retorna 1000)

saldo %= 5 (retorna o modulo da divisao)

-> Operadores Lógicos
- usados junto com os operadores de comparçao para montar uma expressão logica
retorna um valor boleano
Operador e -> and 
Operador ou -> or (apenas uma condição como vdd retorna True)
Operador negação -> not (ele da o inverso da verdade) - sequências vazias são False
Parenteses -> precedência de comparação

-> Operadores de identidade
-Utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória
is e is not (é ou não é)

-> Operadores de associação
- in e not in (esta ou não esta)
curso = “Curso de Python”
(“Python” in curso) - retorna True
(“Abacaxi” not in curso) - retorna False

/////////////////////////////////
# Estruturas Condicionais e de Repetição em Python

### Identação e blocos
 - mantem o codigo fonte mais legivele manutenivel, no python pela identação o interpretador consegue determinar onde se inicia o bloco de comando e onde finaliza
 - a cada novo bloco utilizo 4 espaços em branco e inicializa com dois pontos (:)

 Exemplo:

 if variavel == 1:
     print('Numero 1')

--------------------------------------
--------------------------------------

### Estruturas condicionais
 -> permite o desvio de fluxo de controle quando determinadas expressões lógicas são atendidas

 (if/ else) -> teremos dois desvio, caso o bloco do if seja verdadeiro o bloco de comando sera executado, caso contradio o bloco do else será executado.

 (if/elif/else) =--> usaremos quando precisamos de mais de dois desvios, sera uma nova expressão logica e caso a expressão seja verdadeira, o bloco sera executado. (evitar usar grandes estruturas de codigo pois aumenta a complexidade)


 -> if aninhado
 posso criar estruturas condicionais aninhadas, colocando estruturas de if/elif/else dentro de bloco de if/elif/else

 -> if ternario - permite escrever uma condição em uma única linha. composto de 3 partes, retorno caso a expressão seja vdd, expressão logica, e retorno caso a expressão nao seja atendida
status = mensagem caso vdd if (condição) esle mensagem caso false
 status = "Sucesso" if saldo >= else "Falha"

--------------------------------------
--------------------------------------
### Estruturas de repetição

-> utilizadas para repetir um trecho de codigo um determinado nº de vezes (pode ser o nº conhecido previamente ou determinado atraves de expressão logica)

comando for - quando sabemos previamente o nº de vezes que precisamos ser repetido

### Função range
produz uma sequencia de numeros inteiros a partir de um inicio e para em um fim.
 range(inicio,fim,passada)
 range(start,stop,step)

 ### Comando While
 -> faz sentido utiliza-lo quando não sei quantas vezes irei executar o codigo. 

 while variavel!=0:
     comando
     if condicaçao = True:
     break

quando eu quero cortar o laço de um while utilizo o break 
para pular um bloco utilizo o continue