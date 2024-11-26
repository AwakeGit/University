import threading
import time


def compute_formula1(x_values, results1):
    for x in x_values:
        f1 = x ** 2 - x ** 2 + x ** 4 - x ** 5 + x + x
        results1.append(f1)


def compute_formula2(x_values, results2):
    for x in x_values:
        f2 = x + x
        results2.append(f2)


def compute_formula3(results1, results2, results3):
    for f1, f2 in zip(results1, results2):
        f3 = f1 + f2
        results3.append(f3)


def main(n_iterations):
    x_values = range(1, n_iterations + 1)
    results1 = []
    results2 = []
    results3 = []

    # Шаги 1 и 2: Параллельные вычисления формул 1 и 2
    start_time_step1_2 = time.time()

    thread1 = threading.Thread(target=compute_formula1, args=(x_values, results1))
    thread2 = threading.Thread(target=compute_formula2, args=(x_values, results2))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time_step1_2 = time.time()
    duration_step1 = end_time_step1_2 - start_time_step1_2

    # Шаг 3: Вычисление формулы 3
    start_time_step3 = time.time()
    compute_formula3(results1, results2, results3)
    end_time_step3 = time.time()
    duration_step3 = end_time_step3 - start_time_step3

    total_duration = duration_step1 + duration_step3

    print(f"Результаты для {n_iterations} итераций:")
    print(f"Шаги 1 и 2 (параллельно): {duration_step1:.6f} секунд")
    print(f"Шаг 3: {duration_step3:.6f} секунд")
    print(f"Общее время: {total_duration:.6f} секунд\n")


if __name__ == "__main__":
    print("Задание 1: Использование потоков\n")
    main(10000)
    main(100000)
