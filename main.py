# -*- coding:utf-8 -*-
import os
import re
import sys
import time


def logParser_initHelper(**kwargs):
    if len(kwargs['search_text']) == 0:
        print(f'(List) "search_text" not be empty')
        sys.exit(1)
    elif len(kwargs['except_pattern']) == 0:
        print(f'(List) "except_pattern" not be empty')
        sys.exit(1)
    elif kwargs['regexp_file'] == '' or kwargs['regexp_file'] == None:
        print(f'(Str) "regexp_file" not be empty')
        sys.exit(1)
    return True


def logParser_swapcaseString(catalog):
    return [format_text(text) for format_text in [str.upper, str.lower] for text in catalog]


def logParser(path, regexp_file, search_text, except_pattern):
    if path == '': path = './'
    if logParser_initHelper(regexp_file=regexp_file, search_text=search_text, except_pattern=except_pattern):
        for owndir, subdir, files in os.walk(path, False):
            for file in files:
                if re.compile(regexp_file).search(file) != None:
                    input_result = input(f'Open file: {os.path.join(owndir, file)}? \nY/N or EXIT \n')
                    if input_result.lower() == 'y':
                        pattern = [re.compile(txt) for txt in logParser_swapcaseString(search_text)]
                        pattern_pass = [re.compile(txt) for txt in logParser_swapcaseString(except_pattern)]
                        with open(os.path.abspath(os.path.join(owndir, file)), 'r') as s:
                            lines_read = s.readlines()
                            for line in lines_read:
                                result_search = [rst.group() for rst in
                                                 [own_pattern.search(line) for own_pattern in pattern] if rst != None]
                                if len(result_search) > 0:
                                    print(line)
                                    for i in range(1, 10000):
                                        if (lines_read.index(line) + i) <= len(lines_read) - 1:
                                            tmp = [None for pattern_p in pattern_pass if
                                                   pattern_p.search(lines_read[lines_read.index(line) + i]) == None]
                                            if len(tmp) == len(pattern_pass):
                                                print(lines_read[lines_read.index(line) + i])
                                            else:
                                                break
                    elif input_result.lower() == 'exit':
                        print('User killed main app')
                        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    # '''
    # path = os.path.split(sys.argv[0])[0]  # home dir logParser
    #
    # regexp_file = '\d*\D*.log' # В каких файлах ищем (регуляркой парсим имя файла)
    #
    # search_text = ['2019-12-05', 'error'] # Что ищем
    #
    # except_pattern = ['DEBUG', 'INFO', 'WARNING', 'CRITITCAL'] # Эти паттерны нужны для определения конца строки search_text
    # так как ошибка может записываться многострочно в лог, при сработке этих регулярок перестает выводиться на экран
    # нужное сообщение (типо поняли конец message)
    # '''

    path = os.path.split(sys.argv[0])[0]
    regexp_file = '\d*\D*.log'
    search_text = ['error']
    except_pattern = ['DEBUG', 'INFO', 'WARNING', 'CRITITCAL', 'error']

    sys.exit(logParser(path, regexp_file, search_text, except_pattern))
