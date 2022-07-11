import numpy as np
import pandas as pd
from time import sleep

exp_lst=[['Name', 'Age', 'Gender'],
        ['Ann', 98, 'Female'],
        ['Joe', 76, 'Male'],
        ['Cunt', None, 'Helicopter'],
        ['Damien', 67, 'Male'],
        ['Lisa', 66, 'Female']]

# exp_df=pd.DataFrame({k: v for k,v in zip(exp_lst[0],[[exp_lst[j][i] for j in range(1,len(exp_lst))] for i in range(len(exp_lst[0]))])})
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
# exp_data=pandas.DataFrame({k: v for k,v in zip(exp_lst[0],[[exp_lst[j][i] for j in range(1,len(exp_lst))] for i in range(len(exp_lst[0]))])})
# print(exp_data.to_string(index=False))

