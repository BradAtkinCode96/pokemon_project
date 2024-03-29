my_list = ["eggs", "wine", "milk"]
MENU = ["Show the list",
"Add item",
"Remove item",
"Clear the list",
"Search"]


def pretty_print(lst):
    print("\n")
    for i in range(len(lst)):
        print(f"{i+1}. {lst[i]}")


def list_add(item:str):
    if item.isalpha():
        my_list.append(item)
    else:
        print("List items must be letters only")

def list_remove(index):
    if index > 0 and index <= len(my_list):
        removed = my_list.pop(index-1)
        print(f"{removed} was removed from the list")
    else:
        print("Error, the number is not in range")

def list_search(input:str):
    input = input.lower()
    result = []
    for item in my_list:
        if input in item:
            result.append(item)
    return result

print("Hello, welcome to the shopping list app")
choice = None

while choice != 0:
    try:
        pretty_print(MENU)
        choice = int(input("Please select an option, or press 0: "))
        if choice == 1:
            print("Here is the current list:")
            pretty_print(my_list)
        elif choice == 2:
            item = input("What would you like to add? ")
            list_add(item)
        elif choice == 3:
            if len(my_list) == 0:
                print("The list is empty")
                continue
            pretty_print(my_list)
            index = input("Enter the item number you would like to remove: ")
            try:
                index = int(index)
                list_remove(index)
            except ValueError:
                print("Error, enter an integer in range")
        elif choice == 4:
            my_list.clear()
        elif choice == 5:
            user_input = input("Please enter a search term: ")
            result = list_search(user_input)
            if len(result) > 0:
                print("Here are the matches:")
                pretty_print(result)
            else:
                print("Nothing matches")

    except ValueError:
        print(f"Error, '{choice}' is not a valid option")
