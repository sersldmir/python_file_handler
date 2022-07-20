
import numpy as np
import pandas as pd
from time import sleep


exp_lst=[['Name', 'Age', 'Gender', 'Money'],
        ['Ann', 98, 'Female', 456],
        ['Joe', 76, 'Male', 111],
        ['Cunt', None, 'Helicopter', np.NaN],
        ['Damien', 67, 'Male', 908],
        ['Lisa', 66, 'Female', 780]
        ]

exp_lst1=[['Name', 'Age', 'Gender', 'Money'],
        ['An', 981, 'Femal', 4565],
        ['Jo', 761, 'Mal', 1115],
        ['Cnt', 1, 'Helicopte', 87],
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

exp_df_reworked=pd.DataFrame(exp_lst4[1:], columns=exp_lst4[0])
print(exp_df_reworked)


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

