import math

junction_boxes = []
distances = []
circuits = []

def calculate_distance(a, b):
    distance = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
    # print("calculate_distance:", a, b, distance)
    return distance

def parse_data_file(datafile):
    temp_list = []
    with open(datafile) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            coordinates = list(map(int, line.split(",")))
            temp_list.append(coordinates)

    return temp_list


def calculate_distances_between_points(junction_boxes):
    print(f'junction_boxes: {junction_boxes}')
    res = []
    for i_a, el_a in enumerate(junction_boxes):
        for i_b, el_b in enumerate(junction_boxes[i_a+1:]):
            print(f'el_a: {el_a}, el_b: {el_b}, distance: {calculate_distance(el_a, el_b)}')
            res.append((calculate_distance(el_a, el_b), i_a, i_b, el_a, el_b)) 
    # results = [(calculate_distance(a, b), i_a, i_b, a, b) for i_a, a in enumerate(junction_boxes) for i_b, b in enumerate(junction_boxes[i_a+1:])]
    return sorted(res)


def calculate_shortest_circuits(data, iterations):
    # init the 
    

    result = [[data[0][1], data[0][2]]]
    for i in range(0, iterations):       
        flat_data = [x for sublist in result for x in sublist]
        print(f'i: {i}, data[i]: {data[i]}')
        if data[i][1] in flat_data:
            if data[i][2] in flat_data:
                # both already in the list - skip
                pass
            else:
                # find the circuit where A is located and add B to it
                for el in result:
                    if data[i][1] in el:
                        el.append(data[i][2])
        elif data[i][2] in flat_data:
            if data[i][1] in flat_data:
                # both already in the list - skip
                pass
            else:
                # find the circuit where B is located and add A to it
                for el in result:
                    if data[i][2] in el:
                        el.append(data[i][1])
        else:
            # neither point exists in the results array -> we add them as a new circuit
            result.append([data[i][1], data[i][2]])
             
    return result


def calculate_circuitss_product(data):
    result = 1
    for num in data[:3]:
        result *= len(num)
        
    return result

junction_boxes = parse_data_file("test.txt")
distances = calculate_distances_between_points(junction_boxes)
circuits = calculate_shortest_circuits(distances, 10)
result = calculate_circuitss_product(circuits)
# print(junction_boxes)
# print(distances)
print(circuits)
print(f'final size of curcits: {result}')

# {\displaystyle d(p,q)={\sqrt {(p_{1}-q_{1})^{2}+(p_{2}-q_{2})^{2}+(p_{3}-q_{3})^{2}}}.}