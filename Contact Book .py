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

        if name == "" or phone == "":
            print("Invalid input")
        elif name.lower() in (n.lower() for n in contacts):
            print("Contact already exists")
        else:
            contacts[name] = phone
            print("Contact added!")
            
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts yet")
        else:
            print("\nContacts:")
            for i, (name, phone) in enumerate(contacts.items(), 1):
                print(f"{i}. {name} : {phone}")

    elif choice == "3":
        search = input("Enter name to search: ")
        found = False
        for name, phone in contacts.items():
            if name.lower() == search:
                print(name, ":", phone)
                found = True
                break

        if not found:
            print("Contact not found")

    elif choice == "4":
       delete = input("Enter name to delete: ").strip().lower()

        found = False
        for name in list(contacts.keys()):
            if name.lower() == delete:
                del contacts[name]
                print("Contact deleted!")
                found = True
                break

        if not found:
            print("Contact not found")

    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Wrong choice")
