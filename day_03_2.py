#*************************************************************************
#  Advent of Code 2022
#  Day 01 (Part 1)
#
#  Author: Nikolaj Gribakin (xASM)
#  Email: n.gribakin@gmail.com
#  Tel:   +420 773078426
#  
#*************************************************************************

input_file = open("day3.txt", "r")
lines = input_file.readlines()  #read all data

chrs_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0
group_id = 0
group_line = []

for line in lines:
    group_line.append(line.strip())
    group_id = group_id + 1

    if (group_id == 3):
        found_chr = ''.join(set(group_line[0]).intersection(group_line[1]))
        found_chr = ''.join(set(found_chr).intersection(group_line[2]))
       
        priority = chrs_str.find(found_chr)+1
        result = result + priority
   
        group_line = []
        group_id = 0
   
print(result)
input_file.close()

