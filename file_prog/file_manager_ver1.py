'''File handler project. Made on Linux Ubuntu 22.04 
Capabilities:
- working with csv files and perfoming some operations with them (add, divide, subtract, multiply, compare columns; concatenating, splitting and merging) 
- pickling and unpickling files
- working with text files'''

from typing import List, Union
from __future__ import annotations
import pandas as pd
import numpy as np
from time import sleep

class My_data_class(object):
    """Custom data class to work with data"""
    def __init__(self, data: Union[list, pd.DataFrame], name: str, type_data:str='list_of_lists') -> None:
        """Constructor. Receives either a list of lists or a DataFrame and its name
        taken from a user. Type_data parameter corresponds with the type of data received"""
        if type_data == 'list_of_lists':
            # self.main_data=pd.DataFrame({k: v for k,v in zip(data[0],[[data[j][i] for j in range(1,len(data))] for i in range(len(data[0]))])})
            self.main_data=pd.DataFrame(data[1:], columns=data[0])
        elif type_data == 'data_frame':
            self.main_data=data
        self.name=name

    def change_name(self, new_name:str) -> None:
        """Method that allows to change the name of your data"""
        assert type(new_name) == str, 'Name must be a string!'
        self.name = new_name

    def __repr__(self):
        """Printing method. Outputs DataFrame without indexes"""
        return self.main_data.to_string(index=False)

    def get_rows_by_number(self, start:int, end:int=0, alter_table:bool=False) -> Union[None, pd.DataFrame]:
        """Method for choosing rows the indexes of which are in range start:stop.
        Alter_table parameter allows the user to alter their current data or save results in a separate file"""
        assert 0 < start < len(self.main_data) and ((start <= end <= len(self.main_data)) or end==0), 'Wrong boundaries!'
        result=self.main_data.iloc[start:] if end == 0 else self.main_data.iloc[start:end+1]
        if alter_table==True:
            print('The data has been altered!!!')
            self.main_data = result
            print(self)
        if alter_table==False:
            return result
            # ask in a main program whether to save or not
            

    def get_rows_by_value(self, *values, alter_table:bool=False) -> Union[None, pd.DataFrame]:
        """Method for choosing rows the first values of which are *values.
        Alter_table parameter allows the user to alter their current data or save results in a separate file"""
        result=self.main_data.loc[self.main_data[self.main_data.columns[0]].isin(values)]
        if alter_table==True and not result.empty:
            print('The data has been altered!!!')
            self.main_data = result 
            print(self)
        if alter_table==False and not result.empty:
            return result
            # ask in a main program whether to save or not
        if result.empty:
            raise ValueError('Such values are not found!')
    
    def get_values(self, column:str) -> str:
        """Method for getting values out of a certain column in a DataFrame"""
        assert type(column)==str, 'Wrong type of value'
        assert column in self.main_data.columns, 'No such column'
        return self.main_data.loc[:, column].to_string(index=False)

    def set_values(self, column:str, *values) -> None: 
        """Method for setting values in a certain column in a DataFrame"""
        assert type(column)==str, 'Wrong type of value'
        assert column in self.main_data.columns, 'No such column'
        assert len(values)>0, 'No values!'
        for index, value in zip(range(len(values)), values): self.main_data.loc[index, column] = value
        print('Assignment successful!')
        print(self)

    def del_line(self, shoot_number:int) -> None:
        """Method for deleting a row in the DataFrame"""
        assert 0 < shoot_number < len(self.main_data), 'Wrong row number!'
        data_after_row_deletion=self.main_data.drop(shoot_number-1)
        data_after_row_deletion.index=range(len(self.main_data)-1)
        self.main_data=data_after_row_deletion
        print('Row deleted successfully!')
        print(self)

    def merge(self, another_table:My_data_class, true_merge:bool=False, by_number:bool=True) -> My_data_class:
        """Method for merging two My_data_class objects. If true_merge parameter is True, the objects merge like inner join in sql;
        otherwise like outer join. If by_number is true, the tables merge on index; if false - on the values of the first column 
        (in this case first columns of the two tables must be identical)"""
        if by_number==True:
            assert any([i in list(another_table.main_data.index) for i in list(self.main_data.index)]), 'Merge is impossible!'
            merge_res=pd.merge(self.main_data, another_table.main_data, how='outer' if true_merge==False else 'inner', left_index=True, right_index=True)
        if by_number==False:
            assert self.main_data.columns[0] == another_table.main_data.columns[0], 'Merge is impossible!'
            merge_res=pd.merge(self.main_data, another_table.main_data, how='outer' if true_merge==False else 'inner', on=self.main_data.columns[0])
        return My_data_class(merge_res, self.name+'_*_'+another_table.name, type_data='data_frame')
        # ask whether to save in the main program
    
    def concat(self, another_table:My_data_class) -> My_data_class:
        """Method for concetanating two tables aka My_Data_Class objects"""
        assert all(self.main_data.columns == another_table.main_data.columns), 'Columns do not match!'
        con_res=pd.concat(self.main_data, another_table.main_data)
        return My_data_class(con_res, self.name+'_+_'+another_table.name, type_data='data_frame')
        # ask whether to save in the main program
    
    def split(self, splitter:int=None) -> My_data_class:
        """Method for splitting a table into two tables with a splitter - index number"""
        assert 0 < splitter < len(self.main_data), 'Wrong splitter!'
        split_res1, split_res2 = self.main_data[:splitter+1], self.main_data[splitter+1:]
        return My_data_class(split_res1, self.name+f'_to_row_{splitter}', type_data='data_frame'), My_data_class(split_res2, self.name+f'_from_row_{splitter}', type_data='data_frame')
        # ask whether to save in the main program
    
    def compare(self, column_1:str, column_2:str, symbol:str) -> Union[list, pd.DataFrame]:
        """Method for comparing two columns in a My_data_class object. Supported comparions: >, <, ==, !=, <=, >= """
        assert column_1 in self.main_data.columns and column_2 in self.main_data.columns, 'Wrong columns!'
        assert symbol in ['==','<=','>=','!=','>','<'], 'Wrong comparison symbol!'
        transit_data_frame=self.main_data.copy(deep=True)
        if symbol=='==':
            bool_series=self.main_data[column_1]==self.main_data[column_2]
        elif symbol=='<=':
            bool_series=self.main_data[column_1]<=self.main_data[column_2]
        elif symbol=='>=':
            bool_series=self.main_data[column_1]>=self.main_data[column_2]
        elif symbol=='!=':
            bool_series=self.main_data[column_1]!=self.main_data[column_2]
        elif symbol=='>':
            bool_series=self.main_data[column_1]>self.main_data[column_2]
        elif symbol=='<':
            bool_series=self.main_data[column_1]<self.main_data[column_2]
        transit_data_frame[column_1+'_'+symbol+'_'+column_2]=bool_series
        return bool_series, transit_data_frame[[column_1, column_2, column_1+'_'+symbol+'_'+column_2]]
        

    def filter(self, bool_list:List[bool], alter_table:bool=False) -> Union[None, pd.DataFrame]:
        """Method for getting a DataFrame with a bool list or altering a current My_data_class object"""
        if alter_table==True:
            self.main_data=self.main_data.loc[bool_list]
        else:
            return self.main_data.loc[bool_list]
            # ask whether to save in the main program

    def column_math(self, column_1:str, column_2:str, symbol:str, alter_table:bool=False) -> Union[None, pd.DataFrame]:
        """Method for perfoming addition, subtraction, multiplication, division with two columns of the My_data_class object.
        If alter_table is True, the data will be altered; otherwise a copy will be made"""
        assert column_1 in self.main_data.columns and column_2 in self.main_data.columns, 'Wrong columns!'
        assert symbol in ['+', '-', '*', '/'], 'Wrong comparison symbol!'
        if symbol=='+':
            operator_res=self.main_data[column_1]+self.main_data[column_2]
        elif symbol=='-':
            operator_res=self.main_data[column_1]-self.main_data[column_2]
        elif symbol=='*':
            operator_res=self.main_data[column_1]*self.main_data[column_2]
        elif symbol=='/':
            operator_res=self.main_data[column_1]/self.main_data[column_2]
        if alter_table==True:
            self.main_data[column_1+'_'+symbol+'_'+column_2]=operator_res
            print(self)
        else:
            main_data_copy=self.main_data.copy(deep=True)
            main_data_copy[column_1+'_'+symbol+'_'+column_2]=operator_res
            return main_data_copy
        

    @staticmethod
    def regular_save(data:pd.DataFrame, format:str, file_name:str) -> None:
        """The static method saves data into a file.
        Supported formats: csv, pkl, txt"""
        try:
                if format == 'csv':
                        data.to_csv(file_name +'.csv', index = False)
                        print(f'Data successfully saved in csv file under the name: {file_name + ".csv"}!')
                if format == 'pickle':
                        data.to_pickle(file_name +'.pkl')
                        print(f'Data successfully pickled under the name: {file_name + ".pkl"}!')
                if format == 'txt':
                        with open(file_name+'.txt', mode='w') as file: file.write(data.to_string(index=False))
                        print(f'Data successfully saved in txt under the name {file_name+".txt"}!')
        except OSError:
            raise ValueError('Invalid file name!')
    
    # main save function
    def save_table(self, format:str='csv', max_rows:int=0) -> None:
        """Saves data into a file. Is able to split data into multiple files. 
        Supported formats: csv, txt, pkl"""
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
        
    

def data_builder(contents:list = None) -> My_data_class:
    """The function creates data either from user input or a ready list of lists and converts into an object of My_data_class"""
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

def load_data(file_name:str, format:str='csv') -> pd.DataFrame:
    """The function loads data from a file, which name is passed as an argument
    Supported formats: csv, pkl, txt"""
    try:
        if format == 'csv':
            data=pd.read_csv(file_name)
            return data
        if format == 'pickle':
            data=pd.read_pickle(file_name)
            return data
        if format == 'txt':
            with open('test_data.txt', mode = 'r') as file:
                data=[i.split() for i in file.read().split('\n')]
                return data
    except FileNotFoundError:
        print('File not found')
        raise

def load_existing_data(*file_names:str, format:str='csv') -> My_data_class:
    """The function loads data from existing files into a Pandas DataFrame.
    It can take unlimited amount of single format files and put it into one data frame
    Supported formats: txt, pkl, csv"""
    assert all(type(i)=='str' and format in i for i in file_names), ''
    if format == 'txt':
        for number, file in enumerate(file_names):
            transit_data=load_data(file, format)
            if number == 0:
                data=transit_data
            else:
                data.append([i for i in transit_data[1:]])
        print('Loading complete!')
        return My_data_class(data, input('Input the name of the data without format:\n'))
    else:
        if len(file_names) > 1:
            data=[load_data(file, format) for file in file_names]
            print('Loading complete!')
            return My_data_class(pd.concat(data, ignore_index=True), input('Input the name of the data without format:\n'), type_data='data_frame')
        else:
            data=load_data(file_names[0], format)
            print('Loading complete!')
            return My_data_class(data, input('Input the name of the data without format:\n'), type_data='data_frame')
            
# testing data_builder()
# test1=data_builder()
# print(test1)


# testing saving data
# test2=data_builder()
# test2.save_table('csv', 0)
# test2.save_table('pickle', 0)
# test2.save_table('txt', 0)

# exp_lst=[['Name', 'Age', 'Gender'],
#         ['Ann', 98, 'Female'],
#         ['Joe', 76, 'Male'],
#         ['Cunt', None, 'Helicopter'],
#         ['Damien', 67, 'Male'],
#         ['Lisa', 66, 'Female']]

# exp_df = data_builder(exp_lst)
# print(exp_df)
# exp_df.save_table(max_rows=2)
# exp_df.save_table('txt')
# exp_df.save_table('pickle')

# exp_pickle_data=load_existing_data('test_data.pkl', format='pickle')
# exp_txt_data=load_existing_data('test_data.txt', format='txt')
# exp_csv_data=load_existing_data('test_data-1.csv', 'test_data-2.csv', 'test_data-3.csv')
# print(exp_pickle_data)
# print('\n'*2)
# print(exp_txt_data)
# print('\n'*2)
# print(exp_csv_data)