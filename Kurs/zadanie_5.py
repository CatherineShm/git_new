#Napisz program obliczajacy koszt przejazdu z miasta A do B na
#podstawie podanej przez uzytkownika liczby kilometrów, ceny paliwa
#oraz spalania. Zapytaj uzytkownika takze o nazwy miejscowosci.
#Przykładowe komunikat programu:
#Miasto A: Warszawa
#Miasto B: Gdansk
#Dystans Warszawa-Gdansk: 420
#Cena paliwa: 4.55
#Spalanie na 100 km: 5.5
#Koszt przejazdu Warszawa-Gdansk to 105 PLN
miasto_a = input("Podaj pierwsze miasto: ")
miasto_b = input("Podaj gruge miasto: ")
kilometry = float(input("Podaj liczbe kilometrow: "))
cena_paliwa = float(input("Podaj cene paliwa: "))
spalanie = float(input("Spalanie na 100 km to: "))
koszt = (kilometry / 100) * spalanie * cena_paliwa
print("Koszt przejazdu to", round(koszt, 1), "zl.")