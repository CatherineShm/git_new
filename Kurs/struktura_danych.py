#krotka, tupla
#niezmienna!!!
x = (1, 2, 3, 10, 12, "ala", "mnm", 2.0)
#    0  1  2   3   4     5     6     7
print(x)
print(type)
print(dir(x))

print(x.index("ala"))
print(len(x))
print(len("ala"))
print(x.count(12)) # policzyć ile razy cos jest
if "ppp" in x:
    print(x.index("ppp"))

print("b" in "Olaf")
print(x[0])
print(x[-3])
print(x[:6])
print(x[0:6])
print(x[::2]) #co drugi element
print(x[::-1])
