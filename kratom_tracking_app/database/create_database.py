import sqlite3

def create_database(): 
    try: 
        connection = sqlite3.connect("kratom.db")
        cursor = connection.cursor()
    
    # Create the table for dose tracking

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS doses (
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            timestamp TEXT, 
                            quantity REAL
                        )
                        """)

        connection.commit()
        connection.close()
        
        print('############################')
        print("Hello donovan!\nThe database was created successfully!\nREPEAT\nREPEAT\nREPEAT\n")
        print('asdjf;lkasdjf;alskdjfalsdkjf\n')
        print('############################\n')
        print("Hello donovan!\nThe database was created successfully!!!\n")
        ('############################\n')
    except sqlite3.Error as e: 
        ('############################')
        print("Hello donovan!\nThe database was NOT created successfully!\nREPEAT NOT\nREPEAT NOT\nREPEAT NOT\n")
        print("Error occured while creating the database: \n", e)
if __name__ == '__main__':
    create_database()
    
    
