def exibeMenu():
  print("#### MENU ####\n")
  print("0- SAIR\n")
  print("1- SOMAR\n")
  print("2- SUBITRAISSE\n")
  print("3- MUTIPLICAR\n")
  print("4- DIVIDIR\n")
  opção = int(input("Escolha uma opção: "))
  return opção

def somar(numero1, numero2):
  resultado = numero1 + numero2
  return resultado


def subitrair(numero1, numero2):
  resultado = numero1 - numero2
  return resultado

def mutiplicar(numero1, numero2):
  resultado = numero1 * numero2
  return resultado

def dividir(numero1, numero2):
  resultado = numero1 / numero2
  return resultado



num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

while True:

  opção = exibeMenu()


  if opção == 0:
    print("Programa finalizado...")
    break
  elif opção == 1:
    print(f"A soma dos números inseridos é: {somar(num1,num2)}")
  elif opção == 2:
    print(f"A subtração dos númers inseridos é: {subitrair(num1,num2)}")
  elif opção == 3:
    print(f"A mutiplicação dos números inseridos é: {mutiplicar(num1, num2)}")
  elif opção == 4:
    print(f"A divisão dos números inseridos é: {dividir(num1, num2)}")
  else:
    print("Opção invalida!")



