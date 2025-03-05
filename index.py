def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("O intervalo inicial não contém uma raiz.")
    
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def false_position_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("O intervalo inicial não contém uma raiz.")
    
    for _ in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c


def f(x):
    return x**3 - x - 2

a, b = 1, 2
raiz_bisseccao = bisection_method(f, a, b)
raiz_falsa_posicao = false_position_method(f, a, b)

print(f"Raiz encontrada pelo método da bissecção: {raiz_bisseccao}")
print(f"Raiz encontrada pelo método da falsa posição: {raiz_falsa_posicao}")