def falsa_posicao(f, a, b, tol=1e-6, max_iter=100):
    """
    Método da falsa posição (Regula Falsi) para encontrar raízes de uma função f no intervalo [a, b].
    
    Parâmetros:
    f        - Função contínua f(x).
    a        - Limite inferior do intervalo.
    b        - Limite superior do intervalo.
    tol      - Tolerância para critério de parada.
    max_iter - Número máximo de iterações.
    
    Retorno:
    Aproximação da raiz da função.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("O método da falsa posição requer que f(a) e f(b) tenham sinais opostos.")

    for _ in range(max_iter):
        # Calcula o ponto c usando interpolação linear
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if abs(f(c)) < tol:  # Critério de parada
            return c

        # Ajusta o intervalo [a, b] baseado no sinal de f(c)
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c  # Retorna a melhor aproximação da raiz

# Exemplo de uso:
def funcao(x):
    return x**2 - 2  # Encontrando a raiz de x^2 - 2 = 0 (√2)

raiz = falsa_posicao(funcao, 1, 2)
print(f"A raiz aproximada é {raiz:.6f}")
