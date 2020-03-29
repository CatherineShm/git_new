import datetime
current_year = int(datetime.datetime.now().year)
urodzenie = int(input("Podaj rok urodzenia : "))
x = current_year - urodzenie
if x >= 18:
    print("Jesteś pełnoletni!")
else:
    print("Nie jesteś pełnoletni.")
