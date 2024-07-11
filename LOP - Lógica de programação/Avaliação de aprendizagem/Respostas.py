#1 - Questão

qtd_folhas = int(input("Por favor, insira o núrumero de folhas á serem imprimidas: "))
total = qtd_folhas * 0.80
print(f"O total a ser pago por {qtd_folhas} é R$ {total:.1f}")

#2 - Questão

s_hora = float(input("Informe o seu salario por hora: "))
h_trabalhadas = float(input("Informe a quantidade de horas trabalhadas por dia: "))
total = (h_trabalhadas * s_hora) * 22
print(f"Nesse ritimo de trabalho, seu salario deverá ser de R$ {total:.2f} mensais")

#3 - Questão

nome = str(input("Olá, por favor insira seu nome: "))
qtd_horas = float(input(f"Olá {nome}! Agora por favor, insira a quantidade de horas que voçê dorme por dia: "))
porcentagem = (qtd_horas / 24) * 100
print(f"{nome}, voçê passa {porcentagem:.2f}% do seu tempo de vida dormindo")

#4 - 
qtd_dias = int(input("Olá, informe quantos dias voçê ficou hospedado: "))
qtd_pessoas = int(input("Informe agora quantas pessoas ficaram no seu quarto: "))
if qtd_pessoas == 1:
  total = qtd_dias * 110
  print(f"O total a ser pago é de: R${total:.2f}")
elif qtd_pessoas == 2:
    total = qtd_dias * 130
    print(f"O total a ser pago é de: R${total:.2f}")
else:
  print("Desculpe, algo deu errado! Tente rever o dado da quantidade de pessoas! Já que nossa pusada só conforta quartos para uma ou duas pessoas!")
