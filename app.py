import os

FOLDER = 'contacts/'
EXTENSION = '.txt'

# Contacts class
class Contact():
    def __init__(self, name, phone, category):
        self.name = name
        self.phone = phone
        self.category = category

def app():
    # Check if the contact's folder exists
    create_directory()
    # Show menu
    show_menu()
    # Ask the user what to do
    ask = True
    while ask:
        option = input('Select an option from the menu: \n')
        option = int(option)

        # Execute option
        if option == 1:
            add_contact()
            ask = False
        elif option == 2:
            print('Edit contact')
            ask = False
        elif option == 3:
            print('Show contacts')
            ask = False
        elif option == 4:
            print('Search contact')
            ask = False
        elif option == 5:
            print('Delete contact')
            ask = False
        else:
            print('The given option is not valid, please try again')

def add_contact():
    print('Please answer the next fields:')

    contact_name = input('Write the name of the contact:\n')

    exists = os.path.isfile(f'{ FOLDER }{ contact_name }{EXTENSION}')

    if not exists:
        contact_phone = input('Add the contact\'s phone:\n')
        contact_category = input('Add the contact\'s category:\n')

        contact = Contact(contact_name, contact_phone, contact_category)
        
        with open(f'{ FOLDER }{ contact.name }{EXTENSION}', 'w') as file:
            file.write(f'Name: { contact.name } \n')
            file.write(f'Phone: { contact.phone } \n')
            file.write(f'Category: { contact.category } \n')
        
        print('\n The contact has been added! \n')
    else:
        print('That contact already exists')

    # Restart app
    app()


def show_menu():
    print('1) Add new contact')
    print('2) Edit contact')
    print('3) Show contacts')
    print('4) Search contact')
    print('5) Delete contact')

def create_directory():
    if not os.path.exists(FOLDER):
        # Create folder
        os.makedirs(FOLDER)


app()