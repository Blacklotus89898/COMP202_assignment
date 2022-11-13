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
    #>>> load_regular_image("try.txt")
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
    #print(new_matrix_list)#convert to return
    return(new_matrix_list) #convert to return
        
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

    #>>> load_compressed_image("invalid.pgm")
    raise IndexError("The dimension is incorrect")
    """
    new_matrix_list = []
    fobj = open(filename, "r")
    content = fobj.read()
    content_list = content.split('\n')
    if content_list[0] != 'P2C':
        raise AssertionError("The format is not in compressed PGM")
    k = content_list[1].split(' ')
    width = int(k[0])
    height = int(k[1])
    #max_white_value = float(content_list[2])
    matrix_list = content_list[3:]
    #raise error
    if len(matrix_list) < height:
        raise IndexError("The dimension is incorrect")
    for row in range(int(height)):

        line = matrix_list[row].split()
        if line.count("x") > 1*width:
            raise AssertionError("Too many x pixels")
        new_matrix_list.append(line)
    if not is_valid_compressed_image(new_matrix_list):         
        raise AssertionError("The format is not in valid compressed PGM")
    fobj.close()
    return(new_matrix_list)#convert to return

#load_compressed_image("comp.pgm.compressed")
"""fobj = open("invalid.pgm","w")
fobj.write("P2C\n30 5\n255\nabc3x23 0x0x07\n")
fobj.close()
fobj = open("invalid.pgm","r")
c = fobj.read()
for line in fobj:
    print(line.strip)
print(c)
fobj.close()"""
#load_compressed_image("invalid.pgm")
#load_compressed_image("try.txt")

def load_image(filename):
    """
    """
    fobj = open(filename, "r")
    content = fobj.read()
    content_list = content.split('\n')
    if content_list[0] == 'P2':
        return load_regular_image(filename)
    elif content_list[0] == 'P2C':
        return load_compressed_image(filename)
    else:
        raise AssertionError("The file is not a PGM or compressed PGM")

#load_image("comp.pgm.compressed")
#load_image("invalid.pgm")


def save_regular_image(matrix_list, filename):
    """(list(list), str)-> Nonetype
    Take a nested list and filename as input to format a pgm file

    #>>> save_regular_image([[2]*5, [3]*5], "test.pgm")

    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\\n10 3\\n255\\n0 0 0 0 0 0 0 0 0 0\\n255 255 255 255 255 255 255 255 255 255\\n0 0 0 0 0 0 0 0 0 0\\n'
    >>> fobj.close()

    >>> image = [[0]*10, [255]*10, [0]*10]
    >>> save_regular_image(image, "test.pgm")
    >>> image2 = load_image("test.pgm")
    >>> image == image2
    True

    """

    fobj = open(filename, "w")
    fobj.write("P2\n")
    if not is_valid_image(matrix_list):
        raise AssertionError("The matrix is not a valid PGM")
    width = len(matrix_list[0])
    height = len(matrix_list)
    fobj.write(str(width) + " " + str(height)+"\n")
    #max_white_value = 0
    max_white_value = 255 # tahst a constatn dumymy
    newline = ""
    for row in range(height):
        for element in range(width):
            if int(matrix_list[row][element]) > max_white_value:
                max_white_value = (matrix_list[row][element])

            newline += str(matrix_list[row][element]) 
            if element != (int(width)-1):
                newline += " "
        newline += "\n"

    fobj.write(str(max_white_value)+"\n")
    fobj.write(newline)
    fobj.close()


#save_regular_image([[2]*5, [3]*5], "test.pgm")
"""image = [[2]*5, [3]*5]
save_regular_image([[2]*5, [3]*5], "test.pgm")
fobj = open("test.pgm", 'r')
print(fobj.read())
fobj.close()
image2 = load_image('test.pgm')
print(image == image2)
"""

def save_compressed_image(matrix_list, filename):
    """(list, str)-> Nonetype

    >>> save_compressed_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    >>> image = [["0x5", "200x2"], ["111x7"]]
    >>> save_compressed_image(image, "test.pgm")
    >>> image2 = load_compressed_image("test.pgm")
    >>> image == image2
    True
    """
    
    fobj = open(filename, "w")
    fobj.write("P2C\n")
    if not is_valid_compressed_image(matrix_list):
        raise AssertionError("The matrix is not a valid comrpressed PGM image")
    #width = len(matrix_list[0])
    width = 0
    specific_line = matrix_list[0]
    for element in specific_line:
        mylist = str(element).split("x")
        width += int(mylist[1])
    height = len(matrix_list)
    fobj.write(str(width) + " " + str(height)+"\n")
    max_white_value = 255
    fobj.write(str(max_white_value)+"\n")
    newline = ""
    for row in range(height):
        for i in range(len(matrix_list[row])):
            newline += matrix_list[row][i]
            if i != len(matrix_list[row])-1:
                newline += " "
        #for element in matrix_list[row]: # use index
         #   newline += str(element) 
          #  if element != (matrix_list[row][-1]):
           #     newline = newline + " "
        newline += "\n"
    fobj.write(newline)
    fobj.close()


#save_compressed_image([["0x5", "200x2"], ["111x7"]],'test_c.pgm')


def save_image(matrix_list, filename):
    """(list, str)->Nonetype
    >>> save_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    """
    for row in range(len(matrix_list)):
        for element in matrix_list[row]:
            if type(element) == str:
                save_compressed_image(matrix_list, filename)
            elif type(element) == int:
                save_regular_image(matrix_list, filename)
            else:
                raise AssertionError("The content of the file is not PGM")

def invert(matrix_list):
    """(list)-> list
    Returns the invered matrix image of the input matrix
    >>> image = [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    >>> invert(image)
    [[255, 155, 105], [55, 55, 55], [0, 0, 0]]
    >>> image == [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    True
    """
    new_matrix = []
    if not is_valid_image(matrix_list):
        raise AssertionError("Invalid PGM matrix")
    for row in range(len(matrix_list)):
        new_line = []
        for element in matrix_list[row]:
            element -= 255
            if element < 0:
                element = -element
            new_line.append(element)
        new_matrix.append(new_line)
    return new_matrix

def flip_horizontal(matrix_list):
    """(list)-> list
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]
    """
    new_matrix = []
    if not is_valid_image(matrix_list):
        raise AssertionError("Invalid PGM matrix")
    for row in range(len(matrix_list)):
        new_row = []
        i = 1
        while i < len(matrix_list[row])+1:
            new_row.append(matrix_list[row][-i])
            i += 1
        new_matrix.append(new_row)
    return new_matrix

def flip_vertical(matrix_list):
    """"(list)-> list

    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 3, 4, 5]]
    """
    if not is_valid_image(matrix_list):
        print("Bad matrix")
        #call a validity function that detects the error
    new_matrix = []
    for row in range(len(matrix_list)):
        new_matrix.append(matrix_list[-row-1])
    return new_matrix



def crop(matrix_list, j, i, height, width):
    """(list, int, int, int, int)-> list
    Crops the matrix according to the dimension and starting i, j position
    >>> crop([[5, 5, 5], [5, 6, 6], [6, 6, 7]], 1, 1, 2, 2)
    [[6, 6], [6, 7]]
    
    >>> crop([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]], 1, 2, 2, 1)
    [[6], [10]]
        
    
    """
    if not is_valid_image(matrix_list):
        print("Bad matrix")
        #call a validity function that detects the error
    new_matrix = []
    for row in range(height):
        new_row = []
        for element in range(width):
            new_row.append(matrix_list[j+row][i+element])
        new_matrix.append(new_row)
    return (new_matrix)


def find_end_of_repetition(my_list,index, target):
    """"(list, int, int)-> int 
    Returns the last consecutive recurrence of target starting from index
    >>> find_end_of_repetition([5, 3, 5, 5, 5, -1, 0], 2, 5)
    4
    >>> find_end_of_repetition([1, 2, 3, 4, 5, 6, 7], 6, 7)
    6
    """
    while index < len(my_list) and my_list[index] == target:
        index +=1
    return index-1


def compress(matrix_list):
    """(list)->list
    Converts non-compressed matrix to compressed image matrix
    >>> compress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    [['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]

    """

    compressed_list = []
    for row in range(len(matrix_list)):
        index = 0
        line = []
        while index < len(matrix_list[row]):
            ending_index = find_end_of_repetition(matrix_list[row], index, matrix_list[row][index])
            line.append(str(matrix_list[row][index])+ "x" + str(ending_index - index + 1)) 
            
            index = ending_index+1

        compressed_list.append(line)
    #print(compressed_list)
    return(compressed_list)

def decompress(compressed_list):
    """(list)-> list
    Coverts a compressed list to a matrix list
    >>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    >>> image = [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    >>> compressed_image = compress(image)
    >>> image2 = decompress(compressed_image)
    >>> image == image2
    True
    """
    matrix_list = []
    for row in range(len(compressed_list)):
        line = []
        for element in compressed_list[row]:
            pixel = element.split('x')
            for repeat in range(int(pixel[1])):
                line.append(int(pixel[0]))
        matrix_list.append(line)
    #print(matrix_list) 
    return matrix_list

def process_command(cmd_str):
    """
    
    >>> process_command("LOAD<comp.pgm> CP DC INV INV SAVE<comp2.pgm>")
    >>> image = load_image("comp.pgm")
    >>> image2 = load_image("comp2.pgm")
    >>> image == image2
    """
    cmd = cmd_str.split(" ")
    for element in cmd:
        if 'LOAD' in element:
            mylist = element.split("<")
            filename = mylist[1][:-1]
            #filename = element[element.find("<")+1:element.find(">")]
            matrix_list =load_image(filename)

        elif 'SAVE' in element:
            mylist = element.split("<")
            filename = mylist[1][:-1]
            save_image(matrix_list, filename)
            
        elif 'INV' in element:
            matrix_list = invert(matrix_list)
        elif 'FH' in element:
            matrix_list = flip_horizontal(matrix_list)
        elif 'FV' in element:
            matrix_list = flip_vertical(matrix_list)
        elif 'CR' in element:
            element.split("<")
            parameter_list = mylist[1][:-1]
            parameter_list = parameter_list.split(",")
            a, b, c, d = parameter_list[0:4]
            matrix_list = crop(matrix_list, int(a),int(b),int(c),int(d))
        elif 'CP' in element:
            matrix_list = compress(matrix_list)
        elif 'DC' in element:
            matrix_list = decompress(matrix_list)
        else:
            raise AssertionError("Invalid comand")
    return

#save_compressed_image(compress(load_image('comp.pgm')), 'comp.pgm.compressed')
#print(compress(load_image('comp.pgm')), 'comp.pgm.compressed')

#process_command("LOAD<comp.pgm> CP SAVE<comp.pgm.compressed>")
#print(save_compressed_image(compress(load_image('comp.pgm')), 'comp.pgm.compressed'))
#print(load_compressed_image("comp.pgm.compressed"))




"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()

"""