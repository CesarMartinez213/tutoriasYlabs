N=int(input('ingrese N: '))
tabla=[[None for i in range(N)] for j in range(N)]
BordeIzq = N//2 - 1
BordeDer = N//2 + 1
k=1

for i in range(N//2 + 1):
    for j in range((BordeIzq-i),(BordeDer+i)):
        tabla[i][j] = k
        k = k + 1

contBorde=0

for i in range(N//2 + 2):
    contBorde= contBorde + 1
    for j in range((BordeIzq+contBorde),(BordeDer-contBorde)):
        tabla[i][j]=k
        k=k+1
print(tabla)