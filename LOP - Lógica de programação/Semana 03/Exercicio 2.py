"""
1 - Um edital de concorrência pública avaliará propostas considerando três critérios: qualidade, preço e prazo. Cada um dos três critérios recebe uma nota de 0 a 10. Escreva um programa que leia as notas de preço, prazo e qualidade de uma proposta e escreva sua nota geral, baseando-se nos seguintes critérios:

Se a nota da qualidade for inferior a 7, a nota geral será 0 independentemente dos outros fatores. Se a nota da qualidade for igual ou superior a 7, e a nota do preço for igual ou superior a 7, então a nota geral será a média das três notas, ou seja (qualidade + preço + prazo) / 3 Se a nota da qualidade for igual ou superior a 7 e a nota do preço for inferior a 7, então a nota geral será a média das três notas, mas com peso 2 para a nota do preço, ou seja, (qualidade + 2*preço + prazo)/4
"""
qualidade = float(input("Digite a nota de qualidade: "))
preco = float(input("Digite a nota de preço: "))
prazo = float(input("Digite a nota de prazo: "))

if not (0 <= qualidade <= 10 and 0 <= preco <= 10 and 0 <= prazo <= 10):
    print("Erro: Todas as notas devem estar entre 0 e 10.")
else:
    if qualidade < 7:
        nota_geral = 0
    elif qualidade >= 7:
        if preco >= 7:
            nota_geral = (qualidade + preco + prazo) / 3
        else:
            nota_geral = (qualidade + 2*preco + prazo) / 4

    print(f"A nota geralé: {nota_geral:.2f}")
 
"""
2 - Um ano é bissexto se for divisível por 4. Exceção a essa regra são os anos divisíveis por 100, os quais não são bissextos. Exceção a essa segunda regra são os anos divisíves por 400, os quais são bissextos. Escreva um programa que leia um número e escreva se ele corresponde ou não a um ano bissexto. É possíve usar um único "if" com condição composta para determinar se o ano é bissexto.
"""
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

"""
3 - Faça um programa para calcular o Índice de Massa Corporal (IMC) que é uma medida utilizada pela Organização Mundial de Saúde para avaliar o grau de obseidade de um indivíduo. O IMC é calculado pela relação entre o peso (em kg) dividido pelo quadrado da altura (em metros) do indivíduo. Uma vez calculdo o IMC, imprima-o e também informe a classificação resultante seundo a tabela fornecida pelo Sistema de Vigilância Alimentar Nutricional:
"""
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Baixo peso"
elif 18.5 <= imc < 25:
    classificacao = "Peso normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
elif 30 <= imc < 35:
    classificacao = "Obesidade grau I"
elif 35 <= imc < 40:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III"

print(f"O IMC é: {imc:.2f}")
print(f"A classificação é: {classificacao}")
