#Name: Steve Chen
#ID: 261106847

MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'

def get_nth_row_from_map(str, n, width, height):
    """(str, int, int, int)-> str
    Takes string of the map, row index n, the height and the width to returns the nth row as a string
    >>> get_nth_row_from_map('^..>>>..v', 1, 3, 3)
    '>>>'
    >>> get_nth_row_from_map('^..>>>..v', 2, 3, 3)
    '..v'
    >>> get_nth_row_from_map('^..>>>..v', 3, 3, 3)
    ''
    """
    if n not in range(height):
        return ""
    else:
        start = n*width
        end = n*width+width
        return str[start:end]

def print_treasure_map(string, width, height):
    """(str, int, int)-> NoneType
    Takes a map string, width and height to print the map
    >>> print_treasure_map('123456789', 3, 3)
    123
    456
    789
    >>> print_treasure_map('123456789', 9, 1)
    123456789
    >>> print_treasure_map('123456789', 1, 9)
    1
    2
    3
    4
    5
    6
    7
    8
    9
    """
    k = 0
    for k in range (height):
        print(get_nth_row_from_map(string, k, width, height))

def change_char_in_map(string, row, col, c, width, height):
    """(str, int, int, int, int, int) -> str
    Take map string of dimension width and height with character c of index of row and col to return a new map string with c
    >>> change_char_in_map('123456789',1,1,'x',3,3)
    123
    4x6
    789
    >>> change_char_in_map('123456789',0,0,'x',3,3)
    x23
    456
    789
    >>> change_char_in_map('123456789',2, 2 ,'x',3,3)
    123
    456
    78x
    """
    if row not in range(height) or col not in range(width):
        return string
    else:
        index = row*width + col
        new_string = string[:index] + c + string[index+1:]
        return new_string


def get_proportion_travelled(string):
    """(string) -> float
    Take a map string and return the percentage of breadcrumbs over string length
    >>> get_proportion_travelled("1X34X6XX9")
    0.44
    >>> get_proportion_travelled("1234567X9")
    0.11
    >>> get_proportion_travelled("1X3")
    0.33
    """
    percentage = string.count(BREADCRUMB_SYMBOL)/len(string) 
    return round(percentage,2)

def get_nth_map_from_3D_map(string, n, width, height, depth):
    """(string, int, int, int, int)-> str
    Take map string with dimension width and height and depth and returns the nth map 
    >>> get_nth_map_from_3D_map('123456789876543210', 2, 3, 3, 2)
    ''
    >>> get_nth_map_from_3D_map('123456789876543210', 1, 3, 3, 2)
    876543210
    >>> get_nth_map_from_3D_map('123456789876543210', 0, 3, 3, 2)
    123456789
    """
    map_length = width*height
    if n in range(depth):
        return string[n*map_length:(n+1)*map_length]
    else:
        return ""

def print_3D_treasure_map(string, width, height, depth):
    """(str, int, int, int)->NoneType
    Take map string with dimension width and height and depth and print the maps separately
    >>> print_3D_treasure_map('123456789087654321', 3, 3, 2)
    123
    456
    678

    087
    654
    321
    >>> print_3D_treasure_map('123456789087654321', 2, 2, 1)
    12
    34
    >>> print_3D_treasure_map('123456789087654321', 2, 2, 3)
    12
    34

    56
    78

    90
    87
    """
    level = 0
    for level in range(depth):
        new_string = get_nth_map_from_3D_map(string, level, width, height, depth)
        print_treasure_map(new_string, width, height)
        if level+1 < depth:
            print()

def change_char_in_3D_map(string, row, column, d, c, width, height, depth):
    """(str, int, int, int, int, int, int, int)-> string
    Change the character of index row and column on the map of dimnesion width and heigth using the new character c
    >>> change_char_in_3D_map('123456789087654321', 0,0,0,'#',3, 3, 2)
    #23456789087654321
    >>> change_char_in_3D_map('123456789087654321', 0,2,0,'#',3, 3, 2)
    12#456789087654321
    >>> change_char_in_3D_map('123456789087654321', 2,2,1,'#',3, 3, 2)
    123456789087654321#
    """
    if row in range(height) and column in range(width) and d in range(depth): 
        # map_index = len(string)/row*col
        #change_char_in_map(string[d*width*heigth:], row, col, c width, height)
        index = d*width*height*width + row*width + column
        new_string = string[:index] + c + string[index+1:]
        return new_string
    else:
        return string
