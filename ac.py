''' Aluna : Fernanda Santiago Camacho 
    Matrícula : 202308079344
    dia 22/08/2023'''

"""
Elabore um código em Python que resolva uma equação do segundo grau ax² + bx + c = 0. O programa deve pedir os 
parâmetros a, b e c da equação e deve calcular 
as raízes pela fórmula de Bhaskara. Considere que as raízes são reais. Exemplo: a = 1, b = -6, c = 8 dá como raízes 4 e 2."""

'''a = float(input("digite um número: "))
b = float(input("digite um número: "))
c = float(input("digite um número: "))
delta = b**2 - 4*a*c
r1 = (-b + delta **0.5)/(2*a)
r2 = (-b - delta **0.5)/(2*a)
print("valor do primeiro x: ", r1, "valor do segundo x: ",r2)'''

'''Elabore um programa que leia uma variável inteira ano. Em seguida, exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto.
Um ano é bissexto se ele é múltiplo de quatro. 
No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. Então 1995 não é bissexto, 2012 é bissexto,
1900 não é bissexto e 2000 é bissexto'''

ano =int(input('informe o ano:'))
print(ano%4 == 0 and ano % 100!=(not ano % 400!=0))

