import pygame

def read(name):
    table = []
    with open(name, 'r') as file:
        for line in file:
            l = []
            for val in line:
                if val != ',' and val != '\n':
                    l.append(int(val))
            table.append(l)
    if table[0] == []:
        table.pop(0)
    return table

def neighbors(table, index, length):
    # Unpack index
    x, y = index
    corners = [(0, 0), (0, length - 1), (length - 1, 0), (length - 1, length - 1)]
    neighbors = 0

    # Check for edges or corners
    if (x, y) in corners:
        action = corners.index((x, y))
        
        match action:
            case 0:
                return table[0][1] + table[1][0] + table[1][1]
            
            case 1:
                return table[length - 2][0] + table[length - 2][1] + table[length - 1][1]
            
            case 2:
                return table[0][length - 2] + table[1][length - 2] + table[1][length - 1]
            
            case 3:
                return table[length - 2][length - 1] + table[length - 2][length - 2] + table[length - 1][length - 2]
    
    # Left edge
    elif x == 0:
        return table[y - 1][0] + table[y - 1][1] + table[y][1] + table[y + 1][0] + table[y + 1][1]

    # Right edge
    elif x == length - 1:
        return table[y - 1][length - 1] + table[y - 1][length - 2] + table[y][length - 2] + table[y + 1][length - 1] + table[y + 1][length - 2]

    # Top
    elif y == 0:
        return table[0][x - 1] + table[0][x + 1] + table[1][x - 1] + table[1][x] + table[1][x + 1]

    # Bottom
    elif y == length - 1:
        return table[length - 2][x - 1] + table[length - 2][x] + table[length - 2][x + 1] + table[length - 1][x - 1] + table[length - 1][x + 1] 

    else:
        for i in range(-1, 2):
            neighbors += table[y - 1][x + i]
            neighbors += table[y + 1][x + i]
        neighbors += table[y][x - 1] + table[y][x + 1]
    return neighbors

def zeros(length):
    return [[0 for _ in range(length)] for _ in range(length)]