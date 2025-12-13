import math

junction_boxes = []
distances = []
circuits = []

def calculate_distance(a, b):
    distance = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
    # print(a, b, distance)
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
    results = [(calculate_distance(a, b), a, b) for i, a in enumerate(junction_boxes) for b in junction_boxes[i+1:]]
    return sorted(results)


def calculate_shortest_circuits(data, iterations):
    temp = []
    temp.extend(data[:iterations])
    result = []
    print(temp)

    return result

junction_boxes = parse_data_file("test.txt")
distances = calculate_distances_between_points(junction_boxes)
circuits = calculate_shortest_circuits(distances, 10)
# print(junction_boxes)
# print(distances)

# {\displaystyle d(p,q)={\sqrt {(p_{1}-q_{1})^{2}+(p_{2}-q_{2})^{2}+(p_{3}-q_{3})^{2}}}.}