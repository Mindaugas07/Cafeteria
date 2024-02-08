from console import fg, bg, fx
import os


class Restaurant:
    TABLE_LIST = []

    def __init__(self, name: str, address: str, phone_number: str, menu: dict) -> None:
        self.name: str = name
        self.address: str = address
        self.phone_number: str = phone_number
        self.menu: dict = menu

    @staticmethod
    def show_app_menu() -> str:
        return input(
            f"""
If you want to see the meniu press {"--1--":^100}
If you want to browse available tables and make reservations press {"--2--":^35} 
If you want to view existing reservations or cancel them press {"--3--":^43} 
If you want to manage reservation details press {"--4--":^73} 
Press --9-- to quit our app                          
"""
        )

    def show_restaurant_menu(self) -> str:
        return f"""
We can offer you these pizzas today: {self.menu['pica']}
Drinks: {self.menu['drinks']}
"""

    def add_table(self, number_of_seats) -> None:
        table_number = restaurant_tables[number_of_seats][0][0]
        table_capacity = restaurant_tables[number_of_seats][0][1]
        table_avail = restaurant_tables[number_of_seats][0][2]

        self.new_table = Table(
            table_number=table_number,
            capacity=table_capacity,
            availability=table_avail,
        )
        Restaurant.TABLE_LIST.append(self.new_table)

    def list_tables(self) -> None:
        return Restaurant.TABLE_LIST

    def reserve_table(self, table_id: int) -> None:
        for self.table in Restaurant.TABLE_LIST:
            if table_id == int(self.table.table_number):
                self.table.mark_unavailable()

    def available_tables_menu(self) -> str:
        for index, table in enumerate(self.list_tables()):
            index += 1
            if table.availability == True:
                print(f"{table} Spauskite --{index}-- jei norite rezervuoti si stala.")
                index -= 1
        print()
        print("Press --9-- if you want to go back to main menu.")

    def __str__(self) -> str:
        return headline_name_terminal_style(
            f"""---Welcome to Pica Utah Jazz restaurant! ---
Address: {self.address}, phone: {self.phone_number}                     
"""
        )


class Table:
    def __init__(
        self, table_number: str, capacity: int, availability: bool = True
    ) -> None:
        self.table_number: str = table_number
        self.capacity: int = capacity
        self.availability: bool = availability

    def is_available(self, table_id: int) -> bool:
        return self.availability

    def mark_available(self) -> None:
        self.availability = True

    def mark_unavailable(self) -> None:
        self.availability = False

    def __str__(self) -> str:
        if self.availability:
            table_avalability = "laisvas"
        else:
            table_avalability = "uzimtas"
        return f"Stalas nr. {self.table_number} yra {table_avalability} ir prie jo telpa {self.capacity} zmones."


class Reservation:
    def __init__(
        self, customer_name: str, party_size: int, reservation_time: str, table_id: str
    ) -> None:
        self.customer_name: str = customer_name
        self.party_size: int = party_size
        self.reservation_time: str = reservation_time
        self.table_id: str = table_id

    def calculate_total(self) -> float:
        pass

    def print_reservation(self) -> str:
        pass


pica_jazz_menu = {
    "pica": {
        "Havaju": 12.2,
        "Napolio": 10.1,
        "Salami": 9.99,
        "Parma": 10.50,
        "Tuna": 15.20,
    },
    "drinks": {"Tea": 2.0, "Water": 1.5, "Vytautas": 2.5},
}
headline_name_terminal_style = fg.green + fx.bold
text_terminal_style = fg.blue
jazz_place = Restaurant(
    name="Pica Utah Jazzz",
    address="Laisves al. 14, Kaunas",
    phone_number="+37060377788",
    menu=pica_jazz_menu,
)

restaurant_tables = {
    "two_seater": [("1", 2, True), ("2", 2, True), ("3", 2, True)],
    "four_seater": [("4", 4, True), ("5", 4, True), ("6", 4, True)],
    "family_seater": [("7", 6, True), ("8", 6, True)],
}


os.system("cls")
jazz_place.add_table("two_seater")
restaurant_tables["two_seater"].pop(0)
jazz_place.add_table("four_seater")
restaurant_tables["four_seater"].pop(0)
jazz_place.add_table("family_seater")
restaurant_tables["family_seater"].pop(0)
jazz_place.add_table("two_seater")
restaurant_tables["two_seater"].pop(0)
print(jazz_place)


while True:
    try:
        user_option = jazz_place.show_app_menu()
    except:
        print("Wrong input. Please enter a number from the list...")
        break
    if user_option == "1":
        os.system("cls")
        print(jazz_place)
        print(jazz_place.show_restaurant_menu())

    elif user_option == "2":
        os.system("cls")
        print(jazz_place)
        user_option = jazz_place.available_tables_menu()

    elif user_option == "3":
        os.system("cls")
        print(jazz_place)
        jazz_place.reserve_table(1)
        # jazz_place.reserve_table(4)

    elif user_option == "4":
        os.system("cls")
        print(jazz_place)

    elif user_option == "9":
        os.system("cls")
        break

    else:
        os.system("cls")
        print("Wrong input. Please enter a number from the list...")
