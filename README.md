# python_file_handler
Made on Linux Ubuntu 22.04

My Python project dedicated to handling csv, pickle and txt files. A rework of my uni beginner project, i.e. improved with Pandas

Current capabilities:
- working with csv files and perfoming some operations with them (add, divide, subtract, multiply, compare columns; concatenating, splitting and merging) 
- pickling and unpickling files
- working with text files
- creating data on the go

__Version log__:

_Version 0.1_
- Added function creating data directly in the programm for further use

_Version 0.2_
- Added function saving data in one .csv, .txt or .pkl file

_Version 0.3_
- Changed data class: deleted rows and colums attributes in order to do everything with Pandas
- Changed saving data function: better implementation of Pandas to save text files
- Added parameter "max-rows" to saving data function: to split data into several files when saving
- Changed data builder: added optional parameter "contents" that allows to create objects of the custom data class with a ready list of lists 

_Version 0.4_
- Added loading function with unlimited amount of single type files loading
- Added some documentation

_Version 0.5_
- Added functions get_rows_by_number and get_rows_by_value that output rows of the given DataFrame taking numbers of the rows or values of the first column respectively as an input. Also have options to alter the current data or save result in a separate file

_Version 0.6_
- Added functions get_values, set_values, del_line, merge, concat, split. More details in their documentations
- Reworked __ init __ for list of lists
- Added annotations
- Slight changes in other functions

_Version 0.7_
- Added functions compare, filter, column_math. More details in their documentations
