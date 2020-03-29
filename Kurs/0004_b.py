first_name = input("imie: ")
last_name = input("nazwisok: ")
b_year = input("rok ur: ")
profession = input("zawod: ")
result = f"""
{"imie i nazwisko:"} {first_name:>10}{last_name.capitalize()}
{"============================="}
{"rok urodzenia:"} {b_year:<10}
{"zawód:"}         {profession} 
"""
print(result)