total_joltage = 0

# with open("test.txt") as new_file:
with open("input.txt") as new_file:
    
    for line in new_file:
        last_num_was_highest = False
        result_list = [0, 0, 0]
        line = line.replace("\n", "")
        
        for i, c in enumerate(line):
            
            # handle the last action            
            if c == len(line) -1:
                if last_num_was_highest == True:
                    result_list[1] = result_list[0]
                    result_list[0] = result_list[2]
                continue
            
            # if the previous action moved index 1 to 0, force the current number to index 1
            if last_num_was_highest == True:
                result_list[1] = int(c)
                last_num_was_highest = False
                continue
             
            # reset last action flag
            last_num_was_highest = False
            
            # set index 1 if num is higher
            if int(c) > result_list[1]:
                result_list[1] = int(c)
            
            # move index 1 to index 0 if it is higher
            if result_list[1] > result_list[0]:
                result_list[2] = result_list[0]
                result_list[0] = result_list[1]
                last_num_was_highest = True
                
            # print(result_list, end=", ")
        
        local_result = int(str(result_list[0]) + str(result_list[1]))
        print(local_result, ": ", line)
        total_joltage += local_result
                
print("total_joltage", total_joltage)