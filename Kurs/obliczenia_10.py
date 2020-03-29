number_1 = int(input("Podaj pierwszą liczbę: "))
number_2 = int(input("Podaj drugą liczbę: "))
operation = input("Podaj rodzaj operacji: ")
if operation == "-" :
    print(number_1 - number_2)
elif operation == "+" :
    print(number_1 + number_2)
elif operation == "*" :
    print(number_1 * number_2)
elif operation == "/" :
    print(number_1 / number_2)
else:
    print("Wystąpił błąd: podałeś niepoprawną  operację.")
