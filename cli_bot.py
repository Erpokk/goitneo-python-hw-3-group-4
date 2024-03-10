from collections import UserDict
from datetime import datetime
from datetime import date
from classes import AddressBook, Record

def input_error(func):   
    def inner(*args, **kwargs):   
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Given key not found"
        except IndexError:
            return "Index out of range"

    return inner

@input_error
def parse_input(user_input):    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def change_contact(args, contacts):   
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact {name} not found."

@input_error
def show_all (contacts):
    all_contacts = []
    for name, phone in contacts.items():
        all_contacts.append(f'{name} {phone}')
    return "\n".join(all_contacts)

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact {name} not found."

@input_error
def add_contact(args, book):
    name, phone = args
    if book.find(name) == "Not found":
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added."
    else:
        return "This contact is already in contacts. Use command 'change'."

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "all":
            print(show_all(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
