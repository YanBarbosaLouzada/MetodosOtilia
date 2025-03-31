import numpy as np

def gauss_elimination(A, b):
    n = len(A)
    A = A.astype(float)
    b = np.array(b, dtype=float)  # Correção: Converter b para array do NumPy
    
    print("\nPasso 1: Matriz aumentada inicial")
    augmented_matrix = np.hstack((A, b.reshape(-1, 1)))
    print(augmented_matrix)
    
    # Fase de eliminação
    print("\nPasso 2: Escalonamento da matriz")
    for k in range(n - 1):
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]
            print(f"Passo {k+1}.{i}: Modificação da linha {i} usando a linha {k}")
            augmented_matrix = np.hstack((A, b.reshape(-1, 1)))
            print(augmented_matrix)
    
    # Retrossubstituição
    print("\nPasso 3: Resolução do sistema por retrossubstituição")
    x = np.zeros(n)
    for k in range(n - 1, -1, -1):
        soma = np.dot(A[k, k+1:], x[k+1:])
        x[k] = (b[k] - soma) / A[k, k]
        print(f"x[{k}] calculado: {x[k]}")
    
    return x

# Entrada do usuário
n = int(input("Digite a dimensão da matriz: "))
A = np.zeros((n, n))
b = []

print("Digite os elementos da matriz A linha por linha:")
for i in range(n):
    A[i] = list(map(float, input().split()))

print("Digite os elementos do vetor b:")
b = list(map(float, input().split()))

x = gauss_elimination(A, b)
print("\nSolução do sistema:", x)


# Entrada do usuário
n = int(input("Digite a dimensão da matriz: "))
A = np.zeros((n, n))
b = np.zeros(n)

print("Digite os elementos da matriz A linha por linha:")
for i in range(n):
    A[i] = list(map(float, input().split()))

print("Digite os elementos do vetor b:")
b = list(map(float, input().split()))

x = gauss_elimination(A, b)
print("\nSolução do sistema:", x)

