import numpy as np

def decomposicao_LU(A, b):
    n = len(A)
    L = np.eye(n)
    U = A.astype(float)
    
    print("\nPasso 1: Inicialização das matrizes L e U")
    print("Matriz L:")
    print(L)
    print("Matriz U:")
    print(U)
    
    # Triangularização
    print("\nPasso 2: Triangularização da matriz U e construção de L")
    for i in range(n-1):
        for k in range(i+1, n):
            m = U[k, i] / U[i, i]
            U[k, i:] -= m * U[i, i:]
            L[k, i] = m
            print(f"Passo {i+1}.{k}: Modificação da linha {k} usando a linha {i}")
            print("Matriz L:")
            print(L)
            print("Matriz U:")
            print(U)
    
    # Resolução do sistema Lower (Ly = b)
    print("\nPasso 3: Resolução do sistema Ly = b")
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
        print(f"y[{i}] calculado: {y[i]}")
    
    # Resolução do sistema Upper (Ux = y)
    print("\nPasso 4: Resolução do sistema Ux = y")
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
        print(f"x[{i}] calculado: {x[i]}")
    
    return x

# Entrada do usuário
n = int(input("Digite a dimensão da matriz: "))
A = np.zeros((n, n))
b = np.zeros(n)

print("Digite os elementos da matriz A linha por linha:")
for i in range(n):
    A[i] = list(map(float, input().split()))

print("Digite os elementos do vetor b:")
b = list(map(float, input().split()))

x = decomposicao_LU(A, b)
print("\nSolução do sistema:", x)