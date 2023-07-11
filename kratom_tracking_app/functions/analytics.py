import sqlite3

def calculate_total_doses(): 
    connection = sqlite3.connect("kratom_tracking_app\database\kratom.db")
    cursor = connection.cursor()
    
    #? Count the number of rows in the 'doses' table
    
    cursor.execute("SELECT COUNT(*) FROM doses")
    total_doses = cursor.fetchone()[0]
    
    connection.close()
    
    return total_doses

def calculate_dose_frequency():
    connection = sqlite3.connect("kratom_tracking_app\database\kratom.db")
    cursor = connection.cursor()
    
    #!TODO 
    #? Query to calculate dose frequency
    
    connection.close()
    
    return dose_frequency