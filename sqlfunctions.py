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


def insert_recipe(cat_id, name, time, link, steps):
    conn = None
    sql = """INSERT INTO public.recipes(category_id, recipe_name, recipe_time, recipe_link, recipe_steps)
                VALUES(%s);"""
    cat_id = cat_id
    name = name
    time = time
    link = link
    steps = steps
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        cur.execute(f"INSERT INTO public.recipes(category_id, recipe_name, recipe_time, recipe_link, recipe_steps) VALUES ('{cat_id}','{name}', '{time}', '{link}', '{steps}');")

        conn.commit()
        print("data inserted into database")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
