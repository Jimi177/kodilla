import logging
logging.basicConfig(level=logging.DEBUG)

calculation_type_dict = {1: "+", 2: "-", 3: "*",4: "/"}
values = []
how_many_numbers = 2
math_string = ""

try:
    calculation_type = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    if calculation_type > 4:
        print("Podałeś nieodpowiednią liczbę")
        exit(1)
except ValueError:
    print("Podaj liczbę do określenia rodzaju działania")


if calculation_type == 1 or calculation_type == 3:
    try:
        how_many_numbers = int(input("Z ilu liczb będzie składać się to działanie? "))
    except ValueError:
        print("Podano nieodpowiednią liczbę wartości")
        exit(1)

    for x in range(how_many_numbers):
        try:
            y = int(input("Podaj wartośc nr."+str(x+1)+ " "))
            values.append(y)
        except ValueError:
            print("Podano nieodpowiednią wartość")
            exit(1)
else:
    for x in range(how_many_numbers):
        try:
            y = int(input("Podaj wartośc nr."+str(x+1)+ " "))
            values.append(y)
        except ValueError:
            print("Podano nieodpowiednią wartość")
            exit(1)

for number in values:
    math_string += str(number) + " " + calculation_type_dict[calculation_type] +" "

clean_math_string = str(math_string[:-2])
result = str(eval(clean_math_string))
logging.debug("Wykonuję działanie: " + clean_math_string)
print("Wynik działania: "+result)





