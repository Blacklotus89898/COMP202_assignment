#Name: Steve Chen
#ID: 261106847

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

            string_list = compressed_image[row][element].split("x")
            
            if float(string_list[0]) < 0 or float(string_list[0]) > 255:
                return False

            sum_B += float(string_list[1]) 
        if row == 0:
            current_sum_B = sum_B
            
        elif sum_B != current_sum_B:
            return False
    return True

def load_regular_image(filename):
    """(str)->list
    Takes a filename and converts it into a an image matrix
    If the format is not valid raise AssetionError
    Returns an image matrix
    >>> load_regular_image("try.txt")
    AssertionError: The format is not in valid PGM
    >>> load_regular_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    """
    new_matrix_list = []
    fobj = open(filename, "r")
    content = fobj.read()
    content_list = content.split('\n')
    if content_list[0] != 'P2':
        raise AssertionError("The format is not in valid PGM")
    k = content_list[1].split(' ')
    width = float(k[0])
    height = float(k[1])
    max_white_value = float(content_list[2])
    matrix_list = content_list[3:]
    for row in range(int(height)):
        n = matrix_list[row].split()
        for j in range(int(width)):
            n[j] = int(n[j])
        new_matrix_list.append(n)
    if not is_valid_image(new_matrix_list):
        raise AssertionError("The format is not in valid PGM")
    fobj.close()
    return(print(new_matrix_list))
        
    #print(new_matrix_list)
"""   for row in range(height):  
        for element in range(width):
        image_matrix = image_matrix.append()
"""
"""for line in fobj:
        print(line.strip("\n"))"""
    #fobj.close()

    #print(content)
""" content = fobj.read()
    if not is_valid_compressed_image(content) or not is_valid_image(content):
        raise ValueError("The image is not in valid PGM format")
    for i in range(len(content)):
        mylist.append(content[i])
    fobj.close()
    return mylist"""
    


#load_regular_image("comp.pgm")
#load_regular_image("try.txt")
#load_regular_image("dragon.pgm")

def load_compressed_image(filename):
    """(str)->list
    Takes a filename and converts it into a an image matrix
    If the format is not valid raise AssetionError
    >>> fobj = open("invalid.pgm","w")
    >>> fobj.write("P2C\\n30 5\\n255\\nabc3x23 0x0x07\\n")
    28
    >>> fobj.close()
    >>> load_compressed_image("invalid.pgm")
    """
    new_matrix_list = []
    fobj = open(filename, "r")
    content = fobj.read()
    content_list = content.split('\n')
    if content_list[0] != 'P2C':
        raise AssertionError("The format is not in compressed PGM")
    k = content_list[1].split(' ')
    width = float(k[0])
    height = float(k[1])
    #max_white_value = float(content_list[2])
    matrix_list = content_list[3:]
    #raise error
    for row in range(int(height)):
        n = matrix_list[row].split()
        new_matrix_list.append(n)
    if not is_valid_compressed_image(new_matrix_list):
        raise AssertionError("The format is not in valid compressed PGM")
    fobj.close()
    return(print(new_matrix_list))

#load_compressed_image("comp.pgm.compressed")
fobj = open("invalid.pgm","w")
fobj.write("P2C\n30 5\n255\nabc3x23 0x0x07\n")
fobj.close()
fobj = open("invalid.pgm","r")
c = fobj.read()
for line in fobj:
    print(line.strip)
print(c)
fobj.close()
#load_compressed_image("invalid.pgm")
#load_compressed_image("try.txt")

def load_image(filename):
    """
    """
    fobj = open(filename, "r")
    content = fobj.read()
    content_list = content.split('\n')
    if content_list[0] == 'P2':
        load_regular_image(filename)
    elif content_list[0] == 'P2C':
        load_compressed_image(filename)
    else:
        raise AssertionError("The file is not a PGM or compressed PGM")



if __name__ == "__main__":
    import doctest
    doctest.testmod()
