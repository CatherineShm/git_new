number_1 = int(input("Podaj pierwszą liczbę: "))
number_2 = int(input("Podaj drugą liczbę: "))
operation = input("Podaj rodzaj operacji: ")
if operation == "-" :
    print("Wynik: ", number_1 - number_2)
elif operation == "+" :
    print("Wynik: ", number_1 + number_2)
elif operation == "*" :
    print("Wynik: ", number_1 * number_2)
elif operation == "/" :
    if number_2 != 0 :
        print("Wynik: ", round(number_1 / number_2, 2))
    else:
        print("Nie można dzielić przez zero.")
else:
    print("Wystąpił błąd: podałeś niepoprawną  operację.")
