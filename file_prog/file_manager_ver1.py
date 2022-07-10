'''File handler project. Made on Linux Ubuntu 22.04 
Capabilities:
- working with csv files and perfoming some operations with them (add, divide, subtract, multiply, compare columns; concatenating, splitting and merging) 
- pickling and unpickling files
- working with text files'''

# import csv, pickle
import pandas as pd
import numpy as np
from time import sleep

# Custom class to work with data
class My_data_class(object):
    def __init__(self, data, name):
        self.rows=data
        self.columns=[[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
        self.main_data=pd.DataFrame({k: v for k,v in zip(data[0],[[data[j][i] for j in range(1,len(data))] for i in range(len(data[0]))])})
        self.name=name


    def __repr__(self):
        return self.main_data.to_string(index=False)

    # method for saving data in different formats, apart from .txt
    @staticmethod
    def regular_save(data, format, file_name):
        try:
            if format == 'csv':
                data.to_csv(file_name +'.csv', index = False)
                print(f'Data successfully saved in csv file under the name: {file_name + ".csv"}!')
            if format == 'pickle':
                data.to_pickle(file_name +'.pkl')
                print(f'Data successfully pickled under the name: {file_name + ".pkl"}!')
        except OSError:
            raise ValueError('Invalid file name!')

    # method for saving data in .txt
    @staticmethod
    def regular_txt_save(data, file_name):
        try:
            with open(file_name, mode='w') as file:
                for line in data:
                    file.write('\t'.join([str(i) for i in line])+'\n')
            print(f'Data successfully saved in txt under the name {file_name+".txt"}!')
        except OSError:
            raise ValueError('Invalid file name!')
    
    def save_table(self, format='csv', max_rows=0):
        if max_rows < 0:
            max_rows = 0
        elif max_rows == 0:
            if format != 'txt':
                My_data_class.regular_save(self.main_data, format, self.name)
            else:
                My_data_class.regular_txt_save(self.rows, self.name)
        else:
            ...
        
    

# creation of data from the programm itself
def data_builder():
    data = []
    while True:
        try:
            titles=input("Input the titles' names with space as separators\n")
            print('Processing titles....')
            sleep(0.6)
            list_of_titles=titles.split()
            assert not '' in list_of_titles or not ' ' in list_of_titles, "Got empty titles!"
            data.append(list_of_titles)
            while True:
                raw_values = input('Input values with space as separators. If one of your values is empty, type "None". If you are done with inserting values, press Enter without typing anything\n')
                print('Processing values...')
                sleep(0.6)
                try:
                    if raw_values == '':
                        data_name= input('Input the name of the data without format:\n')
                        return My_data_class(data, data_name)
                    else:
                        values=[i.strip() for i in raw_values.split()]
                        assert len(values)==len(list_of_titles), "The amount of values does not correspond with the amount of titles!"
                        data.append([np.nan if i=='None' else i for i in values])
                except AssertionError as err:
                    print(err)
        except AssertionError as err:
            print(err)
        
# testing data_builder()
# test1=data_builder()
# print(test1)


# testing saving data
# test2=data_builder()
# test2.save_table('csv', 0)
# test2.save_table('pickle', 0)
# test2.save_table('txt', 0)