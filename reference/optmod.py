#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from basemod import *
def concat(k,s):
    try:
        assert k[0]==s[0], 'Названия данных столбцов не совпадают!'
        assert len(k[0])==len(s[0]), 'Количества данных столбцов не совпадают!'
        u=[k[0]]
        for i in range (1,len(k)):
            u.append(k[i])
        for j in range (1,len(s)):
            u.append(s[j])
        save_tablecsv(u)
    except AssertionError as err:
        print(err)


# In[ ]:


def split(k,row_number=3):
    s=k[0]
    d,u=[s],[s]
    for i in range (1,row_number+1):
        d.append(k[i])
    save_tablecsv(d)
    for i in range (row_number+1,len(k)):
        u.append(k[i])
    save_tablecsv(u)


# In[ ]:


def load_w_ty(k,dic):
    for g in dic.keys():
        if type(g)==int:
            names=[h for h in range(len(list(dic.keys())))]
        else:
            names=k[0]
    g=0
    values=list(dic.values())
    while g<len(names):
        for i in range(1, len(k)):
            try:
                if values[g]=='int':
                    k[i][g]=int(k[i][g])
                elif values[g]=='float':
                    k[i][g]=float(k[i][g])
                elif values[g]=='bool':
                    if k[i][g]=='True':
                        k[i][g]=True
                    else:
                        k[i][g]=False
                elif values[g]=='str':
                    if k[i][g]=='' or k[i][g]==' ' or k[i][g]=='None':
                        k[i][g]=None 
            except ValueError:
                print(f'Значение - {k[i][g]} - в {g} столбце {i} строчке не соответствует заданному типу! Присваиваем ему None')
                k[i][g]=None
        g+=1
    return dic,k
    


# In[ ]:


def add(k):
    print_table(k)
    names=k[0]
    names.append('Результаты_сложения')
    an=input('С какими столбцами хотите сделать сложение? Формат ввода: столбец1 столбец2 и тд. Вводить названия столбцов')
    wished_columns=an.split()
    try:
        addlst=[names.index(i) for i in wished_columns]
        for i in range(1,len(k)):
            res=0
            for g in addlst:
                assert type(k[i][g])!=str, 'Нельза  строки'
                if type(k[i][g])==int or type(k[i][g])==float or type(k[i][g])==bool:
                    res+=k[i][g]
            k[i].append(res)
        print_table(k)
    except AssertionError as err:
        print(err)
    except ValueError:
        print('Ввели неправильные значения')


def sub(k):
    print_table(k)
    names=k[0]
    names.append('Результаты_вычитания')
    an=input('С какими столбцами хотите сделать вычитание? Формат ввода: столбец1 столбец2 и тд. Вводить названия столбцов')
    wished_columns=an.split()
    try:
        addlst=[names.index(i) for i in wished_columns]
        for i in range(1,len(k)):
            for g in addlst:
                assert type(k[i][g])!=str, 'Нельза строки'
                if addlst.index(g)==0:
                    if type(k[i][g])==int or type(k[i][g])==float or type(k[i][g])==bool:
                        res=k[i][g]
                else:
                    if type(k[i][g])==int or type(k[i][g])==float or type(k[i][g])==bool:
                        res-=k[i][g]
            k[i].append(res)
        print_table(k)
    except AssertionError as err:
        print(err)
    except ValueError:
        print('Ввели неправильные значения')
        
        
def mul(k):
    print_table(k)
    names=k[0]
    names.append('Результаты_умножения')
    an=input('С какими столбцами хотите сделать умножение? Формат ввода: столбец1 столбец2 и тд. Вводить названия столбцов')
    wished_columns=an.split()
    try:
        addlst=[names.index(i) for i in wished_columns]
        for i in range(1,len(k)):
            res=1
            for g in addlst:
                assert type(k[i][g])!=str, 'Нельза строки'
                if type(k[i][g])==int or type(k[i][g])==float or type(k[i][g])==bool:
                    res*=k[i][g]
            k[i].append(res)
        print_table(k)
    except AssertionError as err:
        print(err)
    except ValueError:
        print('Ввели неправильные значения')
        
        
def div(k):
    print_table(k)
    names=k[0]
    names.append('Результаты_деления')
    an=input('С какими столбцами хотите сделать деление? Формат ввода: столбец1 столбец2 и тд. Вводить названия столбцов')
    wished_columns=an.split()
    try:
        addlst=[names.index(i) for i in wished_columns]
        for i in range(1,len(k)):
            for g in addlst:
                assert type(k[i][g])!=str, 'Нельза строки'
                if addlst.index(g)==0:
                    if type(k[i][g])==int or type(k[i][g])==float or type(k[i][g])==bool:
                        res=k[i][g]
                else:
                    if type(k[i][g])==int or type(k[i][g])==float or type(k[i][g])==bool:
                        res/=k[i][g]
            k[i].append(res)
        print_table(k)
    except AssertionError as err:
        print(err)
    except ValueError:
        print('Ввели неправильные значения')
    except ZeroDivisionError:
        print('Деление на ноль')


# In[ ]:


def eq(k):
    print_table(k)
    names=k[0]
    res=[]
    an=input('С какими столбцами хотите сделать сравнение(только 2 столбца)? Формат ввода: столбец1=столбец2 и тд. Вводить названия столбцов')
    wished_columns=an.split()
    try:
        complst=[names.index(i) for i in wished_columns]
        assert len(complst)==2, 'Wrooong'
        for i in range(1,len(k)):
            try:
                if k[i][complst[0]]==k[i][complst[1]]:
                    res.append(True)
                else:
                    res.append(False)
            except TypeError:
                print('Нельзя сравнивать такие типы')
                res.append(None)
        return res
    except AssertionError as err:
        print(err)
    except ValueError:
        print('Ввели неправильные значения')
        
def gr(k):
    print_table(k)
    names=k[0]
    res=[]
    an=input('С какими столбцами хотите сделать сравнение(>)? Формат ввода: столбец1>столбец2 и тд. Вводить названия столбцов')
    wished_columns=an.split()
    try:
        complst=[names.index(i) for i in wished_columns]
        assert len(complst)==2, 'Wrooong'
        for i in range(1,len(k)):
            try:
                if k[i][complst[0]]>k[i][complst[1]]:
                    res.append(True)
                else:
                    res.append(False)
            except TypeError:
                print('Нельзя сравнивать такие типы')
                res.append(None)
        return res
    except AssertionError as err:
        print(err)
    except ValueError:
        print('Ввели неправильные значения')
        
def ls(k):
    print_table(k)
    names=k[0]
    res=[]
    an=input('С какими столбцами хотите сделать сравнение(<)? Формат ввода: столбец1<столбец2 и тд. Вводить названия столбцов')
    wished_columns=an.split()
    try:
        complst=[names.index(i) for i in wished_columns]
        assert len(complst)==2, 'Wrooong'
        for i in range(1,len(k)):
            try:
                if k[i][complst[0]]<k[i][complst[1]]:
                    res.append(True)
                else:
                    res.append(False)
            except TypeError:
                print('Нельзя сравнивать такие типы')
                res.append(None)
        return res
    except AssertionError as err:
        print(err)
    except ValueError:
        print('Ввели неправильные значения')
        
def ge(k):
    print_table(k)
    names=k[0]
    res=[]
    an=input('С какими столбцами хотите сделать сравнение(>=)? Формат ввода: столбец1 столбец2 и тд. Вводить названия столбцов')
    wished_columns=an.split()
    try:
        complst=[names.index(i) for i in wished_columns]
        assert len(complst)==2, 'Wrooong'
        for i in range(1,len(k)):
            try:
                if k[i][complst[0]]>=k[i][complst[1]]:
                    res.append(True)
                else:
                    res.append(False)
            except TypeError:
                print('Нельзя сравнивать такие типы')
                res.append(None)
        return res
    except AssertionError as err:
        print(err)
    except ValueError:
        print('Ввели неправильные значения')
    
def le(k):
    print_table(k)
    names=k[0]
    res=[]
    an=input('С какими столбцами хотите сделать сравнение(<=)? Формат ввода: столбец1 столбец2 и тд. Вводить названия столбцов')
    wished_columns=an.split()
    try:
        complst=[names.index(i) for i in wished_columns]
        assert len(complst)==2, 'Wrooong'
        for i in range(1,len(k)):
            try:
                if k[i][complst[0]]<=k[i][complst[1]]:
                    res.append(True)
                else:
                    res.append(False)
            except TypeError:
                print('Нельзя сравнивать такие типы')
                res.append(None)
        return res
    except AssertionError as err:
        print(err)
    except ValueError:
        print('Ввели неправильные значения')
        
def ne(k):
    print_table(k)
    names=k[0]
    res=[]
    an=input('С какими столбцами хотите сделать сравнение(!=)? Формат ввода: столбец1 столбец2 и тд. Вводить названия столбцов')
    wished_columns=an.split()
    try:
        complst=[names.index(i) for i in wished_columns]
        assert len(complst)==2, 'Wrooong'
        for i in range(1,len(k)):
            try:
                if k[i][complst[0]]!=k[i][complst[1]]:
                    res.append(True)
                else:
                    res.append(False)
            except TypeError:
                print('Нельзя сравнивать такие типы')
                res.append(None)
        return res
    except AssertionError as err:
        print(err)
    except ValueError:
        print('Ввели неправильные значения')
        


# In[ ]:


def filter_rows(k,bool_list, copy_table=False):
    bool_list.insert(0,'Head')
    res=[]
    i=0
    while i<=len(bool_list)-1:
        if bool_list[i]=='Head':
            res.append(k[i])
        if bool_list[i]==True:
            res.append(k[i])
        i+=1
    if copy_table==False:
        print_table(res)
    else:
        save_tablecsv(res)
    

