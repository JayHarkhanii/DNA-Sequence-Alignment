import matplotlib.pyplot as plt
import csv
  
# Plotting the Graph of CPU Time VS Problem Size 
X_arr = []
Y_arr = []
Z_arr = []  
basic_temp_dict = {}
efficient_temp_dict = {}

# Using the basic_time.csv file in thr CSV_Files Folder
with open('./CSV_Files/basic_time.csv','r') as basic_t:
    b_lines = csv.reader(basic_t, delimiter=',')
    for row in b_lines:
        basic_temp_dict[float(row[2])] = float(row[1])
        # Without Sorting, the X array and Y array would be the following two lines
        #X_arr.append(row[2])
        #Y_arr.append(row[1])

# Sorting the array according to the Problem Szze
basic_temp_dict = sorted(basic_temp_dict.items())
#print(basic_temp_dict)
for k,v in basic_temp_dict:
    X_arr.append(k)
    Y_arr.append(v)

# Using the efficient_time.csv file in thr CSV_Files Folder
with open('./CSV_Files/efficient_time.csv','r') as efficient_t:
    e_lines = csv.reader(efficient_t, delimiter=',')
    for row in e_lines:
        efficient_temp_dict[float(row[2])] = float(row[1])

# Sorting the array acc to the Problem Size
efficient_temp_dict = sorted(efficient_temp_dict.items())
for k,v in efficient_temp_dict:
    Z_arr.append(v)

# Graph Plot
plt.grid(visible=None)
plt.plot(X_arr, Y_arr, label = "CPU Time of Basic Algorithm")
plt.plot(X_arr, Z_arr, label = "CPU Time of Efficient Algorithm")
  
plt.xticks(rotation = 25)
plt.xlabel('Problem_Size')
plt.ylabel('CPU Time')
plt.title('CPU Time VS Problem Size', fontsize = 20)
plt.grid()
plt.legend()

# CPU Time VS Problem Size is saved in the Graph_Plots folder
plt.savefig('Graph_Plots/CPUPlot.png')

plt.show()

# -------------------------------------------------------------------------------------------------------------------------------------------------
# Plotting the Graph of Memory Usage VS Problem Size 

X_arr = []
Y_arr = []
Z_arr = []  
m_basic_temp_dict = {}
m_efficient_temp_dict = {}

# Using the basic_memory.csv file in thr CSV_Files Folder
with open('./CSV_Files/basic_memory.csv','r') as basic_mem:
    b_lines = csv.reader(basic_mem, delimiter=',')
    for row in b_lines:
        m_basic_temp_dict[float(row[2])] = float(row[1])
        # Without Sorting, the X array and Y array would be the following two lines
        # X_arr.append(row[0])
        # Y_arr.append(row[1])

# Sorting the array according to the Problem Szze
m_basic_temp_dict = sorted(m_basic_temp_dict.items())
for k,v in m_basic_temp_dict:
    X_arr.append(k)
    Y_arr.append(v)


# Using the efficient_memory.csv file in thr CSV_Files Folder
with open('./CSV_Files/efficient_memory.csv','r') as efficient_t:
    e_lines = csv.reader(efficient_t, delimiter=',')
    for row in e_lines:
        m_efficient_temp_dict[float(row[2])] = float(row[1])

# Sorting the array acc to the Problem Size
m_efficient_temp_dict = sorted(m_efficient_temp_dict.items())
for k,v in m_efficient_temp_dict:
    Z_arr.append(v)

print(m_basic_temp_dict)
print(m_efficient_temp_dict)

# Graph Plot
plt.grid(visible=None)
plt.plot(X_arr, Y_arr, label = "Memory Usage of Basic Algorithm")

plt.plot(X_arr, Z_arr, label = "Memory Usage of Efficient Algorithm")  
plt.xticks(rotation = 25)
plt.ylim(0,31000)
plt.xlabel('Problem_Size')
plt.ylabel('Memory_Usage')
plt.title('Memory_Usage VS Problem Size', fontsize = 20)
plt.grid()
plt.legend()

# CPU Time VS Problem Size is saved in the Graph_Plots folder
plt.savefig('Graph_Plots/MemoryPlot.png')

plt.show()


