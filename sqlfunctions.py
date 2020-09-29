import recipes
import psycopg2
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        cur.execute('SELECT recipe_name, recipe_time, recipe_link, recipe_steps FROM public.recipes')
        select = cur.fetchone()
        print(" - Recipt name - Estimated time - Recipt Link - Steps")
        print(select)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def insert_recipe(x):
    category_id = x
    name = input("Enter a name of the dish")
    time = input("How long does it take to make")
    link = input("Do you have a link for the recipe?")
    steps = []
    print("how do you cook the dish?")
    while True:
        step = input()
        if step.isdigit() == 0:
            break
        else:
            steps.append(step)
            print("next step?")

    print(category_id, name, time, link, steps)

    def insertion(category_id, name, time, link, steps):
        conn = None
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()

            cur.execute(f"INSERT INTO public.recipes(category_id, recipe_name, recipe_time, recipe_link, recipe_steps) VALUES ('{category_id}','{name}', '{time}', '{link}', '{steps}');")

            conn.commit()
            print("data inserted into database")
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

    #insertion(cateogry_id, name, time, link, steps)


def random_recipe(x):
    pass


def all_recipes():
    pass
