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
            edit_contact()
            ask = False
        elif option == 3:
            show_contacts()
            ask = False
        elif option == 4:
            search_contact()
            ask = False
        elif option == 5:
            print('Delete contact')
            ask = False
        elif option == 6:
            ask = False
        else:
            print('The given option is not valid, please try again')

def add_contact():
    print('Please answer the next fields:')

    contact_name = input('Write the name of the contact:\n')

    exists = contact_exists(contact_name)

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

def edit_contact():
    print('Write the contact\'s name to edit it')
    previous_name = input('Name: \n')

    exists = contact_exists(previous_name)

    if exists:
        contact_name = input('Write the new name:\n')
        contact_phone = input('Add the new phone:\n')
        contact_category = input('Add the new category:\n')

        contact = Contact(contact_name, contact_phone, contact_category)

        with open(f'{ FOLDER }{ previous_name }{ EXTENSION }', 'w') as file:
            file.write(f'Name: { contact.name } \n')
            file.write(f'Phone: { contact.phone } \n')
            file.write(f'Category: { contact.category } \n')

            os.rename(f'{ FOLDER }{ previous_name }{ EXTENSION }', f'{ FOLDER }{ contact.name }{ EXTENSION }')

    else:
        print('The given contact doesn\'t exists')
    
    app()

    print('1) Add new contact')

def show_menu():
    print('2) Edit contact')
    print('3) Show contacts')
    print('4) Search contact')
    print('5) Delete contact')
    print('6) EXIT')

def show_contacts():
    files = os.listdir(FOLDER)
    
    files_txt = [i for i in files if i.endswith(EXTENSION)]

    for file in files_txt:
        with open(f'{ FOLDER }{ file }') as contact:
            for line in contact:
                print(line.rstrip())
            print('\n')
    
    app()
            
def search_contact():
    name = input('Select the contact that you want to search: \n')

    try:
        with open(f'{ FOLDER }{ name }{ EXTENSION }') as contact:
            print('\n Contact Information \n')

            for line in contact:
                print(line.rstrip())
            print('\n')
    except IOError:
        print('The contact doesn\'t exists')
        print(IOError)
    finally:
        app()

def create_directory():
    if not os.path.exists(FOLDER):
        # Create folder
        os.makedirs(FOLDER)

def contact_exists(name):
    return os.path.isfile(f'{ FOLDER }{ name }{ EXTENSION }')

app()