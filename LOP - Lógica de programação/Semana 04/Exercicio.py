"""
1 - Escreva um algoritmo que leia três valores inteiros e diferentes, e mostre-os em ordem decrescente.
"""
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

if n1 == n2 or n1 == n3 or n2 == n3:
  print("Os números precisão ser diferentes!")
else:
  if n1 < n2 and n2 < n3:
    print(f"A ordem decrescente é; {n3}, {n2}, {n1} ")
  elif n1 < n3 and n3 < n2:
    print(f"A ordem decrescente é; {n2}, {n3}, {n1} ")
  elif n2 < n1 and n1 < n3:
    print(f"A ordem decrescente é; {n3}, {n1}, {n2} ")
  elif n2 < n3 and n3 < n1:
    print(f"A ordem decrescente é; {n1}, {n3}, {n2} ")
  elif n3 < n1 and n1 < n2:
    print(f"A ordem decrescente é; {n2}, {n1}, {n3} ")
  elif n3 < n2 and n2 < n1:
    print(f"A ordem decrescente é; {n1}, {n2}, {n3} ")

"""
2 - Escreva um algoritmo que leia o código de um determinado produto e mostre a sua classificação. Utilize a seguinte tabela como referências.

Código Classificação 1 Alimento não-perecível 2, 3 ou 4 Alimento perecível 5 ou 6 Vestuário 7 Higiene Pessoal 8 até 15 Limpeza e Utensílios Domésticos

Qualquer outro código Inválido
"""
codigo = int(input("Incira o código do produto: "))
if codigo == 1:
  print("Alimento não-perecivel")
elif codigo == 2 or codigo == 3 or codigo == 4:
  print("Alimento perecivel")
elif codigo == 5 or codigo == 6:
  print("Vestuario")
elif codigo == 7:
  print("Higiene pessoal")
elif codigo >= 8 and codigo <= 15:
  print("Limpesa e Utensílios Domesticos")
else:
  print("Código Invalido")

"""
3 - Calcule a média aritmética das três notas de um aluno e mostre, além do valor da média, uma mensagem de "Aprovado", caso a média seja igual ou superior a 7; a mensagem “em prova final” caso a média seja menor que 7 e maior ou igual a 4; e "reprovado", caso contrário.
"""
nota1 = float(input("Por favor, informe a primeira nota: "))
nota2 = float(input("Por favor, informe a segunda nota: "))
nota3 = float(input("Por favor, informe a terceira nota: "))
media = (nota1 + nota2 + nota3)/3

if nota1 > 10 or nota2 > 10 or nota3 > 10:
  print("Notas invalidas!")
else:
  if media >= 7:
    print("Aprovado")
  elif media < 7 >= 4:
    print("Em prova final")
  else:
    print("Reprovado")

"""
4 - Faça um algoritmo que leia quatro números (Opção, Num1, Num2 e Num3) e mostre a soma dos números se Opção for 2; o produto se Opção for 3; e se a soma de Num1 com Num2 é maior, menor ou igual a Num3 se Opção for 4. Os únicos valores aceitáveis para a variável Opção são 2, 3 e 4.
"""
Num1 = float(input("Informe o primeiro numero: "))
Num2 = float(input("Informe o segundo numero: "))
Num3 = float(input("Informe o terceiro numero: "))
Opcao = int(input("Qual opção deseja realizar? "))

if Opcao !=2 and Opcao !=3 and Opcao !=4:
  print("opção invalida, tente 2, 3 ou 4")
elif Opcao == 2:
  produto = (Num1 * Num2 * Num3)
  print(f"O produto dos númeos é: {produto}")
elif Opcao == 3:
  soma = Num1 + Num2 + Num3
  print(f"A soma dos números é: {soma}")
else:
  if (Num1 + Num2) > Num3:
    print(f"A soma de {Num1} e {Num2} é maior do que {Num3}")

  elif  (Num1 + Num2) < Num3:
    print(f"A soma de {Num1} e {Num2} não é maior do que {Num3}")

  elif (Num1 + Num2) == Num3:
    print(f"A soma de {Num1} e {Num2} é igual ao terceiro número incerido, que é {Num3}")

"""
5 - Escreva um algoritmo que determine o número de dias que uma pessoa já viveu até a data de HOJE (26/06/2024). Considere que um mês tenha 30 dias.
"""
dia_nasc = int(input("Informe o dia de nascimento: "))
mes_nasc = int(input("Informe o mês de nascimento: "))
ano_nasc = int(input("Informe o ano de nascimento: "))

dia_atual = 26
mes_atual = 6
ano_atual = 2024

anos = ano_atual - ano_nasc
meses = mes_atual - mes_nasc
dias = dia_atual - dia_nasc

if dias < 0:
    meses -= 1
    dias += 30

if meses < 0:
    anos -= 1
    meses += 12

total_dias = anos * 12 * 30 + meses * 30 + dias

print(f"O total de dias vividos até hoje é: {total_dias} dias")

