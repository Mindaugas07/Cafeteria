from console import fg, bg, fx
import os


class Restaurant:
    def __init__(self, name: str, address: str, phone_number: str, menu: dict) -> None:
        self.name: str = name
        self.address: str = address
        self.phone_number: str = phone_number
        self.menu: dict = menu

    @staticmethod
    def show_meniu():
        print()

    def add_table(self) -> None:
        pass

    def list_tables(self) -> None:
        pass

    def reserve_table(self) -> None:
        pass

    def __str__(self) -> str:
        return headline_name_terminal_style(
            f"""---Welcome to Pica Utah Jazz restaurant! ---
Address: {self.address}, phone: {self.phone_number}                     
"""
        )


class Table:
    def __init__(self, table_number: str, capacity: int, availability: bool) -> None:
        self.table_number: str = table_number
        self.capacity: str = capacity
        self.availability: bool = availability

    def is_available(self) -> bool:
        pass

    def mark_available(self) -> bool:
        pass

    def mark_unavailable(self) -> bool:
        pass


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


pica_jazz_menu = {"Havaju": 12.2, "Napolio": 10.1}
headline_name_terminal_style = fg.green + fx.bold
text_terminal_style = fg.blue
jazz_place = Restaurant(
    name="Pica Utah Jazzz",
    address="Laisves al. 14, Kaunas",
    phone_number="+37060377788",
    menu=pica_jazz_menu,
)

os.system("cls")

print(jazz_place)

while True:
    try:
        user_option = input(
            f"""
If you want to see the meniu press {"--1--":^100}
If you want to browse available tables and make reservations press {"--2--":^35} 
If you want to view existing reservations or cancel them press {"--3--":^43} 
If you want to manage reservation details press {"--4--":^73} 
Press --9-- to quit our app                          
"""
        )
    except:
        print("Wrong input. Please enter a number from the list...")
        break
    if user_option == "1":
        os.system("cls")
        print(jazz_place)

    elif user_option == "2":
        os.system("cls")
        print(jazz_place)

    elif user_option == "3":
        os.system("cls")
        print(jazz_place)

    elif user_option == "4":
        os.system("cls")
        print(jazz_place)

    elif user_option == "9":
        os.system("cls")
        break

    else:
        os.system("cls")
        print("Wrong input. Please enter a number from the list...")
