## Kratom Tracking App - Personal Version

### Overview
The Kratom Tracking App - Personal Version is a standalone application designed for personal use. It allows you to log your kratom doses and track your usage over time. This documentation provides instructions on setting up and running the app, as well as details about its functionality.

### Installation
To run the Kratom Tracking App - Personal Version, ensure that you have Python installed on your machine. You can download Python from the official Python website (https://www.python.org) and follow the installation instructions specific to your operating system.

### Setup
1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd kratom_tracking_app
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage
1. Create the database:
   - Run the following command to create the SQLite database:
     ```
     python database/create_database.py
     ```

2. Start the app:
   - Run the following command to start the app:
     ```
     python main.py
     ```

3. Follow the instructions displayed in the console to interact with the app:
   - Select options from the menu by entering the corresponding numbers.
   - Log doses, view dose data, and calculate analytics based on your kratom usage.

### Examples
- Logging a dose:
  ```
  === Kratom Tracking App ===
  1. Log Dose
  2. View Dose Data
  3. Calculate Analytics
  0. Exit
  Enter your choice: 1

  Enter the timestamp (YYYY-MM-DD HH:MM:SS): 2023-07-09 10:00:00
  Enter the quantity: 2.5

  Dose logged successfully!
  ```

- Viewing dose data:
  ```
  === Kratom Tracking App ===
  1. Log Dose
  2. View Dose Data
  3. Calculate Analytics
  0. Exit
  Enter your choice: 2

  ID  |  Timestamp            |  Quantity
  ---------------------------------------
  1   |  2023-07-09 10:00:00  |  2.5
  ```

- Calculating analytics:
  ```
  === Kratom Tracking App ===
  1. Log Dose
  2. View Dose Data
  3. Calculate Analytics
  0. Exit
  Enter your choice: 3

  Total Doses: 1
  ```

Please note that this version of the app is for personal use, and no user authentication is implemented. Make sure to keep the database file (`kratom.db`) secure as it contains your logged dose data.

That's the documentation for the Kratom Tracking App - Personal Version. You can further customize and expand it based on your specific requirements and preferences.

Now, let's move on to creating a branch in your Git repository using the terminal.

To create a new branch, follow these steps:

1. Make sure you're in the root directory of your project in the terminal.

2. Check the current branch you're on:
   ```
   git branch
   ```

3. Create a new branch with a descriptive name:
   ```
   git branch <branch-name>
   ```

4. Switch to the new branch:
   ```
   git checkout <branch-name>
   ```

5. Confirm that you're now on the new branch:
   ```
   git branch
   ```

Now you have successfully created and switched to a new branch. You can continue making changes, commits, and pushes on this branch while keeping the main branch untouched.

Remember to use meaningful branch names that reflect the purpose or feature you're working on. Additionally, regularly commit and push your changes to ensure they are saved in your repository.

If you ever need to switch back to the main branch, use the following command:
```
git checkout main
```

Feel free to ask any questions or seek further assistance with the documentation or branching process.