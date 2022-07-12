# python_file_handler
Made on Linux Ubuntu 22.04

My Python project dedicated to handling csv, pickle and txt files. A simple working tool with the potential of future modifications

Current capabilities:
- working with csv files and perfoming some operations with them (add, divide, subtract, multiply, compare columns; concatenating, splitting and merging) 
- pickling and unpickling files
- working with text files
- creating data on the go

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
