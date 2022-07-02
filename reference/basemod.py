#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pickle
import csv


def create_tabledata():
    res = []
    while True:
        try:
            names = input(
                'Введите название заголовков через запятую:\n*Если хотите пустую ячейку, вводите пробел(так же через запятую.)')
            assert not names == '' and not names == ' ', "ошибка. если хотите ввести пустую ячейку, ставьте пробел(так же через запятую.)"
            n = names.split(',')
            y = []
            for i in n:
                if i == ' ' or i == '':
                    y.append(None)
                else:
                    y.append(i)
            res.append(y)
            while True:
                transit = input(
                    'Введите значения ячеек через запятую. Когда решите закончить, нажмите сразу Enter \n*Если вы хотите ввеси пустую ячейку, ставьте вместо символа пробел(так же через запятую)')
                try:
                    if transit == '':
                        return res
                    else:
                        assert len(transit.split(',')) == len(
                            n), 'Значений больше либо меньше, чем количество объявленных ячеек!!'
                        t = transit.split(',')
                        k = []
                        for i in t:
                            if i == ' ' or i == '':
                                k.append(None)
                            else:
                                k.append(i)
                        res.append(k)
                except AssertionError as err:
                    print(err)
        except AssertionError as err:
            print(err)
        else:
            return res
            break


def save_tablecsv(n, max_rows=0):
    try:
        names = n[0]
        if max_rows == 0:
            while True:
                try:
                    x = input('Введите название файла с расширением:\n')
                    assert '.csv' in x, 'Неверный формат файла '
                    with open(x, mode='w', encoding='1251') as f:
                        file_writer = csv.writer(
                            f, delimiter=';', lineterminator='\r')
                        file_writer.writerow(names)
                        for i in range(1, len(n)):
                            file_writer.writerow(n[i])
                    print('Запись в значений в файл закончена')
                    break
                except AssertionError as err:
                    print(err)
                except OSError:
                    print('Ошибка. Недопустимые символы в названии файла')
        else:
            numrow = len(n)-1
            assert max_rows >= 0, 'Отрицательное число'
            assert type(max_rows) == int, 'Вещественное число'
            num = numrow//max_rows
            num_p = numrow/max_rows
            be = 1
            en = be+max_rows
            if num_p > num:
                num += 1
            for i in range(1, num+1):
                while True:
                    try:
                        x = input('Введите название файла без расширения:\n')
                        assert '.csv' not in x, 'Введите название без расширения!'
                        with open(x+str(i)+'.csv', mode='w', encoding='1251') as u:
                            file_w = csv.writer(
                                u, delimiter=';', lineterminator='\r')
                            file_w.writerow(names)
                            for q in range(be, en):
                                file_w.writerow(n[q])
                            be += max_rows
                            en += max_rows
                            if be > len(n)-1:
                                be = len(n)-1
                            if en > len(n)-1:
                                en = len(n)
                        print('Разбивка окончена. Результаты сохранены')
                        break
                    except AssertionError as err:
                        print(err)
                    except OSError:
                        print('Ошибка. Недопустимые символы в названии файла')
    except AssertionError as err:
        print(err)


def load_tablecsv(*args):
    lst = [i for i in args]
    res, transit = [], []
    try:
        for i in range(len(lst)):
            with open(lst[i], encoding='1251') as f:
                file_reader = csv.reader(f, delimiter=";")
                for g in file_reader:
                    k = []
                    for i in g:
                        if i == '' or i == ' ':
                            k.append(None)
                        else:
                            k.append(i)
                    transit.append(g)
                for g in range(len(transit)):
                    if transit[g] not in res:
                        res.append(transit[g])
        return res
    except FileNotFoundError:
        print('файл не найден')


# In[ ]:

def save_tablepickle(n, max_rows=0):
    try:
        if max_rows == 0:
            while True:
                try:
                    x = input('Введите название файла\n')
                    with open(x, mode='wb') as f:
                        pickle.dump(n, f)
                    print('Запись в значений в файл закончена')
                    break
                except OSError:
                    print('Ошибка. Недопустимые символы в названии файла')
        else:
            numrow = len(n)-1
            assert max_rows >= 0, 'Отрицательное число'
            assert type(max_rows) == int, 'Вещественное число'
            num = numrow//max_rows
            num_p = numrow/max_rows
            be = 1
            en = be+max_rows
            names = n[0]
            res = []
            res.append(names)
            if num_p > num:
                num += 1
            for i in range(1, num+1):
                while True:
                    try:
                        x = input('Введите название файла без расширения:\n')
                        with open(x+str(i), mode='wb') as u:
                            for q in range(be, en):
                                res.append(n[q])
                            pickle.dump(res, u)
                            be += max_rows
                            en += max_rows
                            if be > len(n)-1:
                                be = len(n)-1
                            if en > len(n)-1:
                                en = len(n)
                        print('Разбивка окончена. Результаты сохранены')
                        break
                    except AssertionError as err:
                        print(err)
                    except OSError:
                        print('Ошибка. Недопустимые символы в названии файла')
    except AssertionError as err:
        print(err)


def load_tablepickle(*args):
    lst = [i for i in args]
    res, transit = [], []
    try:
        for i in range(len(lst)):
            with open(lst[i], mode='rb') as f:
                file_reader = pickle.loads(f.read())
                for i in file_reader:
                    for g in i:
                        k = []
                        if g == '' or g == ' ':
                            k.append(None)
                        else:
                            k.append(g)
                    transit.append(i)
                for g in range(len(transit)):
                    if transit[g] not in res:
                        res.append(transit[g])
        return res
    except FileNotFoundError:
        print('файл не найден')


# In[ ]:


def save_tabletxt(n, max_rows=0):
    try:
        if max_rows == 0:
            while True:
                try:
                    x = input('Введите название файла\n')
                    with open(x, mode='w') as f:
                        for l in n:
                            for i in l:
                                tr = ','.join(str(i) for i in l)
                            f.write(tr+'\n')
                    print('Запись в значений в файл закончена')
                    break
                except OSError:
                    print('Ошибка. Недопустимые символы в названии файла')
        else:
            numrow = len(n)-1
            assert max_rows >= 0, 'Отрицательное число'
            assert type(max_rows) == int, 'Вещественное число'
            num = numrow//max_rows
            num_p = numrow/max_rows
            be = 1
            en = be+max_rows
            names = n[0]
            res = []
            res.append(names)
            if num_p > num:
                num += 1
            for i in range(1, num+1):
                while True:
                    try:
                        x = input('Введите название файла без расширения:\n')
                        with open(x+str(i), mode='w') as u:
                            for q in range(be, en):
                                res.append(n[q])
                            for l in res:
                                for i in l:
                                    tr = ','.join(str(i) for i in l)
                                u.write(tr+'\n')
                            be += max_rows
                            en += max_rows
                            if be > len(n)-1:
                                be = len(n)-1
                            if en > len(n)-1:
                                en = len(n)
                            res = []
                            res.append(names)
                        print('Разбивка окончена. Результаты сохранены')
                        break
                    except AssertionError as err:
                        print(err)
                    except OSError:
                        print('Ошибка. Недопустимые символы в названии файла')
    except AssertionError as err:
        print(err)


def load_tabletxt(*args):
    lst = [i for i in args]
    res, transit = [], []
    try:
        for i in range(len(lst)):
            with open(lst[i], mode='r') as f:
                for i in f:
                    i = i.strip()
                    transit.append(i.split(','))
                for g in range(len(transit)):
                    if transit[g] not in res:
                        res.append(transit[g])
        return res
    except FileNotFoundError:
        print('файл не найден')


# In[ ]:


def get_rows_by_number(k, start, stop=0, copy_table=False):
    try:
        assert stop >= 0, 'Неверно задан конец интервала записи'
        res = []
        names = k[0]
        if stop == 0:
            transit = k[start]
            res.append(names)
            for i in transit:
                res.append(i)
            if copy_table == True:
                save_tablecsv(res)
            else:
                print_table(res)
        else:
            transit = k[start:stop+1]
            res.append(names)
            for i in transit:
                res.append(i)
            if copy_table == True:
                save_tablecsv(res)
            else:
                print_table(res)

    except AssertionError as err:
        print(err)


# In[ ]:


def get_rows_by_index(k, *val, copy_table=False):
    g = [i for i in val]
    try:
        assert len(g) <= len(k)-1, 'Выход за пределы таблицы!'
        res = []
        names = k[0]
        res.append(names)
        col = 0
        for i in range(len(g)):
            for h in range(1, len(k)):
                if g[i] == k[h][col]:
                    res.append(k[h])
        if copy_table == True:
            save_tablecsv(res)
        else:
            print_table(res)
    except AssertionError as err:
        print(err)


# In[ ]:


def get_column_types(k, by_number=False):
    def is_float(x_):
        count_ = 0
        x = x_[1:len(x_)]
        if x_[0] != '.' and not(x_[0].isdigit() and x_[0] != '-'):
            return False
        for i in x:
            if i != '.' and not i.isdigit():
                return False
            if i == '.':
                count_ += 1
            if count_ > 1:
                return False
        return True

    def is_digit(x_):
        x = x_[1:len(x_)]
        if not x_[0].isdigit() and x_[0] != '-':
            return False
        for i in x:
            if not i.isdigit():
                return False
        return True

    if by_number == False:
        key = k[0]
    else:
        key = [i for i in range(len(k[0]))]
    value = []
    for i in range(len(k[1])):
        if is_digit(k[1][i]) == False:
            if is_float(k[1][i]):
                value.append('float')
        else:
            value.append('int')
        if k[1][i] == 'True' or k[1][i] == 'False':
            value.append('bool')
        if is_digit(k[1][i]) == False and is_float(k[1][i]) == False and not(k[1][i] == 'True' or k[1][i] == 'False'):
            value.append('str')
    dic = {k: v for k, v in zip(key, value)}
    return dic


# In[ ]:


def set_column_types(k, dic, by_number=False):
    def is_float(x_):
        count_ = 0
        x = x_[1:len(x_)]
        if x_[0] != '.' and not(x_[0].isdigit() and x_[0] != '-'):
            return False
        for i in x:
            if i != '.' and not i.isdigit():
                return False
            if i == '.':
                count_ += 1
            if count_ > 1:
                return False
        return True

    def is_digit(x_):
        x = x_[1:len(x_)]
        if not x_[0].isdigit() and x_[0] != '-':
            return False
        for i in x:
            if not i.isdigit():
                return False
        return True

    if by_number == False:
        keys = [i for i in dic.keys()]
        for i in range(len(keys)):
            keys[i] = k[0][i]
    else:
        keys = [i for i in range(len(k[0]))]
        for i in range(len(keys)):
            keys[i] = k[0][i]
    value = [i for i in dic.values()]
    print('Исходный словарь')
    print({f: g for f, g in zip(keys, value)})
    for i in range(len(value)):
        print(f'Вы хотите поменять тип столбца {keys[i]}?')
        while True:
            try:
                answer = input('Введите ваш ответ "Да" или "Нет":\n')
                assert answer == 'Да' or answer == 'Нет', 'Не тот ответ. Введите ещё раз'
            except AssertionError as err:
                print(err)
            else:
                break
        if answer == 'Да':
            print('''Поддерживаемые значения:
                Bool - логический тип
                Int - целое число
                Float - вещественное число
                Str - текст
                ''')
            while True:
                try:
                    ty = input('Тип?\n')
                    assert ty == 'Bool' or ty == 'Int' or ty == 'Float' or ty == 'Str', 'Wrong Format'
                except AssertionError as err:
                    print(err)
                else:
                    break
            if ty == 'Bool':
                value[i] = 'bool'
            elif ty == 'Int':
                value[i] = 'int'
            elif ty == 'Float':
                value[i] = 'float'
            elif ty == 'Str':
                value[i] = 'str'
    res = {ke: va for ke, va in zip(keys, value)}
    return res


# In[ ]:


def get_values(k, column=0):
    try:
        assert column <= len(k[0])-1, 'Выход за пределы таблицы!'
        res = []
        for i in range(1, len(k)):
            res.append(k[i][column])
        print(res)
    except AssertionError as err:
        print(err)


# In[ ]:


def get_value(k, column=0):
    try:
        res = []
        res.append(k[1][column])
        print(res)
    except AssertionError as err:
        print(err)


# In[ ]:


def set_values(k, values, column=0):
    try:
        assert column <= len(k[0])-1, 'Выход за пределы таблицы!'
        assert len(values) <= len(k)-1, 'Выход за пределы таблицы!'
        print(f'Будут произведены изменения в колонке {k[0][column]}')
        values.insert(0, k[0][column])
        for i in range(len(values)):
            k[i][column] = values[i]
        print(k)
        save_tablecsv(k)
    except AssertionError as err:
        print(err)


# In[ ]:


def set_value(k, value, column=0):
    if value == '' or value == ' ' or value == 'None':
        value = None
    try:
        assert column <= len(k[0])-1, 'Выход за пределы таблицы!'
        print(f'Будут произведены изменения в колонке {k[0][column]}')
        k[1][column] = value
        save_tablecsv(k)
    except AssertionError as err:
        print(err)


# In[ ]:


def print_table(k):
    for i in k:
        print(i)


# In[ ]:
