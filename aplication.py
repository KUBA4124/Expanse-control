from  functions import display, add, delete, categories, date_search, edit
import sys
while True:
    print("1. Wyświetlenie wydatków")
    print("2. Dodawanie wydatku")
    print("3. Usuwanie wydatku")
    print("4. Edytowanie wydatku")
    print("5. Wyświetlanie kategorii")
    print("6. Filtrowanie po dacie")
    print("7. Zakończ program")

    try:
        option = int(input("Wybierz opcje: (1-7)"))
        print()

        if option == 1:
            display()
        elif option == 2:
            add()
        elif option == 3:
            delete()
        elif option == 4:
            edit()
        elif option == 5:
            categories()
        elif option == 6:
            date_search()
        elif option == 7:
            sys.exit()
    except ValueError:
        print("Podaj liczbę")