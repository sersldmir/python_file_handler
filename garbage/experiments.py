from __future__ import annotations
from typing import Union
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
        self.name = new_name

    def __repr__(self):
        """Printing method. Outputs DataFrame without indexes"""
        return self.main_data.to_string(index=False)

    def get_rows_by_number(self, start:int, end:int=0, alter_table:bool=False) -> pd.DataFrame:
        """Method for choosing rows the indexes of which are in range start:stop.
        Alter_table parameter allows the user to alter their current data or save results in a separate file"""
        assert 0 < start < len(self.main_data) and ((start <= end <= len(self.main_data)) or end==0), 'Wrong boundaries!'
        result=self.main_data.iloc[start:] if end == 0 else self.main_data.iloc[start:end+1]
        if alter_table==True:
            print('The data has been altered!!!')
            self.main_data = result
            return self.main_data
        if alter_table==False:
            return result
            # ask in a main program whether to save or not
            

    def get_rows_by_value(self, *values, alter_table:bool=False) -> pd.DataFrame:
        """Method for choosing rows the first values of which are *values.
        Alter_table parameter allows the user to alter their current data or save results in a separate file"""
        result=self.main_data.loc[self.main_data[self.main_data.columns[0]].isin(values)]
        if alter_table==True and not result.empty:
            print('The data has been altered!!!')
            self.main_data = result 
            return self.main_data
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

    def set_values(self, column:str, *values) -> pd.DataFrame: 
        """Method for setting values in a certain column in a DataFrame"""
        assert type(column)==str, 'Wrong type of value'
        assert column in self.main_data.columns, 'No such column'
        assert len(values)>0, 'No values!'
        for index, value in zip(range(len(values)), values): self.main_data.loc[index, column] = value
        print('Assignment successful!')
        return self.main_data

    def del_line(self, shoot_number:int) -> None:
        """Method for deleting a row in the DataFrame"""
        assert 0 < shoot_number < len(self.main_data), 'Wrong row number!'
        data_after_row_deletion=self.main_data.drop(shoot_number)
        data_after_row_deletion.index=range(len(self.main_data)-1)
        self.main_data=data_after_row_deletion
        print('Row deleted successfully!')

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
    
    def compare(self, column_1:str, column_2:str, symbol:str) -> Union[pd.Series, pd.DataFrame]:
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
        

    def filter(self, bool_list:pd.Series, alter_table:bool=False) -> pd.DataFrame:
        """Method for getting a DataFrame with a bool list or altering a current My_data_class object"""
        if alter_table==True:
            self.main_data=self.main_data.loc[bool_list]
            return self.main_data
        else:
            return self.main_data.loc[bool_list]
            # ask whether to save in the main program

    def column_math(self, column_1:str, column_2:str, symbol:str, alter_table:bool=False) -> pd.DataFrame:
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
            return self.main_data
        else:
            main_data_copy=self.main_data.copy(deep=True)
            main_data_copy[column_1+'_'+symbol+'_'+column_2]=operator_res
            return main_data_copy
            # ask in a main program whether to save or not
        

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
        assert max_rows >=0, 'Wrong number of rows!'
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
    assert all([format in i for i in file_names]), 'Wrong names!'
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

exp_lst=[['Name', 'Age', 'Gender', 'Money'],
        ['Ann', 98, 'Female', 456],
        ['Joe', 76, 'Male', 111],
        ['Cunt', None, 'Helicopter', np.NaN],
        ['Damien', 67, 'Male', 908],
        ['Lisa', 66, 'Female', 780]
        ]

exp_lst1=[['Name', 'Age', 'Gender', 'Money'],
        ['An', 98111, 'Femal', 4565],
        ['Jo', 761, 'Mal', 1115],
        ['Cnt', 100, 'Helicopte', 87],
        ['Dmien', 671, 'Mal', 9058],
        ['Lsa', 6, 'Femal', 7803]
        ]

exp_lst2=[
        ['Sirname', 'Salary'],
        ['Lol', 442],
        ['U', 12],
        ['Tur', 345],
        ['Ila', 566],
        ['Qwa', 89]
]

exp_lst3=[['Sirname', 'Salary'],
        ['Pol', 54],
        ['Lo', 21],
        ['As', 81]
]

exp_lst4=[['Name', 'Salary', 'Birth_date', 'Eye Color'],
        ['Ann', 9822, '23.09.98', 'brown'],
        ['Joe', 761, '25.08.99', 'brown'],
        ['Cunt', 9, '12.03.12', 'grey'],
        ['Damien', 44, '09.12.95', 'brown'],
        ['Lisa', 98, '22.10.94', 'brown']
        ]


exp_df=pd.DataFrame({k: v for k,v in zip(exp_lst[0],[[exp_lst[j][i] for j in range(1,len(exp_lst))] for i in range(len(exp_lst[0]))])})
exp_df1=pd.DataFrame({k: v for k,v in zip(exp_lst1[0],[[exp_lst1[j][i] for j in range(1,len(exp_lst1))] for i in range(len(exp_lst1[0]))])})
exp_df2=pd.DataFrame({k: v for k,v in zip(exp_lst2[0],[[exp_lst2[j][i] for j in range(1,len(exp_lst2))] for i in range(len(exp_lst2[0]))])})
exp_df3=pd.DataFrame({k: v for k,v in zip(exp_lst3[0],[[exp_lst3[j][i] for j in range(1,len(exp_lst3))] for i in range(len(exp_lst3[0]))])})
exp_df4=pd.DataFrame({k: v for k,v in zip(exp_lst4[0],[[exp_lst4[j][i] for j in range(1,len(exp_lst4))] for i in range(len(exp_lst4[0]))])})

exp_df_reworked=pd.DataFrame(exp_lst1[1:], columns=exp_lst1[0])

exp_csv_data=load_existing_data('test_truemerge.csv')
print(exp_csv_data)

# print(int('aa'))


# lst_r_words=input().split()
# def pr(*args):
#         return '&'.join(args)

# print(pr(*lst_r_words))


# print(exp_df_reworked)
# print('\n'*2)
# res=exp_df_reworked.copy(deep=True)
# bool_res=exp_df_reworked['Age'] >= exp_df_reworked['Money']
# res['Age >= Money']=bool_res
# print(res[['Money','Age','Age >= Money']])
# print('\n'*2)
# print(exp_df_reworked.loc[bool_res])
# print('\n'*2)
# print(exp_df_reworked)



# splitter=2
# print(exp_df4)
# print('\n'*2)
# print(exp_df4[:splitter+1])
# print('\n'*2)
# print(exp_df4[splitter+1:])



# print(any([i in [5, 4, 3, 2, 1] for i in [10, 9, 8, 7, 6, 1]]))
# print(list(exp_df.index))
# print(list(exp_df4.index))





# print(exp_df.columns[0] == exp_df4.columns[0])



# print('\n')
# print('First data set')
# print(exp_df)
# print('\n'*2)
# print('Second data set')
# print(exp_df4)
# print('\n'*2)
# merged_df=pd.merge(exp_df, exp_df4, how='inner', on=exp_df.columns[0])
# print('Merged data set')
# print(merged_df)



# print('\n'*2)
# print('Concatanated data set')
# print('\n'*2)
# concat_df=pd.concat([exp_df, exp_df2])
# print(concat_df)


# exp_df1=exp_df.drop(2)
# exp_df1.index=range(len(exp_df)-1)
# print(exp_df1)

# print('Gender' in exp_df.columns)
# exp_df.loc[0, 'Gender']='hehe'
# exp_df.loc[1, 'Gender']='ww'
# exp_df.loc[2, 'Gender']='ew'
# exp_df.loc[3, 'Gender']='gross'
# print('\n'*2)
# print(exp_df)

# print('The age values\n')
# print(exp_df.loc[:, 'Age'].to_string(index=False))


# print('\n\nConditional selection\n')
# print(exp_df.loc[exp_df['Gender']=='Female'])
# values=['Joe', 'Ann', 'Cunt']
# print(len(exp_df))
# print(exp_df.loc[])
# res=exp_df.loc[exp_df[exp_df.columns[0]].isin(values)]
# print('Empty' if res.empty else res)

# print(exp_df)
# print()
# # exp1, exp2, exp3 = exp_df.iloc[0], exp_df.iloc[1], exp_df.iloc[2]
# # print(exp1, exp2, exp3, sep='\n')
# # print()
# exp4, exp5 = exp_df.iloc[0:2], exp_df.iloc[2:5]
# print(exp4, exp5, sep='\n'*2)
# print()
# print(len(exp5))
# # transposing
# list_of_lists=[[exp_lst[j][i] for j in range(1,len(exp_lst))] for i in range(len(exp_lst[0]))]
# # for i in range(len(exp_lst[0])):
# #     tr=[]
# #     for j in range(1,len(exp_lst)):
# #         tr.append(exp_lst[j][i])
# #     list_of_lists.append(tr)
# print(list_of_lists)


# ser=exp_data.loc[:, 'Age'] < exp_data.loc[:, 'Money']
# print(ser.to_string(index=False))

# with open('test_data.txt', mode = 'r') as file:
#         data=file.read().split('\n')
#         data_1=[i.split() for i in data]
# print(data_1)
# exp_1=pd.DataFrame({k: v for k,v in zip(data_1[0],[[exp_lst[j][i] for j in range(1,len(data_1))] for i in range(len(data_1[0]))])})
# print(exp_1)
# exp_1['Mul_age']=exp_1['Age']*3
# print(exp_1)
# exp_1['Mul_name']=exp_1['Name']*2
# print(exp_1)

# def exp_func(*args):
#         return len(args)

# print(exp_func(3.4, 'eew', 42, 0))

# a=[9]
# for i,v in enumerate(a):
#         print(i,v, sep='-')
# print(i)

# exp_data=pd.DataFrame({k: v for k,v in zip(exp_lst[0],[[exp_lst[j][i] for j in range(1,len(exp_lst))] for i in range(len(exp_lst[0]))])})
# exp_data1=pd.DataFrame({k: v for k,v in zip(exp_lst1[0],[[exp_lst1[j][i] for j in range(1,len(exp_lst1))] for i in range(len(exp_lst1[0]))])})
# exp_con=pd.concat(exp_data1, ignore_index=True)
# print(exp_con)

