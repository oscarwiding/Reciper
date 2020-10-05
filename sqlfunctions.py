import recipes
import psycopg2
import random
from config import config


def insert_recipe(x):
    #First creates the Recipe and then inserts it into the database

    recipe = recipes.create_recipe(x)
    print(recipe)

    def insertion(category_id, name, time, link):
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(f"INSERT INTO public.recipes(category_id, recipe_name, recipe_time, recipe_link) VALUES "
                        f"('{category_id}','{name}', '{time}', '{link}');")

            conn.commit()
            print("Recipe inserted into database")
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    insertion(recipe.category, recipe.name, recipe.time, recipe.link)


def random_recipe(x):
    #Picks a random recipe from the database based on the choosen category

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(f"SELECT recipe_name, recipe_time, recipe_link FROM public.recipes where category_id = {x}")
        select = cur.fetchall()
        print(" - Recipe name - Estimated time - Recipe Link")
        print(select[random.randint(0, len(select)-1)])
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def all_recipes():
    #Gets all the recipes from the database
    
    conn = None
    try:
        params = config()

        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute('SELECT recipe_name, recipe_time, recipe_link FROM public.recipes')
        select = cur.fetchall()
        print(" - Recipe name - Estimated time - Recipe Link")
        for recipe in select:
            print(recipe)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

