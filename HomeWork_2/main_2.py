def match_pairs(boys, girls):
    # Проверяем, равное ли количество юношей и девушек
    if len(boys) != len(girls):
        print("Внимание, кто-то может остаться без пары.")
        return

    # Сортируем списки юношей и девушек по алфавиту
    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)

    print("Идеальные пары:")
    # Перебираем пары с одинаковыми индексами и выводим их
    for boy, girl in zip(boys_sorted, girls_sorted):
        print(f"{boy} и {girl}")


# Пример 1
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

match_pairs(boys, girls)

print()

# Пример 2
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

match_pairs(boys, girls)
