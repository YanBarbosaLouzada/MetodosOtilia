def f(x):
    # Defina aqui a função para a qual deseja encontrar a raiz
    return x**2 - 2  # Exemplo: f(x) = x^2 - 2 (raiz em x = sqrt(2))

def bisseccao(a, b, precisao):
    # Verifica se a função muda de sinal no intervalo [a, b]
    if f(a) * f(b) > 0:
        print("A função não muda de sinal no intervalo dado.")
        return None
    
    # Inicializa o ponto médio
    c = a
    passo = 1
    
    # Iterações do método da bisseção
    while (b - a) / 2 > precisao:
        # Calcula o ponto médio
        c = (a + b) / 2
        print(f"Passo {passo}: c = {c}, f(c) = {f(c)}")  # Exibe o ponto médio e o valor da função no ponto
        
        # Verifica se encontramos a raiz
        if f(c) == 0:
            return c
        
        # Atualiza o intervalo [a, b] com base no sinal de f(c)
        if f(c) * f(a) < 0:  # Se a raiz está entre a e c
            b = c
        else:  # Se a raiz está entre c e b
            a = c
        
        passo += 1
    
    return c

# Entrada de dados pelo usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
precisao = float(input("Digite a precisão desejada: "))

raiz = bisseccao(a, b, precisao)
if raiz is not None:
    print(f"A raiz aproximada é: {raiz}")
