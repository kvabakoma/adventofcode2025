total_joltage = 0    
    
# with open("test.txt") as new_file:
with open("input.txt") as new_file:
    
    for line in new_file:
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
        total_joltage += local_result
                
print("total_joltage:", total_joltage)