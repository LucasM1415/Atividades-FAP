z = [15, 8, 9, 5, 8]
i = z.count(8)
print(i)
print(f"{i}")


z = [15, 8, 9, 5, 8]
i = z.sort()
print(i)
i = z.sort(reverse = True)
print(i)


z = [15, 8, 9, 5, 8]
z.reverse()
print(z)


z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del z[2]
z.remove(5)
z.append(11)
z.append(12)
z.insert(0,0)
print(len(z))


matriz = [[1,2], [1,2]]
for i in matriz:
 for i in matriz[0]:
  print(i)


  numeros = []
cont = 0
print("=========================================")
print("Olá, para começar, incira os 8 números")
print("=========================================")
print("")

while cont < 8:
  numero = float(input("Informe o número: "))
  numeros.append(numero)
  cont = cont + 1

print("")
print("================================================")
print("1.Exibir lista\n2.Calcular média\n3.Calcular soma\n4.Calcular maior\n5.Calcular menor")
print("================================================")
print("")

inicio = int(input("Olá, informe a opção que deseja: "))
if inicio == 1 or inicio == 2 or inicio == 3 or inicio == 4 or inicio == 5:

  if inicio == 1:
    print(f"Os valores inceridos foram: {numeros}")

  elif inicio == 2:
    N_Media = 0
    for i in numeros:
      N_Media = N_Media + i
    media = N_Media / len(numeros)
    print(f"A média dos valores inceridos é {media:.2f}")

  elif inicio == 3:
    N_Soma = 0
    for i in numeros:
      N_Soma = N_Soma + i2
    print(f"A soma dos valores inceridos é: {N_Soma:.2f}")

  elif inicio == 4:
    Maior = max(numeros)
    print(f"O maior valor invcerido foi: {Maior}")

  elif inicio == 5:
    Menor = min(numeros)
    print(f"O menor valor incerido foi: {Menor}")

else:
  print("Entrada invalida!")