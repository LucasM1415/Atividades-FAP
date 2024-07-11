""""
Questão 1
Escreva um programa que leia um número e escreva o valor da raiz cúbica deste. Para resolver o o problema, use a seguinte identidade

Exemplos:

Entrada | Saída

125 | 5.0

64 | 3.99999999999

1 | 1
"""
numero = int(input("Por favor, insira um número inteiro: "))
raiz = numero**(1/3)
print(f"{raiz:.16f}")

"""
Questão 2
Você está envolvido em um projeto de engenharia e precisa calcular a quantidade de piso para uma sala a ser construída, bem como a quantidade de tinta a ser usada nas paredes. Precisa também saber qual o volume da sala em metros quatrados para estimar a potência necessária para o ar condicionado. Para tanto, escreva um programa que leia 3 números correspondendo ao valor da altura, comprimento e largura da sala em metros e em seguida imprima as seguintes informações:

A área do piso da sala: largura * comprimento
O volume da sala: altura * comprimento * largura
A área das paredes da sala: 2 * altura * largura + 2 * altura * comprimento
Valores para teste:

altura | comprimento | largura | área da sala | volume | área das paredes

3 | 5 | 9 | 45 | 135 | 84

2 | 1 | 3 | 3 | 6 | 16

5 | 20 | 10 | 200 | 1000 | 300
"""
altura = float(input("Insira a altura: "))
comprimento = float(input("Incira o comprimento: "))
largura = float(input("Incira a largura: "))

area_piso = largura * comprimento
volume = altura * comprimento * largura
area_parede = 2 * altura * largura + 2 * altura * comprimento


print(f"Altura: ", altura)
print(f"Comprimento: ", comprimento)
print(f"Largura: ", largura)
print(f"Área do piso: ", area_piso)
print(f"Volume: ", volume)
print(f"Área das paredes: ", area_parede)

"""
Questão 3
Você gostaria de saber quantos segundos se passaram desde a meia-noite? Escreva um programa que leia valores inteiros para hora, minutos e segundo. Em seguida, o programa deve calcular e imprimir quantos segundos se passaram no total desde a última meia-noite até a hora lida. Deixamos a fórmula por sua conta.
"""
hora = int(input("Informe a hora atual: "))
minuto = int(input("Informe o minuto atual: "))
segundo = int(input("Informe os segundos atuais: "))

hora_s = hora * 3600
minuto_s = minuto * 60

total = hora_s + minuto_s + segundo

print(total, "segundos")