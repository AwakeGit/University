items = {
    'milk15': {'name': 'молоко 1.5%', 'count': 34, 'price': 89.9},
    'cheese': {'name': 'сыр молочный 1 кг.', 'count': 12, 'price': 990.9},
    'sausage': {'name': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
}

price_less_20 = {
    key: (True if items[key]['count'] < 20 else False) for key, val in
    items.items()
}

for i in price_less_20.items():
    print(*i)
