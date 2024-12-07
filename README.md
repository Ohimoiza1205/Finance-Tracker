# Advanced Personal Finance Tracker

## Project Overview
The **Advanced Personal Finance Tracker** is a PyQt5-based desktop application designed to help users manage their personal finances. It allows users to add and track their financial transactions, categorize them, and visualize their spending habits through graphs. Additionally, it integrates real-time data, such as exchange rates, to provide up-to-date financial insights.

## Features
- **Add Transactions**: Users can input transactions with date, description, amount, and category (e.g., groceries, rent).
- **Transaction Table**: A table that displays all financial transactions stored in an SQLite database.
- **Spending Analysis**: A graph showing total spending by category, updated dynamically as new transactions are added.
- **Real-time Data Fetching**: Fetches real-time data such as exchange rates using an API (currently set to fetch USD exchange rates).
- **SQLite Database**: Stores transactions locally using SQLite for persistent data management.

## Technologies Used
- **Python**: Programming language used to build the application.
- **PyQt5**: Framework used to build the graphical user interface (GUI).
- **SQLite**: Database used to store financial transactions locally.
- **Matplotlib**: Used to plot graphs for spending analysis.
- **Requests**: Used to fetch real-time data from APIs (e.g., exchange rates).

## Installation

### Prerequisites
Make sure you have Python 3.x installed on your machine. You also need to install the required Python libraries:

```bash
pip install PyQt5 matplotlib requests
```
### Run the Application
Clone the repository and navigate to the project directory. Then run the following command to start the application:
```bash
python finance_tracker_app.py
```

### Usage
- **Adding a Transaction**
**Input format**: To add a transaction, enter the following format into the input field:
```javascript
Date Description Amount Category
Example: 2024-12-01 Groceries 50 Food
```
**Add Transaction**: After entering the transaction details, click the Add Transaction button to add it to the database and update the table.

- **Viewing Transactions**
The Transaction Table will automatically display all stored transactions, showing the date, description, amount, and category.

- **Spending Analysis Graph**
The Spending by Category graph is automatically updated every time a transaction is added. It shows a bar chart of the total amount spent in each category.

- **Real-Time Data Fetching**
The application fetches real-time exchange rates using an external API and displays them in the console. You can expand this feature to display the data in the GUI.

- **Screenshots**
Spending Analysis Graph
![image](https://github.com/user-attachments/assets/717a805e-c792-4323-8f46-3136c1e0274d)

## Database
The application uses an SQLite database to store all financial transactions. It creates a table called transactions with the following schema:

- **``id (INTEGER)``**: Primary key for each transaction.
- **``date (TEXT)``**: Date of the transaction.
- **``description (TEXT)``**: Description of the transaction.
- **``amount (REAL)**``: Amount of money involved in the transaction.
- **``category (TEXT)**``: Category of the transaction (e.g., Food, Rent, Entertainment).

## Contributions
Contributions are welcome! If you'd like to contribute to the project, follow the steps below:

- Fork the repository.
- Create a new branch (``git checkout -b feature-branch``).
- Commit your changes (``git commit -m 'Add feature'``).
- Push to the branch (``git push origin feature-branch``).
- Create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
If you have any questions or suggestions, feel free to reach out:

Email: omoiza@ttu.edu
GitHub: @Ohimoiza1205

