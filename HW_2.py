import numpy as np
import matplotlib.pyplot as plt

# Завдання 1: Створити два вектори x та y для створення графіку залежностей

x = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
y = [2, 3, 4, 5, 6, 7, 8, 9, 10]

#Завдання 2: Побудувати лінійний графік залежності y від x
plt.plot(x, y)
plt.title('Лінійний графік')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Завдання 3: Побудувати стовпчикову діаграму для векторів x та y

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.bar(x, y)
plt.title('Стовпчикова діаграма')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Завдання 4: Побудувати гістограму для випадкового розподілу з 100 елементів
data = np.random.randn(100)
plt.hist(data, bins=10, edgecolor='black')
plt.title('Гістограма')
plt.xlabel('Значення')
plt.ylabel('Частота')
plt.show()

# Завдання 5: Побудувати точкову діаграму для векторів x та y
x = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
y = [2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.scatter(x, y)
plt.title('Точкова діаграма')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Завдання 6: Побудувати кругову діаграму для вектора зі значеннями [10, 20, 30, 40] та міток ['A', 'B', 'C', 'D']
# Hint: plt.pie()
values = [10, 20, 30, 40 ]
labels = ['A', 'B', 'C', 'D']
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('Кругова діаграма')
plt.show()

# Завдання 7: Побудувати графік функції `y = x^2` на відрізку [0, 5]
# Hint: np.linspace()
x = np.linspace(0, 5, 100)
y = x**2
plt.plot(x, y)
plt.title('Графік функції y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# Завдання 8: Побудувати графіки функцій `y = sin(x)` та `y = cos(x)` на відрізку [-2π, 2π]
# Hint: np.pi, np.linspace(), np.sin(), np.cos()
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.title('Графіки функцій sin(x) та cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


# Завдання 9: Побудувати графік залежності y від x з випадковим розподілом точок
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y)
plt.title('Випадкова точкова діаграма')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Завдання 10: Побудувати два графіки у двох окремих під-графіках (subplots) залежності sin(x) та cos(x) на відрізку [-2π, 2π]
fig, axs = fig, axs = plt.subplots(1, 2, figsize=(10, 5))

x = np.linspace(-2*np.pi, 2*np.pi, 100)

y1 = np.sin(x)
y2 = np.cos(x)

axs[0].plot(x, y1)
axs[0].set_title('sin(x)')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')

axs[1].plot(x, y2)
axs[1].set_title('cos(x)')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')

plt.tight_layout()
plt.show()