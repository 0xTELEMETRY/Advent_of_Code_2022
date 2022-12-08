#*************************************************************************
#  Advent of Code 2022
#  Day 08 (Parts 1)
#  Software Design Requirements:    day08_Req.txt
#  Input Data:                      day8.txt
#                                   
#  Author: Nikolaj Gribakin (xASM)
#  Email: n.gribakin@gmail.com
#  Tel:   +420 773078426
#  
#*************************************************************************
input_file = open("day8.txt", "r")
total_lines = len(input_file.readlines()) #get total lines
input_file.seek(0)
line_len = len(input_file.readline().strip())  #get line length
print(total_lines, line_len)
print(2*(total_lines-2) + 2*line_len)

perimetr = 2*(total_lines-2) + 2*line_len
print("---->", perimetr, total_lines, line_len)
input_file.seek(0)
trees = []
lines = input_file.readlines()
for line in lines:
    line = line.strip()
    trees.append(line)

max_x = line_len - 1
max_y = total_lines - 1
visible_trees = 0
y = 0
x = 0

def square_height(x, y, tree_height):
    
    visible = 0
    
    for i in range(0,x):
        height = int(trees[y][i])
        if (i!=x):
            if (height>=int(tree_height)):
                visible = 1
                break
            
                
    if (visible == 0):
        return 0
    
    visible = 0
              
    for i in range(x, line_len):
        height = int(trees[y][i])
        if (i!=x):
            if (height>=int(tree_height)):
                visible = 1
                break

    if (visible == 0):
        return 0

    visible = 0
    
    for j in range(0,y):
        height = int(trees[j][x])
        if (j!=y):
            if (height>=int(tree_height)):
                visible = 1
                break
            
    if (visible == 0):
        return 0                
    
    visible = 0
    
    for j in range(y, total_lines):
        height = int(trees[j][x])
        if (j!=y):
            if (height>=int(tree_height)):
                visible = 1
                break            
                
    return visible


visible_trees = 0


for y in range(1, max_y):
    for x in range(1, max_x):
        current_height = trees[y][x]
        if (square_height(x,y, current_height) == 0):
            visible_trees = visible_trees + 1
        

print (visible_trees+perimetr, visible_trees, perimetr)
   
# ----- end -----