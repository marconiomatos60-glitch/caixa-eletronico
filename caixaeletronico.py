print("caixa eletronico")

valor = int(input("digite um valor para saque (minimo R$ 2):"))
                 
if valor < 2:
   print("valor invalido")

else:
    notas100 = valor // 100
    valor %= 100

    notas50 = valor // 50
    valor %= 50

    notas20 = valor // 20
    valor %= 20

    notas10 = valor // 10
    valor %= 10

    notas5 = valor // 5
    valor %= 5

    notas2 = valor // 2
    valor %= 2

        
print("\n saque realizado com sussesso")
if notas100 > 0:        
        print(f"notas de 100: {notas100}")

if notas50 > 0:        
    print(f"notas de 50: {notas50}")

if notas20 > 0:        
    print(f"notas de 20: {notas20}")

if notas10 > 0:        
    print(f"notas de 10: {notas10}")

if notas5 > 0:        
    print(f"notas de 5: {notas5}")


if notas2 > 0:        
    print(f"notas de 2: {notas2}")






        
    
