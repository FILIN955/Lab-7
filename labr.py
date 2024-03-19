import numpy as np
import random
from time import perf_counter
import matplotlib.pyplot as plt


list1 = [random.randint(1, 100) for _ in range(1000000)]
list2 = [random.randint(1, 100) for _ in range(1000000)]
array1 = np.array(list1)
array2 = np.array(list2)

start_time = perf_counter()
result_list = [a * b for a, b in zip(list1, list2)]
end_time = perf_counter()
print(f"Время перемножения для стандартных списков: {end_time - start_time} секунд")

start_time = perf_counter()
result_array = np.multiply(array1, array2)
end_time = perf_counter()
print(f"Время перемножения для массивов NumPy: {end_time - start_time} секунд")

data = np.genfromtxt('data2.csv', delimiter=',')  # Получение данных из файла
hist = np.array(data[:, 1])[1:]

def hist1():
    plt.hist(hist, 100)       # Построение первой нормальной гистограммы
    plt.title('Гистограмма')
    plt.xlabel('hardness')
    plt.ylabel('значения')
    plt.grid()
    plt.show()

def hist2():
    plt.hist(hist, 100, density=True)       # Построение второй нормализованной гистограммы
    plt.title('Нормализованная гистограмма')
    plt.xlabel('hardness')
    plt.ylabel('Частота')
    plt.grid()
    plt.show()

print(f'Cреднеквадратичное отклонение - {np.std(hist)}')  # Вывод среднеквадратичного отклонения

def graph3d():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(x ** y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='coolwarm')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('3D - График sin(x^y')
    plt.show()


hist1()
hist2()
graph3d()
