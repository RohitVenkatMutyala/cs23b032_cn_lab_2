n = 10
p_values = [i / 10 for i in range(1, 11)]

print("Slotted ALOHA Simulation")
print("Number of nodes:", n)
print("p values:", p_values)
def analytical_success(n, p):
    return n * p * ((1 - p) ** (n - 1))
analytical_results=[]
for p in p_values:
    analytical_results.append(analytical_success(n, p))

print("Analytical success probabilities:")
print(analytical_results)
