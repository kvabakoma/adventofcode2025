dial = list(range(100))
current_key = 50

with open("input.txt") as new_file:
    count = 0
    total_length = 0

    for line in new_file:
        count += 1

print("Total n of lines:", count)