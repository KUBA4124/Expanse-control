import csv
import datetime


FIELDNAMES = ['amount', 'category', 'date', 'description']

def display():
    try:
        with open('expansions.csv', encoding='UTF-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                print(f"Kwota: {row['amount']}")
                print(f"Kategoria: {row['category']}")
                print(f"Data: {row['date']}")
                print(f"Opis: {row['description']}")
                print()
    except FileNotFoundError:
        print("Nie znaleziono pliku")



def add():
    amount = float(input("Podaj kwotę wydatku np (49.99): "))
    category = input("Podaj kategorię np (Jedzenie, Transport, Rozrywka): ").capitalize()
    date = input("Podaj datę (DD-MM-YYYY) ")
    description = input("Dodaj opis np. ('Nowe ubrania') ")
    print()
    with open('expansions.csv', 'a', newline='', encoding='UTF-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        csv_writer.writerow({
            'amount': amount,
            'category': category,
            'date': date,
            'description': description
        })
        
    with open('bilans.csv', 'a', newline='', encoding='UTF-8') as csv_file:
        fieldnames = ['amount', 'category']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writerow({
            'amount': amount,
            'category': category
        })

def edit():
    expenses = []
    bilans_data = []
    description = input("Podaj opis do edycji: ")
    with open('expansions.csv', encoding='UTF-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['description'] == description:
                new_amount = float(input("Podaj nową kwotę (np: 49.99) "))
                new_category = input("Wprowadź nową kategorię: ")
                new_date = input("Wprowadź nową datę: (DD-MM-YYYY) ")
                new_description = input("Wprowadź nowy opis: ")
                print()

                row['amount'] = new_amount
                row['category'] = new_category
                row['date'] = new_date
                row['description'] = new_description

            expenses.append(row)

            bilans_data.append({
                'amount': row['amount'],
                'category': row['category']
            })

    with open('expansions.csv', 'w', encoding='UTF-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        csv_writer.writeheader()

        for expense in expenses:
            csv_writer.writerow(expense)

    with open('bilans.csv', 'w', newline='', encoding='UTF-8') as csv_file:
        fieldnames = ['amount', 'category']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in bilans_data:
            csv_writer.writerow(row)

    print("Plik zaktualizowany pomyślnie")


def delete():
    expenses = []
    description = input("Podaj opis do usunięcia: ").strip().lower()
    date = str(input("Podaj date: ")).strip()
    print()
    with open("expansions.csv", encoding='UTF-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['description'].strip().lower() == description and row['date'].strip() == date:
                continue
            expenses.append(row)

    with open('expansions.csv', 'w', encoding='UTF-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        csv_writer.writeheader()
        for expanse in expenses:
            csv_writer.writerow(expanse)

    print("Pomyślnie usunięto wydatek\n")

    with open('bilans.csv', 'w', newline='', encoding='UTF-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['amount', 'category'])
        csv_writer.writeheader()
        for row in expenses:
            csv_writer.writerow({
                'amount': row['amount'],
                'category': row['category']
            })

def categories():
    try:
        with open('expansions.csv', encoding='UTF-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            print("Kategorie: ")
            for row in csv_reader:
                print(row['category'])
            print()
    except FileNotFoundError:
        print("Nie znaleziono pliku")

def date_search():
    date = str(input("Informację z jakiej daty cię interesują? (DD-MM-YYYY)"))
    print()
    counter = 0

    with open('expansions.csv', encoding='UTF-8', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['date'] == date:
                print(f"Kwota: {row['amount']}")
                print(f"Kategoria: {row['category']}")
                print(f"Data: {row['date']}")
                print(f"Opis: {row['description']}")
                counter += 1
                print()
    if counter == 0:
        print("Nie ma wydatku z taką datą")
        print()
