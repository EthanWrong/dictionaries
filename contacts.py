"""Code that stores and manages contacts
- Using EASYGUI
- Contact ID (main dictionary key), First Name, Last Name, Mobile, Email
- Ability to search list
- Ability to print full list
- Ability to quit program
- Ability to add contact
"""

from easygui import *

# example contact list
ethan_contacts = {
    "owner": "Ethan",
    "next_id": 3,  # initially be one. Acts as PK, so no ids will be repeated
    "contacts": {
        1: {"first_name": "Michael",
            "last_name": "Winder",
            "mobile": "027 121 1254",
            "email": "michael.winder@gmail.com"},
        2: {"first_name": "Samuel",
            "last_name": "Burgess",
            "mobile": "022 123 9867",
            "email": "samuel.burgess123@hotmail.com"}
    }
}


def print_contacts(contact_list):
    print("***Contacts***")
    print()
    for contact_id in contact_list["contacts"]:
        contact = contact_list["contacts"][contact_id]
        print(f"Contact ID: {contact_id}")
        print(f"First Name: {contact['first_name']}")
        print(f"Last Name: {contact['last_name']}")
        print(f"Mobile: {contact['mobile']}")
        print(f"Email: {contact['email']}")
        print()
    msgbox("Contacts have been printed in the Python Console")


def add_contact(contact_list):
    first_name = enterbox("Enter First Name")
    last_name = enterbox("Enter Last Name")
    mobile = enterbox("Enter Mobile Number")
    email = enterbox("Enter Email Address")

    contact_id = contact_list["next_id"]
    contact_list["next_id"] += 1

    contact_list["contacts"][contact_id] = {"first_name": first_name,
                                            "last_name": last_name,
                                            "mobile": mobile,
                                            "email": email}

    return contact_list


def search_contact(contact_list):
    search = enterbox("Enter the Name, Number, or Email of any contact")
    if not search:
        return
    occurrences = 0
    matching_contacts = []
    for contact_id in contact_list["contacts"]:
        contact = contact_list["contacts"][contact_id]
        for attr in contact:
            if search.lower() in contact[attr].lower():
                occurrences += 1
                matching_contacts.append(contact_id)

    # remove repetitions in matching_contacts
    seen = set()

    # Loop through the list and remove duplicates
    for i in range(len(matching_contacts)):
        if matching_contacts[i] in seen:
            matching_contacts[i] = None
        else:
            seen.add(matching_contacts[i])

    matching_contacts = [i for i in matching_contacts if i is not None]

    # print to console
    print("***Contact Search Results***")
    for i in matching_contacts:
        contact = contact_list["contacts"][i]
        print(f"Contact ID: {i}")
        print(f"First Name: {contact['first_name']}")
        print(f"Last Name: {contact['last_name']}")
        print(f"Mobile: {contact['mobile']}")
        print(f"Email: {contact['email']}")
        print()

    msgbox(f"{occurrences} occurrence(s) of '{search}' found in Contacts\n\n"
           f"Check Python Console for details")


def main(contact_list):
    choice = buttonbox("What action would you like to perform?",
                       choices=["Add Contact", "Search Contact",
                                "Print Contacts",
                                "Quit"])

    if choice == "Add Contact":
        contact_list = add_contact(contact_list)
    elif choice == "Search Contact":
        search_contact(contact_list)
    elif choice == "Print Contacts":
        print_contacts(contact_list)
    elif choice == "Quit":
        msgbox("Contacts have been stored in a variable.\n\n"
               "Goodbye.")
        return contact_list
    return main(contact_list)


ethan_contacts = main(ethan_contacts)
