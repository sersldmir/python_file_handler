'''File handler project. Made on Linux Ubuntu 22.04 
Capabilities:
- working with csv files and perfoming some operations with them (add, divide, subtract, multiply, compare columns; concatenating, splitting and merging) 
- pickling and unpickling files
- working with text files'''

# import csv, pickle
import pandas as pd
import numpy as np
from time import sleep

# custom data class
class My_data_class(object):
    def __init__(self, data, name):
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
                if format == 'txt':
                        with open(file_name+'.txt', mode='w') as file:
                                str_dt = data.to_string(index=False)
                                file.write(str_dt)
                        print(f'Data successfully saved in txt under the name {file_name+".txt"}!')
        except OSError:
            raise ValueError('Invalid file name!')
    
    # main save function
    def save_table(self, format='csv', max_rows=0):
        if max_rows < 0:
            max_rows = 0
        elif max_rows == 0 or max_rows == len(self.main_data):
                My_data_class.regular_save(self.main_data, format, self.name)
        else:
            amount_of_files = len(self.main_data) // max_rows
            if amount_of_files < len(self.main_data) / max_rows:
                amount_of_files+=1
            beginnig_of_the_slice, end_of_the_slice, file_num = 0, max_rows, 1
            for i in range(1, amount_of_files+1):
                My_data_class.regular_save(self.main_data[beginnig_of_the_slice:end_of_the_slice], format, self.name+f'-{file_num}')
                beginnig_of_the_slice+=max_rows
                end_of_the_slice+=max_rows
                file_num+=1
        
    

# creation of data from the programm itself or composing it from list of lists
def data_builder(contents=None):
    data = []
    if contents is not None:
        data_name= input('Input the name of the data without format:\n')
        data = contents
        return My_data_class(data, data_name)
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

exp_lst=[['Name', 'Age', 'Gender'],
        ['Ann', 98, 'Female'],
        ['Joe', 76, 'Male'],
        ['Cunt', None, 'Helicopter'],
        ['Damien', 67, 'Male'],
        ['Lisa', 66, 'Female']]

exp_df = data_builder(exp_lst)
print(exp_df)
exp_df.save_table(max_rows=5)
exp_df.save_table('txt')