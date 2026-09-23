import random
import math
import matplotlib.pyplot as plt

# --- 1. Собственные функции расчета (без готовых библиотечных функций) ---
def MX(lst):
    """Вычисление математического ожидания (среднего)"""
    return sum(lst) / len(lst)

def DX(lst):
    """Вычисление дисперсии по формуле 1/n * sum((x - mean)^2)"""
    mean = MX(lst)
    # Можно через цикл, как у тебя, или через генератор (генератор чуть "питоничнее")
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def get_median(lst):
    """Вычисление медианы упорядоченной выборки"""
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2.0
    else:
        return sorted_lst[mid]

# --- 2. Генерация исходной последовательности (Вариант 3: Гамма-распределение) ---
random.seed(42)
a = []
# gammavariate принимает alpha (форма) и beta (масштаб), оба > 0
for i in range(10000):
    a.append(random.gammavariate(2.0, 2.0))

# Расчет характеристик исходной последовательности
mean1 = MX(a)
var1 = DX(a)
med1 = get_median(a)

print("=== Исходные данные (Гамма-распределение, N=10000) ===")
print(f"  Среднее (MX)   = {mean1:.4f}")
print(f"  Дисперсия (DX) = {var1:.4f}")
print(f"  Медиана        = {med1:.4f}")
print()

# --- 3. Генерация новой последовательности (синусы исходной) ---
sin_values = []
for x in a:
    sin_values.append(math.sin(x))

# Расчет характеристик для последовательности синусов
mean2 = MX(sin_values)
var2 = DX(sin_values)
med2 = get_median(sin_values)

print("=== Последовательность sin(x) ===")
print(f"  Среднее (MX)   = {mean2:.4f}")
print(f"  Дисперсия (DX) = {var2:.4f}")
print(f"  Медиана        = {med2:.4f}")
print()

# --- 4. Визуализация (отличное дополнение к отчету!) ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.hist(a, bins=50, edgecolor='black', color='skyblue')
ax1.set_title('Рисунок 2.1 - Исходное гамма-распределение')
ax1.set_xlabel('Значения x')
ax1.set_ylabel('Частота')

ax2.hist(sin_values, bins=50, edgecolor='black', color='lightcoral')
ax2.set_title('Рисунок 2.2 - Распределение sin(x)')
ax2.set_xlabel('Значения sin(x)')
ax2.set_ylabel('Частота')

plt.tight_layout()
plt.show()