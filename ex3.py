import random
import matplotlib.pyplot as plt

random.seed(42)

beta = 2.0
alphas = [0.5, 1.0, 2.0, 5.0]
n_samples = 10000

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Рисунок 3 - Влияние параметра alpha на форму гамма-распределения (beta=2.0)', fontsize=14)

for i, alpha in enumerate(alphas):
    row = i // 2
    col = i % 2
    ax = axes[row, col]

    seq = [random.gammavariate(alpha, beta) for _ in range(n_samples)]

    ax.hist(seq, bins=50, color='skyblue', edgecolor='black', density=True, alpha=0.8)

    ax.set_title(f'Случай {i + 1}: alpha = {alpha}, beta = {beta}')
    ax.set_xlabel('Значения')
    ax.set_ylabel('Плотность вероятности')
    ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()