import math

def calculate_cos_approximation(x, n):
    sum = 0.0
    for i in range(n):
        term = ((-1)**i) * (x**(2*i)) / math.factorial(2*i) #?learn this formula
        sum += term
    return sum

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
approximation = calculate_cos_approximation(x, n)

print(f"The sum of the first {n} terms of the series for cos({x}) is {approximation}")