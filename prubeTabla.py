N=int(input('ingrese N: '))
tabla=[[None for i in range(N)] for j in range(N)]
BordeIzq = (N//2)
BordeDer = (N//2)
k=2
tabla[0][N//2] = 1
for i in range(1,N-1):
    if(i<=N//2):
        for j in range((BordeIzq-i),(BordeDer+i)+1):
            tabla[i][j] = k
            k = k + 1
    else:
        BordeIzq = N//2
        BordeDer = (N-1)
        for j in range(i-BordeIzq,BordeDer):
            tabla[i][j]=k
            BordeDer = BordeDer - 1
            k=k+1

tabla[N-1][N//2] =k
for fila in tabla:
    print(fila)
