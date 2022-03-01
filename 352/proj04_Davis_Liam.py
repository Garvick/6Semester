import csv
#Filename 
FILENAME = "proj04_contacts.csv"

#updates list
def write_contact(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts) 

#reads list
def read_contacts():
    contacts = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
        return contacts

#print contacts list
def list_contacts(contacts):
    for i in range (len(contacts)):
        contacts = contacts[i]
        print(str(i+1) + ". " + contacts[0] + " (" + contacts[1] + ") ")
    print()

#adds contact
def add_contact(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contacts.append(contact)
    write_contacts(contacts)
    print(name + " was added. /n")

#deletes contact
def delete_contact(contacts):
    index = int(input("number: "))
    contact = contacts.pop(index - 1)
    write_contacts(contacts)
    print(contact[0] + " was deleted./n")

#prints the menu
def display_menu():
    print("Contact Manager")
    print()
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - view a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    exit("exit - Exit program")

#the operation of the menu
def main():
    display_menu()
    contacts = read_contacts()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_contacts(contacts)
        elif command.lower() == "add":
            add_contact(contacts)
        elif command.lower() == "del":
            delete_contact(contacts)
        elif command.lower() == "exit":
            break
        else:
            print("not a valid command. Please try again./n")
    print("Bye!")

if __name__== "__main__":
    main()