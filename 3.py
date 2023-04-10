import requests
from collections import Counter

# Получаем HTML-код страницы
url = 'https://www.python.org'
response = requests.get(url)
html = response.text

# Считаем частоту символов в HTML-коде
freq = Counter(html)

# Выводим результаты
print('Частота символов в HTML-коде страницы', url)
for char, count in freq.most_common():
    if char.isprintable() and not char.isspace():
        print(f'Символ "{char}" встречается {count} раз')