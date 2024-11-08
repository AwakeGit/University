from datetime import datetime

# Определение форматов для каждой газеты
date_formats = {
    "The Moscow Times": "%A, %B %d, %Y",  # Wednesday, October 2, 2002
    "The Guardian": "%A, %d.%m.%y",  # Friday, 11.10.13
    "Daily News": "%A, %d %B %Y"  # Thursday, 18 August 1977
}


def parse_date(input_str):
    for newspaper, date_format in date_formats.items():
        try:
            date = datetime.strptime(input_str, date_format)
            print(f"{newspaper}: {date}")
            return date
        except ValueError:
            continue
    print("Дата не соответствует ни одному формату. Попробуйте снова.")


# Основной цикл программы
print("Введите дату в формате газеты или 'exit' для завершения.")
while True:
    user_input = input("Дата: ")
    if user_input.lower() == "exit":
        break
    parse_date(user_input)
