#Get numbers in dial no paramerters. Propts user for thr numbrt of dials for lock combination. Needs to have at least 3 dials.
import random 

def get_number_of_dials():
    global dials
    dials = input("Each lock has how many dials? ")
    if float(dials) < 3:
        print("The Number of Dials needs to be 3 or greater.")
get_number_of_dials()

def get_how_many_to_list():
    global combos
    combos = input("How many combinations should I generate? ")
    float(combos)
get_how_many_to_list()


def get_number():
    i = float(dials)
    while i < 0 != float(combos):
        for x in random.randrange (0, dials):
            if x == combos: break
            print (x)
            
get_number()

def next_combo_number():
    pass

