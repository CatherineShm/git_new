min_x = None
max_x = None

while True :
    number = input("Wprowadź liczbę lub x aby skączyć")
    if number == "x" :
        break
    number = int(number)
    if min_x is None or number < min_x:
        min_x = number
    if max_x is None or number > max_x:
        max_x = number
print(f"Wartosc maks : {max_x}")
print(f"Wartosc minim : {min_x}")