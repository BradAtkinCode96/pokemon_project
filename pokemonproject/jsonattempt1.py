import json

with open(r"C:\Users\Bradl\Documents\GitHub\PokemonProject\pokemonproject\shrtpokedex.json") as file:
    json_data = file.read()
    mylist = json.loads(json_data)

MENU = ["Search by Name",
        "Search by Id",
        "Filter by Type 1",
        "Filter by Type 2",
        "Filter by Speed Range",
        "Filter by Weight Range",
        "Filter by HP Range"]

FILTERMENU = ["Filter by Type 1",
              "Filter by Type 2",
              "Filter by Speed Range",
              "Filter by Weight Range",
              "Filter by HP Range",
            ]

TYPEMENU = ["Filter by Type 1",
            "Filter By Type 2",
            ]

HEIGHTMENU = ["Filter by meters",
              "Filter by feet",
              ]

WEIGHTMENU = ["Filter by kg",
              "Filter by pounds",
              ]

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

def printKeysLeft():
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
    user_input = input("Enter the id of the Pokémon: ")
    id_out = [] 
    for pokemon in mylist: 
        if pokemon["Id"] == user_input:
            id_out.append(pokemon)
    pretty_print(id_out)

def filter_type(): #i have the filter for the list but don't know how to not hardcode the choice of the category to filter by
    user_input = input("Enter the type of the Pokémon: ")    
    filterlist = []
    for pokemon in mylist: 
        if pokemon["Type 1"].lower() == user_input.lower():
            filterlist.append(pokemon)

def speed_range():
    try:
        min_val = int(input("Enter the minimum speed: "))
        max_val = int(input("Enter the maximum speed: "))
        filtered_pokemon = []
        for pokemon in mylist: 
            if min_val <= int(pokemon["Speed"]) <= max_val:
                filtered_pokemon.append(pokemon)       
        pretty_print(filtered_pokemon.get("Speed"))
    except ValueError:
        print("Is that a valid input?")


def weight_range(min_val, max_val, unit):
    filtered_pokemon = []
    for pokemon in mylist: 
        if min_val <= pokemon[f"{unit}"] <= max_val:
            filtered_pokemon.append(pokemon["Name"])       
    pretty_print(filtered_pokemon)

def height_range(min_val, max_val, unit):
    try:
        filtered_pokemon = []
        for pokemon in mylist: 
            if min_val <= pokemon[f"{unit}"] <= max_val:
                filtered_pokemon.append(pokemon["Name"])       
        pretty_print(filtered_pokemon)
    except ValueError:
        print("That is not valid input. Please try again")

def HP_range():
    try:
        min_val = int(input("Enter the minimum HP: "))
        max_val = int(input("Enter the maximum HP: "))
        filtered_pokemon = []
        for pokemon in mylist: 
            if min_val <= pokemon["HP"] <= max_val:
                filtered_pokemon.append(pokemon["Name"])       
        pretty_print(filtered_pokemon)
    except ValueError:
        print("Please input an interger: ")

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
            pretty_print(WEIGHTMENU)
            selection = input("Filter by Kg or lbs?: ")
            try:
                selection == int(selection)
                if selection == 1:
                    unit = "Weight (kg)"
                    min_val = input("MIN WEIGHT (kg): ")
                    max_val = input("MAX WEIGHT (kg): ")
                    weight_range(min_val, max_val, unit)
                if selection == 2:
                    unit = "Weight (lbs)"
                    min_val = input("MIN WEIGHT (lbs): ")
                    max_val = input("MAX WEIGHT (lbs): ")
                    weight_range(min_val, max_val, unit)
            except ValueError:
                print("Please make a valid selection")
        elif choice == 7:
            selection = input("Filter by meters or f?: ")
            try:
                selection == int(selection)
                if selection == 1:
                    unit = "Height (m)"
                    min_val = input("MIN HEIGHT (m): ")
                    max_val = input("MAX HEIGHT (m): ")
                    weight_range(min_val, max_val, unit)
                if selection == 2:
                    unit = "Height (ft)"
                    min_val = input("MIN HEIGHT (ft): ")
                    max_val = input("MAX HEIGHT (ft): ")
                    weight_range(min_val, max_val, unit)
            except ValueError:
                print("not a valid selection")
        elif choice == 8:
            print("Exiting...")    
            break     
    except ValueError:
        print(f"Error, '{choice}' is not a valid option")
