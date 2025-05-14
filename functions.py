import csv
import datetime


FIELDNAMES = ['amount', 'category', 'date', 'description']

def display():
    try:
        with open("category.csv") as csv_file:
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
    date = (input("Podaj datę (DD-MM-YYYY) "))
    description = input("Dodaj opis np. ('Nowe ubrania') ").capitalize()
    print()
    with open('category.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        csv_writer.writerow({
            'amount': amount,
            'category': category,
            'date': date,
            'description': description
        })

def delete():
    expenses = []
    description = input("Podaj opis do usunięcia: ").capitalize()
    date = str(input("Podaj date: "))
    print()
    with open("category.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['description'] == description and row['date'] == date:
                continue

            expenses.append(row)

    with open('category.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        csv_writer.writeheader()
        print("Pomyślnie usunięto wydatek")
        print()
        for expanse in expenses:
            csv_writer.writerow(expanse)

def categories():
    try:
        with open("category.csv") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                print("Kategorie: ")
                print(row['category'])
                print()
    except FileNotFoundError:
        print("Nie znaleziono pliku")