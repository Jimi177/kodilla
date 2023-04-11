items = {"Monitor": [299, "Szt", 997], "Klawiatura": [499, "Szt", 199.3], "Myszka": [122, "Szt", 99]}
sold_items = {}

def get_items():
    print("Name\t\tQuantity\tUnit\tUnit Price (PLN)")
    print("----\t\t--------\t----\t----------------")
    for item in items:
        line = "{0:10s}\t{1:3d}\t\t\t{2:3s}\t\t{3:4d}"
        print(line.format(item, items[item][0], items[item][1],items[item][2]))

def get_sold_items():
    print("Name\t\tQuantity\tUnit\tUnit Price (PLN)")
    print("----\t\t--------\t----\t----------------")
    for item in sold_items:
        line = "{0:10s}\t{1:3d}\t\t\t{2:3s}\t\t{3:4d}"
        print(line.format(item, items[item][0], items[item][1], items[item][2]))
    print("Zysk: "+str(money))

def add_item():
    name = str(input("Wprowadź nazwę produktu: "))
    quantity = int(input("Wprowadź ilość produktu: "))
    unit = str(input("Wprowadź miarę ilości: "))
    price = int(input("Wprowadź cenę jedną miarę ilości produktu: "))
    items[name] = [quantity,unit,price]

def sell_item():
    name = str(input("Wprowadź nazwę produktu: "))
    if items[name]:
        print("Towar znajduje się na magazynie w ilości "+str(items[name][0]))
        amount = int(input("Jaką ilość chcesz sprzedać? "))

        if amount <= items[name][0]:
            print("Pomyślna sprzedaż")
            items[name][0] -= amount
            sold_items[name] = [amount,items[name][1], items[name][2]]
            get_items()
        else:
            print("Niewystarczająca ilość produktu w magazynie")

def get_costs():
    costs = 0

    for item in items:
       costs += items[item][0] * items[item][2]

    print("Wartość towaru znajdującego się na magazynie: "+str(round(costs,2)))

def get_incomes():
    income = 0

    for item in sold_items:
        income += sold_items[item][0] * sold_items[item][2]

    print("Wartość towaru znajdującego się na magazynie: " + str(round(income,2)))

def show_revenue():
    costs = 0
    income = 0

    for item in items:
        costs += items[item][0] * items[item][2]

    for item in sold_items:
        income += sold_items[item][0] * sold_items[item][2]

    revenue = income - costs

    print("Revenue: "+ str(round(revenue,2)))

def export_items_to_csv():
    print("test")

def menu():
    command = str(input("What would you like to do?: ")).lower()

    if command == "get":
        get_items()
    elif command == "add":
        add_item()
    elif command == "sell":
        sell_item()
    elif command == "get sold":
        get_sold_items()
    elif command == "costs":
        get_costs()
    elif command == "income":
        get_incomes()
    elif command == "revenue":
        show_revenue()
    else:
        print("Dostępne komendy: get, add, sell, get sold, costs, income, revenue")




