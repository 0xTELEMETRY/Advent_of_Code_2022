#*************************************************************************
#  Advent of Code 2022
#  Day 08 (Parts 1..2)
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
    line_of_sight_1 = 0
    line_of_sight_2 = 0
    line_of_sight_3 = 0
    line_of_sight_4 = 0
    
    visible = 0
    
    for i in range(x-1, -1, -1):
        height = int(trees[y][i])
        if (i!=x):
            line_of_sight_1 = line_of_sight_1 + 1
            if (height>=int(tree_height)):
                visible = 1
                break
            
                
    
    visible = 0
              
    for i in range(x, line_len):
        height = int(trees[y][i])
        if (i!=x):
            line_of_sight_2 = line_of_sight_2 + 1
            if (height>=int(tree_height)):
                visible = 1
                break
        
    visible = 0
    
    for j in range(y-1,-1, -1):
        height = int(trees[j][x])
        if (j!=y):
            line_of_sight_3 = line_of_sight_3 + 1
            if (height>=int(tree_height)):
                visible = 1
                break
            
                
    
    visible = 0
    
    for j in range(y, total_lines):
        height = int(trees[j][x])
        if (j!=y):
            line_of_sight_4 = line_of_sight_4 + 1
            if (height>=int(tree_height)):
                visible = 1
                break
            
                

    scene_score = line_of_sight_1 * line_of_sight_2 * line_of_sight_3 * line_of_sight_4
    print (line_of_sight_1, line_of_sight_2, line_of_sight_3, line_of_sight_4)
    return scene_score


visible_trees = 0
max_global_scene_score = 0
global_scene_score = 0


for y in range(1, max_y):
    for x in range(1, max_x):
        current_height = trees[y][x]
        global_scene_score = square_height(x,y, current_height)
        if (global_scene_score> max_global_scene_score):
            max_global_scene_score = global_scene_score

        

print (max_global_scene_score)
   
# ----- end -----