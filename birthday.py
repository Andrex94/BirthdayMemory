#!/usr/bin/env python3


import sys

BIRTHDAYS = {}


def add_birthday():
    while True:
        name = input("Enter a name or press [ENTER] for other options: ").lower().capitalize()
        if name == "":
            break
        if name in BIRTHDAYS:
            print(f"{name}'s  birthday is {BIRTHDAYS[name]}")
            break
        print(f"I do not have a birthday for {name}")
        print(f"Do you want to add a birthday for {name}? (y/n)")
        add_birthday_option = input().lower()
        if add_birthday_option == "y":
            new_birthday = input("Add a new birthday: ").lower().capitalize()
            BIRTHDAYS[name] = new_birthday
            print(f"{name}'s birthday is added")
            continue
        if add_birthday_option == "n":
            print(f"{name}'s birthday is not added")
            break
        print("Invalid input")
        continue


def list_birthdays():
    while True:
        print("Do you want to see your birthday list? (y/n)")
        birthday_list_option = input().lower()
        if birthday_list_option == "y":
            if len(BIRTHDAYS) == 0:
                print("Birthday list is empty.")
                add_birthday()
            for name, date in BIRTHDAYS.items():
                print(f"{name}: {date}")
                break
        if birthday_list_option == "n":
            print("Birthday list not shown")
        print("Invalid input")
        continue


def delete_birthday():
    while True:
        if len(BIRTHDAYS) == 0:
            add_birthday()
        print("Do you want to delete a birthday? (y/n)")
        delete_birthday_option = input().lower()
        if delete_birthday_option == "y":
            if len(BIRTHDAYS) == 0:
                print("Birthday list is empty.")
                break
            print("What birthday do you want to delete?")
            remove_birthday = input().lower().capitalize()
            name = remove_birthday
            if remove_birthday in BIRTHDAYS:
                del BIRTHDAYS[name]
                print(f"{remove_birthday} birthday is deleted.")
                continue
            print(f"No birthday with the name {input()} exists.")
        if delete_birthday_option == "n":
            print("No birthday deleted.")
            break
        print("Invalid input")
        break


def birthday():
    print("Welcome to the birthday program.")
    add_birthday()
    list_birthdays()
    delete_birthday()
    print("Thank you for using the birthday program.")
    sys.exit()


birthday()
