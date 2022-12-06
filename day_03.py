input_file = open("day3.txt", "r")
lines = input_file.readlines()  #read all data

first_half = ""
second_half = ""

chrs_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

line_len = 0

result = 0

for line in lines:

    line = line.strip()

    line_len = len(line)
    divider = int(line_len/2)

    first_half = line[0:divider]
    second_half = line[divider:line_len]
    #print(" --> ", line, " ", first_half, " ", second_half)

    found_chr = ''.join(set(first_half).intersection(second_half))
    
    priority = chrs_str.find(found_chr)+1
    if (found_chr == "Z"):
        print (priority)

    result = result + priority
    
print(result)
input_file.close()

    

