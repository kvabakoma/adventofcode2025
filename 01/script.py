dial = list(range(100))
current_key = 50
result = 0

def calculate_next_key(curr_key, action):
    action = line.replace("\n", "")
    # print(curr_key, action)
        
    # add / remove key value
    if action[0] == "L":
        curr_key -= int(action[1:])
    elif action[0] == "R":
        curr_key += int(action[1:])
        
    # normalize the key value
    if curr_key > len(dial) -1:
        curr_key = curr_key % len(dial)
    elif curr_key < 0:
        curr_key = dial[curr_key % len(dial)]
    
    return curr_key

# with open("test.txt") as new_file:
with open("input.txt") as new_file:
    count = 0
    total_length = 0

    for line in new_file:
        current_key = calculate_next_key(current_key, line)
        if current_key == 0:
            result += 1

print(result)