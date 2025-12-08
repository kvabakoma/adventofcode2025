fresh_ingredient = []


def parse_file():
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
            
# data = (ranges, ingredients)
data = parse_file()
# print(data)
result = count_fresh_ingredients(data)
print(f'Fresh Ingredients: {result}')