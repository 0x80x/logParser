# logParser
Утилита для поиска колючевых слов в стандартных логах


path = os.path.split(sys.argv[0])[0]  # home dir logParser

regexp_file = '\d*\D*.log' # В каких файлах ищем (регуляркой парсим имя файла)

search_text = ['2019-12-05', 'error'] # Что ищем

except_pattern = ['DEBUG', 'INFO', 'WARNING', 'CRITITCAL'] # Эти паттерны нужны для определения конца строки search_text
так как ошибка может записываться многострочно в лог, при сработке этих регулярок перестает выводиться на экран
нужное сообщение (типо поняли конец message)