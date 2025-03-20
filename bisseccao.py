def bisseccao(f, a, b, tol=1e-6):
    """
    Método da bissecção para encontrar raízes de uma função f no intervalo [a, b].
    
    Parâmetros:
    f   - Função contínua f(x).
    a   - Limite inferior do intervalo.
    b   - Limite superior do intervalo.
    tol - Tolerância para critério de parada.
    
    Retorno:
    Aproximação da raiz da função.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("O método da bissecção requer que f(a) e f(b) tenham sinais opostos.")

    while (b - a) / 2 > tol:
        c = (a + b) / 2  # Calcula o ponto médio
        if f(c) == 0:    # Se f(c) for exatamente zero, encontramos a raiz
            return c
        elif f(a) * f(c) < 0:
            b = c  # A raiz está no intervalo [a, c]
        else:
            a = c  # A raiz está no intervalo [c, b]

    return (a + b) / 2  # Retorna a melhor aproximação da raiz

# Exemplo de uso:
def funcao(x):
    return x**2 - 2  # Queremos encontrar a raiz de x^2 - 2 = 0 (√2)

raiz = bisseccao(funcao, 1, 2)
print(f"A raiz aproximada é {raiz:.6f}")
