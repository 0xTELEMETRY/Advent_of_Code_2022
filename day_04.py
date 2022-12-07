#*************************************************************************
#  Advent of Code 2022
#  Day 04 (Parts 1..2)
#  Software Design Requirements:    day04_Req.txt
#  Input Data:                      day4.txt
#
#  Author: Nikolaj Gribakin (xASM)
#  Email: n.gribakin@gmail.com
#  Tel:   +420 773078426
#  
#*************************************************************************

input_file = open("day4.txt", "r")
lines = input_file.readlines()  #read all data
c = 0
result = 0

for line in lines:
    line = line.strip()
    c = c+1

    ranges = line.split(",")
    #print(ranges)
    
    range_1= ranges[0]
    range_2 = ranges[1]
    
    min_max_1 = range_1.split("-")
    min_max_2 = range_2.split("-")
    
    min_1 = int(min_max_1[0])
    max_1 = int(min_max_1[1])
    min_2 = int(min_max_2[0])
    max_2 = int(min_max_2[1])

    if (min_1>max_1):
        print("issue 1", min_1, max_1, range_1, range_2)
    if (min_2>max_2):
        print("issue 2", min_2, max_2)
        
    
    print(c, ": ", min_1, " - ", max_1, "==", min_2, " - ", max_2)
    
    if ((min_1>=min_2) and (max_2>=min_1)) or ((min_1<=min_2) and (max_1>=min_2)):
        result = result + 1
        
print (result, " ", c)
input_file.close()

#-----eof------
   

