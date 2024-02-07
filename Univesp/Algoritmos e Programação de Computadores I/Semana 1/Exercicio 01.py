"""
Ler uma temperatura em graus Celsius e apresentá-la convertida
em graus Fahrenheit. A fórmula de conversão é F ← C * 9 / 5 + 32,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

"""

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 9 / 5 + 32

print(f"A temperatura em Fahrenheit é {fahrenheit:.2f}°F")

