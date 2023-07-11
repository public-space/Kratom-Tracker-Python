import time
import random
import sys
from colorama import Fore, Back, Style
from functions import data_manipulation, analytics

#?---------------------Menu Functions---------------------# 

#!-------------- Display Menu-------------!#

def display_menu(): 
    time.sleep(1)
    print("\n\n")
    print("+++ === +++ === +++ === +++ === +++")
    print("=== +++ Kratom Tracking App +++ ===")
    print("+++ === +++ === +++ === +++ === +++")
    print("1. Log Dose")
    print("2. View Dose Data")
    print("3. Calculate Analytics")
    print("0. Exit")
    print("+++ === +++ === +++ === +++ === +++\n\n")
    time.sleep(0.5)
    
#!-------------- Process Menu Choices-------------!#

def process_menu_choice(choice): 
    if choice == "1":
        log_dose()
    elif choice == "2":
        view_dose_data()
    elif choice == "3":
        calculate_analytics()
    elif choice == "0":
        print(Fore.BLUE + "Goodbye my guy. Stay strong. You got this. :" + Style.RESET_ALL)
        sys.exit()
    else:
        print(Fore.RED + Back.BLACK + "\n\n")
        print("+++ === +++ === +++ === +++ === +++")
        print("Invalid choice boyo. Please try again. :)")
        print("INVALID CHOICE MY GUY --- INVALID CHOICE MY GUY ---")
        print("+++ === +++ === +++ === +++ ==\n" + Style.RESET_ALL)
        time.sleep(0.5)
       
#?---------------------Dose  Functions---------------------# 

#!--------------------Log Dose--------------------#
 
def log_dose():
    print("=== +++ Log Dose +++ ===")
    
    quantity_type = input("Enter the quantity type:  (grams, teaspoons, extract): ")
    quantity = float(input("Enter the quantity: "))
    
    timestamp = data_manipulation.log_dose(quantity_type, quantity)
    
    #! Print the timestamp of the logged dose
    print("Dose logged successfully at {}".format(timestamp))
    
    #! Print the analytics of the logged dose
    print(f"Total Doses: {analytics.calculate_total_doses()}")
    
    print(f"Time since last dose: {analytics.calculate_time_since_last_dose(timestamp)}")
    
    print(f"Number of doses today: {analytics.calculate_doses_today()}")
    
    time.sleep(0.5) #? Add a delay to make the output more readable

#!--------------------calculate time since last dose--------------------# 

def calculate_time_since_last_dose(last_dose_timestamp):
    last_dose_time = datetime.strptime(last_dose_timestamp, "%Y-%m-%d %H:%M:%S")
    
    time_difference = datetime.now() - last_dose_time
    
    seconds = time_difference.total_seconds()
    minutes = seconds / 60
    hours = minutes / 60
    
    return f"{int(hours)} hours, {int(minutes % 60)} minutes, {int(seconds % 60)} seconds"
    

#!--------------------View Dose Data--------------------# 

def view_dose_data(): 
    print("=== +++ View Dose Data +++ ===")
    
    dose_data = get_dose_data()
    
    print("+++ === +++ === +++ === +++ === +++")
    print("ID  | Timestamp          | Quantity")
    print("-----------------------------------")  
    # Iterate through each dose in the dose_data list
    for dose in dose_data: 
        # Format and print each dose information in a row
        print(f"{dose[0]:<4} |   {dose[1]:19}  |  {dose[2]:.2f}\n")
    
    time.sleep(0.5)


#!--------------------Calculate Analytics--------------------# 

def calculate_analytics():
    print("=== +++ Calculate Analytics +++ ===")
    
    total_doses = analytics.calculate_total_doses()
    last_dose_timestamp = analytics.get_last_dose_timestamp()
    time_since_last_dose = analytics.calculate_time_since_last_dose(last_dose_timestamp)
    doses_today = analytics.calculate_doses_today()
    
    print("+++ === +++ === +++ === +++ === +++")
    print("Total Doses: {}".format(total_doses))
    print("Time since last dose: {}".format(time_since_last_dose))
    print(f"Number of doses today: {doses_today}\n")  
    time.sleep(0.5)
    


#?---------------------Quote---------------------# 


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
    print(Fore.GREEN + "=== +++ Encouraging Quote: +++ ===" + Style.RESET_ALL)
    print(f"{quote}\n")
    time.sleep(0.5)

#?---------------------Main---------------------# 


if __name__ == "__main__":
    display_menu()