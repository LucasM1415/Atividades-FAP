#1 -  Escreva um programa que receba como entrada dois números inteiros e exiba a soma e o produto entre eles.

numero_1 = int(input("Por favor, incira o primeiro número: "))
numero_2 = int(input("Por favor, incira o segundo número: "))
soma = numero_1 + numero_2
produto = numero_1 * numero_2
print(f"A soma dos números {numero_1} e {numero_2} é {soma}")
print(f"O produto dos números {numero_1} e {numero_2} é {produto}")

#2 - Regiane vai comemorar o aniversário de seu filho e quer encomendar docinhos. Sabendo que cada brigadeiro custa R$ 0,90, escreva um programa que receba como entrada a quantidade de brigadeiros encomendados e exiba o valor total gasto com duas casas decimais.

quantidade = int(input("Informe a quantidade de brigadeiros a serem encomendados: "))
total = quantidade * 0.90
print(f"O total a ser pago por {quantidade} brigadeiros é R${total:.2f}")

#3 - Não satisfeita, Regiane resolveu agradar ainda mais seus convidados adicionando alguns cajuzinhos à encomenda. Modifique o programa anterior para que ele passe a receber como entrada também a quantidade de cajuzinhos desejados, e exiba o novo valor total gasto com duas casas decimais (preço cajuzinho: R$ 0,70 a unidade).

quantidade_brigadeiro = int(input("Informe a quantidade de brigadeiros a serem encomendados: "))
quantidade_cajuzinho = int(input("Informe a quantidade de cajuzinho a serem encomendados: "))

total_brigadeiro = quantidade_brigadeiro * 0.90
total_cajusinho = quantidade_cajuzinho * 0.70
total = total_brigadeiro + total_cajusinho

print(f"O total a ser pago por {quantidade_brigadeiro} brigadeiros e {quantidade_cajuzinho} é R${total:.2f}")

#4 - Modifique o programa anterior uma vez mais para que ele receba também a quantidade de crianças convidadas, e passe a exibir também a quantidade total de docinhos de qualquer tipo que cada criança poderá comer. 

quantidade_brigadeiro = int(input("Informe a quantidade de brigadeiros a serem encomendados: "))
quantidade_cajuzinho = int(input("Informe a quantidade de cajuzinho a serem encomendados: "))
quantidade_criancas = int(input("Informe a quantidade de crianças esperadas:  "))

total_doces = quantidade_brigadeiro + quantidade_cajuzinho
doce_por_crianca = total_doces / quantidade_criancas
total_brigadeiro = quantidade_brigadeiro * 0.90
total_cajusinho = quantidade_cajuzinho * 0.70
total = total_brigadeiro + total_cajusinho

print(f"O total a ser pago por {quantidade_brigadeiro} brigadeiros e {quantidade_cajuzinho} é R${total:.2f},sendo {doce_por_crianca:.0f} doces por criança")

#5 - Betina trabalha em um escritório de advocacia e todos os dias analisa vários processos. Sabendo que ela cumpre um expediente diário de 8h, escreva um programa que receba como entrada quantos minutos ela leva para analisar cada processo, e exiba o total de processos revisados em um dia de trabalho. (Dica: Uma hora tem 60 minutos) (Dica: um processo não pode ser analisado parcialmente, apenas totalmente).

minutos_por_processo = float(input("Informe o tempo gastado por processo em minutos: "))
total_prosesos =  480 / minutos_por_processo
print(f"O total de processos revisados por dia deverá ser de {total_prosesos:.0f}")

#6 - Soraia foi fazer compras no supermercado de seu bairro e tomou um susto!! A dúzia de laranjas está caríssima, custando R$ 9,00!! Escreva um programa que receba como entrada a quantidade de laranjas que Soraia deseja comprar, e exiba o valor total necessário para realizar a compra com duas casas decimais de precisão. (Dica: uma dúzia corresponde a 12 laranjas, mas cada laranja também pode ser vendida separadamente).

qtd_laranjas = int(input("Informe a quantidade de laranjas que deseja comprar: "))
total = qtd_laranjas * 0.75
print(f"O valor a ser pago por {qtd_laranjas} é R${total:.2f}")

#7 - Todos os anos, os motoristas devem pagar ao Detran o IPVA (Imposto sobre a Propriedade de Veículos Automotores) e uma taxa de trânsito. Caso paguem o IPVA com antecedência, recebem um desconto de 5% apenas no valor desse imposto. Escreva um programa que receba como entrada o valor do IPVA e o valor da taxa de trânsito, e exiba o total a ser pago (com duas casas decimais de precisão) por um motorista que deseja quitar sua dívida cinco dias antes do prazo. 

ipva = float(input("Informe o valor do IPVA: "))
transito = float(input("Informe o valor da taxa de transito: "))
desconto = ipva - (ipva * 0.05)
total = desconto + transito

print(f"O total a ser pago é R$ {total:.2f}")


#8 - Sabendo que uma Copiadora cobra R$ 0,08 por cada cópia feita, escreva um programa que receba como entrada a quantidade de folhas de um livro e exiba o valor total a ser pago para copiá-lo com duas casas decimais. (Lembrete: cada folha corresponde a duas páginas – frente e verso)

qtd_folhas = int(input("Informe a quantidade de folhas a serem impressas: "))
total = qtd_folhas * 0.08
print(f"O total a ser pago por {qtd_folhas} folhas é de R$ {total:.2f}")

#9 - A biblioteca de Palmares empresta gratuitamente seus livros a alunos, professores e funcionários de todo o campus. Entretanto, sempre que um usuário atrasa a entrega de um livro, ele tem que pagar uma multa de R$ 0,75 por cada dia de atraso. Escreva um programa que receba como entrada a quantidade de dias de atraso do empréstimo de um livro, e exiba o valor da multa a ser paga pelo usuário com duas casas decimais.

dias_atrasados = int(input("Informe a quantidade de dias atrasados: "))
multa = dias_atrasados * 0.75
print(f"O total a ser pago em multas é de R$ {multa:.2f}") 

#10 - Um restaurante self-service de Palmares cobra R$ 20 por quilo nas refeições. Sabendo que, na hora de determinar o valor da refeição, deve ser desconsiderado o peso do prato vazio (230 gramas), escreva um programa que receba como entrada o peso total do prato de um cliente em gramas e exiba o preço cobrado com duas casas decimais. (Lembrete: 1 quilo = 1000 gramas)

peso = float(input("Informe o valor em gramas: "))
peso_real = peso - 230.00
valor = peso_real * 0.02
print(f"O valor a ser pago é de R${valor:.2f}")