from functions.data_manipulation import log_dose, get_dose_data
from functions.analytics import calculate_total_doses

def test_create_database(): 
    #?TODO Code to check if the database files exists and is valid
    pass

def test_logging_dose(): 
    timestamp = "2023-07-09 12:34:56"
    quantity = 2.5
    
    log_dose(timestamp, quantity)
    
    #?TODO Code to validate if the dose is logged correctlty
    
def test_retrieving_dose_data():
    dose_data = get_dose_data()
    
    #TODO Code to verify if the retrieved dose data is correct
    
def test_calculating_analytics():
    total_doses = calculate_total_doses()
    
    #TODO Code to validate the total number of doses
    
#! Run the test cases
def run_tests():
    test_create_database()
    test_logging_dose()
    test_retrieving_dose_data()
    test_calculating_analytics()
    
run_tests()
