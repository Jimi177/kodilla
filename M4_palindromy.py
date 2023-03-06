'''
Zadanie 1
Pamiętasz zadanie z listą zakupów?

Załóżmy, że mamy do zrobienia zakupy spożywcze, potrzebujemy pójść do piekarni, w której kupujemy chleb, bułki oraz pączka. Poza tym po drodze wstąpimy też do warzywniaka, gdzie kupimy marchew, seler i rukolę.

W pliku, który właśnie utworzyliśmy:

zdefiniuj słownik zawierający listę zakupów, gdzie kluczem jest nazwa sklepu, a wartością lista przedmiotów, które chcesz kupić w danym sklepie.
Następnie za pomocą pętli for, przeiteruj po tym słowniku i wyświetl napis w postaci: Idę do <sklep> i kupuję tam <rzeczy>.
Dodatkowo, używając wbudowanych metod operacji na napisach, spowoduj, aby nazwy sklepów i towarów były wypisane wielką literą (sięgnij do oficjalnej dokumentacji, by odnaleźć taką funkcjonalność).
Na koniec, w ostatniej linii wypisz W sumie kupuję <X> produktów.. X to sumaryczna liczba towarów, które są na listach.
Twój program po uruchomieniu, powinien wyświetlić następujące informacje:
'''

shops = {"piekarni":("chleb", "bułki", "pączki"), "warzywniaka":("marchew", "seler", "rukola")}
x = 0

print("Lista Zakupów")
for shop in shops:
    print("Ide do " + shop.capitalize() +", kupuję tam: " + str(shops[shop]))
    x += len(shops[shop])

print(x)

'''
Zadanie 2
Napisz program, który:

Dla liczb z zakresu od 0 do 100, wyświetli te, które są podzielne przez 5.
W następnym wierszu wyświetli te liczby podniesione do potęgi 3.
'''

for x in range(0,101):
    if x % 5 == 0:
        print(x**3)