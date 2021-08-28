n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

if n3 < n2 and n3 < n1:
    print(f"MENOR = {n3} ")
elif n2 < n1:
    print(f"MENOR = {n2} ")
else:
    print(f"MENOR = {n1} ")