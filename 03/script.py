total_joltage_two = 0    
total_joltage_twelve = 0

def find_largest_two_num_joltage(line):
    result_list = [0, 0]
    line = line.replace("\n", "")
    
    for i, c in enumerate(line):
        
        # handle the last action            
        if i == len(line) -1:
            if int(c) > result_list[1]:
                result_list[1] = int(c)
        
        # set index 0 if num is higher 
        elif int(c) > result_list[0]:
            result_list[0] = int(c) 
            result_list[1] = 0
            
        # move index 1 to index 0 if it is higher
        elif int(c) > result_list[1]:
            result_list[1] = int(c)
            
        # print(result_list, end=", ")
    
    local_result = int(str(result_list[0]) + str(result_list[1]))
    print(local_result, ": ", line)
    return local_result    
    
    
def find_largest_twelve_num_joltage(line):
    return 1
    
    
with open("test.txt") as new_file:
# with open("input.txt") as new_file:
    
    for line in new_file:
        total_joltage_two += find_largest_two_num_joltage(line)
        total_joltage_twelve += find_largest_twelve_num_joltage(line)
        
                
print("total_joltage_two:", total_joltage_two)
print("total_joltage_twelve:", total_joltage_twelve)