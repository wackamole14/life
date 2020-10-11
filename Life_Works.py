# import sys
# rows = int(sys.argv[1])
# columns = int(sys.argv[2])
import random
simulation = 1
columns,rows = 20,8
matrix = [[random.randint(0,1) for x in range(columns)] for y in range(rows)]

def setUpBoard():
# print top of box
    for i in range(columns + 2):
        print('_', end="")
    print('\n', end="")
    # print the sums in the matrix
    for x in range(rows):
        print("|", end="")
        for y in range(columns):
            # Begin rule for printing
            if matrix[x][y] == 1:
                print("x", end="")
            else:
                print(" ", end="")
        print("|")
    for i in range(columns + 2):
        print('-', end="")
    print('\n')

    print("Life has begun. Would you like to simulate the next iteration? (y/n)")
    answer = input()
    if answer.lower() != "y":
        return False
    else:
        return True

def life():
    iterating = True
    while iterating:
        global simulation
        if simulation == 1:
            iterating = setUpBoard()
            # print top of box
        for i in range(columns + 2):
            print('_', end="")
        print('\n', end="")
            # print the sums in the matrix
        for x in range(rows):
            print("|", end="")
            for y in range(columns):
                #check placments
                neighbors,live = checkNeigh(x,y)
                    # Begin rule for printing
                if live == True:
                    if neighbors == 2 or neighbors == 3:
                        print("x", end="")
                        matrix[x][y] = 1
                    else:
                        print(" ", end="")
                        matrix[x][y] = 0
                else:
                    if neighbors == 3:
                        print("x", end="")
                        matrix[x][y] = 1
                    else:
                        print(" ", end="")
                        matrix[x][y] = 0
            print("|")
        for i in range(columns + 2):
            print('-', end="")
        print('\n')
        simulation += 1
        print(f"Simulation: {simulation}")
        print("would you like to simulate the next iteration? (y/n)")
        answer2 = input()
        if answer2.lower() == "y":
            continue
        else:
            break

def checkNeigh(x,y):
#check for corner cases
    neighbors = 0
    live = False
    if x != 0:
        top = True
    else:
        top = False
    if x != rows-1:
        bottom = True
    else:
        bottom = False
    if y != 0:
        left = True
    else:
        left = False
    if y != columns-1:
        right = True
    else:
        right = False
    if matrix[x][y] == 1:
        live = True
#check top
    if top == True:
        #middle
        if matrix[x - 1][y] == 1:
            neighbors += 1
        #left
        if left == True:
            if matrix[x-1][y-1] == 1:
                neighbors += 1
        #right
        if right == True:
            if matrix[x - 1][y + 1] == 1:
                neighbors += 1
#check sides of life
    #left
    if left == True:
        if matrix[x][y - 1] == 1:
            neighbors += 1
    #right
    if right == True:
        if matrix[x][y + 1] == 1:
            neighbors += 1
 #check bottom of life
    if bottom == True:
        if matrix[x + 1][y - 1] == 1:
            neighbors += 1
        if left== True:
            if matrix[x + 1][y] == 1:
                neighbors += 1
        if right == True:
            if matrix[x + 1][y + 1] == 1:
                neighbors += 1
    return neighbors, live

life()