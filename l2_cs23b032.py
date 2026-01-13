import random 
slots=1000
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
def empirical_success(n, p, slots):
    success = 0
    for _ in range(slots):
        transmitting = 0
        for _ in range(n):
            if random.random() < p:
                transmitting += 1
        if transmitting == 1:
            success += 1
    return success / slots

empirical_results = []

for p in p_values:
    empirical_results.append(empirical_success(n, p, slots))

print("Empirical success probabilities:")
print(empirical_results)

