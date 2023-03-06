import logging
logging.basicConfig(level=logging.DEBUG)

calculation_type_dict = {1: "+", 2: "-", 3: "*",4: "/"}
values = []
how_many_numbers = 0
math_string = ""

def calculation_type_define(context):
    while True:
        try:
            number = int(input(context))
            if number > 4:
                print("Brak typu działania, spróbuj ponownie: ")
                continue
            else:
                return number
                break
        except ValueError:
            print("Wprowadź odpowiedni klucz działania 1-4")

def how_many_values(context):
    while True:
        if calculation_type == 1 or calculation_type == 3:
            try:
                number = int(input(context))
                if number > 1:
                    return number
                    break
                else:
                    print("Zbyt mało zmiennych, wprowadź przynajmniej 2")
            except ValueError:
                print("Podaj poprawną wartość")
        else:
            print("Dla odejmowania oraz dzielenia podaj 2 wartości")
            number =2
            return number
            break

def calculation_construction(numbers):
    temp_values = []

    while len(temp_values) != numbers:
        try:
            for x in range(numbers):
                v = int(input("Wprowadź wartość nr."+str(x+1)+": "))
                temp_values.append(v)
        except ValueError:
            print("Podaj poprawną wartość")

    return temp_values

def math_string_construction(values):
    s = ""
    for number in values:
        s += str(number) + " " + calculation_type_dict[calculation_type] + " "

    return s

calculation_type = calculation_type_define("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
how_many_numbers = how_many_values("Z ilu liczb będzie składać się to działanie? ")
values = calculation_construction(how_many_numbers)
math_string = math_string_construction(values)


clean_math_string = str(math_string[:-2])
result = str(eval(clean_math_string))
logging.debug("Wykonuję działanie: " + clean_math_string)
print("Wynik działania: "+result)








