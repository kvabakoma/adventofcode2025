
def count_splits(filename):  
    splits = 0
    with open(filename) as new_file:       
        first_split_found = False 
        for line in new_file:
            splits_on_this_line = 0
            for ch in line:                    
                if ch == "^":
                    splits_on_this_line += 1
            
            if splits_on_this_line > 0:
                if first_split_found == False:
                    first_split_found = True
                else:
                    splits += splits_on_this_line
    
    return splits
            

result = count_splits("input.txt")
print(f'total splits: {result}')