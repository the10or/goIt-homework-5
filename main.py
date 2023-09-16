from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str):
        super().__init__(value)
        if value.isdigit() and len(value) == 10:
            self.value = value
        else:
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        number_found = False
        for number in self.phones:
            if number.value == phone:
                number_found = True
                return number
        if not number_found:
            raise ValueError



    def remove_phone(self, phone):
        for number in self.phones:
            if number.value == phone:
                self.phones.remove(number)

    def edit_phone(self, phone_old, phone_new):
        phone = self.find_phone(phone_old)
        phone.value = phone_new

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self[record.name.value] = record

    def find(self, name):
        return self[name] if name in self.keys() else None

    def delete(self, name):
        if name in self.keys():
            self.pop(name)


