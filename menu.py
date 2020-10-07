import sqlfunctions as sql


def main_menu():
    print("Welome Home, \nwhat do you wanna do today?")
    print("1. Cook some food")
    print("2. Add more recipes to your library")
    print("3. Show all the recipes in the library")
    print("0. Exit")
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
        elif int(choice) == 0:
            selected = True
        else:
            print("Oops, that don't seem to be an option. \npick between 1, 2 and 3")
    return False


def chef_menu():
    print("What kind of food do you wish to cook?")
    categories = sql.get_category()

    i = 1
    for category in categories:
        print(f"{i}. {category}")
        i += 1
    print("0. Exit")

    selected = False
    while not selected:
        choice = input("")
        if not choice.isdigit():
            print("You can only enter numbers, ")
        elif 0 < int(choice) < len(categories)+1:
            choice.isdigit()
            sql.random_recipe(choice)
            main_menu()
            selected = True
        elif int(choice) == 0:
            choice.isdigit()
            main_menu()
            selected = True
        else:
            print(f"only enter a number from 0 to {len(categories)}")


def recipe_collector():
    print("recipe Collector")
    print("What type of recipe do you want to add")
    categories = sql.get_category()

    i = 1
    for category in categories:
        print(f"{i}. {category}")
        i += 1
    print("0. Exit")

    selected = False
    while not selected:
        choice = input("")
        if not choice.isdigit():
            print("You can only enter numbers, ")
        elif 0 < int(choice) < len(categories)+1:
            choice.isdigit()
            sql.insert_recipe(choice)
            main_menu()
            selected = True
        elif int(choice) == 0:
            choice.isdigit()
            main_menu()
            selected = True
        else:
            print(f"only enter a number from 0 to {len(categories)}")


def all_menu():
    print("All the recipes")
    sql.all_recipes()
    main_menu()
