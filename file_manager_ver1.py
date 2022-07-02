'''File handler project. Made on Linux Ubuntu 22.04 
Capabilities:
- working with csv files and perfoming some operations with them (add, divide, subtract, multiply, compare columns; concatenating, splitting and merging) 
- pickling and unpickling files
- working with text files'''

import csv, pickle
import pandas as pd
import numpy as np
from time import sleep

class My_data_class(object):
    def __init__(self, data):
        self.rows=data
        self.columns=[[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
        self.main_data=pd.DataFrame({k: v for k,v in zip(data[0],[[data[j][i] for j in range(1,len(data))] for i in range(len(data[0]))])})


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
                        return My_data_class(data)
                    else:
                        values=raw_values.split()
                        assert len(values)==len(list_of_titles), "The amount of values does not correspond with the amount of titles!"
                        data.append([np.nan if i=='None' else i for i in values])
                except AssertionError as err:
                    print(err)
        except AssertionError as err:
            print(err)
        
test1=data_builder()
print(test1.main_data.to_string(index=False))