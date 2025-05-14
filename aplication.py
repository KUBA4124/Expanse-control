from  functions import display, add, delete, categories
import sys
while True:
    print("1. Wyświetlenie wydatków")
    print("2. Dodawanie wydatków")
    print("3. Usuwanie wydatków")
    print("4. Wyświetlanie kategorii")
    print("5. Zakończ program")

    try:
        option = int(input("Wybierz opcje: (1-5)"))
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
            sys.exit()
    except ValueError:
        print("Podaj liczbę")