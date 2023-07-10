import sqlite3

def log_dose(timestamp, quantity):
    connection = sqlite3.connect("../database/kratom.db")
    cursor = connection.cursor()
    
    #? Insert the dose into the "doses" table
    
    cursor.execute("INSERT INTO doses (timestamp, quantity) VALUES (?, ?)", (timestamp, quantity))
    
    connection.commit()
    connection.close()
    
def get_dose_data():
    connection = sqlite3.connect("../database/kratom.db")
    cursor = connection.cursor()
    
    # Retrieve all dose data from the 'doses' table
    
    cursor.execute("SELECT * FROM doses")
    dose_data = cursor.fetchall()
    
    connection.close()
    
    return dose_data