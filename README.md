## Утилита для поиска колючевых слов в стандартных логах

## Использование
Изменить в файле main.py нужные параметры (пример выше) и запутить main.py

path - задаем путь где будем искать фалы которые подходят под регулярку regexp_file

regexp_file - регулярка для поиска нужных файлов с логами

search_text - type list. Можно указать дату и часть текста которую мы ищем (можно и просто часть текста или дату)

except_pattern - type list. Эти паттерны нужны для определения конца строки search_text
так как ошибка может записываться многострочно в лог, при сработке этих регулярок перестает выводиться на экран
нужное сообщение (типо поняли конец message)

Патерны под капотом формируются как и прописные так и заглавные, поэтому будут искать и те и те вхождения. 
Скрипт работает на python3.6+



path = os.path.split(sys.argv[0])[0]

regexp_file = '\d*\D*.log'

search_text = ['2019-12-05', 'error'] 

except_pattern = ['DEBUG', 'INFO', 'WARNING', 'CRITITCAL'] 
