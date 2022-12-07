#*************************************************************************
#  Advent of Code 2022
#  Day 01 (Parts 1..2)
#  Software Design Requirements:    day01_Req.txt
#  Input Data:                      day1.txt
#
#  Author: Nikolaj Gribakin (xASM)
#  Email: n.gribakin@gmail.com
#  Tel:   +420 773078426
#  
#*************************************************************************

input_file = open("day1.txt", "r")
lines = input_file.readlines()  #read all data

current_elf_cal = 0
max_elf_cal = 0
max_elf_cal_list = []
elf_id = 0

for line in lines:
    if (line != '\n'):
        current_elf_cal = current_elf_cal + int(line)
    else:   
        max_elf_cal_list.append(current_elf_cal)
        elf_id = elf_id+1
        current_elf_cal = 0
        
#last calculation        
max_elf_cal_list.append(current_elf_cal)
elf_id = elf_id+1

max_elf_cal_list.sort()
input_file.close()

max_3 = max_elf_cal_list[elf_id-1] + max_elf_cal_list[elf_id-2] + max_elf_cal_list[elf_id-3]

print(max_3)

#-----eof------
