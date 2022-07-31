# This section contains the imports for running the code

# time library is used to measure the time taken to execute the code
import time
import os

# tracemalloc library is used to calculate the menmory used by the program for a give input file
import tracemalloc

# importing the Basic_Algorithm.py file
import Basic_Algorithm

# importing the Efficient_Algorithm.py file
import Efficient_Algorithm

# argparse library is used to write user-friendly command-line interfaces
import argparse

# import the utils.py file which is used to generate the X and Y strings
import utils

mismatch_penalty = [[0, 110, 48, 94],
                    [110, 0, 118, 48],
                    [48, 118, 0, 110],
                    [94, 48, 110, 0]]

gap_penalty = 30


# Using the ArgParser for taking the input of the file using command line 
parser = argparse.ArgumentParser()                                               

parser.add_argument("--file", "-f", help = 'Enter the file along with file_path', type=str, required=False)
parser.add_argument("--efficient", "-e", help = 'For Executing the Efficient Algorithm')
#parser.add_argument("--directory", "-d", help = 'Enter the directory name')
args = parser.parse_args()
current_file = args.file

# Creating a basic_time.csv file to insert the time values of the Basic DP Algorithm
if not args.efficient:
    time_file = open("./CSV_files/basic_time.csv", "w")
    time_file.close()


    # Creating a basic_memory.csv file to save the memory usage of the Basic DP Algorithm
    memory_file = open('./CSV_files/basic_memory.csv', 'w')
    memory_file.close()
else:
    # Creating a efficient_time.csv file to insert the time values of the Efficient DP Algorithm
    time_file = open("./CSV_files/efficient_time.csv", "w")
    time_file.close()


    # Creating a efficient_time.csv file to insert the time values of the Efficient DP Algorithm
    memory_file = open('./CSV_files/efficient_memory.csv', 'w')
    memory_file.close()

# ---------------------------------------------------------------------------------------------------------
# For Multiple Files
# if args.directory:
#     # # Code For Multiple Input Files in the input_files directory

#     # Name of the folder where the input files are stored
#     directory = 'input_files'
        
#     # Stores the list of all the files that are in the 'input_files' folder
#     files_list = []

#     # Appending all the files to the files_list
#     for file in os.listdir('./{}'.format(directory)):
#         if not file.startswith('.'):
#             files_list.append(file)

#     #print(files_list)
#     i,j = 1,1


#     if not args.efficient:

#         for file in files_list:
#             tracemalloc.start()

#             #print('File Name:', file)
                
#             # Calling the 'String_Generator' function with the filepaths of all the files in the 'input_files' folder
#             X_string, Y_string = utils.String_Generator('./{}/{}'.format(directory, file))

#             # Using time module to calculate the time taken for executing each input file
#             start_time = time.time()
#             X, Y, total_cost = Efficient_Algorithm.divide_and_conquer(X_string, Y_string, mismatch_penalty, gap_penalty)
#             end_time = time.time()

#             with open('./CSV_files/basic_memory.csv', 'a') as m_file:

#                 #print('I:', i)
#                 snapshot = tracemalloc.take_snapshot()  
#                 mem_used = tracemalloc.get_traced_memory()[1]  
#                 print('Memory Used:', mem_used)
#                 m_file.write(str(i) + ',' + str(mem_used) + ',' + str(len(X_string)))
#                 i += 1
#                 m_file.write('\n')
                    
                

#             # Adding the execution time of each input file in the 'time.csv' file
                
#             with open('./CSV_files/basic_time.csv', 'a') as t_file:
#                 t_file.write(str(j) + ',' + str(end_time-start_time) + ',' + str(len(X_string)))
#                 t_file.write('\n')
#                 j += 1 

#             # with open('./output.txt', 'w') as op_file:
#             #     op_file.write(str(X[:50]) + "  " + str(X[-50:]) + '\n')
#             #     op_file.write(str(Y[:50]) + " " + str(Y[-50:]) + '\n')
#             #     op_file.write(str(total_cost) + '\n')
#             #     op_file.write(str(end_time - start_time) + '\n')
#             #     op_file.write(str(mem_used))   

#     else:
#         for file in files_list:
#             tracemalloc.start()

#             #print('File Name:', file)
                
#             # Calling the 'String_Generator' function with the filepaths of all the files in the 'input_files' folder
#             X_string, Y_string = utils.String_Generator('./{}/{}'.format(directory, file))

#             # Using time module to calculate the time taken for executing each input file
#             start_time = time.time()
#             X, Y, total_cost = Basic_Algorithm.get_Minimum_Penalty(X_string, Y_string, mismatch_penalty, gap_penalty)
#             end_time = time.time()

#             with open('./CSV_files/efficient_memory.csv', 'a') as m_file:

#                 #print('I:', i)
#                 snapshot = tracemalloc.take_snapshot()  
#                 mem_used = tracemalloc.get_traced_memory()[1]  
#                 print('Memory Used:', mem_used)
#                 m_file.write(str(i) + ',' + str(mem_used) + ',' + str(len(X_string)))
#                 i += 1
#                 m_file.write('\n')
                    
                

#             # Adding the execution time of each input file in the 'time.csv' file
                
#             with open('./CSV_files/efficient_time.csv', 'a') as t_file:
#                 t_file.write(str(j) + ',' + str(end_time-start_time) + ',' + str(len(X_string)))
#                 t_file.write('\n')
#                 j += 1 
#         time_to_execute = time.time() - start_time

#         # Cost of Sequence Alignment
#         #print('Cost:' ,total_cost)
#         string_length = len(X_string) + len(Y_string)

# # ---------------------------------------------------------------------------------------------------
# else:
# For Single File
# Memory is in bytes and time is in seconds
tracemalloc.start()
start_time = time.time()


# Here we are assuming that the input.txt file will be in the same directory of the main_file.py
X_string, Y_string = utils.String_Generator('{}'.format(current_file))

# For Efficient Algorithm    
if args.efficient:
    X, Y, total_cost = Efficient_Algorithm.divide_and_conquer(X_string, Y_string, mismatch_penalty, gap_penalty)

# For Basic Algorithm
else:
    X, Y, total_cost = Basic_Algorithm.get_Minimum_Penalty(X_string, Y_string, mismatch_penalty, gap_penalty)
    
time_to_execute = time.time() - start_time

# Cost of Sequence Alignment
#print('Cost:' ,total_cost)
string_length = len(X_string) + len(Y_string)

# Adding the memory usage for Basic Algorithm to the basic_memory.csv file which is stored in the CSV_files Folder    
i, j = 1,1
if not args.efficient:
    with open('./CSV_files/basic_memory.csv', 'a') as m_file:
        snapshot = tracemalloc.take_snapshot()  
        mem_used = tracemalloc.get_traced_memory()[1]  
        mem_used = mem_used/1024
        m_file.write(str(i) + ',' + str(mem_used) + ',' + str(string_length))
        i += 1
        m_file.write('\n')
            
    # Adding the execution time for Basic Algorithm to the basic_time.csv file which is stored in the CSV_files Folder
        
    with open('./CSV_Files/basic_time.csv', 'a') as t_file:
        t_file.write(str(j) + ',' + str(time_to_execute) + ',' + str(string_length))
        t_file.write('\n')
        j += 1 

# Adding the memory usage for Efficient Algorithm to the efficient_memory.csv file which is stored in the CSV_files Folder    
elif args.efficient:
    with open('./CSV_files/efficient_memory.csv', 'a') as m_file:
        snapshot = tracemalloc.take_snapshot()  
        mem_used = tracemalloc.get_traced_memory()[1]  
        mem_used /= 1024
        m_file.write(str(i) + ',' + str(mem_used) + ',' + str(string_length))
        i += 1
        m_file.write('\n')
            
    # Adding the execution time for Basic Algorithm in the efficient_time.csv file which is stored in the CSV_files Folder
        
    with open('./CSV_Files/efficient_time.csv', 'a') as t_file:
        t_file.write(str(j) + ',' + str(time_to_execute) + ',' + str(string_length))
        t_file.write('\n')
        j += 1 

# output.txt file contains the data asked in the Part B of Goals section
with open('./output.txt', 'w') as op_file:
    op_file.write(str(X[:50]) + "  " + str(X[-50:]) + '\n')
    op_file.write(str(Y[:50]) + " " + str(Y[-50:]) + '\n')
    op_file.write(str(total_cost) + '\n')
    op_file.write('Memory in KBs is: ' + str(mem_used) + '\n')
    op_file.write('Time in seconds is:' + str(time_to_execute))


#Printing the data that stored in the output.txt file
# print('\nX First 50:', X[:50])
# print('Y First 50:', Y[:50])
# print('X Last 50:', X[-50:])
# print('Y Last 50:', Y[-50:])
# print(string_length)
# print('Cost:', total_cost)
# print('Memory in KBs is:', mem_used)
# print('Time in seconds is:', time_to_execute)