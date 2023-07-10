import time
import random

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
        print("\n\n")
        print("+++ === +++ === +++ === +++ === +++")
        print("Invalid choice boyo. Please try again. :)")
        print("INVALID CHOICE MY GUY --- INVALID CHOICE MY GUY ---")
        print("+++ === +++ === +++ === +++ ==\n")
        
def log_dose():
    print("=== +++ Log Dose +++ ===")
    
    quantity_type = input("Enter the quantity type:  (grams, teaspoons, extract): ")
    quantity = float(input("Enter the quantity: "))
    
    timestamp = data_maniulation.log_dose(quantity_type, quantity)
    
    #! Print the timestamp of the logged dose
    print("Dose logged successfully at {}".format(timestamp))
    
    #! Print the analytics of the logged dose
    print(f"Total Doses: {analytics.calculate_total_doses()}")
    
    print(f"Time since last dose: {analytics.calculate_time_since_last_dose(timestamp)}")
    
    print(f"Number of doses today: {analytics.calculate_doses_today()}")
    
    time.sleep(0.5) #? Add a delay to make the output more readable

def view_dose_data(): 
    #? Implement the log to view dose data
    pass

def calculate_analytics():
    #?Implement the logic to calculate analytics
    pass

def print_encouraging_quote():
    quotes = [
        'Stay strong my guy',
        'You got this pal',
        "Believe in yourself. You've got this",
        'You are a beast my friend',
         "Every step counts. You're making progress!",
        "Don't give up. You're stronger than you think!",
        "Stay positive and keep going!",
        "You're doing great! Keep it up!",
    ]
    
    quote = random.choice(quotes)
    print("+++ === +++ === +++ === +++ === +++")
    print("=== +++ Encouraging Quote: +++ ===")
    print(f"{quote}\n")
    time.sleep(0.5)

if __name__ == "__main__":
    display_menu()