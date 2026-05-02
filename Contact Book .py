contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        if name.strip() == "" or phone.strip() == "":
            print("Invalid input")
        else:
            contacts[name] = phone
            print("Contact added!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts yet")
        else:
            print("\nContacts:")
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "3":
        search = input("Enter name to search: ")

        if search in contacts:
            print(search, ":", contacts[search])
        else:
            print("Contact not found")

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Wrong choice")