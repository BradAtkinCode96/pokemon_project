
import json

with open(r"C:\Users\Bradl\Documents\GitHub\PokemonProject\pokemonproject\shrtpokedex.json") as file:
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
        "Filter by HP Range"]

SUBMENU = ["Would you like to filter further?",
           "Filter by Type",
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

def filter_by_type(type_to_filter):
    filtered_pokemon = []
    for pokemon in mylist:
        try:
            if pokemon["Type 1"].lower() == type_to_filter.lower() or pokemon["Type 2"].lower() == type_to_filter.lower():
                filtered_pokemon.append(pokemon["Name"])
        except ValueError:
            print("valid selection please")
    pprint(filtered_pokemon)

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

def layerFilter(extralist): #plug in the returned list from previous filter
    print("Do you want to filter further?")
    option = input(f"{pretty_print(SUBMENU)}")
    if option != 0:
        if option == 1:
            type_to_filter = input("Enter the type to search:")
            dlayerfilter = []
            layerfilter = []
    for pokemon in extralist:
        try:
            if pokemon["Type 1"].lower() == type_to_filter.lower() or pokemon["Type 2"].lower() == type_to_filter.lower():
                layerFilter.append(pokemon["Name"])
                dlayerfilter.append(pokemon)
        except ValueError:
            print("valid selection please")
    pprint(layerfilter)

print("Welcome to the pokedex")
choice = None

while choice != 0:
    try:
        pretty_print(MENU)
        choice = int(input("Please make a selection: "))
        if choice == 1: #NAME SEARCH
            result = name_search()
        elif choice == 2: #ID SEARCH
            id_search()
        elif choice == 3: #TypE Filter
            user_input = input("What type do you want to filter by?: ")
            filter_by_type(user_input)
        elif choice == 4: #speed
            filter_range("speed", "Speed")
        elif choice == 5: #weight
            selection = input("Search by:\n"
                            "1. Kilograms\n"
                            "2. Pounds\n"
                            "Your choice: ")
            try: 
                selection = int(selection)
                if selection == 1:
                    filter_range("Weight", "Weight (kg)")
                if selection == 2:
                    filter_range("Weight", "Weight (lbs)")
            except ValueError:
                print("You must select a number")
        elif choice == 6: #height
                    filter_range("Height", "Height (m)")
        elif choice == 7: #HP
            filter_range("HP", "HP")
        elif choice == 8:
            print("Exiting...")    
            break     
    except ValueError:
        print(f"Error, '{choice}' is not a valid option")
