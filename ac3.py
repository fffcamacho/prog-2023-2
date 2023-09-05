"""Aluna : Fernanda Santiago Camacho 
    Matrícula : 202308079344
    dia 05/09/2023"""

# 1 Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo a tabela a seguir, baseado no salário atual. Após o aumento ser realizado, informe na tela:

# O salário antes do reajuste;
# O percentual de aumento aplicado;
# O valor do aumento;
# O novo salário, após o aumento.

# Salários até R$ 280,00 (incluindo)      Aumento de 20%
#  Salários entre R$ 280,00 e R$ 700,00    Aumento de 15%
#  Salários entre R$ 700,00 e R$ 1500,00   Aumento de 10%
#  Salários de R$ 1500,00 em diante        Aumento de 5%

def salario():
    salario = float(input("Digite o seu salário:R$ "))
    salario_aumento_20 = salario * 20/100
    salario_aumento_15 = salario * 15/100
    salario_aumento_10 = salario * 10/100
    salario_aumento_5 = salario * 5/100
    if salario <=280:
        print(f"Seu salário era de:R$ {salario}\n",
        "Houve um aumento de 20%\n",
        f"O aumento foi de {salario_aumento_20}\n",
        f"Seu Salário será de:R${salario_aumento_20 + salario}")
    elif salario >280 and salario <=700:
        print(f"Seu salário era de:R$ {salario}\n",
        "Houve um aumento de 15%\n",
        f"O aumento foi de: R${salario_aumento_15}\n"
        f"Seu Salário será de:R${salario_aumento_15 + salario}")
    elif salario >700 and salario <=1500:
        print(f"Seu salário era de:R$ {salario}\n",
        "Houve um aumento de 10%\n",
        f"O aumento foi de {salario_aumento_10}\n",
        f"Seu Salário será de:R${salario_aumento_10 + salario}")
    else:
        print(f"Seu salário era de:R$ {salario}\n",
        "Houve um aumento de 5%\n",
        f"O aumento foi de {salario_aumento_5}\n",
        f"Seu Salário será de:R${salario_aumento_5 + salario}")

salario()

# 2 Implementa uma função que receba um número e exiba o dia correspondente da semana (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

def dia_semana():
    numero = (int(input("Digite um número de 1 à 7: ")))
    if numero == 1:
        print("Domigo")
    elif numero ==2:
        print ("Segunda")
    elif numero == 3:
        print ("Terça")
    elif numero == 4:
        print ("Quarta")
    elif numero == 5:
        print ("Quinta")
    elif numero == 6:
        print("Sexta")
    elif numero == 7:
        print("Sábado")
    else:
        print("Valor inválido")
dia_semana()
    
# 3 Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax^2 + bx + c. O programa deverá receber os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

# Se o usuário informar o valor de a igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real, informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raízes reais, informe-as ao usuário.

def equacao():
    a = (float(input("Digite o valor: ")))
    if a == 0:
        print ("ENCERRADO.")
    else:
        b = (float(input("Digite o valor: ")))
        c = (float(input("Digite o valor: ")))
        delta = b**2 - 4*a*c
        r1 = (-b + delta **0.5)/(2*a)
        r2 = (-b - delta **0.5)/(2*a)
        if delta < 0:
            print ("programa Encerrado! Delta negativo.")
        elif delta == 0:
            print ("A equação possui apenas uma raíz real")
        else:
            print ("A equação possui duas raízes reais")

equacao()