"""
Napisz skrypt, który zapyta o imię i nazwisko z wykorzystaniem input, a następnie przywita się
(funkcją print z odpowiednim tekstem) z wykonawcą tego skryptu, nawet jeśli ma najdłuższe na świecie nazwisko.
"""

name = input("What is your name?: ")
last_name = input("What is your last name?: ")
origin = input("Where are you from?: ")

print("Witaj " + str(name) +" "+str(last_name)+" z "+str(origin))