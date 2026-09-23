import random
import matplotlib.pyplot as plt

def MX(lst):
    return sum(lst) / len(lst)

def DX(lst):
    mean = MX(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

random.seed(42)
n_samples = 10000

mu_1, sigma_1 = 0.0, 1.0
seq_1 = [random.normalvariate(mu_1, sigma_1) for _ in range(n_samples)]

mu_2, sigma_2 = 5.0, 2.5
seq_2 = [random.normalvariate(mu_2, sigma_2) for _ in range(n_samples)]

emp_mx_1, emp_dx_1 = MX(seq_1), DX(seq_1)
emp_mx_2, emp_dx_2 = MX(seq_2), DX(seq_2)

theor_dx_1, theor_dx_2 = sigma_1**2, sigma_2**2

print("Эксперимент 1 (mu=0, sigma=1)")
print(f"Эмпирическое MX: {emp_mx_1:.4f} | Теоретическое mu: {mu_1}")
print(f"Эмпирическое DX: {emp_dx_1:.4f} | Теоретическое DX (sigma^2): {theor_dx_1:.4f}\n")

print("Эксперимент 2 (mu=5, sigma=2.5)")
print(f"Эмпирическое MX: {emp_mx_2:.4f} | Теоретическое mu: {mu_2}")
print(f"Эмпирическое DX: {emp_dx_2:.4f} | Теоретическое DX (sigma^2): {theor_dx_2:.4f}")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Рисунок 4 - Влияние параметров μ и σ на нормальное распределение (N=10000)', fontsize=14)

axes[0].hist(seq_1, bins=50, color='skyblue', edgecolor='black', density=True)
axes[0].set_title(f'Нормальное распределение\n(μ={mu_1}, σ={sigma_1})')
axes[0].set_xlabel('Значения')
axes[0].set_ylabel('Плотность вероятности')
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

axes[1].hist(seq_2, bins=50, color='lightcoral', edgecolor='black', density=True)
axes[1].set_title(f'Нормальное распределение\n(μ={mu_2}, σ={sigma_2})')
axes[1].set_xlabel('Значения')
axes[1].set_ylabel('Плотность вероятности')
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()