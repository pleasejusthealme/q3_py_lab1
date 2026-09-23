import matplotlib.pyplot as plt
import random
import math

def get_std_dev(d):
    n = len(d)
    mean = sum(d) / n
    variance = sum((x - mean) ** 2 for x in d) / n
    return math.sqrt(variance)

def get_median(d):
    sorted_d = sorted(d)
    n = len(sorted_d)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_d[mid - 1] + sorted_d[mid]) / 2.0
    else:
        return sorted_d[mid]

def srav(before, after, metric_name):
    if before < after:
        print(f"{metric_name}: до перемешивания ({before:.4f}) < после ({after:.4f})")
    elif before == after:
        print(f"{metric_name}: до перемешивания ({before:.4f}) == после ({after:.4f})")
    else:
        print(f"{metric_name}: до перемешивания ({before:.4f}) > после ({after:.4f})")

n_elements = 500
a = [random.randint(1, 100) for _ in range(n_elements)]
sh = a.copy()

sr1 = sum(a) / len(a)
md1 = get_median(a)
std1 = get_std_dev(a)

random.shuffle(sh)

sr2 = sum(sh) / len(sh)
md2 = get_median(sh)
std2 = get_std_dev(sh)

print("Сравнение характеристик")
srav(sr1, sr2, "Среднее значение")
srav(md1, md2, "Медиана")
srav(std1, std2, "Стандартное отклонение")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Гистограмма ДО
ax1.hist(a, bins=20, color="skyblue", edgecolor="black")
ax1.set_title("Рисунок 1 - Распределение до перемешивания")
ax1.set_xlabel("Значения")
ax1.set_ylabel("Частота")
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Гистограмма ПОСЛЕ
ax2.hist(sh, bins=20, color="lightcoral", edgecolor="black")
ax2.set_title("Рисунок 2 - Распределение после перемешивания")
ax2.set_xlabel("Значения")
ax2.set_ylabel("Частота")
ax2.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()