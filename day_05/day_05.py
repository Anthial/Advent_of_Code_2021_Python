import numpy as np

def part_1():
    matrix = np.zeros((1000, 1000))
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.split('\n')[0]
            line = line.split(' -> ')
            #get x1, y1 and x2, y2
            point_1 = line[0].split(',')
            x1 = int(point_1[0])
            y1 = int(point_1[1])
            point_2 = line[1].split(',')
            x2 = int(point_2[0])
            y2 = int(point_2[1])
            if x1 == x2 or y1==y2:
                draw_straight_line(x1, x2, y1, y2, matrix)
    return matrix
            

def draw_straight_line(x1, x2, y1, y2, matrix):
    if x1 == x2:
        ymax = max(y1, y2)
        ymin = min(y1, y2)
        #plus one since there is a need for an inclusive range
        for a in range(ymax-ymin + 1):
            a += ymin
            matrix[x1, a] += 1
    else:
        xmax = max(x1, x2)
        xmin = min(x1, x2)
        for a in range(xmax-xmin + 1):
            a += xmin 
            matrix[a, y1] += 1

def overlapping_points(matrix):
    return (matrix >= 2).sum()

def part_2(matrix):
    #so sad to do io again but I can't be bothered to make it better, but I mean if one needed both straigh and diagonal lines one could just move the diagonal update into part_1()
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.split('\n')[0]
            line = line.split(' -> ')
            #get x1, y1 and x2, y2
            point_1 = line[0].split(',')
            x1 = int(point_1[0])
            y1 = int(point_1[1])
            point_2 = line[1].split(',')
            x2 = int(point_2[0])
            y2 = int(point_2[1])
            if y1 != y2 and x1 != x2:
                draw_diagonal_line(matrix, x1, x2, y1, y2)
    return matrix

def draw_diagonal_line(matrix, x1, x2, y1, y2):
    x_plus = False
    y_plus = False
    if x1 < x2:
        x_plus = True
    if y1 < y2:
        y_plus = True
    #remember to allow for the while loop to actually hit x2 as well
    if x_plus:
        x2 +=1
    else:
        x2 -= 1
    #basic matrix iteration
    while x1 != x2:
        matrix[x1, y1] += 1
        if x_plus:
            x1 += 1
        else:
            x1 -= 1
        if y_plus:
            y1 += 1
        else:
            y1 -= 1 


    
    

if __name__ == '__main__':
    matrix = part_1()
    print(overlapping_points(matrix))
    print(overlapping_points(part_2(matrix)))