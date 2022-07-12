import numpy as np
import pandas as pd
from time import sleep

exp_lst=[['Name', 'Age', 'Gender', 'Money'],
        ['Ann', 98, 'Female', 456],
        ['Joe', 76, 'Male', 111],
        ]
exp_lst1=[['Name', 'Age', 'Gender', 'Money'],
        ['Cunt', None, 'Helicopter', 321],
        ['Damien', 67, 'Male', 908],
        ['Lisa', 66, 'Female', 780]]

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

a=[9]
for i,v in enumerate(a):
        print(i,v, sep='-')
print(i)

# exp_data=pd.DataFrame({k: v for k,v in zip(exp_lst[0],[[exp_lst[j][i] for j in range(1,len(exp_lst))] for i in range(len(exp_lst[0]))])})
# exp_data1=pd.DataFrame({k: v for k,v in zip(exp_lst1[0],[[exp_lst1[j][i] for j in range(1,len(exp_lst1))] for i in range(len(exp_lst1[0]))])})
# exp_con=pd.concat(exp_data1, ignore_index=True)
# print(exp_con)