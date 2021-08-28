
print("Digite outros dois numeros: ")
x = int(input())
y = int(input())

if x > y:
    print("DECRESCENTE")
else: 
    print("CRESCENTE")
    
while x != y:
    print("Digite outros dois numeros: ")
    x = int(input())
    y = int(input())

    if x > y:
        print("DECRESCENTE")
    elif x < y: 
        print("CRESCENTE")