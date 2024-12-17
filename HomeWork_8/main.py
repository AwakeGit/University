import pandas as pd


class CustomerDescriptionGenerator:
    """
    Класс для обработки CSV-файла с данными о покупателях и формирования текстового отчета.

    Атрибуты:
        input_file (str): Путь к входному CSV-файлу.
        output_file (str): Путь к выходному TXT-файлу.
        data (DataFrame): DataFrame с загруженными и обработанными данными.
    """

    def __init__(self, input_file: str, output_file: str):
        """
        Инициализация класса с путями к файлам.

        Аргументы:
            input_file (str): Путь к входному CSV-файлу.
            output_file (str): Путь к выходному TXT-файлу.
        """
        self.input_file = input_file
        self.output_file = output_file
        self.data = None

    def load_data(self):
        """
        Загрузка данных из CSV-файла в DataFrame.

        Исключения:
            Вызывает ошибку при невозможности загрузки файла.
        """
        try:
            self.data = pd.read_csv(self.input_file)
            print("Данные успешно загружены.")
        except Exception as e:
            print(f"Ошибка загрузки данных: {e}")
            raise

    def transform_data(self):
        """
        Преобразование данных для дальнейшей работы.

        Переименовывает колонки для удобного доступа к данным.
        Обрабатывает пропущенные значения и приводит текст к нужному виду.
        """

        self.data.rename(
            columns={
                "name": "ФИО",
                "sex": "Пол",
                "age": "Возраст",
                "device_type": "Устройство",
                "browser": "Браузер",
                "bill": "Сумма чека",
                "region": "Регион",
            },
            inplace=True,
        )

        # Заполняем пропущенные значения
        self.data = self.data.copy()
        self.data["Пол"] = self.data["Пол"].fillna("-")
        self.data["Возраст"] = self.data["Возраст"].fillna(0)
        self.data["Устройство"] = self.data["Устройство"].fillna(
            "неизвестного устройства"
        )
        self.data["Браузер"] = self.data["Браузер"].fillna("неизвестного браузера")
        self.data["Сумма чека"] = self.data["Сумма чека"].fillna(0)
        self.data["Регион"] = self.data["Регион"].fillna("-")

        print("Данные успешно преобразованы.")

    def generate_descriptions(self):
        """
        Генерация текстовых описаний для каждого покупателя по шаблону.

        Возвращает:
            list: Список строк с текстовыми описаниями.
        """
        descriptions = []

        for _, row in self.data.iterrows():

            gender_word = "мужского" if row["Пол"] == "male" else "женского"
            action_word = "совершил" if row["Пол"] == "male" else "совершила"

            device_word = {
                "mobile": "мобильного",
                "tablet": "планшетного",
                "laptop": "ноутбука",
                "desktop": "стационарного",
            }.get(row["Устройство"], row["Устройство"])

            # Формирование строки с описанием пользователя
            description = (
                f"Пользователь {row['ФИО']} {gender_word} пола, {int(row['Возраст'])} лет "
                f"{action_word} покупку на {row['Сумма чека']} у.е. с {device_word} браузера {row['Браузер']}. "
                f"Регион, из которого совершалась покупка: {row['Регион']}."
            )
            descriptions.append(description)
        print("Описания успешно сгенерированы.")
        return descriptions

    def save_descriptions(self, descriptions):
        """
        Сохранение текстовых описаний в выходной TXT-файл.

        Аргументы:
            descriptions (list): Список строк для записи в файл.

        Исключения:
            Вызывает ошибку при невозможности сохранения файла.
        """
        try:
            with open(self.output_file, "w", encoding="utf-8") as file:
                for description in descriptions:
                    file.write(description + "\n")
            print(f"Описания успешно сохранены в файл: {self.output_file}")
        except Exception as e:
            print(f"Ошибка сохранения файла: {e}")
            raise

    def run(self):
        """
        Основной метод, запускающий весь процесс:
        1. Загрузка данных.
        2. Преобразование данных.
        3. Генерация текстовых описаний.
        4. Сохранение описаний в файл.
        """
        self.load_data()
        self.transform_data()
        descriptions = self.generate_descriptions()
        self.save_descriptions(descriptions)


if __name__ == "__main__":

    input_path = "web_clients_correct.csv"
    output_path = "customer_descriptions.txt"

    generator = CustomerDescriptionGenerator(input_path, output_path)
    generator.run()
