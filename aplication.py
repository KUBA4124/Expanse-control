from  functions import display, add, delete, categories, date_search
import sys
while True:
    print("1. Wyświetlenie wydatków")
    print("2. Dodawanie wydatków")
    print("3. Usuwanie wydatków")
    print("4. Wyświetlanie kategorii")
    print("5. Filtrowanie po dacie")
    print("6. Zakończ program")

    try:
        option = int(input("Wybierz opcje: (1-6)"))
        print()

        if option == 1:
            display()
        elif option == 2:
            add()
        elif option == 3:
            delete()
        elif option == 4:
            categories()
        elif option == 5:
            date_search()
        elif option == 6:
            sys.exit()
    except ValueError:
        print("Podaj liczbę")