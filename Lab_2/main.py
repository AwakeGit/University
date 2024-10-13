def calculate_total_price(store_data, shopping_list):
    """
    Рассчитывает общую стоимость покупок для переданного магазина
    на основе списка покупок пользователя.
    """
    total = 0
    for item in shopping_list:
        if item in store_data:
            total += store_data[item]['price'] * shopping_list[item]
    return total


if __name__ == '__main__':
    products = {
        'Магазин 1': {
            'Молоко': {
                'price': 95,
                'count': 1
            },
            'Хлеб': {
                'price': 50,
                'count': 1
            },
            'Яблоки': {
                'price': 120,
                'count': 1
            },
            'Картофель': {
                'price': 30,
                'count': 1
            },
            'Мясо': {
                'price': 450,
                'count': 1
            }
        },
        'Магазин 2': {
            'Молоко': {
                'price': 100,
                'count': 1
            },
            'Хлеб': {
                'price': 52,
                'count': 1
            },
            'Груши': {
                'price': 130,
                'count': 1
            },
            'Картофель': {
                'price': 32,
                'count': 1
            },
            'Курица': {
                'price': 300,
                'count': 1
            }
        },
        'Магазин 3': {
            'Молоко': {
                'price': 90,
                'count': 1
            },
            'Хлеб': {
                'price': 48,
                'count': 1
            },
            'Яблоки': {
                'price': 115,
                'count': 1
            },
            'Картофель': {
                'price': 28,
                'count': 1
            },
            'Мясо': {
                'price': 470,
                'count': 1
            }
        },
        'Магазин 4': {
            'Молоко': {
                'price': 110,
                'count': 1
            },
            'Хлеб': {
                'price': 49,
                'count': 1
            },
            'Яблоки': {
                'price': 118,
                'count': 1
            },
            'Бананы': {
                'price': 85,
                'count': 1
            },
            'Курица': {
                'price': 310,
                'count': 1
            }
        },
        'Магазин 5': {
            'Молоко': {
                'price': 92,
                'count': 1
            },
            'Хлеб': {
                'price': 55,
                'count': 1
            },
            'Апельсины': {
                'price': 140,
                'count': 1
            },
            'Картофель': {
                'price': 31,
                'count': 1
            },
            'Мясо': {
                'price': 460,
                'count': 1
            }
        }
    }

    shopping_list = {}
    print(
        "Введите список товаров, которые вы собираетесь купить (нажмите Enter для завершения ввода):")

    while True:
        item = input("Товар: ")
        if not item:
            break
        count = int(input(f"Количество {item}: "))
        shopping_list[item] = count

    if not shopping_list:
        print("Список покупок пуст!")
        exit()

    # Расчет стоимости покупок в каждом магазине
    cheapest_store = None
    most_expensive_store = None
    min_price = float('inf')
    max_price = float('-inf')

    for store, items in products.items():
        total_price = calculate_total_price(items, shopping_list)

        # Поиск самого дешевого магазина
        if total_price < min_price:
            min_price = total_price
            cheapest_store = store

        # Поиск самого дорогого магазина
        if total_price > max_price:
            max_price = total_price
            most_expensive_store = store

        print(f"Магазин: {store}, Общая стоимость: {total_price} руб.")

    print(
        f"\nСамый дешевый магазин: {cheapest_store}, Общая стоимость: {min_price} руб.")
    print(
        f"Самый дорогой магазин: {most_expensive_store}, Общая стоимость: {max_price} руб.")
