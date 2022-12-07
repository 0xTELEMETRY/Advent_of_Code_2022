#*************************************************************************
#  Advent of Code 2022
#  Day 01 (Part 1)
#  Software Design Requirements:    day02_Req.txt
#  Input Data:                      day2.txt
#
#  Author: Nikolaj Gribakin (xASM)
#  Email: n.gribakin@gmail.com
#  Tel:   +420 773078426
#  
#*************************************************************************

input_file = open("day2.txt", "r")
lines = input_file.readlines()  #read all data

#A X - Rock (1)
#B Y - Paper (2)
#C Z - Scissors (3)

win = ["A Y", "B Z", "C X"]
draw = ["A X", "B Y", "C Z"]
loose = ["A Z", "B X", "C Y"]

score_selected_shape = 0
score_game_result = 0

current_shape = ''
result = 0

for line in lines:
    opponent_shape = line[0]
    my_shape = line[2]
    line = line.strip()
    
    if (line in win):
        score_game_result = 6
    if (line in draw):
        score_game_result = 3
    if (line in loose):
        score_game_result = 0
    
    my_shape = line[2]
    if (my_shape=="X"):
        score_selected_shape = 1
    if (my_shape=="Y"):
        score_selected_shape = 2
    if (my_shape=="Z"):
        score_selected_shape = 3

    result = result + score_game_result + score_selected_shape
    print(score_game_result, " ", score_selected_shape)

print(" --> ", result)
input_file.close()

#-----eof------

