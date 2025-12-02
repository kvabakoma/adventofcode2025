
def find_duplicates(range_start, range_end):
    i = int(range_start)    
    res = 0
    
    my_list = list(range(int(range_start), int(range_end)+1, 1))
    for el in my_list:
        skip = False
        el_str = str(el)
        str_len = len(el_str)
        if str_len % 2 == 0:
            print(el_str[:str_len//2], el_str[str_len//2:])
            if el_str[:str_len//2] == el_str[str_len//2:]:
                res += el         
                skip = True                   
    
        if skip == False:
            pattern = ""
            c = el_str[0]
            while c not in pattern:
                
            for c in el_str:
                if c not in pattern:
                    pattern += c
                    print(pattern)
                else:
                    print('pre break')
                    break
            
            temp_str = el_str
            while pattern in temp_str:
                temp_str = temp_str[len(pattern)-1:]
            
            if temp_str == "":
                res += el 
    
    return res

count = 0
with open("test.txt") as new_file:
# with open("input.txt") as new_file:
    
    for line in new_file:
        line.replace("\n", "")
        line.replace(" ", "")
        ranges_raw = line.split(",")
        ranges = []
        for el in ranges_raw:
            el_split = el.split("-")
            duplicates = find_duplicates(el_split[0], el_split[1])
            count += duplicates

print(count)