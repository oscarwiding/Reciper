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
    print("1. Dinner")
    print("2. Dessert")
    print("3. Entrees")
    print("4. Preserves")
    print("0. Go back")

    selected = False
    while not selected:
        choice = input("")
        if not choice.isdigit():
            print("You can only enter numbers, ")
        elif int(choice) == 1:
            sql.random_recipe(1)
            main_menu()
            selected = True
        elif int(choice) == 2:
            sql.random_recipe(2)
            main_menu()
            selected = True
        elif int(choice) == 3:
            sql.random_recipe(3)
            main_menu()
            selected = True
        elif int(choice) == 4:
            sql.random_recipe(4)
            main_menu()
            selected = True
        elif int(choice) == 0:
            main_menu()
            selected = True
        else:
            print("Oops, that don't seem to be an option. \npick between 1, 2, 3, 4 and 0")


def recipe_collector():
    print("recipe Collector")
    print("What type of recipe do you want to add")
    print("1. Dinner")
    print("2. Dessert")
    print("3. Entrees")
    print("4. Preserves")
    print("0. Go back")
    selected = False
    while not selected:
        choice = input("")
        if not choice.isdigit():
            print("You can only enter numbers, ")
        elif int(choice) == 1:
            sql.insert_recipe(2)
            main_menu()
            selected = True
        elif int(choice) == 2:
            sql.insert_recipe(2)
            main_menu()
            selected = True
        elif int(choice) == 3:
            sql.insert_recipe(3)
            main_menu()
            selected = True
        elif int(choice) == 4:
            sql.insert_recipe(4)
            main_menu()
            selected = True
        elif int(choice) == 0:
            main_menu()
            selected = True
        else:
            print("Oops, that don't seem to be an option. \npick between 1, 2, 3, 4 and 0")


def all_menu():
    print("All the recipes")
    sql.all_recipes()
    main_menu()
