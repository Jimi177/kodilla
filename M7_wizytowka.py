#imię, nazwisko, nazwa firmy, stanowisko, adres e-mail.
from faker import Faker
f = Faker()

class BaseContact():
    def __init__(self, name, last_name, phone_number,email):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def contact(self):
        print(f"Select number: ",{self.phone_number},"to", {self.name}, {self.last_name})

    @property
    def label_length(self):
        return self.message

    def label_length(self):
        label_length = len(self.name, self.last_name + 1)
        message = ("Data lenght: ",label_length)

class BusinessContact(BaseContact):
    def __init__(self, position, company_name, business_phone_number):
        self.position = position
        self.company_name = company_name
        self.business_phone_number = business_phone_number

    def contact(self):
        print(f"Select number: ", {self.business_phone_number},"to", {self.name}, {self.last_name})

def menu():
    quantity = int(input("How mand cards do u want to generate: "))
    card_type = input("Which type of card do you want? NormalContact / BaseContact / BusinessContact: ")
    sort_by = input("How do you want to sort cards?By name / last_name / email: ")

    cards = create_contacts(quantity,card_type)

    if sort_by == "name":
        return sorted_by_name(cards)
    elif sort_by == "last_name":
        return sorted_by_last_name(cards)
    elif sort_by == "email":
        return sorted_by_email(cards)

def create_contacts(quantity,card_type):
    cards = []

    for _ in range(quantity):
        name, *last_name = f.name().split(" ")
        last_name2 = " ".join(last_name)
        company_name = f.company().split(",")[0]
        position = f.job().split(",")[0]
        email = name + last_name2 + "@gmail.com"

        card = Card(name=name,last_name=last_name2,company_name=company_name,position=position,email=email)
        cards.append(card)

    return cards

def sorted_by_name(cards):
    return sorted(cards, key=lambda card: card.name)

def sorted_by_last_name(cards):
    return sorted(cards, key=lambda card: card.last_name)

def sorted_by_email(cards):
    return sorted(cards, key=lambda card: card.email)

data = menu()

print("Name\t\t\tLast Name\t\tCompany Name\t\t\t\tPosition\t\t\t\t\t\t\t\tE-mail")
for card in data:
    line = "{0:10s}\t\t{1:15s}\t{2:25s}\t{3:35s}\t\t{4:25s}"
    print(line.format(card.name,card.last_name,card.company_name,card.position,card.email))

