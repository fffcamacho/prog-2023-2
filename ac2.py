"""Aluna : Fernanda Santiago Camacho 
    Matrícula : 202308079344
    dia 30/08/2023"""

# 1 - Monte uma função que recebe um salário por hora e o número de horas trabalhadas no mês,
# e retorne o salário a ser recebido.

def calculo_salario(salario, horas):
    calculo = salario * horas
    return calculo

valor_salario = calculo_salario(6.82, 220)


# 2 - Elabore uma função que receba três números e exiba na tela
# (a) o produto do dobro do primeiro com metade do segundo; 
# (b) a soma do triplo do primeiro com o terceiro; e 
# (c) o terceiro elevado ao cubo.

def calculo_tres_numeros (dobro,soma,cubo):
    produto_dobro = dobro * 2 * soma/2
    soma_triplo = dobro * 3 + cubo
    elevado_cubo = cubo**3
    print('O valor do dobro do primeiro com metade do segundo:', produto_dobro)
    print("a soma do triplo do primeiro com o terceiro: ", soma_triplo )
    print("o terceiro elevado ao cubo: ",elevado_cubo )

calculo_tres_numeros (2, 4, 3)

# 3 - Elabore uma função com as mesmas regras do exercício anterior, porém retornando os três resultados, ao invés de exibi-los na tela

def calculo_tres_numeros (dobro,soma,cubo):
    produto_dobro = dobro * 2 * soma/2
    produto_triplo = dobro * 3 + cubo
    produto_cubo = cubo**3
    return produto_dobro, produto_triplo, produto_cubo

valor = calculo_tres_numeros (4, 4, 8)

# 4 - Elabore uma função que receba uma variável inteira ano. Em seguida, retorne o resultado da expressão lógica que indica se um ano é ou não bissexto. Um ano é bissexto se ele é múltiplo de quatro. No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

def ano_bissexto ():
    ano = int (input("Digite o ano: "))
    calculo_ano = ano%4==00 and ano%100!=0 or ano%400==0
    return calculo_ano

dados_ano = ano_bissexto()
#print(dados_ano)       coloquei o print, mas no enunciado não informa se precisa, na dúvida eu coloquei como opção aqui.
