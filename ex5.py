import random
import math
import matplotlib.pyplot as plt

N_values = [1000, 10000, 50000, 100000, 200000, 1000000]
pi_estimates = []
errors = []

true_pi = math.pi

print(f"{'N':>10} | {'Оценка Pi':>10} | {'Абсолютная ошибка':>18}")
print("-" * 45)

for N in N_values:
    inside_count = 0

    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            inside_count += 1

    pi_est = 4 * inside_count / N
    pi_estimates.append(pi_est)

    error = abs(pi_est - true_pi)
    errors.append(error)

    print(f"{N:>10} | {pi_est:>10.6f} | {error:>18.6f}")

plt.figure(figsize=(10, 6))
plt.plot(N_values, errors, marker='o', color='royalblue', linestyle='-', linewidth=2, markersize=8)

plt.title("Рисунок 5 - Зависимость абсолютной ошибки оценки π от количества точек N")
plt.xlabel("Количество точек (N)")
plt.ylabel("Абсолютная ошибка |оценка - π|")

plt.xticks(N_values, rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)

plt.xscale('log')

plt.tight_layout()
plt.show()