import json
import datetime

# Определяем функцию для обхода словаря и замены полей "updated"
def update_updated(obj):
    if isinstance(obj, dict):
        for key in obj:
            if key == "updated":
                obj[key] = datetime.datetime.now().isoformat()
            else:
                update_updated(obj[key])
    elif isinstance(obj, list):
        for item in obj:
            update_updated(item)

# Читаем JSON-файл
with open("file.json", "r") as f:
    data = json.load(f)

# Обходим словарь и заменяем поля "updated"
update_updated(data)

# Записываем обновленные данные в файл
with open("file_updated.json", "w") as f:
    json.dump(data, f)