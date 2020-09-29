def main_menu():
    print("Welome Home, \nwhat do you wanna do today?")
    print("1. Cook some food")
    print("2. Add more recipes to your library")
    print("3. Show all the recipes in the library")
    selected = False
    while not selected:
        choice = input("")
        if not choice.isdigit():
            print("You can only enter numbers, ")
        elif int(choice) == 1:
            chef_menu()
            selected = True
        elif int(choice) == 2:
            recipe_collector()
            selected = True
        elif int(choice) == 3:
            all_menu()
            selected = True
        else:
            print("Oops, that don't seem to be an option. \npick between 1, 2 and 3")


def chef_menu():
    print("Chef Menu")


def recipe_collector():
    print("recipe Collector")


def all_menu():
    print("All the recipes")


def main():
    pass


if __name__ == '__main__':
    main()
