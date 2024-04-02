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
    user_input = input("Enter the type of the Pokémon: ")    
    filterlist = []
    for pokemon in mylist: 
        if pokemon["Type 1"].lower() == user_input.lower():
            filterlist.append(pokemon)

def speed_range():
    min_val = int(input("Enter the minimum speed: "))
    max_val = int(input("Enter the maximum speed: "))
    filtered_pokemon = []
    for pokemon in mylist: 
        if min_val <= int(pokemon["Speed"]) <= max_val:
            filtered_pokemon.append(pokemon)       
    pretty_print(filtered_pokemon.get("Speed"))

def weight_rangelb():
    min_val = int(input("Enter the minimum weight (lbs): "))
    max_val = int(input("Enter the maximum weight (lbs): "))
    filtered_pokemon = []
    for pokemon in mylist: 
        if min_val <= pokemon["Weight (lbs)"] <= max_val:
            filtered_pokemon.append(pokemon)       
    pretty_print(filtered_pokemon)

def weight_rangekg(min_val, max_val, unit):
    filtered_pokemon = []
    for pokemon in mylist: 
        if min_val <= pokemon[f"{unit}"] <= max_val:
            filtered_pokemon.append(pokemon)       
    pretty_print(filtered_pokemon)

def height_rangem():
    min_val = int(input("Enter the minimum height (m): "))
    max_val = int(input("Enter the maximum height (m): "))
    filtered_pokemon = []
    for pokemon in mylist: 
        if min_val <= pokemon["Height (m)"] <= max_val:
            filtered_pokemon.append(pokemon)       
    pretty_print(filtered_pokemon)

def height_rangeft():
    min_val = int(input("Enter the minimum height (ft): "))
    max_val = int(input("Enter the maximum height (ft): "))
    filtered_pokemon = []
    for pokemon in mylist: 
        if min_val <= pokemon["Height (ft)"] <= max_val: # pokemon(f"{}")
            filtered_pokemon.append(pokemon)       
    pretty_print(filtered_pokemon)

def HP_range():
    min_val = int(input("Enter the minimum height (ft): "))
    max_val = int(input("Enter the maximum height (ft): "))
    filtered_pokemon = []
    for pokemon in mylist: 
        if min_val <= pokemon["HP"] <= max_val:
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
        elif choice == 2: #ID SEARCH
            id_search()
        elif choice == 3: #Type 1 FILTER
            filter_by_type()
        elif choice == 4: #Type 2 Filter
            filter_by_type()
        elif choice == 5: #speed
            speed_range()
        elif choice == 6: #weight
            selection = input("What do you want to filter by?\n"
                            "1. Weight (lbs)"
                            "2. Weight (kg)"
                            "Your selection: ")
            selection = int(selection)
            if selection == 1:
                weight_rangelb()
            if selection == 2:
                weight_rangekg()
        elif choice == 7:
            HP_range()
        elif choice == 8:
            print("Exiting...")    
            break     
    except ValueError:
        print(f"Error, '{choice}' is not a valid option")
