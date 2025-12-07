# 2 dimentional array
# loop through each entry
# check adjacent tiles
    # row-1 index-1, index, index+1
    # row index-1, index+1
    # row+1 index-1, index, index+1
# 
list2d = []
max_filled_neighbors = 3

def find_tiles_with_sub4_neighbors():
    result = 0
    char = "@"
    
    for row_index, row in enumerate(list2d):
        
        for el_index, el in enumerate(row):
            if list2d[row_index][el_index] != char:
                continue
            
            neighbors = []
            filled_neighbors = 0
            
            # check top row
            if row_index > 0:                
                if el_index > 0: 
                    neighbors.append([row_index-1, el_index-1])
                                
                neighbors.append([row_index-1, el_index])
                
                if el_index < len(row)-1:
                    neighbors.append([row_index-1, el_index+1])
                
            # check el's row
            if el_index > 0:
                neighbors.append([row_index, el_index-1])

            if el_index < len(row)-1:
                neighbors.append([row_index, el_index+1])
            
            # check bottom row
            if row_index < len(row)-1:
                if el_index > 0: 
                    neighbors.append([row_index+1, el_index-1])
                                
                neighbors.append([row_index+1, el_index])
                
                if el_index < len(row)-1:
                    neighbors.append([row_index+1, el_index+1])
                    
            # print(f'[{row_index},{el_index}], neighbors:{neighbors}')
            for el in neighbors:                                  
                if list2d[el[0]][el[1]] == char:
                    filled_neighbors += 1                         
            
            if filled_neighbors <= max_filled_neighbors:
                result += 1
                # print(row_index, el_index, filled_neighbors)
                
    
    return result

# with open("test.txt") as new_file:
with open("input.txt") as new_file:
    
    for line in new_file:        
        line = line.replace("\n", "")
        list2d.append(list(line))        
        
        
result = find_tiles_with_sub4_neighbors()
print(result)