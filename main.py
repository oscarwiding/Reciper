import menu
import recipes
import sqlfunctions as sql


def main():
    #menu.main_menu()
    sql.connect()
    sql.insert_recipe(1, "Korv med korv", 10, "www.mat.se", "steg 1, stek korven")


if __name__ == '__main__':
    main()
