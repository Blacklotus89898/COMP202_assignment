#Name: Steve Chen
#ID: 261106847

ROOM_NAME = "IDK"
AUTHOR = "NoneType"
PUBLIC = False

def introduction_message():
    """(void)->NoneType
    Prints introduction
    >>> introduction_message()
    Welcome to the game.
    The objects you can use are: Apple, Banana, Carrot
    """
    print("Welcome to the game. \n The objects you can use are: Apple, Banana, Carrot ")

def prompt_user():
    """(void)->NoneType
    Prints the user's prompt
    >>> prompt_user() 
    Just pick an object!!! 
    To consume the apple, type: bite. To peel the banana, type: pull. To cut the carrot enter: chop
    """
    print("Just pick an object!!! \nTo consume the apple, type: bite. To peel the banana, type: pull. To cut the carrot enter: chop")
    
def list_commands():
    """(void)->NoneType
    Prints the commands
    >>> list_commands()
    >List of commands: 
    bite apple 
    pull banana
    chop carrot
    """
    print(">List of commands: \nbite apple \npull banana\nchop carrot")

def get_user_input():
    """(void)->int
    For every user's input, prints a message and returns the point value
    >>> get_user_input()
    >>> apple
    Apple is for dessert. It won't help you escape.
    >>> get_user_input()
    >>> banana
    The banana is consumed before the apple. +1 Power
    >>> get_user_input()
    >>> carrot
    Veggie is first, congrats. U gained 2 power!
    """
    act = str(input("Type your command: "))
    act = act.lower()
    print(act)

    if "apple" in act:
        print("Apple is for dessert. It won't help you escape.")
        return 0
    elif "banana" in act:
        print("The banana is consumed before the apple. +1 Point")
        return 1
    elif "carrot" in act:
        print("Veggie is first, congrats. U gained 2 points!")
        return 2
    elif "commands" in act or "list" in act:
        print("Don't forget the commands!")
        list_commands()
        return 0
    else:
        print("Alert, this is a wrong command input!!!")
        print("Type a valid command.")
        return 0
    

def escape():
    """(void)->int
    loops and calls get_user_input() until the user has enough points to escape,
    returns the number of point

    >>> escape()
    get_user_input()
    >>> banana
    The banana is consumed before the apple. +1 Power
        get_user_input()
    >>> banana
    The banana is consumed before the apple. +1 Power    
    get_user_input()
    >>> banana
    The banana is consumed before the apple. +1 Power



    """
    point_count = 0
    while point_count < 3:
        point = get_user_input()
        if point != "exit()":
            point_count = point_count + point
        
        else: 
            return
    return point_count

def escape_room():
    """ (void)-> NoneType
    Function of the escape room, prints the escape message.
    >>> escape_room()
    >>> introduction_message()
    prompt_user()
    list_commands()
    escape()
    get_user_input()
    >>> banana
    The banana is consumed before the apple. +1 Power
    get_user_input()
    >>> banana
    The banana is consumed before the apple. +1 Power    
    get_user_input()
    >>> banana
    The banana is consumed before the apple. +1 Power
    Congrats! You escaped with 3 points.

    """
    introduction_message()
    prompt_user()
    list_commands()
    points = escape()
    print("Congrats! You escaped with " + str(points)+ " points.")
    return





