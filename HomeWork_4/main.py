def hanoi(n, start, auxiliary, target, moves):
    """Рекурсивный алгоритм для решения задачи Ханойской башни."""
    if n == 1:
        moves.append((n, start, target))
        return

    hanoi(n - 1, start, target, auxiliary, moves)
    moves.append((n, start, target))
    hanoi(n - 1, auxiliary, start, target, moves)


def input_data():
    """Запрашивает у пользователя количество дисков."""
    while True:
        try:
            n = int(input("Введите количество дисков: "))
            if n < 1:
                print("Количество дисков должно быть больше нуля.")
            else:
                return n
        except ValueError:
            print("Пожалуйста, введите целое число.")


def print_moves(moves):
    """Выводит последовательность ходов в консоль."""
    for disk, start, target in moves:
        print(f"Диск {disk}: Стержень {start} -> Стержень {target}")


def save_to_file(moves, filename="решение.txt"):
    """Сохраняет последовательность ходов в текстовый файл."""
    with open(filename, "w", encoding="utf-8") as file:
        for disk, start, target in moves:
            file.write(f"Диск {disk}: Стержень {start} -> Стержень {target}\n")


def main():
    print("Задача Ханойская башня.")
    n = input_data()
    moves = []
    hanoi(n, 1, 2, 3, moves)
    print("\nРешение:")
    print_moves(moves)
    save_to_file(moves)


if __name__ == "__main__":
    main()
