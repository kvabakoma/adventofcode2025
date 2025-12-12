
def count_splits(filename):  
    splitter_char = "^"
    splits = 0
    with open(filename) as new_file:       
        splits = 0
        beams = []
        for i_line, line in enumerate(new_file):
            
            splits_in_this_line = 0
            
            # initialize beams list
            if i_line == 0:
                beams = [False] * len(line)
                for i_char, ch in enumerate(line):
                    if ch == "S":
                        beams[i_char] = True
                        break
                continue
            
            # handle splits and beams    
            for i_char, ch in enumerate(line):
                if ch == splitter_char:
                    if beams[i_char] == True:
                        beams[i_char] = False
                        beams[i_char-1] = True
                        beams[i_char+1] = True
                        splits_in_this_line += 1
                        
            splits += splits_in_this_line
                    
    return splits
            

result = count_splits("input.txt")
print(f'total splits: {result}')