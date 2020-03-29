x = 7
temp = 0
while x > 0 :
    t = float(input("Podaj temperaturę: "))
    x = x - 1
    temp += t

print("Średnia z temperatór to: ", f"{t/7 : .2f}", "stopni. ")

