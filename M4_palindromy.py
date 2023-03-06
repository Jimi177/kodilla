"""
Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem.
Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.

Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.
"""

def palindrom_check(word):
    test_word = [*word]
    test_word.reverse()
    new_word = "".join(map(str,test_word))

    if word == new_word:
        return True
    else:
        return False


print(palindrom_check("test"))