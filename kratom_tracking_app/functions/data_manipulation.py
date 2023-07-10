import sqlite3
from datetime import datetime

def log_dose(quantity_type, quantity):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    connection = sqlite3.connect("../database/kratom.db")
    cursor = connection.cursor()
    
    #! Insert the dose into the "doses" table
    
    cursor.execute("INSERT INTO doses (timestamp, quantity_type, quantity) VALUES (?, ?)", (timestamp, quantity_type, quantity))
    
    connection.commit()
    connection.close()
    
    return timestamp()
    
def get_dose_data():
    connection = sqlite3.connect("../database/kratom.db")
    cursor = connection.cursor()
    
    # Retrieve all dose data from the 'doses' table
    
    cursor.execute("SELECT * FROM doses")
    dose_data = cursor.fetchall()
    
    connection.close()
    
    return dose_data