import json
import xml.etree.ElementTree as ET

# Чтение данных из JSON
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Создание корневого элемента XML
root = ET.Element("people")

for person in data:
    # Создаем элемент для каждого человека
    person_elem = ET.SubElement(root, "person")
    for key, value in person.items():
        # Создаем подэлемент для каждого атрибута человека
        child = ET.SubElement(person_elem, key)
        child.text = str(value)

# Запись данных в XML файл
tree = ET.ElementTree(root)
tree.write("data.xml", encoding="utf-8", xml_declaration=True)
