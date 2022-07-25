from file_manager_ver1 import *
from numpy import number
from time import sleep

print('Initializing...')
sleep(1)
cycle_count=0
while cycle_count!='stop':
    if cycle_count==0:
        print("""Hello! This is the file manager program! I am here to serve you! Seems, you have no data to work with...
        Please, load your data from a file (or files to combine data into one data set) or create one now""")
        sleep(0.5)
        print('''Choose your option by typing a number:
            1) Load file
            2) Create data
            3) Exit''')
        while True:
            answer=input('Input here:\n')
            if answer=='3':
                cycle_count='stop'
                break
            elif answer=='2':
                data=data_builder()
                cycle_count+=1
                print('Now you have loaded your data. Generating menu...')
                break
            elif answer=='1':
                while True:
                    format_file=input('What is the format of your file(-s)? [csv/pkl/txt]\n')
                    if format_file in ['csv', 'pkl', 'txt']:
                        break
                    else:
                        print('Wrong option!')
                file_names=input('Input the name of the file(-s; if so use space button as a separator) (with format!)\n').split()
                data=load_existing_data(*file_names, format=format_file)
                cycle_count+=1
                print('Now you have loaded your data. Generating menu...')
                break
            else:
                print('Wrong number!')
    if cycle_count > 0:
        print('\n'*3)
        sleep(1)
        print('''Here is what I can do:
        1) Change the name of the data set
        2) Get rows from the data set by number
        3) Get rows from the data set by the value of the first column
        4) Get values from a certain column
        5) Set values from a certain column
        6) Print the data set
        7) Delete a line from the data set
        8) Merge data sets
        9) Concatanate data sets (or add line(-s))
        10) Reload the data set
        11) Split the data set into two by a row number
        12) Compare columns (Supported: ==, >=, <=, !=, >, <) of the data set and compose a different data set based on the result
        13) Perform math operations with columns (Supported: +, -, /, *)
        14) Save your data set into a file (Supported formats: csv, pkl, txt)
        15) Exit
        ''')
        answer=input('Input here:\n')
        if answer=='15':
            cycle_count='stop'
            break
        elif answer=='1':
            while True:
                try:
                    data.change_name(input('Input new name:\n'))
                    print('Name changed!')
                except AssertionError:
                    print('Wrong value!')
                else:
                    break
        elif answer=='2':
            while True:
                try:
                    beginning=input('Input the beginning of the row selection: \n')
                    end=input('Input the end of the row selection (if you want to select the rows till the end, type 0)\n')
                    if_alter=input('Do you wish to alter the table at hand? Yes or no\n')
                    if if_alter not in ['yes', 'Yes', 'no', 'No']:
                        raise ValueError('Wrong save question answer!')
                    result=data.get_rows_by_number(int(beginning), int(end), alter_table= True if if_alter in ['Yes', 'yes'] else False)
                except ValueError as err:
                    print(err)
                    print('Try again!')
                except AssertionError as err:
                    print(err)
                    print('Try again!')
                else:
                    break
            print('\n')
            print(result)
            while True:
                answer=input('Do you wish to save the result?\n')
                if answer in ['Yes', 'yes', 'no', 'No']:
                    break
                else:
                    print('Wrong answer!')
            if answer in ['Yes', 'yes']:
                while True:
                    file_format=input('In what format do you wish to save the result? Csv, pkl or txt?\n')
                    if file_format in ['csv', 'pkl', 'txt']:
                        break
                    else:
                        print('Wrong format!')
                while True:
                    try:
                        file_name=input('Input the name of the file without the format\n')
                        My_data_class.regular_save(result, file_format, file_name)
                    except ValueError as err:
                        print('Wrong file name!')
                    else:
                        break
        elif answer=='3':
            while True:
                try:
                    wanted_values=input('Input the values by which you wanna identify the rows with space:\n').split()
                    if_alter=input('Do you wish to alter the table at hand? Yes or no\n')
                    if if_alter not in ['yes', 'Yes', 'no', 'No']:
                        raise ValueError('Wrong save question answer!')
                    result=data.get_rows_by_value(*wanted_values, alter_table = True if if_alter in ['Yes', 'yes'] else False)
                except ValueError as err:
                    print(err)
                    print('Try again!')
                else:
                    break
            print('\n')
            print(result)
            while True:
                answer=input('Do you wish to save the result?\n')
                if answer in ['Yes', 'yes', 'no', 'No']:
                    break
                else:
                    print('Wrong answer!')
            if answer in ['Yes', 'yes']:
                while True:
                    file_format=input('In what format do you wish to save the result? Csv, pkl or txt?\n')
                    if file_format in ['csv', 'pkl', 'txt']:
                        break
                    else:
                        print('Wrong format!')
                while True:
                    try:
                        file_name=input('Input the name of the file without the format\n')
                        My_data_class.regular_save(result, file_format, file_name)
                    except ValueError as err:
                        print('Wrong file name!')
                    else:
                        break
        elif answer=='4':
            while True:
                try:
                    column_name=input('Input the name of the column\n')
                    print('The requested values:\n')
                    print(data.get_values(column_name))
                    print('\n')
                except AssertionError as err:
                    print(err)
                    print('Try again!')
                else:
                    break
        elif answer=='5':
            while True:
                try:
                    column_name=input('Input the name of the column\n')
                    lst_of_values=input('Input the desired values with space\n').split()
                    print('Here is the result!\n')
                    print(data.set_values(column_name, *lst_of_values))
                    print('\n')
                except AssertionError as err:
                    print(err)
                    print('Try again!')
                else:
                    break
        elif answer=='6':
            print(data)
            print('\n')
        elif answer=='7':
            while True:
                try:
                    shoot=input('Input the number of the row you would like to delete\n')
                    data.del_line(int(shoot))
                    print('Line deleted!\n')
                except ValueError:
                    print('Failed to convert to number!')
                    print('Try again!')
                except AssertionError as err:
                    print(err)
                    print('Try again!')
                else:
                    break
        elif answer=='8':
            print('Provide another piece of data!')
            sleep(0.5)
            print('''Choose your option by typing a number:
            1) Load file
            2) Create data''')
            while True:
                answer=input('Input here:\n')
                if answer=='2':
                    another_piece_of_data=data_builder()
                    print('Additional data provided!')
                    break
                elif answer=='1':
                    format_file=input('What is the format of your file(-s)? [csv/pkl/txt]\n')
                    while True:
                        if format_file in ['csv', 'pkl', 'txt']:
                            break
                        else:
                            print('Wrong option!')
                    file_names=input('Input the name of the file(-s; if so use space button as a separator) (with format!)\n').split()
                    another_piece_of_data=load_existing_data(*file_names, format=format_file)
                    print('Additional data provided!')
                    break
                else:
                    print('Wrong number!')
            print('''There are two merges here:
            1) true merge. Works like inner join in sql
            2) pseudo merge. Works like outer join in sql
            ''')
            while True:
                if_merge=input('Input here\n')
                if if_merge in ['1', '2']:
                    break
                else:
                    print('Wrong number!')
            while True:
                if_number=input('Would you like to join by number(index) or by the value of the first column? [by number/by value]\n')
                if if_number in ['by number', 'by value']:
                    break
                else:
                    print('Wrong number!')
            try:
                result=data.merge(another_piece_of_data, true_merge = True if if_merge == '1' else False, by_number = False if if_number == 'by value' else True)
            except AssertionError as err:
                print(err)
            print('\n')
            print(result)
            while True:
                answer=input('Do you wish to save the result?\n')
                if answer in ['Yes', 'yes', 'no', 'No']:
                    break
                else:
                    print('Wrong answer!')
            if answer in ['Yes', 'yes']:
                while True:
                    file_format=input('In what format do you wish to save the result? Csv, pkl or txt?\n')
                    if file_format in ['csv', 'pkl', 'txt']:
                        break
                    else:
                        print('Wrong format!')
                while True:
                    try:
                        file_name=input('Input the name of the file without the format\n')
                        My_data_class.regular_save(result.main_data, file_format, file_name)
                    except ValueError as err:
                        print('Wrong file name!')
                    else:
                        break
        elif answer=='9':
            print('Provide another piece of data!')
            sleep(0.5)
            print('''Choose your option by typing a number:
            1) Load file
            2) Create data''')
            while True:
                answer=input('Input here:\n')
                if answer=='2':
                    another_piece_of_data=data_builder()
                    print('Additional data provided!')
                    break
                elif answer=='1':
                    format_file=input('What is the format of your file(-s)? [csv/pkl/txt]\n')
                    while True:
                        if format_file in ['csv', 'pkl', 'txt']:
                            break
                        else:
                            print('Wrong option!')
                    file_names=input('Input the name of the file(-s; if so use space button as a separator) (with format!)\n').split()
                    another_piece_of_data=load_existing_data(*file_names, format=format_file)
                    print('Additional data provided!')
                    break
                else:
                    print('Wrong number!')
            try:
                result=data.concat(another_piece_of_data)
            except AssertionError as err:
                print(err)
            except ValueError as err:
                print(err)
            print('\n')
            print(result)
            while True:
                answer=input('Do you wish to save the result?\n')
                if answer in ['Yes', 'yes', 'no', 'No']:
                    break
                else:
                    print('Wrong answer!')
            if answer in ['Yes', 'yes']:
                while True:
                    file_format=input('In what format do you wish to save the result? Csv, pkl or txt?\n')
                    if file_format in ['csv', 'pkl', 'txt']:
                        break
                    else:
                        print('Wrong format!')
                while True:
                    try:
                        file_name=input('Input the name of the file without the format\n')
                        My_data_class.regular_save(result.main_data, file_format, file_name)
                    except ValueError as err:
                        print('Wrong file name!')
                    else:
                        break
        elif answer=='10':
            print('''Choose your option by typing a number:
            1) Load file
            2) Create data''')
            while True:
                answer=input('Input here:\n')
                if answer=='2':
                    data=data_builder()
                    print('Data reloaded!')
                    break
                elif answer=='1':
                    while True:
                        format_file=input('What is the format of your file(-s)? [csv/pkl/txt]\n')
                        if format_file in ['csv', 'pkl', 'txt']:
                            break
                        else:
                            print('Wrong option!')
                    file_names=input('Input the name of the file(-s; if so use space button as a separator) (with format!)\n').split()
                    data=load_existing_data(*file_names, format=format_file)
                    print('Data reloaded!')
                    break
                else:
                    print('Wrong number!')
        elif answer=='11':
            while True:
                try:
                    split_num=input('Input the number of the split row\n')
                    res1, res2 = data.split(int(split_num))
                except ValueError:
                    print('Failed to convert the split number!')
                except AssertionError as err:
                    print(err)
                else:
                    break
            print('\n')
            print(res1, res2, sep='\n'*2)
            while True:
                answer=input('Do you wish to save the result?\n')
                if answer in ['Yes', 'yes', 'no', 'No']:
                    break
                else:
                    print('Wrong answer!')
            if answer in ['Yes', 'yes']:
                while True:
                    file_format=input('In what format do you wish to save the result? Csv, pkl or txt?\n')
                    if file_format in ['csv', 'pkl', 'txt']:
                        break
                    else:
                        print('Wrong format!')
                while True:
                    try:
                        file_name1=input('Input the name of the first file without the format\n')
                        file_name2=input('Input the name of the second file without the format\n')
                        My_data_class.regular_save(res1.main_data, file_format, file_name1)
                        My_data_class.regular_save(res2.main_data, file_format, file_name2)
                    except ValueError as err:
                        print('Wrong file name!')
                    else:
                        break
        elif answer=='12':
            while True:
                inquery=input('Input the inquery in such format: column1 symbol column2\n').split()
                if len(inquery)==3:
                    break
                else:
                    print('Wrong inquery!')
            try:
                list_of_bool, comp_res = data.compare(inquery[0], inquery[2], inquery[1])
            except AssertionError as err:
                print(err)
            print('\n')
            print(comp_res)
            while True:
                answer=input('Would you like to filter the rows based on comparison results?\n')
                if answer in ['Yes', 'yes', 'no', 'No']:
                    break
                else:
                    print('Wrong answer!')
            if answer in ['Yes', 'yes']:
                while True:
                    if_alter=input('Do you wish to alter the table at hand? Yes or no\n')
                    if if_alter in ['yes', 'Yes', 'no', 'No']:
                        break
                    else:
                        print('Wrong answer!')
                result = data.filter(list_of_bool, alter_table = True if if_alter == 'Yes' or 'yes' else False)
                print('\n')
                print(result)
                while True:
                    answer=input('Do you wish to save the result?\n')
                    if answer in ['Yes', 'yes', 'no', 'No']:
                        break
                    else:
                        print('Wrong answer!')
                if answer in ['Yes', 'yes']:
                    while True:
                        file_format=input('In what format do you wish to save the result? Csv, pkl or txt?\n')
                        if file_format in ['csv', 'pkl', 'txt']:
                            break
                        else:
                            print('Wrong format!')
                    while True:
                        try:
                            file_name=input('Input the name of the file without the format\n')
                            My_data_class.regular_save(result, file_format, file_name)
                        except ValueError as err:
                            print('Wrong file name!')
                        else:
                            break
        elif answer=='13':
            while True:
                inquery=input('Input the inquery in such format: column1 symbol column2\n').split()
                if len(inquery)==3:
                    break
                else:
                    print('Wrong inquery!')
            while True:
                    if_alter=input('Do you wish to alter the table at hand? Yes or no\n')
                    if if_alter in ['yes', 'Yes', 'no', 'No']:
                        break
                    else:
                        print('Wrong answer!')
            try:
                result = data.column_math(inquery[0], inquery[2], inquery[1], alter_table=True if if_alter=='yes' or 'Yes' else False)
            except AssertionError as err:
                print(err)
            print('\n')
            print(result)
            while True:
                answer=input('Do you wish to save the result?\n')
                if answer in ['Yes', 'yes', 'no', 'No']:
                    break
                else:
                    print('Wrong answer!')
            if answer in ['Yes', 'yes']:
                while True:
                    file_format=input('In what format do you wish to save the result? Csv, pkl or txt?\n')
                    if file_format in ['csv', 'pkl', 'txt']:
                        break
                    else:
                        print('Wrong format!')
                while True:
                    try:
                        file_name=input('Input the name of the file without the format\n')
                        My_data_class.regular_save(result, file_format, file_name)
                    except ValueError as err:
                        print('Wrong file name!')
                    else:
                        break
        elif answer=='14':
            while True:
                file_format=input('In what format do you wish to save the result? Csv, pkl or txt?\n')
                if file_format in ['csv', 'pkl', 'txt']:
                    break
                else:
                    print('Wrong format!')
            print("""Would you like to save the data in one table or multiple tables?
            If in one table, type 0; otherwise type a number of rows allowed in one table""")
            while True:
                try:
                    max_amount_of_rows=input('Input here \n')
                    data.save_table(file_format, int(max_amount_of_rows))
                    print('Saved successfully!')
                except ValueError:
                    print('Wrong number of rows!')
                except AssertionError as err:
                    print(err)
                else:
                    break