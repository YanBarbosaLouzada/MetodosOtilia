def f(x):
    # Defina aqui a função para a qual deseja encontrar a raiz
    return x**2 - 2  # Exemplo: f(x) = x^2 - 2 (raiz em x = sqrt(2))

def falsa_posicao(a, b, precisao):
    # Verifica se a função muda de sinal no intervalo [a, b]
    if f(a) * f(b) > 0:
        print("A função não muda de sinal no intervalo dado.")
        return None
    
    c = a
    while abs(f(c)) > precisao:  # Enquanto a precisão não for atingida
        # Calcula o ponto c usando a fórmula da falsa posição
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"c = {c}, f(c) = {f(c)}")  # Exibe o ponto c e o valor da função em c

        # Verifica se a raiz foi encontrada
        if f(c) == 0:
            return c
        
        # Atualiza o intervalo [a, b]
        if f(c) * f(a) < 0:  # Se a raiz está entre a e c
            b = c
        else:  # Se a raiz está entre c e b
            a = c
    
    return c

# Entrada de dados pelo usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
precisao = float(input("Digite a precisão desejada: "))

raiz = falsa_posicao(a, b, precisao)
if raiz is not None:
    print(f"A raiz aproximada é: {raiz}")
