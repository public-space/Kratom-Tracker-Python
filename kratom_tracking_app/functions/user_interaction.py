def display_menu(): 
    print("\n\n")
    print("+++ === +++ === +++ === +++ === +++")
    print("=== +++ Kratom Tracking App +++ ===")
    print("+++ === +++ === +++ === +++ === +++")
    print("1. Log Dose")
    print("2. View Dose Data")
    print("3. Calculate Analytics")
    print("0. Exit")
    print("+++ === +++ === +++ === +++ === +++\n\n")
     
def process_menu_choice(choice): 
    if choice == "1":
        #? Call the function to log a dose
        pass
    elif choice == "2":
        #? Call the function to view dose data
        pass
    elif choice == "3":
        #? Call the function to calculate analytics
        pass
    elif choice == "0":
        exit()
    else:
        print("+++ === +++ === +++ === +++ === +++")
        print("Invalid choice boyo. Please try again. :)")
        print("+++ === +++ === +++ === +++ === +++\n")
        
def log_dose():
    #?implement to login to log a dose
    pass

def view_dose_data(): 
    #? Implement the log to view dose data
    pass

def calculate_analytics():
    #?Implement the logic to calculate analytics
    pass

if __name__ == "__main__":
    display_menu()