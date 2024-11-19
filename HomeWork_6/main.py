import csv
import json

# Пути к файлам
visit_log_file = 'visit_log__1_.csv'
purchases_file = 'purchase_log.txt'
output_file = 'funnel.csv'

# Шаг 1. Загрузим данные из JSON-файла в словарь
purchases = {}
with open(purchases_file, 'r', encoding='utf-8') as f:
    for line in f:
        record = json.loads(line.strip())
        if record.get("user_id") != "user_id":  # Пропустить заголовок
            purchases[record["user_id"]] = record["category"]

# Шаг 2. Обработаем visit_log.csv и запишем совпадающие строки в funnel.csv
with open(visit_log_file, 'r', encoding='utf-8') as visit_log, \
        open(output_file, 'w', newline='', encoding='utf-8') as funnel:
    reader = csv.reader(visit_log)
    writer = csv.writer(funnel)

    # Записываем заголовок в output файл
    writer.writerow(["user_id", "source", "category"])

    # Построчная обработка visit_log.csv
    for row in reader:
        if row[0] == "user_id":  # Пропустить заголовок
            continue
        user_id, source = row
        category = purchases.get(user_id)  # Проверить наличие покупки
        if category:  # Если покупка есть, записать строку в funnel.csv
            writer.writerow([user_id, source, category])

print(f"Файл '{output_file}' успешно создан.")
