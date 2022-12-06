#*************************************************************************
#  Advent of Code 2022
#  Day 05 (Parts 1..2)
#
#  Author: Nikolaj Gribakin (xASM)
#  Email: n.gribakin@gmail.com
#  Tel:   +420 773078426
#  
#*************************************************************************

input_file = open("day51.txt", "r")
lines = input_file.readlines()  #read all data
result = 0
i = 0

stage = ["","","","","","","","",""]
stage_letter_pos = [1,5,9,13,17,21,25,29,33] 

stage_height_ini = range(8)

input_file.seek(0)

for line in lines:
    line = line.strip()
    line_len = len(line)
    if (line_len<35):
        delta = range(35 - line_len)
        for i in (delta):
            line = line + " "
    
    i = 0
    j = 0 
    stage_letters = range(9)
    for i in (stage_letters):
        if (line[stage_letter_pos[i]]!=" "):
            stage[i] = stage[i] + line[stage_letter_pos[i]]


print (stage)

input_file = open("day5.txt", "r")
lines = input_file.readlines()  #read all data

rules = [0,0,0]

lines_count = 0
for line in lines: #reading rules
    line = line.strip()
    tmp = line.split(" ")
    rule_how_many = int(tmp[1]) #how many
    rule_from = int(tmp[3]) #from
    rule_to = int(tmp[5]) #to
    lines_count = lines_count + 1
    
    load = stage[rule_from-1][0:rule_how_many]
    #load = load[::-1] #reverse string
    
    stage[rule_to-1] = load + stage[rule_to-1]
    stage[rule_from-1] = stage[rule_from-1][rule_how_many:20000]  #Yep, it was dirty, I know :)
    
    
result = stage[0][0]+stage[1][0]+stage[2][0]+stage[3][0]+stage[4][0]+stage[5][0]+stage[6][0]+stage[7][0]+stage[8][0]

print(result)
input_file.close()




