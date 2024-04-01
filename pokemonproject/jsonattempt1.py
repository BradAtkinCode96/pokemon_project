import json

with open(r"C:\Users\Bradl\Documents\GitHub\PokemonProject\pokemonproject\shrtpokedex.json") as file:
    json_data = file.read()
    mylist = json.loads(json_data)

MENU = ["Search by Name",
        "Search by Id",
        "Filter by Type 1",
        "Filter By Type 2",
        "Filter by Speed Range",
        "Filter by Weight Range",
        "Filter by HP Range"]

def pretty_print(lst):
    print("\n")
    for i in range(len(lst)):
        print(f"{i+1}. {lst[i]}")

def printkeys():
    all_keys = []
    for pokemon in mylist:
        for key in pokemon.keys():
            if key not in all_keys:
                all_keys.append(key)
    pretty_print(all_keys)

def valid_types():
    values = []
    for pokemon in mylist:
        values.append(pokemon["Type 1"]) and values.append(pokemon["Type 2"])
    pretty_print(values)

def filter_by_type(type_to_filter):
    filtered_pokemon = []
    print("valid types: " )
    for pokemon in mylist:
        try:
            if pokemon["Type 1"].lower() == type_to_filter.lower() or pokemon["Type 2"].lower() == type_to_filter.lower():
                filtered_pokemon.append(pokemon)
        except ValueError:
            print("valid selection please")


    pretty_print(filtered_pokemon)

def name_search(): 
    user_input = input("Enter the name of the Pokémon: ") 
    for pokemon in mylist: 
        if pokemon["Name"].lower() == user_input.lower():
            print(pokemon)

def id_search(): 
    user_input = input("Enter the name of the Pokémon: ")
    id_out = [] 
    for pokemon in mylist: 
        if pokemon["Id"].lower() == user_input.lower():
            id_out.append(pokemon)

def filter_type(): #i have the filter for the list but don't know how to not hardcode the choice of the category to filter by
    #input
    user_input = input("Enter the type of the Pokémon: ")\
    
    filterlist = []
    for pokemon in mylist: 
        if pokemon["Type 1"].lower() == user_input.lower():
            filterlist.append(pokemon)
def speed_range():
    min_val = int(input("Enter the minimum value of the speed: "))
    max_val = int(input("Enter the maximum value of the speed: "))
    filtered_pokemon = []
    for pokemon in mylist: 
        if min_val <= pokemon[""] <= max_val:
            filtered_pokemon.append(pokemon)       
    pretty_print(filtered_pokemon)

def weight_range():
    min_val = int(input("Enter the minimum value of the weight: "))
    max_val = int(input("Enter the maximum value of the weight: "))
    filtered_pokemon = []
    for pokemon in mylist: 
        if min_val <= pokemon[""] <= max_val:
            filtered_pokemon.append(pokemon)       
    pretty_print(filtered_pokemon)

print("Welcome to the pokedex")
choice = None

while choice != 0:
    try:
        pretty_print(MENU)
        choice = int(input("Please make a selection: "))
        if choice == 1: #NAME SEARCH
            result = name_search()
        if choice == 2: #ID SEARCH
            id_search()
        if choice == 3: #FILTER
            filter_opt = input("What do type you want to filter by?")
        if choice == 4 #weight range
            
            
    except ValueError:
        print(f"Error, '{choice}' is not a valid option")
