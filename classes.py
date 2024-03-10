
from collections import UserDict
from datetime import datetime
from datetime import date

class Field: 
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Birthday(Field):
    def __init__(self, value):
        try:
            birthday = datetime.strptime(value, '%d.%m.%Y').date()
            if birthday > date.today():
                raise ValueError
            super().__init__(birthday)
        except ValueError:
            raise ValueError("Incorrect format or future date. Use format Day/Month/Year (Ex. 01/01/2000).")

class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)
        if len(phone) == 10:
            self.phone = phone
        else:
            self.phone = None

class Record:
    def __init__(self, name):  
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):      
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):     
        phone = Phone(phone)
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):        
        old_phone_instance = Phone(old_phone)
        new_phone_instance = Phone(new_phone)
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone_instance.value:
                self.phones[i] = new_phone_instance
                return "Phone successfully changed"
        return "Phone not found"
    
    def add_birthday(self, birthday):
        try:
            self.birthday = Birthday(birthday)
        except ValueError as e:
            print(e)


    def find_phone(self, phone_numb):        
        for phone in self.phones:
            if phone.value == phone_numb:
                return phone
        return "Phone not found"

    def __str__(self):        
        if self.birthday:
            birthday_str = self.birthday.value.strftime('%d.%m.%Y')
        else:
            birthday_str = "Not specified"
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {birthday_str}"


class AddressBook(UserDict):    
    def __init__(self):        
        super().__init__()
        self.data = {}

    def add_record(self, record):        
        self.data[record.name.value] = record

    def find(self, name):        
        for record in self.data.values():
            if record.name.value == name:
                return record
        return "Not found"

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return "Successfully deleted"
        else:
            return "Unable to delete"

# book = AddressBook()
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("55555555551")
# john_record.add_birthday("11.05.2024")
# print(john_record)