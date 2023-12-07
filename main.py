class Restaurant:
    def __init__(self, name: str, address: str, phone_number: str, menu: dict) -> None:
        self.name: str = name
        self.address: str = address
        self.phone_number: str = phone_number
        self.menu: dict = menu

    def add_table(self) -> None:
        pass

    def list_tables(self) -> None:
        pass

    def reserve_table(self) -> None:
        pass


class Table:
    def __init__(self, table_number: str, capacity: int, availability: bool) -> None:
        self.table_number: str = table_number
        self.capacity: str = capacity
        self.availability: bool = availability


class Reservation:
    def __init__(
        self, customer_name: str, party_size: int, reservation_time: str, table_id: str
    ) -> None:
        self.customer_name: str = customer_name
        self.party_size: int = party_size
        self.reservation_time: str = reservation_time
        self.table_id: str = table_id
