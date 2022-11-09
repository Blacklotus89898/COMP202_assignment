#Name: Steve Chen
#ID: 261106847

import os
def is_valid_image(image):
    """(list) -> bool
    Takes a nested list returns whether the list is a valid PGM matrix
     with each row having the same length
    >>> is_valid_image([[1,2,3],[4,5,6],[7,8,9]])
    True
    >>> is_valid_image([[1],[0,0]])
    False
    >>> is_valid_image([["0x5", "200x2"],["11x7"]])
    False
    """
    for row in range(len(image)):
        if len(image[0]) != len(image[row]):
            return False
    return True

def is_valid_compressed_image(compressed_image):
    """(list)->bool
    Takes a nested list and return if the list is a compressed PGM matrix
    >>> is_valid_compressed_image([["0x5","200x2"],["111x7"]])
    True
    >>> is_valid_compressed_image([[1,2,3],[4,5,6],[7,8,9]])
    False
    >>> is_valid_compressed_image([["0x5","200x2"],["111x6"]])
    False
    """
    
    for row in range(len(compressed_image)):
        sum_B = 0
        for element in range(len(compressed_image[row])):
            if type(compressed_image[row][element]) != str:
                return False
            #compressed_image[row][element].split("x")
            string_list = compressed_image[row][element].split("x")
            
            if float(string_list[0]) < 0 or float(string_list[0]) > 255:
                return False

            sum_B += float(string_list[1]) #float(compressed_image[row][element][1]) 
        if row == 0:
            current_sum_B = sum_B
            
        elif sum_B != current_sum_B:
            return False
    return True

def load_regular_image(filename):
    """(str)->list
    Takes a filename and converts it into a an image matrix

    """
    mylist = []
    c = open(filename, "r")
    """ content = fobj.read()
    if not is_valid_compressed_image(content) or not is_valid_image(content):
        raise ValueError("The image is not in valid PGM format")
    for i in range(len(content)):
        mylist.append(content[i])
    fobj.close()
    return mylist"""
    


load_regular_image("comp.pgm")
#load_regular_image("another.py")
#load_regular_image("dragon.pgm")


#open("lol.txt", 'w')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
