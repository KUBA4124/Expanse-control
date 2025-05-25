Opis:

Aplikacja konsolowa służąca do zarządzania domowym budżetem, stworzona w języku Python. Pozwala na śledzenie wydatków, ich edycję, usuwanie oraz analizę danych na podstawie kategorii i dat.
Wszystkie dane są przechowywane w plikach CSV, co zapewnia prostą integrację i możliwość przeglądania danych w zewnętrznych programach (np. Excel).

Funkcjonalności:

Dodawanie wydatków – użytkownik może wprowadzić kwotę, kategorię, datę oraz opis.

Edycja wydatków – możliwość aktualizacji wszystkich pól (kwota, kategoria, data, opis).

Usuwanie wydatków – na podstawie opisu i daty.

Wyświetlanie wydatków – prezentacja pełnej listy zapisanych danych.

Lista dostępnych kategorii – szybki przegląd istniejących kategorii wydatków.

Zapis do plików CSV:


expansions.csv – pełne dane o wydatkach.

bilans.csv – uproszczone dane: kwota i kategoria.

Synchronizacja danych – każda zmiana w expansions.csv automatycznie aktualizuje dane w bilans.csv.

Generowanie wykresu kołowego (Matplotlib) – wizualizacja udziału kategorii w całkowitych wydatkach.

Struktura danych:


Plik expansions.csv zawiera pola:

amount – kwota wydatku

category – kategoria (np. jedzenie, transport)

date – data w formacie DD-MM-YYYY

description – krótki opis (np. „zakupy spożywcze”)

Plik bilans.csv zawiera pola:

amount

category
(używany głównie do wykresów i analiz)

Przykłady zastosowania:

Codzienne śledzenie wydatków osobistych

Prosty budżet dla studenta lub gospodarstwa domowego

Nauka programowania: praca z plikami, słownikami, listami, biblioteką csv i matplotlib

Rozbudowa o własne funkcje (np. filtry, limity, eksport do PDF)

Możliwości rozwoju:

Wyszukiwanie wydatków po dacie, zakresie dat lub kategorii

Ustawienie miesięcznego budżetu i alertów

Eksport danych do Excela lub JSON

Wersja z interfejsem graficznym (np. Tkinter / PyQt)
