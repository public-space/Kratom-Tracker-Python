from functions.user_interaction import display_menu, process_menu_choice

from database.create_database import create_database


if __name__ == '__main__':
    #? Check if the database exists
    try: 
        with open("database/kratom.db"):
            pass
    except FileNotFoundError: 
        create_database()
        
        
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        process_menu_choice(choice)