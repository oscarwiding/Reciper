import menu


def main():
    running = True
    while running:
        running = menu.main_menu()
    print("Goodbye and enjoy your day")


if __name__ == '__main__':
    main()
