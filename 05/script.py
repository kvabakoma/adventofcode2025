def parse_file_1():
    # with open("test.txt") as new_file:
    with open("input.txt") as new_file:
        
        parsing_fresh_ranges = True 
        fresh_ranges = []
        ingredients = []
        
        for line in new_file:
            
            if line == "\n":
                parsing_fresh_ranges = False            
            elif parsing_fresh_ranges == True:
                line = line.replace("\n", "")
                temp = line.split("-")                
                fresh_ranges.append((int(temp[0]), int(temp[1])))
            else:
                line = line.replace("\n", "")
                ingredients.append(int(line))
        
        return (fresh_ranges, ingredients)
                
def count_fresh_ingredients(data):
    result = 0
    fresh_ingredients = data[0]
    ingredients = data[1]
    for ingredient in ingredients:
        for fresh_range in fresh_ingredients:
            if fresh_range[0] <= ingredient <= fresh_range[1]:
                # print(f'{fresh_range[0]} <= {ingredient} <= {fresh_range[1]}')
                result += 1
                break
    
    return result

def parse_file_2():
    with open("test.txt") as new_file:
    # with open("input.txt") as new_file:

        ordered_ranges_strings = []
    
        for line in new_file:
            
            if line == "\n":
                break
            
            line = line.replace("\n", "")
            line_split = line.split("-")
            ordered_ranges_strings.append([int(line_split[0]), int(line_split[1])])
            
        ordered_ranges_strings.sort()
        
        print(ordered_ranges_strings)
        
            
def compare_next_range(data, next_entry):
    pass            
            
def count_fresh_ingredients_2(data):   
    
    updated_data = []
    for index, el in enumerate(data):
        updated_data = compare_next_range()
            
# data = (ranges, ingredients)
# data = parse_file_1()
# result = count_fresh_ingredients(data)
# print(f'Fresh Ingredients: {result}')

data2 = parse_file_2()
result2 = count_fresh_ingredients_2(data2)
# print(data[0])