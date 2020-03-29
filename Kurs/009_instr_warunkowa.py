x = 12
if x > 10:
    print("Większy")
elif x % 2 == 0:
    print("Parzysty")
elif x % 3 == 0:
    print("Podzielny przez 3")
else:
    print("Żaden z warunków nie jest spełniony")
print("Koniec")
import datetime
current_year = datetime.datetime.now().year
print(current_year)

