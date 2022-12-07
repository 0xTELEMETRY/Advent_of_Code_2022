#*************************************************************************
#  Advent of Code 2022
#  Day 07 (Parts 1..2)
#  Software Design Requirements:    day07_Req.txt
#  Input Data:                      day7.txt
#                                   
#  Author: Nikolaj Gribakin (xASM)
#  Email: n.gribakin@gmail.com
#  Tel:   +420 773078426
#  
#*************************************************************************
input_file = open("day7.txt", "r")
total_lines = len(input_file.readlines())
input_file.seek(0)
dir_path = []
file_system = dict()
path_index = 0
result = 0

for i in range(total_lines):
    line = input_file.readline()  #read all data
    line = line.strip()
    if (line[0:4] == "$ cd"):  #checking if we changeing the directory
        if (line[5:7]==".."):
            del dir_path[-1]
            current_dir_name = dir_path[-1] #get the last element
            path_index = path_index - 1
            
        else:
            current_dir_name = line[5:]
           # print("dir changed to:", current_dir_name)
            path_index = path_index + 1
            dir_path.append(current_dir_name)
            print(dir_path)
            current_path = ""
            i = 0
            for i in range(path_index):
                current_path = current_path + "*" + dir_path[i]
            
            file_system[current_path] = 0 #create new dict element with 0 size (empty)
           
            
    else:
        if (line[0:4] != "$ ls") and (line[0:3] != "dir"):
            
            tmp = line.split(" ")
            file_size = tmp[0]
            #print(">>>", file_system)
            #print(dir_path)
            
            if (file_size!=""):
                current_path = ""
                for i in range(path_index):
                    current_path = current_path + "*" + dir_path[i]
                    old_dir_size = int(file_system[current_path])                    
                    new_dir_size = old_dir_size + int(file_size)
                    file_system[current_path] = new_dir_size

    #print (file_system)
result = 0
for i in file_system:
    if (file_system[i]<100000):
        result = result + file_system[i]
       
print ("Part 1 result: ", result)
#print (file_system)

#print(file_system["*/"])

total_space = 70000000
free_space = total_space - file_system["*/"]
space_needed = 30000000 - free_space

sorted_file_system = sorted(file_system.items(), key=lambda x: x[1], reverse=True)


for i in range(len(sorted_file_system)):
    if (sorted_file_system[i][1]<space_needed): 
        print("Part 2 result: ",sorted_file_system[i-1][1])
        break


input_file.close()
        
    




