def add_contact(contact_book:dict,name,number):
    if name in contact_book.keys():
        return False
    contact_book[name] = number
    return True
def lookup_contact(contact_book:dict,name):
    return contact_book.get(name)
def contact_list(contact_book:dict):
    if not contact_book:
        print("Contact Book is empty")
    else:
        print("\n---- All Contacts ----")
        for name,value in contact_book.items():
            print(f"name:{name} and Phone:{value}")
            print("-----------------------")

contacts = dict()

while True:
    print("Menu Options:")
    print("1.Add Contact")
    print("2.LookUp Contact")
    print("3.View Contacts")
    print("4.Exit")
    user_input = input("\n Select Options 1-4:")
    if user_input =="1":
        name = input("Contact Name:")
        number = input("Contact Number:")
        if add_contact(contacts,name,number):
            print(f"Added {name} in Contact Book")
        else :
            print(f"Error! Already Exists {name} in Contact Book")
    elif user_input =="2":
        name = input("Contact Name:")
        found_number = lookup_contact(contacts,name)
        if found_number:
            print(f"Number for {name} is :{found_number}")
        else :
            print(f"Contact {name} was not Found!")
    elif user_input == "3":
        contact_list(contacts)
    elif user_input == "4":
        print("Exiting Contact Book , SEE You soon!")
        break
    else :
        print("Invalid Option : Select options between 1-4")