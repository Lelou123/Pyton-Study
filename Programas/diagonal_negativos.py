N = int(input("Qual a ordem da matriz? "))

mat = [[0 for x in range(N)] for x in range (N)]

for i in range (0, N):
    for j in range (0, N):
        print(f"Elemento [{i},{j}]: ",end="")
        mat[i][j] = int(input())
        
print("Diagonal principal: ")
for i in range (0, N):
    print(f"{mat[i][i]}  ", end="")

print()
contneg = 0
for i in range(0,N):
    for j in range(0, N):
        if mat[i][j] < 0:
            contneg = contneg + 1
print(f"Quantidade de negativos = {contneg} ")