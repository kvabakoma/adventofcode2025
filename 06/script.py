
def clean_multiple_white_spaces(input_text):
    split_text = input_text.split(" ")
    cleaned_split_text = [s for s in split_text if s != ""]

    return cleaned_split_text


def solve_problems(problem):
    solutions = []

    for el in problem:
        if el[-1] == "+":            
            temp = 0
            for n in el[:-1]:
                temp += int(n)
            solutions.append(temp)
        elif el[-1] == "*":
            temp = 1
            for n in el[:-1]:
                temp *= int(n)
            solutions.append(temp)
        
    return solutions


def format_vertical_problems():
    problems = []

    # with open("test.txt") as new_file:
    with open("input.txt") as new_file:
        counter = 0
        for line in new_file:
            line = line.replace("\n", "")
            line_list = clean_multiple_white_spaces(line)

            if len(problems) == 0:
                for el in line_list:
                    problems.append([])

            for i, el in enumerate(problems):
                el.append(line_list[i])

            counter += 1

    return problems


formatted_problems = format_vertical_problems()
problems_solved = solve_problems(formatted_problems)
print(formatted_problems)
print(problems_solved)
print(f'final total: {sum(problems_solved)}')
# Problem 1:
# 123 * 45 * 6 = 33210
# 328 + 64 + 98 = 490
# 51 * 387 * 215 = 4243455
# 64 + 23 + 314 = 401
# 33210 + 490 + 4243455 + 401 = 4277556
