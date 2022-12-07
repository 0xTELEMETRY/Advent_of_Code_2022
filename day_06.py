#*************************************************************************
#  Advent of Code 2022
#  Day 06 (Parts 1..2)
#  Software Design Requirements:    day06_Req.txt
#  Input Data:                      day6.txt
#
#  Author: Nikolaj Gribakin (xASM)
#  Email: n.gribakin@gmail.com
#  Tel:   +420 773078426
#  
#*************************************************************************
input_file = open("day6.txt", "r")
line = input_file.readline()  #read all data
input_file.close()

strob_size = 14
strob = [""]*strob_size

i = 0
j = 0

line_range = range(len(line.strip())-strob_size+1)

for i in (line_range):
    for j in range(strob_size):
        strob[j] = line[i+j]
    if(len(set(strob)) == len(strob)):
        break
        
print(i+strob_size)

#-----eof------
    




