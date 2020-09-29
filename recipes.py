class RecipeCategory:
    def __init__(self, main_category):
        self.main_category = main_category


class Recipe(RecipeCategory):
    def __init__(self, category, time, link, text):
        super().__init__(RecipeCategory)
        self.category = category
        self.time = time
        self.link = link
        self.text = text
