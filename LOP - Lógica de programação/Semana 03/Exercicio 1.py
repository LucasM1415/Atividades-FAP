"""
1 - Todos os funcionários de uma empresa precisam pagar impostos, mas o percentual varia de acordo com o salário

Funcionários que ganham mais de R$ 1000 pagam 17% de imposto, e os demais pagam 8% de imposto

Escreva um programa que receba como entrada o salário de um funcionário e exiba o valor do imposto que ele terá que pagar
"""
salario = float(input("Digite o salário do funcionário: "))

if salario > 1000:
    imposto = salario * 0.17
else:
    imposto = salario * 0.08

print(f"O valor do imposto é de: R${imposto:.2f}")

"""
2 - O circo chegou na cidade e estão sendo vendidos ingressos a preços promocionais.

Todas as crianças até 5 anos pagam R 10,idososcom60anosoumaispagamR  15, e os demais pagam R$ 25.

Escreva um programa que receba como entrada a idade de uma pessoa e exiba o valor a ser pago pelo ingresso.
"""
idade = int(input("Digite a idade: "))

if idade <= 5:
    preco = 10
elif idade >= 60:
    preco = 15
else:
    preco = 25

print(f"O ingresso custará: R${preco:.2f}")
