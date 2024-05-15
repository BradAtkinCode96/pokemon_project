

"""recieves list filters by type and returns a list"""
def filter_by_type(lst, type_to_filter):            #run in loop                                                                                     
    newlist = []    
    for pokemon in lst:
        try:
            if pokemon["Type 1"].lower() == type_to_filter.lower() or pokemon["Type 2"].lower() == type_to_filter.lower():
                newlist.append(pokemon)
        except ValueError:
            print("valid selection please")
    return newlist

"""receives list of pokemon, atr, min, max and returns a list that is filtered by attributes selected"""
def rangefilter(lst, atrribute, min_val, max_val):
    pass



