"""Aluna : Fernanda Santiago Camacho 
    Matrícula : 202308079344
    dia 12/09/2023"""

# 1) Elabore uma função e_primo(num) que retorna se um número num é primo ou não. Caso num não seja primo, liste todos os números pelos quais num é divisível.

def e_primo(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                nao_primo = (num, "não é primo")
                for i in range(2,num +1):
                    if  num % i == 0:
                        print("Númeors divisiveis: ", i)
                return nao_primo
            break
        else:
            return num, "é primo"
    else:
        return num,"não é primo"


e_primo(100)

# 2) Faça um programa que receba o valor de uma dívida e mostre as opções de parcelamento. O resultado final deve conter as opções de 1, 3, 6, 9 ou 12 parcelas, e o percentual de juros para cada parcela deve ser determinado conforme a primeira tabela, abaixo. O relatório com as opções de pagamento deve conter os seguintes dados: valor dos juros, valor total da dívida (incluindo juros), quantidade de parcelas e valor da parcela. A segunda tabela, abaixo, mostra um exemplo de como o resultado deve ser exibido. No momento, não é necessário formatar os valores.
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#  1                       0
#  3                       10
#  6                       15
#  9                       20
#  12                      25
#  Valor dos Juros Valor Total     Quantidade de Parcelas  Valor da Parcela
#  0               R$ 1.000,00     1                       R$  1.000,00
#  R$ 100,00       R$ 1.100,00     3                       R$    366,00
#  R$ 150,00       R$ 1.150,00     6                       R$    191,67

def divida(valor):

    juros = {
        3: round(valor*0.1, 2),
        6: round(valor*0.15, 2),
        9: round(valor*0.2, 2),
        12: round(valor*0.25, 2)
    }
    print ("valor dos juros R$   0", " valor total R$ ", valor, "Qt de parcelas 0 ", "valor da parcela R$ ", valor)
    for i in range(3,15,3):
        juro =int(juros[i])
        print("Valor dos juros R$ ", juro, "valor total R$ ", valor + juro, "Qt de parcelas", i, "valor da parcela R$ ", round((valor + juro)/i, 2))

divida(1000)



# 3) Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo

def num_positivo(numero):
    entre_0_25 = 0
    entre_26_50 = 0
    entre_51_75 = 0
    entre_76_100 = 0
    for i in numero:
        if i >= 0 and i <= 25:
            entre_0_25 += 1
        elif i >=26 and i <=50:
            entre_26_50 += 1
        elif i >=51 and i <=75:
            entre_51_75 += 1
        elif i >=76 and i <=100:
            entre_76_100 += 1
        elif i < 0:
            break
        else:
            print(f"No intervalo [0-25] tem {entre_0_25} elementos \n",f"No intervalo [26-50] tem {entre_26_50} elementos \n",f"No intervalo [51-75] tem {entre_51_75} elementos \n",f"No intervalo [76-100] tem {entre_76_100} elementos ")

    print(f"No intervalo [0-25] tem {entre_0_25} elementos \n",f"No intervalo [26-50] tem {entre_26_50} elementos \n",f"No intervalo [51-75] tem {entre_51_75} elementos \n",f"No intervalo [76-100] tem {entre_76_100} elementos ")

def main():
    nums = [0, 9, 10,8, 20,26,80,70,65,100]
    print(num_positivo(nums))
main()
