import re


class CarNumberValidator:
    """
    Класс для проверки валидности номера.

    Формат номера:
        1 буква из допустимого списка, 3 цифры, 2 буквы, 2-3 цифры (регион).

    Атрибуты:
        car_number (str): Номер для проверки.
    """

    # Допустимые буквы в номерах (кириллица)
    ALLOWED_LETTERS = "АВЕКМНОРСТУХ"

    def __init__(self, car_number):
        """
        Инициализация объекта CarNumberValidator.

        Args:
            car_number (str): Номер для проверки.
        """
        self.car_number = car_number

    def is_valid(self):
        """
        Проверяет, соответствует ли номер формату.

        Returns:
            bool: True, если номер валиден, иначе False.
        """
        pattern = re.compile(
            rf"^[{self.ALLOWED_LETTERS}]{{1}}\d{{3}}[{self.ALLOWED_LETTERS}]{{2}}\d{{2,3}}$"
        )
        return bool(pattern.match(self.car_number))

    def extract_number_and_region(self):
        """
        Возвращает номер и регион, если номер валиден.

        Returns:
            str: Сообщение о валидности номера и регионе или об ошибке.
        """
        if self.is_valid():
            number = self.car_number[:-2]
            region = (
                self.car_number[-2:]
                if self.car_number[-3].isdigit()
                else self.car_number[-3:]
            )
            return f"Номер {number} валиден. Регион: {region}."
        return "Номер не валиден."


class DuplicateWordRemover:
    """
    Класс для удаления последовательных повторов слов в строке.

    Атрибуты:
        text (str): Исходная строка.
    """

    def __init__(self, text):
        """
        Инициализация объекта DuplicateWordRemover.

        Args:
            text (str): Строка для обработки.
        """
        self.text = text

    def remove_duplicates(self):
        """
        Удаляет последовательные повторы слов из строки.

        Returns:
            str: Строка без повторов.
        """
        pattern = r"\b(\w+)(\s+\1\b)+"
        return re.sub(pattern, r"\1", self.text)


# Основной блок программы
if __name__ == "__main__":
    # Задача 1: Проверка номера
    car_id1 = "А222ВС96"
    car_id2 = "АБ22ВВ193"

    validator1 = CarNumberValidator(car_id1)
    validator2 = CarNumberValidator(car_id2)

    print(validator1.extract_number_and_region())  # Номер А222ВС валиден. Регион: 96.
    print(validator2.extract_number_and_region())  # Номер не валиден.

    # Задача 2: Удаление повторов слов
    some_string = "Напишите функцию функцию, которая будет будет будет удалять все все повторы слов слов из из строки."
    remover = DuplicateWordRemover(some_string)
    result = remover.remove_duplicates()
    print(result)
