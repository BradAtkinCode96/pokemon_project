import json
with open(r"C:\Users\brada\OneDrive\Documents\GitHub\pokemon_project\dataset.json") as file:
    mylist = json.load(file)

import pprint

MENU = ["Search by Name",
        "Search by ID",
        "Filter by Height, Weight and Speed",
        "Select Pokemon for your team",
        "View your team",
        "Clear the Team",
        "Show all move in Pokedex(Across all pokemon)"
        ]
# """
# For pretty printing the menu with number options
# """
def pretty_print(lst):
    print("\n")
    for i in range(len(lst)):
        print(f"{i+1}. {lst[i]}")
# """
# Searches for exact match poke with ID
# """ 
def id_search():
    try:
        user_input = input("Enter the ID of the Pokémon: ")
        for pokemon in mylist:
            if pokemon["Id"] == user_input:
                print("Here is the match:")
                print(pokemon)
                return pokemon
        print("No Pokémon found with that ID.")
    except ValueError:
        print("Please enter a valid ID.")
# """
# Searches for partial match of search query, 
#  if only one pokemon is a match for the query, the pokemon will be printed and returned (for use in the move_display()).
# if more, a list of pokemon name will printed and the number of matches.
def name_search(user_input):
    while True:
        try:
            matches = []
            for pokemon in mylist:
                if user_input.lower() in (pokemon["Name"].lower()):
                    matches.append(pokemon)
            if matches:
                if len(matches) == 1:
                    pprint.pp(matches)
                    print("There is only 1 pokemon that matches your search: ^Details above^")
                    print(matches[0]["Name"])
                    return matches
                elif 0 <= len(matches) <= 5:
                    print("Here are the matches:")
                    pprint.pp(matches)
                    print(f"There are {len(matches)} pokemon that match your search:")
                    print(matches[0]["Name"])
                    break  #escape loop and go back to main menu (not adding multiple pokemon, yet.)
                elif 5 <= len(matches):
                    print("Here are the matches:")
                    pprint.pp(matches)
                    print(f"There are {len(matches)} pokemon that match your search:")
                    print(matches[0]["Name"])
                    print(f"There are {len(matches)} pokemon that match your search:")
                    break
            else:
                print("No Pokémon found with that name.")
        except Exception as e:
            print(f"An error occurred: {e}")
# """
# Takes input for a type of pokemon and returns a pokemon matching the type
# """
def filter_by_type(mylist, type_to_filter):
    result = []
    for pokemon in mylist:
        try:
            if pokemon["Type 1"].lower() == type_to_filter.lower() or pokemon["Type 2"].lower() == type_to_filter.lower():
                result.append(pokemon)
        except ValueError:
            print("valid selection please")
    print(result)
    return result
"""
Retrieves the min max values for all the search criteria for filter_by_range()
"""
def get_min_max():
    try:
        hmin = float(input("Enter minimum Height: "))
        hmax = float(input("Enter maximum Height: "))
        wmin = float(input("Enter minimum Weight: "))
        wmax = float(input("Enter maximum Weight: "))
        smin = float(input("Enter minimum Speed: "))
        smax = float(input("Enter maximum Speed: "))

    except ValueError:
        print("MUst be a valid number")    
    return hmin, hmax, wmin, wmax, smin, smax 
'''
Finds the pokemon that match the min and max values retrived by input through get_min_max()
'''
def filter_by_range(mylist, hmin, hmax, wmin, wmax, smin, smax):
    result = []
    for pokemon in mylist: 
        height = float(pokemon.get("Height (m)", 0))
        weight = float(pokemon.get("Weight (kg)", 0))
        speed = float(pokemon.get("Speed", 0))
        # print(speed, height, weight)
        if (smin <= speed <= smax and hmin <= height <= hmax and wmin <= weight <= wmax): 
            result.append(pokemon)
    pprint.pp(result)
    for i in result:
        print(i["Name"])
        print()
    return result
"""
***Needs refactoring and error catching***
currently: plugs in a list containing all info about ONE poekmon (retrieved when only 1 match in )
            function then extracts and prints those moves for selection by user input
            store the input in a list and makes a new list according to the moves selected
            appends those moves to the pokemon and reutrn the pokemon with 4 active movees
"""
def move_display(alist): #plug in the list from previous function to allow move selection(one pokemon)
    fullmoves = [] #fullmoves[0] is the name. Fullmoves[1]is the dictionary key with value["Description"]etc
    counter = 1
    name = alist[0]["Name"]
    print(f"Here are {name}'s moves: ") # find a way to concatenate pokemon name
    for pokemon in alist:
        moves_dict = pokemon["Moves"] #access the moves key(which is has a dictionary value)
        for i in moves_dict.items():
            move_name = i[0] 
            move_description = i[1]["Description"] 
            fullmoves.append(i) # 
            print(f"{counter}.{move_name}: {move_description}")
            counter += 1
    select = input("Which moves would you like? (4 numbers space-separated): ").split()
    intselect = list(map(int, select))
    active_moves = []
    active_move_pokemon = {}
    for i in intselect:
        active_moves.append(fullmoves[i-1]) #adds the moves to active move list in 
    for move_name, _ in active_moves:
        print(move_name)
    name = alist[0]["Name"]
    active_move_pokemon[name] = active_moves
    pprint.pp(active_move_pokemon)
    print(f"{name} was added with the moves you selected")
    return active_move_pokemon


"""
Takes input of ONE pokemon's information and asks if that pokemon shoud be added
if not, returns to main menu
"""
def add_to_team(match:list):
    while True:
        if len(match) == 1:
            name = match[0]["Name"]
            x = input(f"Would you like to add {name} to your team? y/n: ").lower()
            try:
                if x == "y":
                    return match
                elif x == "n":
                    print(f"{name} was not added to your team")
                    return False
                elif x != "y" or x != "n":
                    print("You did not make a valid selection")
                    continue
            except Exception as e:
                print(f"An error occurred: {e}")
        else: 
            print("More than one pokemon matches that search!")
"""
Writes a list to a json. The json contians the team.
"""
def json_write(lst):
    with open(r'C:\Users\brada\OneDrive\Documents\GitHub\pokemon_project\team.json', 'r') as json_file:
        try:    
            x = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            x = []
        x.append(lst)
        with open(r'C:\Users\brada\OneDrive\Documents\GitHub\pokemon_project\team.json', 'w') as json_file:
            json.dump(x, json_file)


"""
View the team contained in the json. 
"""
def team_view():
    with open(r'C:\Users\brada\OneDrive\Documents\GitHub\pokemon_project\team.json', 'r') as json_file:
        try:
            y = json.load(json_file)
            pprint.pp(y)
        except Exception:
            print("Your team is empty!")
"""
Empties the team contained in the json file
"""
def team_clear():
    with open(r'C:\Users\brada\OneDrive\Documents\GitHub\pokemon_project\team.json', 'w') as json_file:
        print("Your team is now empty")

"""
Main menu
"""
print("Welcome to the Pokédex")
while True:
    try:
        pretty_print(MENU)
        choice = int(input("Please make a selection (0 to quit): "))
        if choice == 1:
            user_input = input("Enter the name of the Pokémon: ")
            name_search(user_input)
        elif choice == 2:
            id_search()
        elif choice == 3:
            hmin, hmax, wmin, wmax, smin, smax = get_min_max()
            filter_by_range(mylist, hmin, hmax, wmin, wmax, smin, smax)
        elif choice == 4:
            pokename = input("Which pokemon would you like to add to your team?: ")
            matchlist = name_search(pokename)
            want_to_add = add_to_team(matchlist)
            if want_to_add == False:
                continue
            else:        
                activemoves = move_display(want_to_add)
                json_write(activemoves)
        elif choice == 5:
            team_view()
        elif choice == 6:
            team_clear()
        elif choice == 7:
            move_display(mylist) 
        elif choice == 0:
            print("Goodbye!")            
            break
        else:
            print("Invalid choice. Please choose a number between 0 and 7. 0 to quit")
    except ValueError:
        print("Invalid choice. Please enter a number.")