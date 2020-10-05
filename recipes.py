class Recipe:
    def __init__(self, category, name, time, link):
        self.category = category
        self.name = name
        self.time = time
        self.link = link


def create_recipe(x):
    category = x
    name = input("Enter a name of the dish? ")
    time = input("How many minutes does it take to make? ")
    link = input("Do you have a link for the recipe? ")

    recipe = Recipe(category, name, time, link)
    return recipe


