# Name: Steve Chen
# ID: 261106847
from math import pi, sqrt
PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED = 4.0
PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED = 3.0
SPECIAL_INGREDIENT = "guacamole"
SPECIAL_INGREDIENT_COST = 19.99
FAIR = True


def get_pizza_area(diameter):
    """ (float) -> float
    Returns the area of pizza with given float diameter as a float
    >>> get get_pizza_area(1)
    0.7853981633974483
    >>> get get_pizza_area(2)
    3.141592653589793
    >>> get get_pizza_area(4)
    12.566370614359172
    """
    area = pi*((float(diameter)/2)**2)
    return area 


def get_diameter_of_pizza(area):
    diameter = (sqrt(area/pi))*2
    return diameter


def get_fair_quantity(diameter1, diameter2):
    """ (floats, floats)-> int
    Take two values of diameter and return the minimum integer number of small pizza with equal or more area than the big pizza
    >>> get_fair_quantity(2,2)
    1
    >>> get_fair_quantity(8,3)
    8
    >>> get_fair_quantity(6,9)
    3
    """ 
    true_amount = get_pizza_area(diameter2) / get_pizza_area(diameter1)
    if diameter1 < diameter2:
        if diameter2 % diameter1 != 0:
            quantity = int(true_amount)+1 
        else:
            quantity = int(true_amount)
        if FAIR == False:
            return int(true_amount*1.5)
        else:
            return quantity
    else:
        true_amount = 1/true_amount
        if diameter1 % diameter2 != 0:
            quantity = int(true_amount)+1 
        else:
            quantity = int(true_amount)
        if FAIR == False:
            return int(true_amount*1.5)
        else:
            return quantity


def pizza_formula(d_large, d_small, c_large, c_small, n_small): 
    '''(Float,Float,Float,Float,int) -> float
    Take 4 known values and one missing value to return the missing value as a float rounded to 2 decimals
    >>> pizza_formula(1,1,1,1,-1)
    1
    >>> pizza_formula(-1,2,3,4,5)
    3.87
    >>> pizza_formula(5,4,-1,3,2)
    2.34
    '''
    product = float((get_pizza_area(d_large)/c_large)*c_small/(get_pizza_area(d_small)*n_small))
    if d_large == -1:
        missing = sqrt(1/product)
        #missing = (get_pizza_area(d_small)*n_small/c_small)*c_large
        return round(missing, 2)
    if d_small == -1:
        missing = sqrt(product/1)
        #missing = (get_pizza_area(d_large)/c_large)*(c_small*n_small)
        return round(missing, 2)
    if c_large == -1:
        missing = product/-1
        #missing = get_pizza_area(d_large)/(get_pizza_area(d_small)/c_small)
        return round(missing, 2)
    if c_small == -1:
        missing = -1/product
        #missing = (get_pizza_area(d_small)*n_small)/(get_pizza_area(d_large)/c_large)
        return round(missing, 2)
    if n_small == -1:
        missing = product/-1
        #missing = (get_pizza_area(d_large)/c_large)/(get_pizza_area(d_small)/c_small)
        return round(missing, 2)


def get_pizza_cake_cost(base_diameter, height_per_level):
    """(int, float)->float
    Take the bases diameter and the height to compute the total cost of the pizza rounded to 2 decimals
    >>> get_pizza_cake_cost(1,2)
    6.28
    >>> get_pizza_cake_cost(2,4)
    62.83
    >>> get_pizza_cake_cost(2,2)
    31.42
    """
    diameter = int(base_diameter)
    total_cost = 0
    while diameter <= base_diameter and diameter >= 1:
        slice_cost = get_pizza_area(diameter)*height_per_level*PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED
        total_cost = total_cost+slice_cost
        diameter -= 1
    if FAIR == True:
        return round(total_cost, 2)
    if FAIR == False:
        return round(total_cost*1.5, 2)


def get_pizza_poutine_cost(diameter, height):
    """(int, float)->float
    Take the diameter and the height to compute the cost of the poutine rounded to 2 decimals
    >>> get_pizza_poutine_cost(10,1)
    235.62
    >>> get_pizza_poutine_cost(1,1)
    23.6
    >>> get_pizza_poutine_cost(6,9)
    763.41
    """
    cost = get_pizza_area(diameter)*height*PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED
    if FAIR == True:
        return round(cost, 2)
    if FAIR == False:
        return round(cost*1.5, 2)


def display_welcome_menu():
    """ no input -> no return
    Displays the menu
    >>> display_welcome_menu()
    Welcome to the best pizza shop ever! Our pizza are not made of 100% real pizza. 
    Please choose an option:
    A. Special orders 
    B. Formula Mode 
    C. Quantity mode"
    """
    print("Welcome to the best pizza shop ever! Our pizza are not made of 100% real pizza.")
    print("Please choose an option:\nA. Special orders \nB. Formula Mode \nC. Quantity mode" )


def special_orders(): 
    '''no input-> returns nothing
    Asks the user to choose between cake and poutine, the height and the diameter of the pizza. 
    Asks if the users wants the sepcial ingredient by confirming using y, and prints the final cost.
    >>> special_orders()
    Would you like the cake or the poutine? cake
    Enter diameter: 6
    Enter height: 9
    Do you want guacamole? y
    The cost is $2592.95
    To be continued
    '''
    if input("Would you like the cake or the poutine? ") == "cake":
        total_cost = get_pizza_cake_cost(int(input("Enter diameter: ")), int(input("Enter height: ")))
        a = input("Do you want "+ SPECIAL_INGREDIENT +"? ")
        if a == "y" or a == "yes":
            price = total_cost+SPECIAL_INGREDIENT_COST
        else:
            price = total_cost
    else:
        cost = get_pizza_poutine_cost(int(input("Enter diameter")), int(input("Enter height")))
        a = input("Do you want "+SPECIAL_INGREDIENT +"? ")
        if a == "y" or a == "yes":
            price = cost+SPECIAL_INGREDIENT_COST
        else:
            price = cost
    print("The cost is $" + str(round(price,2)))


def quantity_mode():
    """no input-> no return
    User inputs two diameter and the function prints the minimum amount of small pizza 
    to buy to have at least the same area as the larger pizza
    >>> quantity_mode()
    Enter diameter 1: 
    >>> 6
    Enter diamter 2: 
    >>> 9
    You should buy 3 pizzas.
    """
    x=int(input("Enter diameter 1: "))
    y=int(input("Enter diameter 2: "))
    quantity = get_fair_quantity(x, y)
    print("You should buy " + str(quantity) + " pizzas.")


def formula_mode():
    """no input->no return value
    User enters 4 pizza values and one missing as -1 
    and the function prints actual the missing value
    >>> formula_mode()
    Enter large diameter: -1
    Enter small diameter: 2
    Enter large price: 3
    Enter small price: 4
    Enter small number: 5
    The missing value is 3.87
    """
    x = float(input("Enter large diameter: "))
    y = float(input("Enter small diameter: "))
    z = float(input("Enter large price: "))
    a = float(input("Enter small price: "))
    b = float(input("Enter small number: "))
    missing = pizza_formula(x,y,z,a,b)
    print("The missing value is "+ str(missing))



def run_pizza_calculator():
    """ no input-> no returns value
    Calls different function depending on the user's input. 
    If the input is not matched, the function prints Invalid mode.
    """
    display_welcome_menu()
    choice = input("Your choice: ")
    if choice == "A" :
        special_orders()

    elif choice == "B":
        formula_mode()
    
    elif choice == "C":
        quantity_mode()
    
    else:
        print("Invalid mode.")

