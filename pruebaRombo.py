N=int(input('ingrese N: '))
tabla=[[ 0 for i in range(N)] for j in range(N)]
BordeArr = (N//2)
BordeAbj = (N//2)
k=2
tabla[N//2][0] = 1
for j in range(1,N-1):
    if(j<=N//2):
        for i in range((BordeArr-j),(BordeAbj+j)+1):
            tabla[i][j] = k
            k = k + 1
    else:
        BordeArr = N//2
        BordeAbj = (N-1)
        for i in range(j-BordeArr,BordeAbj):
            tabla[i][j]=k
            BordeAbj = BordeAbj - 1
            k=k+1

tabla[N//2][N-1] =k
for fila in tabla:
    print(fila)
