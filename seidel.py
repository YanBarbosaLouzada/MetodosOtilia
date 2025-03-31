import numpy as np

def seidel(A, b, x0, tol=1e-10, max_iter=1000):
    n = len(A)
    x = np.copy(x0)
    for it in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            sigma = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sigma) / A[i][i]
        
        print(f"Iteração {it + 1}: {x_new}")  # Imprime as iterações

        if np.linalg.norm(x_new - x, np.inf) < tol:
            return x_new, it + 1
        x = x_new
    return x, max_iter

def get_matrix_input():
    n = int(input("Digite a ordem da matriz: "))
    A = []
    b = []

    print("Digite os elementos da matriz A linha por linha:")
    for i in range(n):
        row = list(map(float, input().split()))
        A.append(row)

    print("Digite os elementos do vetor b:")
    b = list(map(float, input().split()))

    return np.array(A, dtype=float), np.array(b, dtype=float), np.zeros(n)

if __name__ == "__main__":
    A, b, x0 = get_matrix_input()
    
    x, iterations = seidel(A, b, x0)
    print(f"Solução de Seidel: {x}")
    print(f"Número de iterações: {iterations}")
