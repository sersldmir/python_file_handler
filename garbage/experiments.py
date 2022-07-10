import pandas, numpy

exp_lst=[['Name', 'Age', 'Gender'],
        ['Ann', 98, 'Female'],
        ['Joe', 76, 'Male'],
        ['Cunt', None, 'Helicopter']]

# def transp(lst):# функция транспонирования
#     res=[]
#     for i in range(n):
#         tr=[]
#         for j in range(n):
#             tr.append(lst[j][i])
#         res.append(tr)
#     return res 


list_of_lists=[[exp_lst[j][i] for j in range(1,len(exp_lst))] for i in range(len(exp_lst[0]))]
# for i in range(len(exp_lst[0])):
#     tr=[]
#     for j in range(1,len(exp_lst)):
#         tr.append(exp_lst[j][i])
#     list_of_lists.append(tr)
print(list_of_lists)
exp_data=pandas.DataFrame({k: v for k,v in zip(exp_lst[0],[[exp_lst[j][i] for j in range(1,len(exp_lst))] for i in range(len(exp_lst[0]))])})
print(exp_data.to_string(index=False))
