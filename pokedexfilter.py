import json

with open(r"C:\Users\Bradl\Documents\GitHub\PokemonProject\pokemonproject\pokedex1.json") as file:
    json_data = file.read()
    mylist = json.loads(json_data)

import pprint #-> this does work!
pp = pprint.PrettyPrinter(indent=0) 

MENU = ["Search by Name",
        "Search by Id",
        "Filter by Type",
        "Filter by Speed Range",
        "Filter by Weight Range",
        "Filter by Height (m) Range",
        "Filter by HP Range",
        "Add Pokemon to my team: ",
        "View my teams"
        ]

SUBMENU = ["Filter by Type",
           "Filter by Speed Range",
           "Filter by Weight Range",
           "Filter by Height Range",
           "Filter by HP Range",
           "Your choice"
           ]

def pretty_print(lst):
    print("\n")
    for i in range(len(lst)):
        print(f"{i+1}. {lst[i]}")

def id_search(): 
    user_input = input("Enter the id of the Pokémon: ")
    id_out = [] 
    for pokemon in mylist: 
        if pokemon["Id"] == user_input:
            id_out.append(pokemon)
    pprint(id_out)

def filter_by_type(mylist, type_to_filter):
    filtered_pokemon = []
    namelist = []
    for pokemon in mylist:
        try:
            if pokemon["Type 1"].lower() == type_to_filter.lower() or pokemon["Type 2"].lower() == type_to_filter.lower():
                namelist.append(pokemon["Name"])
                filtered_pokemon.append(pokemon)
        except ValueError:
            print("valid selection please")
    pretty_print(namelist)
    return filtered_pokemon
def name_search(): 
    user_input = input("Enter the name of the Pokémon: ") 
    matches = []
    for pokemon in mylist: 
        if user_input.lower() in pokemon["Name"].lower():
            matches.append(pokemon)
    pprint.pp(matches)

def filter_range(attribute_name, unit): # reutrns filterd lst of d. when calling, atribute and unit should be in quptes as they are string    
    min_val = input(f"Enter the minimum {attribute_name}: ") #f and curly brackets lets me print the interchagable variable
    max_val = input(f"Enter the maximum {attribute_name}: ")
    try:
        namelist = []
        filtered_pokemon = []
        min_val = float(min_val)
        max_val = float(max_val)
        for pokemon in mylist: 
            if min_val <= float(pokemon[f"{unit}"]) <= max_val: #there is a speical case here for feet because the feet and inches cannot be converted to a float
                namelist.append(pokemon["Name"]) #list of names (just for printing and ease of reading)
                filtered_pokemon.append(pokemon) #list of all filtered pokemons dictionaries
        pretty_print(namelist)
        return filtered_pokemon
    except ValueError:
        print("Must be an integer")

def move_display(filtered_list): #plug in the list from previous function to allow move selection
    movelist = []
    for pokemon in filtered_list:
        movelist.append(pokemon["Name"]["Moves"])
    pprint(movelist)

def layerFilter(extralist): #plug in the returned list from previous filter. FILTERING A NEWLY RETURNED LIST 
    option = input(f"{pretty_print(SUBMENU)}")
    print("0 to stop filter")
    try: 
        option = int(option)
        while option != 0: #this if is so the filtering keeps prompting until one pokemon left 
            try:
                option = int(option)
                if option != 0:
                    if option == 1: #filtering TYPE
                        type_to_filter = input("Enter the type to search:")
                        namelist = []
                        filtered_pokemon = []
                        for pokemon in extralist:
                            try:
                                if pokemon["Type 1"].lower() == type_to_filter.lower() or pokemon["Type 2"].lower() == type_to_filter.lower():
                                    namelist.append(pokemon["Name"])
                                    filtered_pokemon.append(pokemon)
                            except ValueError:
                                print("valid selection please")
                        pretty_print(namelist)
                        layerFilter(filtered_pokemon) #restart the process with the smaller list
                    elif option == 2:
                            min_val = input("Min value: ")
                            max_val = input("Max value: ")
                            try:
                                namelist = []
                                filtered_pokemon = []
                                min_val = float(min_val)
                                max_val = float(max_val)
                                for pokemon in extralist: 
                                    if min_val <= float(pokemon["Speed"]) <= max_val: #narrowing the list by the filter criteria
                                        namelist.append(pokemon["Name"]) #adding names to the name list (Printing only)
                                        filtered_pokemon.append(pokemon) 
                                        pretty_print(namelist)
                                        layerFilter(filtered_pokemon)#this is new list that is condensed by the filter just complete
                            except ValueError:
                                print("invalid selection")
                    elif option == 3:
                        kglb = input("1 is lbs or\n2 kg?")
                        #error handling if it works later
                        if kglb == "1":
                            min_val = input("Min value: ")
                            max_val = input("Max value: ")
                            try:
                                namelist = []
                                filtered_pokemon = []
                                min_val = float(min_val)
                                max_val = float(max_val)
                                for pokemon in extralist: 
                                    if min_val <= float(pokemon["Weight (lbs)"]) <= max_val:
                                        namelist.append(pokemon["Name"]) 
                                        filtered_pokemon.append(pokemon) 
                                        pretty_print(namelist)
                                        layerFilter(filtered_pokemon)
                            except ValueError:
                                print("valid selection please")                                
                        elif kglb == "2":
                            min_val = input("Min value: ")
                            max_val = input("Max value: ")
                            try:
                                namelist = []
                                filtered_pokemon = []
                                min_val = float(min_val)
                                max_val = float(max_val)
                                for pokemon in extralist: 
                                    if min_val <= float(pokemon["Weight (kg)"]) <= max_val:
                                        namelist.append(pokemon["Name"]) 
                                        filtered_pokemon.append(pokemon) 
                                        pretty_print(namelist)
                                        layerFilter(filtered_pokemon) #for use in the next cycle with smaller.
                        
                            except ValueError:
                                print("valid selection please")
                    elif option == 4:
                        min_val = input("Min value: ")
                        max_val = input("Max value: ")
                        try:
                            namelist = []
                            filtered_pokemon = []
                            min_val = float(min_val)
                            max_val = float(max_val)
                            for pokemon in extralist: 
                                if min_val <= float(pokemon["Height (m)"]) <= max_val:
                                    namelist.append(pokemon["Name"]) 
                                    filtered_pokemon.append(pokemon) 
                                    pretty_print(namelist)
                                    layerFilter(filtered_pokemon) #for use in the next cycle with smaller.               
                        except ValueError:
                            print("valid selection please")
                    elif option == 5:
                        min_val = input("Min value: ")
                        max_val = input("Max value: ")
                        try:
                            namelist = []
                            filtered_pokemon = []
                            min_val = float(min_val)
                            max_val = float(max_val)
                            for pokemon in extralist: 
                                if min_val <= float(pokemon["HP"]) <= max_val:
                                    namelist.append(pokemon["Name"]) 
                                    filtered_pokemon.append(pokemon) 
                                    pretty_print(namelist)
                                    layerFilter(filtered_pokemon) #for use in the next cycle with smaller.               
                        except ValueError:
                            print("valid selection please") 
                    elif option == 6:
                        return choice == None
                    elif option == 0:
                        break
            except ValueError:
                print("not a valid selection")
        else:
            print("only 1 pokemon left")        
    except ValueError:
            print("not a valid selection")

def moveToAdd(pokemon_names, pokemon):
    moves_dict = {}
    for pokemon in mylist:
        if pokemon["Name"] in pokemon_names:
            moves_dict[pokemon["Name"]] = pokemon["Moves"]
            pprint(moves_dict)
    return moves_dict


    

print("Welcome to the pokedex")
choice = None

while choice == None:
    try:
        pretty_print(MENU)
        choice = int(input("Please make a selection: "))
        if choice == 1: #NAME SEARCH
            result = name_search()
        elif choice == 2: #ID SEARCH
            id_search()
        elif choice == 3: #TypE Filter
            user_input = input("What type do you want to filter by?: ")
            newlist = filter_by_type(mylist, user_input) #mylist for first type filter, then newlist for second layer because type becomes redunant after one filter
            yorn = input(f"Do you want to filter {user_input} further? y or n: ")
            if yorn == "y" or "Y":
                layerFilter(newlist)
            else:
                break
        elif choice == 4: #speed
            newlist = filter_range("speed", "Speed")
            yorn = input("Do you want to filter further? y or n: ")
            if yorn == "y" or "Y":
                layerFilter(newlist)
            else:
                break # break for now for whatever
        elif choice == 5: #weight
            selection = input("Search by:\n"
                            "1. Kilograms\n"
                            "2. Pounds\n"
                            "Your choice: ")
            try: 
                selection = int(selection)
                if selection == 1:
                    newlist = filter_range("Weight", "Weight (kg)") # i want to filter the list that this returns
                    yorn = input("Do you want to filter further? y or n: ")
                    if yorn == "y" or "Y":
                        layerFilter(newlist)
                    else:
                        break
                if selection == 2:
                    newlist = filter_range("Weight", "Weight (lbs)")
                    yorn = input("Do you want to filter further?: y or n")
                    if yorn == "y" or "Y":
                        layerFilter(newlist)
                    else:
                        break
            except ValueError:
                print("You must select a number")
        elif choice == 6: #height
                    newlist = filter_range("Height", "Height (m)")
                    yorn = input("Do you want to filter further?: y or n")
                    if yorn == "y" or "Y":
                        layerFilter(newlist)
                    else:
                        break
        elif choice == 7: #HP
            newlist = filter_range("HP", "HP")
            yorn = input("Do you want to filter further?: y or n")
            if yorn == "y" or "Y":
                layerFilter(newlist)
            else:
                break
        elif choice == 8:
            pass            
        elif choice == 9:
            print("Exiting...")    
            break     
    except ValueError:
        print(f"Error, '{choice}' is not a valid option")
