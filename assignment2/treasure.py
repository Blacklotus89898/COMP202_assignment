#Name: Steve Chen
#ID: 261106847
from treasure_utils import *
import random

def generate_treasure_map_row(width, map_3D):
    """ (int, bool)-> str
    Take the wodth of a row and check if the amp is 3D to return a random map string
    >>> generate_treasure_map_row(10, True) 
    <><^^<.>^*
    >>> generate_treasure_map_row(5, False) 
    <.<v.
    >>> generate_treasure_map_row(2, True)
    v< 
    """
    new_string = ""
    for i in range(width):
        symbol = random.randint(1,6)
        if symbol != 1:
            new_string = new_string + MOVEMENT_SYMBOLS[random.randint(0, 3)]
        else:
            new_string = new_string + EMPTY_SYMBOL
    if map_3D:
        movement = random.randint(1,2)
        if movement == 1:
            movement_index = random.randint(0, width-1)
            new_string = new_string[:movement_index] + MOVEMENT_SYMBOLS_3D[random.randint(0,1)]+ new_string[movement_index+1:]#random.choice(MOVEMENT_SYMBOLS_3D) + new_string[movement_index+1:]
    return new_string

def generate_treasure_map(width, height, map_3D):
    """(int, int, bool)->str
    Check is the map is free and returns a map string of dimension width and height
    >>> generate_treasure_map(3, 3, True)
    >v*|^.<<^
    >>> generate_treasure_map(3, 2, True)
    ><<<<>
    >>> generate_treasure_map(4, 4, False)
    >>^<<.^>.v>>.v>v
    """
    string = ''
    for j in range(height):
        string = string + generate_treasure_map_row(width, map_3D)
    string = change_char_in_map(string, 0, 0, '>', width, height)
    return string


def generate_3D_treasure_map(width, height, depth):
    """(int, int, int)-> str
    Returns a map string of dimension width and height of depth level
    >>> generate_3D_treasure_map(3, 3, 2)
    >>*^<<^v*>vv^|<.^> 
    >>> generate_3D_treasure_map(2, 2, 2) 
    >.|v>*v|
    >>> generate_3D_treasure_map(3, 3, 3) 
    >vv.*<<>|>.>v^*><v>v.^<.<<<
    """
    string = ''
    for level in range(depth):
        string = string + generate_treasure_map(width, height, True)
    return string

def right(index, width):
    """(int, int)-> int
    Takes the index and width to return the new index when moving right
    """
    if (index+1)%width != 0:
        index = index + 1
    else:
        index = index + 1 - width
    return index

def left(index, width):
    """(int, intt)-> int
    Returns the new index after moving to the left using
    """
    travelled_map = travelled_map + BREADCRUMB_SYMBOL
    if (index-1)%width == 0:
        new_index = (index-1) + width
    else:
        new_index = index - 1
    return new_index

def up(index, width, height):
    """(int, int, int)-> int
    Returns the new index when moving up
    """
    if int(index/width) % height == 0:
        new_index  = index + (width*height-1)
    else:
        new_index = index - width
    return new_index

def down(index, width, height):
    """(int, int, int)-> int
    Returns the new index after moving down
    
    """
    if int(index/width +1)%(height) == 0:
        new_index = index - width*(height-1)
    else:
        new_index = index + width
    return new_index

def climb(index, width, height):
    """(int, int, int)-> int
    Returns the new inex after moving up a map
    
    """
    new_index = index - width*height
    return new_index

def fall(index, width, height):
    """(int, int, int)-> int
    Returns the new index after moving down a map
    """
    new_index = index + width*height
    return new_index

def get_character(string, index, treasure_count):
    """(str, int, int)-> str
    Returns the movement character preceding the treasure or empty symbol 
    """
    if string[index] == EMPTY_SYMBOL:
        return get_character(string, index-1, treasure_count)

    elif string[index] == TREASURE_SYMBOL:
        return get_character(string, index-1, treasure_count)
        
    else: 
        return string[index]


def check_action(string, index, width, height, treasure_count):
    """(str, int, int, int, int)-> int
    Returns the new index depending on the movement character
    
    """
    character = get_character(string, index, treasure_count)
    if character == '>':
        return right(index, width)
    elif character == '^':
        return up(index, width, height)
    elif character == '<':
        return left(index, width)
    elif character == 'v':
        return down(index, width, height)
    elif character == '|':
        return climb(index, width, height)
    elif character == '*':
        return fall(index, width, height)


def follow_trail(string, row, col, level, width, height, depth, tiles):
    """(str, int, int, int, int, int, int, int)-> str
    Takes the initial index as row and col and follows the map of dimension width and heigth 
    for tiles number of symbol or when reaching a breadcrumb symbol. Returns the travelled map.
    Prints the number of symbol and treasure count
    >>> follow_trail('>>v..v', 0, 0, 0, 3, 2, 1, -1)
    Treasures collected: 0
    Symbols visited: 4
    >>> follow_trail('>>v..v', 0, 0, 0, 3, 2, 1, 0)

    >>> follow_trail('>+....', 0, 0, 0, 3, 2, 1, 5)
    Treasures collected: 1
    Symbols visited: 3
    """
    treasure_count = 0
    s_count = 0
    travelled_map = ''
    transformed_map = ''
    index = level*(width*height) + row*width + col
    if col not in range(width) or row not in range(height) or level not in range(depth) or tiles < -1 or tiles == 0:
        return string

    elif tiles == -1:
        tiles = len(string)

    for i in range(tiles): 
        if string[index] != BREADCRUMB_SYMBOL:
            s_count += 1

        if string[index] == TREASURE_SYMBOL: 
            treasure_count += 1

        if string[index] in MOVEMENT_SYMBOLS: 
            travelled_map = travelled_map + string[len(travelled_map):index]+ BREADCRUMB_SYMBOL
            transformed_map = travelled_map[:index+1] + string[index+1:]

        else:
            travelled_map = travelled_map + string[index]
                    
        previous_index = index    
        index = check_action(string, index, width, height, treasure_count)

        if transformed_map[index] == BREADCRUMB_SYMBOL:
            break
 
    print("Treasures collected: " + str(treasure_count))
    print("Symbols visited: " + str(s_count))
    transformed_map = travelled_map[:previous_index+1] + string[previous_index+1:]
    return transformed_map
